# spec.py
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
# Ensure both the project root and bin/ are on sys.path so modules that expect
# to be run from bin/ (e.g. `import csv_helpers`) continue to work.
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "bin"))

import click
from bin.applications import get_application_module_refs, get_applications_with_module
from bin.loader import load_content


@click.group()
@click.option(
    "--spec-dir", default="specification", help="Path to specification directory"
)
@click.pass_context
def cli(ctx, spec_dir):
    """Planning application data specification CLI."""
    ctx.ensure_object(dict)
    ctx.obj["spec_dir"] = Path(spec_dir)


@cli.group()
def find():
    """Find and query specification elements."""
    pass


# Find subcommands
@find.command()
@click.argument("module_ref")
def applications_with_module(module_ref):
    """Find applications that use a specific module."""
    spec = load_content()
    apps = get_applications_with_module(module_ref, spec)

    if apps:
        click.echo(f"Applications using module '{module_ref}':")
        for app_ref in apps:
            app = spec["application"].get(app_ref, {})
            name = app.get("name", app_ref)
            click.echo(f"  • {app_ref}: {name}")
    else:
        click.echo(f"No applications found using module '{module_ref}'")


@find.command()
@click.argument("application_ref")
def modules_in_application(application_ref):
    """Find all modules used by a specific application."""
    spec = load_content()
    modules = get_application_module_refs(application_ref, spec)

    if modules:
        click.echo(f"Modules in application '{application_ref}':")
        for mod_ref in modules:
            mod = spec.get("module", {}).get(mod_ref, {})
            name = mod.get("name", mod_ref)
            click.echo(f"  • {mod_ref}: {name}")
    else:
        click.echo(f"No modules found for application '{application_ref}'")


if __name__ == "__main__":
    cli()
