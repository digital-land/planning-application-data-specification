import argparse
import csv
import os
from typing import Iterable, List, Optional

from github_api import get_open_issues
from issue_tracking import filter_issues_by_label


def _labels_to_string(labels: Iterable[dict]) -> str:
    return ";".join(label.get("name", "") for label in labels)


def export_open_issues(
    label: Optional[str] = None,
    output_path: Optional[str] = None,
    repo_owner: str = "digital-land",
    repo_name: str = "planning-application-data-specification",
    github_token: Optional[str] = None,
) -> str:
    issues = get_open_issues(
        repo_owner=repo_owner, repo_name=repo_name, github_token=github_token
    )

    if label:
        issues = filter_issues_by_label(issues, label)

    label_fragment = label if label else "all"
    output_file = output_path or f"tmp/extracted-issues-{label_fragment}.csv"

    output_dir = os.path.dirname(output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "number",
                "title",
                "state",
                "html_url",
                "labels",
                "created_at",
                "updated_at",
                "body",
            ],
        )
        writer.writeheader()

        for issue in issues:
            writer.writerow(
                {
                    "number": issue.get("number"),
                    "title": issue.get("title"),
                    "state": issue.get("state"),
                    "html_url": issue.get("html_url"),
                    "labels": _labels_to_string(issue.get("labels", [])),
                    "created_at": issue.get("created_at"),
                    "updated_at": issue.get("updated_at"),
                    "body": issue.get("body", ""),
                }
            )

    return output_file


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract open GitHub issues to a CSV file."
    )
    parser.add_argument(
        "--label",
        dest="label",
        help="Label to filter issues by (exact match, case-insensitive).",
    )
    parser.add_argument(
        "--output",
        dest="output",
        help="Path to write the CSV. Defaults to tmp/extracted-issues-{label}.csv",
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
        default=None,
        help="GitHub token for authenticated requests (optional).",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    output_file = export_open_issues(
        label=args.label,
        output_path=args.output,
        repo_owner=args.repo_owner,
        repo_name=args.repo_name,
        github_token=args.github_token,
    )
    print(f"Saved {args.label or 'all'} open issues to {output_file}")


if __name__ == "__main__":
    main()
