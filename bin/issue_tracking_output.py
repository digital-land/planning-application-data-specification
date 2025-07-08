import os

from csv_helpers import read_csv

discussion_base_url = "https://github.com/digital-land/planning-application-data-specification/discussions/"


def label_to_url(label):
    """
    Convert a label to a URL-friendly format.

    Args:
        label: Label string to convert

    Returns:
        URL-friendly label
    """
    # Convert "component:non-res floorspace" to %20label%3A"component%3Anon-res%20floorspace"
    return f'%20label%3A"{label.replace(" ", "%20").replace(":", "%3A")}"'


def make_issues_url(label):
    """
    Create a GitHub issues URL filtered by a specific label.

    Args:
        label: Label string to filter by

    Returns:
        Complete GitHub issues URL with label filter
    """
    # Base URL for filtered issues
    base_url = "https://github.com/digital-land/planning-application-data-specification"
    filtered_issues_base_url = f"{base_url}/issues?q=is%3Aissue%20state%3Aopen"
    # Add the label filter
    return f"{filtered_issues_base_url}{label_to_url(label)}"


def get_modules_without_current_issues(modules, issue_tracking_data):
    """
    Get a list of modules that have zero current issues by filtering the full modules list.

    Args:
        modules: List of dicts with all module information
        issue_tracking_data: List of dicts with module issue data

    Returns:
        List of dicts containing modules with 0 current_issues
    """
    # Create a lookup dict for issue tracking data by module reference
    issue_lookup = {row.get("module", ""): row for row in issue_tracking_data}

    modules_without_issues = []

    # Filter out modules with an end-date
    # Sort modules by "name"
    sorted_modules = sorted(modules, key=lambda m: m.get("name", ""))

    for module in sorted_modules:
        if module.get("end-date"):
            continue
        module_ref = module.get("reference", "")

        # Check if this module has issue tracking data
        issue_data = issue_lookup.get(module_ref)

        if issue_data:
            # Module has issue tracking data - check current_issues
            current_issues = int(issue_data.get("current_issues", "0"))
            if current_issues == 0:
                modules_without_issues.append(module)
        else:
            # Module has no issue tracking data - assume zero issues
            modules_without_issues.append(module)

    return modules_without_issues


def create_module_link(module_ref, module_name, module_lookup):
    # Create module link if discussion number exists
    module_info = module_lookup.get(module_ref, {})
    discussion_number = module_info.get("discussion-number", "")

    if discussion_number and discussion_number.startswith("#"):
        # Remove the # and create the link
        discussion_id = discussion_number[1:]
        return f"[{module_name}]({discussion_base_url}{discussion_id})"
    else:
        # No discussion link available
        return module_name


def make_markdown_output(issue_tracking_data, modules):
    """
    Create a markdown table from issue tracking data.

    Args:
        issue_tracking_data: List of dicts with module issue data
        modules: List of dicts with module information including discussion numbers

    Returns:
        Markdown formatted table string
    """
    # Create a lookup dict for modules by reference for faster access
    module_lookup = {m.get("reference", ""): m for m in modules}

    # Start building the markdown table
    markdown_lines = [
        "| # | Module | Current Issues | Backlog Issues | GitHub Labels |",
        "|---|--------|----------------|----------------|---------------|",
    ]

    # Process each row in the issue tracking data
    row_number = 1
    for row in issue_tracking_data:
        module_ref = row.get("module", "")
        module_name = row.get("module_name", module_ref)
        current_issues = int(row.get("current_issues", "0"))
        total_issues = int(row.get("total_issues", "0"))
        backlog_issues = total_issues - current_issues
        labels = row.get("labels", "")

        # Skip rows with no current issues
        if current_issues == 0:
            continue

        # Create module link if discussion number exists
        module_info = module_lookup.get(module_ref, {})
        discussion_number = module_info.get("discussion-number", "")

        if discussion_number and discussion_number.startswith("#"):
            # Remove the # and create the link
            discussion_id = discussion_number[1:]
            module_link = f"[{module_name}]({discussion_base_url}{discussion_id})"
        else:
            # No discussion link available
            module_link = module_name

        # Process labels - split by semicolon and create links for each
        label_links = []
        if labels:
            label_list = [label.strip() for label in labels.split(";") if label.strip()]
            for label in label_list:
                label_url = make_issues_url(label)
                label_links.append(f"[{label}]({label_url})")

        # Join all label links with line breaks for better readability
        labels_column = "<br>".join(label_links) if label_links else ""

        # Create the table row
        row_content = f"| {row_number} | {module_link} | {current_issues} | {backlog_issues} | {labels_column} |"
        markdown_lines.append(row_content)
        row_number += 1

    return "\n".join(markdown_lines)


def write_markdown_to_file(markdown_content, filename="issue-tracking/index.md"):
    """
    Write markdown content to a file with the standard header.

    Args:
        markdown_content: The markdown table content to write
        filename: Path to the output file
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Create the complete markdown with header
    full_content = (
        """# Issue tracker

We have been collecting feedback, triaging and working through that feedback.

Below is a list of the modules we still have open issues for. It also includes the number of issues for that module that we've parked and added to a [backlog](https://github.com/digital-land/planning-application-data-specification/issues?q=is%3Aissue%20state%3Aopen%20label%3ABacklog).

When there are no more current issues for a module the module will disappear from the list ([see modules with zero issues](https://github.com/digital-land/planning-application-data-specification/blob/main/issue-tracking/no-issues.md)).
"""
        + markdown_content
    )

    # Write to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"Markdown report written to {filename}")


def generate_no_issues_file(
    zero_issue_modules, modules, filename="issue-tracking/no-issues.md"
):
    """
    Generate a markdown file listing modules with zero current issues.

    Args:
        zero_issue_modules: List of dicts with modules that have zero current issues
        filename: Path to the output file
    """
    # Create a lookup dict for modules by reference for faster access
    module_lookup = {m.get("reference", ""): m for m in modules}

    if not zero_issue_modules:
        print("No modules with zero issues found.")
        return

    # Start building the markdown content
    markdown_lines = [
        "# Modules with Zero Current Issues",
        "The following modules currently have no open issues ([see modules with issues](https://github.com/digital-land/planning-application-data-specification/blob/main/issue-tracking/index.md)).",
        "",
    ]

    for idx, row in enumerate(zero_issue_modules, start=1):
        module_name = row.get("name", row.get("module", "Unknown Module"))
        markdown_lines.append(
            f"{idx}. {create_module_link(row.get('reference', ''), module_name, module_lookup)} (ref: {row.get('reference', 'N/A')})"
        )

    # Join all lines and write to file
    full_content = "\n".join(markdown_lines)

    # Write to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_content)

    print(f"No issues report written to {filename}")


def generate_issue_tracking_index():
    # read the issue tracking data
    issue_tracking_data = read_csv("issue-tracking/latest.csv", as_dict=True)
    issue_tracking_data = sorted(
        issue_tracking_data, key=lambda row: row.get("module_name", "")
    )
    # load the modules
    modules = read_csv("data/planning-application-module.csv", as_dict=True)

    # Generate the markdown output
    markdown_output = make_markdown_output(issue_tracking_data, modules)

    # Write to file
    write_markdown_to_file(markdown_output)

    # generate file with list of modules with zero issues
    zero_issue_modules = get_modules_without_current_issues(
        modules, issue_tracking_data
    )
    generate_no_issues_file(zero_issue_modules, modules)


if __name__ == "__main__":
    generate_issue_tracking_index()
