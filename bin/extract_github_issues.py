import argparse
import csv
import os
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Optional

from github_api import get_open_issues

RAW_ISSUES_FILENAME = "open-issues-raw.csv"
RAW_LABELS_FILENAME = "open-issue-labels-raw.csv"
SPREADSHEET_FILENAME = "open-issues-spreadsheet.csv"

RAW_ISSUE_FIELDS = [
    "issue_number",
    "issue_url",
    "api_url",
    "repository_owner",
    "repository_name",
    "author_login",
    "author_type",
    "title",
    "body",
    "state",
    "comments_count",
    "labels_display",
    "label_count",
    "created_at",
    "updated_at",
    "last_activity_at",
    "fetched_at",
]

RAW_LABEL_FIELDS = [
    "issue_number",
    "issue_url",
    "label_name",
    "label_description",
    "label_colour",
    "label_url",
    "fetched_at",
]

SPREADSHEET_FIELDS = [
    "issue_number",
    "issue_url",
    "author_login",
    "title",
    "body",
    "labels_display",
    "comments_count",
    "label_count",
    "has_labels",
    "has_multiple_labels",
    "created_at",
    "last_activity_at",
    "age_days",
    "days_since_last_activity",
    "fetched_at",
]


def fetch_open_issues(
    repo_owner: str,
    repo_name: str,
    github_token: Optional[str] = None,
) -> List[Dict]:
    return get_open_issues(
        repo_owner=repo_owner,
        repo_name=repo_name,
        github_token=github_token,
    )


def format_labels_display(labels: Iterable[dict]) -> str:
    return ";".join(label.get("name", "") for label in labels if label.get("name"))


def parse_github_datetime(value: str) -> Optional[datetime]:
    if not value:
        return None

    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def whole_days_between(earlier: Optional[datetime], later: datetime) -> Optional[int]:
    if earlier is None:
        return None

    return max((later - earlier).days, 0)


def build_issue_row(
    issue: Dict,
    fetched_at: str,
    repo_owner: str,
    repo_name: str,
) -> Dict[str, object]:
    labels = issue.get("labels", [])
    labels_display = format_labels_display(labels)

    return {
        "issue_number": issue.get("number"),
        "issue_url": issue.get("html_url", ""),
        "api_url": issue.get("url", ""),
        "repository_owner": repo_owner,
        "repository_name": repo_name,
        "author_login": issue.get("user", {}).get("login", ""),
        "author_type": issue.get("user", {}).get("type", ""),
        "title": issue.get("title", ""),
        "body": issue.get("body", ""),
        "state": issue.get("state", ""),
        "comments_count": issue.get("comments", 0),
        "labels_display": labels_display,
        "label_count": len(labels),
        "created_at": issue.get("created_at", ""),
        "updated_at": issue.get("updated_at", ""),
        "last_activity_at": issue.get("updated_at", ""),
        "fetched_at": fetched_at,
    }


def build_label_rows(issue: Dict, fetched_at: str) -> List[Dict[str, object]]:
    issue_number = issue.get("number")
    issue_url = issue.get("html_url", "")
    rows = []

    for label in issue.get("labels", []):
        rows.append(
            {
                "issue_number": issue_number,
                "issue_url": issue_url,
                "label_name": label.get("name", ""),
                "label_description": label.get("description", "") or "",
                "label_colour": label.get("color", ""),
                "label_url": label.get("url", ""),
                "fetched_at": fetched_at,
            }
        )

    return rows


def build_spreadsheet_row(
    issue_row: Dict[str, object],
    extracted_at: datetime,
) -> Dict[str, object]:
    created_at = parse_github_datetime(str(issue_row.get("created_at", "")))
    last_activity_at = parse_github_datetime(str(issue_row.get("last_activity_at", "")))
    label_count = int(issue_row.get("label_count", 0) or 0)

    return {
        "issue_number": issue_row.get("issue_number"),
        "issue_url": issue_row.get("issue_url"),
        "author_login": issue_row.get("author_login"),
        "title": issue_row.get("title"),
        "body": issue_row.get("body"),
        "labels_display": issue_row.get("labels_display"),
        "comments_count": issue_row.get("comments_count"),
        "label_count": label_count,
        "has_labels": "yes" if label_count > 0 else "no",
        "has_multiple_labels": "yes" if label_count > 1 else "no",
        "created_at": issue_row.get("created_at"),
        "last_activity_at": issue_row.get("last_activity_at"),
        "age_days": whole_days_between(created_at, extracted_at),
        "days_since_last_activity": whole_days_between(last_activity_at, extracted_at),
        "fetched_at": issue_row.get("fetched_at"),
    }


def write_csv(path: str, fieldnames: List[str], rows: List[Dict[str, object]]) -> None:
    output_dir = os.path.dirname(path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def export_issue_csvs(
    repo_owner: str = "digital-land",
    repo_name: str = "planning-application-data-specification",
    github_token: Optional[str] = None,
    output_dir: str = "issue-tracking",
) -> Dict[str, str]:
    issues = fetch_open_issues(
        repo_owner=repo_owner,
        repo_name=repo_name,
        github_token=github_token,
    )
    extracted_at = datetime.now(timezone.utc)
    fetched_at = extracted_at.isoformat(timespec="seconds")

    raw_issue_rows = [
        build_issue_row(issue, fetched_at, repo_owner, repo_name) for issue in issues
    ]
    raw_label_rows = [
        row for issue in issues for row in build_label_rows(issue, fetched_at)
    ]
    spreadsheet_rows = [
        build_spreadsheet_row(issue_row, extracted_at) for issue_row in raw_issue_rows
    ]

    outputs = {
        "raw_issues": os.path.join(output_dir, RAW_ISSUES_FILENAME),
        "raw_labels": os.path.join(output_dir, RAW_LABELS_FILENAME),
        "spreadsheet": os.path.join(output_dir, SPREADSHEET_FILENAME),
    }

    write_csv(outputs["raw_issues"], RAW_ISSUE_FIELDS, raw_issue_rows)
    write_csv(outputs["raw_labels"], RAW_LABEL_FIELDS, raw_label_rows)
    write_csv(outputs["spreadsheet"], SPREADSHEET_FIELDS, spreadsheet_rows)

    return outputs


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract open GitHub issues into raw and spreadsheet-friendly CSV files."
    )
    parser.add_argument(
        "--repo-owner",
        dest="repo_owner",
        default="digital-land",
        help="Repository owner. Defaults to digital-land.",
    )
    parser.add_argument(
        "--repo-name",
        dest="repo_name",
        default="planning-application-data-specification",
        help="Repository name. Defaults to planning-application-data-specification.",
    )
    parser.add_argument(
        "--github-token",
        dest="github_token",
        default=os.getenv("GITHUB_TOKEN"),
        help="GitHub token for authenticated requests. Defaults to GITHUB_TOKEN.",
    )
    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        default="issue-tracking",
        help="Directory to write CSV outputs. Defaults to issue-tracking.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    outputs = export_issue_csvs(
        repo_owner=args.repo_owner,
        repo_name=args.repo_name,
        github_token=args.github_token,
        output_dir=args.output_dir,
    )
    print(f"Saved open issues to {outputs['raw_issues']}")
    print(f"Saved open issue labels to {outputs['raw_labels']}")
    print(f"Saved spreadsheet-ready issues to {outputs['spreadsheet']}")


if __name__ == "__main__":
    main()
