from csv_helpers import read_csv
from github_api import count_labels_from_issues, get_issues_with_cache


def load_admin_data():
    data = read_csv("bin/admin_data/label_module_map.csv", as_dict=True)
    return data


def filter_label_counts(label_counts, filter_term, include=True):
    """
    Filter label counts based on whether labels contain a specific term.

    Args:
        label_counts: Counter object with label names and counts
        filter_term: String to search for in label names
        include: If True, return labels that contain the term.
                If False, return labels that don't contain the term.

    Returns:
        Filtered Counter object
    """
    from collections import Counter

    filtered_counts = Counter()

    for label, count in label_counts.items():
        if include and filter_term.lower() in label.lower():
            filtered_counts[label] = count
        elif not include and filter_term.lower() not in label.lower():
            filtered_counts[label] = count

    return filtered_counts


def get_all_label_counts(issues):
    # Count labels
    label_counter = count_labels_from_issues(issues)
    return label_counter


def filter_issues_by_label(issues, label, include=True):
    """
    Filter issues based on whether they have a specific label.

    Args:
        issues: List of issue dictionaries
        label: Label to filter by
        include: If True, return issues with the label.
                If False, return issues without the label.

    Returns:
        List of filtered issues
    """
    filtered_issues = []

    for issue in issues:
        has_label = any(l["name"].lower() == label.lower() for l in issue["labels"])
        if (include and has_label) or (not include and not has_label):
            filtered_issues.append(issue)

    return filtered_issues


def join_counts(records, label_counts, fieldname):
    """
    Join label counts with existing records.

    Args:
        records: List of dictionaries with existing records
        label_counts: Counter object with label counts

    Returns:
        Updated records with label counts added
    """
    for record in records:
        for label, count in label_counts.items():
            if record["github_label"] == label:
                # If the record's label matches the label in counts, add it
                record[fieldname] = count

    return records


def get_component_issue_counts(all_issues):
    data = load_admin_data()
    # count totals for all issues
    all_label_counts = get_all_label_counts(all_issues)
    component_label_counts = filter_label_counts(all_label_counts, "component")
    data = join_counts(data, component_label_counts, "total_issues")

    # do the same for current issue
    current_issues = filter_issues_by_label(all_issues, "backlog", include=False)
    current_label_counts = get_all_label_counts(current_issues)
    current_component_label_counts = filter_label_counts(
        current_label_counts, "component"
    )
    data = join_counts(data, current_component_label_counts, "current_issues")

    return data


def save_issue_report(data, modules, filename="issue-tracking/latest.csv"):
    """
    Save issue report to CSV with module aggregation.

    Format: module, module_name, labels, total_issues, current_issues
    Example: checklist, Checklist, "component: application for tree works - checklist";"component: checklist", 10, 5
    """
    import csv
    import os
    from collections import defaultdict

    # Ensure cache directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Group data by module
    module_data = defaultdict(
        lambda: {
            "module": "",
            "module_name": "",
            "labels": [],
            "total_issues": 0,
            "current_issues": 0,
        }
    )

    # Aggregate data by module
    for record in data:
        module_key = record.get("module", "")
        if not module_key:
            continue

        # Initialize or update module info
        if module_data[module_key]["module"] == "":
            module_data[module_key]["module"] = module_key
            # Find module name from modules list
            module_name = next(
                (
                    m["name"]
                    for m in modules
                    if m.get("reference") == module_key and "name" in m.keys()
                ),
                module_key,  # fallback to module key if name not found
            )
            module_data[module_key]["module_name"] = module_name

        # Add label to the list
        github_label = record.get("github_label", "")
        if github_label:
            module_data[module_key]["labels"].append(github_label)

        # Add issue counts
        module_data[module_key]["total_issues"] += record.get("total_issues", 0)
        module_data[module_key]["current_issues"] += record.get("current_issues", 0)

    # Write to CSV
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "module",
            "module_name",
            "total_issues",
            "current_issues",
            "labels",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for module_key, module_info in sorted(module_data.items()):
            # Join labels with semicolon and wrap in quotes
            labels_str = ";".join(module_info["labels"])

            writer.writerow(
                {
                    "module": module_info["module"],
                    "module_name": module_info["module_name"],
                    "total_issues": module_info["total_issues"],
                    "current_issues": module_info["current_issues"],
                    "labels": labels_str,
                }
            )

    print(f"Issue report saved to {filename}")
    print(f"Modules processed: {len(module_data)}")

    # Print summary
    total_all_issues = sum(m["total_issues"] for m in module_data.values())
    total_current_issues = sum(m["current_issues"] for m in module_data.values())
    print(f"Total issues across all modules: {total_all_issues}")
    print(f"Current issues across all modules: {total_current_issues}")


def gen_issue_report():
    # load modules
    modules = read_csv("data/planning-application-module.csv", as_dict=True)
    # Get all open issues (with caching)
    all_issues, last_fetch_time = get_issues_with_cache()
    backlog_issues = filter_issues_by_label(all_issues, "backlog")
    current_issues = filter_issues_by_label(all_issues, "backlog", include=False)

    data = get_component_issue_counts(all_issues)
    # Save the report
    save_issue_report(data, modules)
    print(f"\nReport generated from {len(all_issues)} total issues")
    print(f"Last fetched: {last_fetch_time}")


if __name__ == "__main__":
    gen_issue_report()
