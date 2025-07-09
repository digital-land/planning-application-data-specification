import glob
import os

specification_dir = "specification"


def count_application_schemas():
    """Count number of application schemas in specification/application (files named *.schema.md)"""
    pattern = os.path.join(specification_dir, "application", "*.schema.md")
    schema_files = glob.glob(pattern)
    return len(schema_files)


def count_fields():
    """Count number of fields in specification/field"""
    field_dir = os.path.join(specification_dir, "field")
    if not os.path.exists(field_dir):
        return 0

    field_files = [f for f in os.listdir(field_dir) if f.endswith(".md")]
    return len(field_files)


def count_module_schemas():
    """Count how many module schemas are in specification/module (files named *.schema.md)"""
    pattern = os.path.join(specification_dir, "module", "*.schema.md")
    schema_files = glob.glob(pattern)
    return len(schema_files)


def count_components():
    """Count how many components are in specification/component"""
    component_dir = os.path.join(specification_dir, "component")
    if not os.path.exists(component_dir):
        return 0

    component_files = [f for f in os.listdir(component_dir) if f.endswith(".md")]
    return len(component_files)


def count_example_files():
    """Count how many example files are in specification/example"""
    example_dir = os.path.join(specification_dir, "example")
    if not os.path.exists(example_dir):
        return 0

    example_files = [
        f for f in os.listdir(example_dir) if f.endswith(".json") or f.endswith(".md")
    ]
    return len(example_files)


def get_declarative_tracking_summary():
    """Get a summary of all declarative specification counts"""
    return {
        "application_schemas": count_application_schemas(),
        "fields": count_fields(),
        "module_schemas": count_module_schemas(),
        "components": count_components(),
        "example_files": count_example_files(),
    }


def print_declarative_tracking_summary():
    """Print a summary of all declarative specification counts"""
    summary = get_declarative_tracking_summary()
    print("Declarative Specification Tracking Summary")
    print("=" * 45)
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
    print()
    total = sum(summary.values())
    print(f"Total Declarative Files: {total}")


def write_summary_to_markdown():
    """
    Write the declarative specification tracking summary to a markdown file
    in the issue-tracking directory called declarative-model-progress.md
    """
    summary = get_declarative_tracking_summary()
    output_dir = "issue-tracking"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "declarative-model-progress.md")
    with open(output_path, "w") as f:
        f.write("# Declarative Specification Tracking Summary\n\n")
        for key, value in summary.items():
            if key == "components":
                line = f"- **Substructures (objects/components)**: {value}"
            else:
                line = f"- **{key.replace('_', ' ').capitalize()}**: {value}"
            f.write(line + "\n")
        total = sum(summary.values())
        f.write(f"\n**Total elements**: {total}\n")


if __name__ == "__main__":
    # print_declarative_tracking_summary()
    write_summary_to_markdown()
