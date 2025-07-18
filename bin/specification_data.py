from csv_helpers import write_csv
from loader import load_content


def generate_field_data():
    """Generate the field data csv of the specification"""
    data = load_content()
    # write the field data to a file
    sorted_fields = sorted(data["field"].items())
    fields_data = [field[1] for field in sorted_fields]
    write_csv(
        fields_data,
        output_file="data/specification/field_data.csv",
        first_headers=[
            "field",
            "name",
            "description",
            "datatype",
            "codelist",
            "component",
            "cardinality",
        ],
        final_headers=["notes", "entry-date", "end-date"],
    )


if __name__ == "__main__":
    generate_field_data()
