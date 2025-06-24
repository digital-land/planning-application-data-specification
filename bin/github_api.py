import os
from collections import Counter
from datetime import datetime
from typing import Any, Dict, List

import requests
from json_helpers import load_json, save_json

# from dotenv import load_dotenv

# load_dotenv()

cached_issues_file = "cache/github_issues_cache.json"


def get_open_issues(
    repo_owner: str = "digital-land",
    repo_name: str = "planning-application-data-specification",
    github_token: str = None,
) -> List[Dict[str, Any]]:
    """
    Fetch all open issues from a GitHub repository.

    Args:
        repo_owner: GitHub repository owner
        repo_name: GitHub repository name
        github_token: GitHub token for authentication (optional)

    Returns:
        List of issue dictionaries
    """
    # if github_token is None:
    #     github_token = os.getenv("GITHUB_TOKEN")

    # HEADERS (use token for higher rate limit)
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    # PAGINATION VARIABLES
    issues_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    params = {"state": "open", "per_page": 100, "page": 1}

    all_issues = []

    # PAGINATE THROUGH RESULTS
    while True:
        try:
            response = requests.get(issues_url, headers=headers, params=params)

            # Handle rate limiting
            if response.status_code == 403:
                print(f"Error 403: {response.json().get('message', 'Forbidden')}")
                if "rate limit" in response.text.lower():
                    print("You've hit the rate limit. Please:")
                    print("1. Wait a bit and try again")
                    print(
                        "2. Add a GITHUB_TOKEN environment variable for higher limits"
                    )
                break

            response.raise_for_status()
            issues = response.json()

            if not issues:
                break

            for issue in issues:
                # Skip pull requests (they are also issues)
                if "pull_request" not in issue:
                    all_issues.append(issue)

            params["page"] += 1

        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            print(f"Response: {response.text}")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    return all_issues


def save_issues_to_file(
    issues: List[Dict[str, Any]], filename: str = cached_issues_file
):
    data = {
        "fetch_timestamp": datetime.now().isoformat(),
        "fetch_timestamp_human": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "issue_count": len(issues),
        "issues": issues,
    }
    save_json(data, filename)


def load_issues_from_file(filename: str = cached_issues_file) -> Dict[str, Any]:
    data = load_json(filename)
    if not data:
        print("No data found.")
        return None

    return data


def get_issues_with_cache(
    cache_hours: int = 1, force_refresh: bool = False
) -> tuple[List[Dict[str, Any]], str]:
    """
    Get issues with caching and timestamp tracking.

    Returns:
        Tuple of (issues_list, last_fetch_time)
    """
    # Try to load existing cache
    cached_data = load_issues_from_file()

    # Check if we need to refresh
    need_refresh = force_refresh

    if cached_data:
        last_fetch_time = cached_data.get("fetch_timestamp_human", "Unknown")
        fetch_timestamp = datetime.fromisoformat(cached_data["fetch_timestamp"])
        age_hours = (datetime.now() - fetch_timestamp).total_seconds() / 3600
        if age_hours >= cache_hours:
            print(f"Cache is too old ({age_hours:.2f} hours), refreshing...")
            need_refresh = True
    else:
        print("No cached data found, fetching new issues...")
        need_refresh = True

    if need_refresh:
        print("Fetching new issues from GitHub...")
        issues = get_open_issues()
        save_issues_to_file(issues)
        last_fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return issues, last_fetch_time

    return cached_data.get("issues", []), last_fetch_time


def count_labels_from_issues(issues: List[Dict[str, Any]]) -> Counter:
    """
    Count labels from a list of issues.

    Args:
        issues: List of issue dictionaries

    Returns:
        Counter object with label counts
    """
    label_counter = Counter()

    for issue in issues:
        for label in issue["labels"]:
            label_counter[label["name"]] += 1

    return label_counter


# USAGE EXAMPLE
if __name__ == "__main__":
    # Get all open issues (with caching)
    issues, last_fetch_time = get_issues_with_cache()

    # Count labels
    label_counter = count_labels_from_issues(issues)

    # OUTPUT RESULTS
    print(f"Found {len(issues)} open issues")
    print("\nOpen issues by label:")
    for label, count in label_counter.most_common():
        print(f"{label}: {count}")

    # You can now work with the issues list
    # For example, get issue titles:
    print("\nIssue titles:")
    for issue in issues[:5]:  # Show first 5
        print(f"- {issue['title']}")

    print(issues)
