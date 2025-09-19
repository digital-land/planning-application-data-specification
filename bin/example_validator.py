#!/usr/bin/env python3

import json
from pathlib import Path
import click
import jsonschema


def _load_json(path):
    """Load a JSON file from the given path."""
    with open(path, "r") as f:
        return json.load(f)


@click.command()
@click.option(
    "--payload",
    "payload_path",
    type=click.Path(exists=True, dir_okay=False, readable=True, path_type=Path),
    required=True,
    help="Path to the sample payload JSON application.",
)
@click.option(
    "--schema-dir",
    "schema_dir",
    type=click.Path(exists=True, file_okay=False, readable=True, path_type=Path),
    required=True,
    help="Path to the directory containing JSON schemas.",
)
def validate_payload(payload_path: Path, schema_dir: Path):
    """
    Validates a JSON payload against the relevant JSON schemas.

    This script reads a JSON payload, inspects its 'application-types' array,
    and validates the payload against the corresponding schema for each type
    found in the specified schema directory.
    """
    print(f"Loading payload from: {payload_path}")
    try:
        payload = _load_json(payload_path)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in payload file: {e}")
        return
    except Exception as e:
        print(f"Error loading payload file: {e}")
        return

    application_types = payload.get("application", {}).get("application-types")

    if application_types is None or not isinstance(application_types, list):
        print(
            "Error: 'application-types' array not found or not a list in payload."
        )
        return

    print(f"Found application types: {', '.join(application_types)}")
    print("-" * 30)

    all_valid = True

    # Loop through application types calling json schema validator using
    # the correct schema for each type
    for application_type in application_types:
        schema_file = schema_dir / f"{application_type}.json"
        print(f"Validating against schema for '{application_type}': {schema_file}")

        if not schema_file.exists():
            print(f"Error: Schema file not found: {schema_file}")
            all_valid = False
            continue

        try:
            schema = _load_json(schema_file)
            validator = jsonschema.Draft7Validator(schema)
            validator.validate(payload)
            print(f"VALID: Payload is valid against '{application_type}.json' schema.")
        except jsonschema.exceptions.ValidationError as e:
            print(
                f"INVALID: Payload is not valid against '{application_type}.json' schema."
            )
            print(f"  Error: {e.message}")
            all_valid = False
        except Exception as e:
            print(
                f"An unexpected error occurred during validation for '{application_type}': {e}"
            )
            all_valid = False

        print("-" * 30)

    if all_valid:
        print(
            "Success: Payload is valid against all specified application type schemas."
        )
    else:
        print("Failure: Payload failed validation against one or more schemas.")


if __name__ == "__main__":
    validate_payload()
