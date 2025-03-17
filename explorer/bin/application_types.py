import os
from collections import defaultdict
from bin.modules import get_modules, get_module_discussion_url

def print_all(app_types):
    print("===")
    print("All application types")
    print("===")
    for app in app_types:
        print(f"{app['name']} (ref: {app['reference']})")


def app_type_overview(app_type, sub_type_ref=None, markdown=False):
    print("Application type")
    print("===")
    print(f"{app_type['name']} (ref: {app_type['reference']})")

    print("\nDescription\n---")
    print(f"{app_type['description']}")

    print("\nLegislation\n---")
    if app_type['legislation']:
        legislation_urls = app_type['legislation'].split(";")
        for url in legislation_urls:
            print(url)
    else:
        print("No legislation specified")

    if sub_type_ref:
        combined_modules = app_type["modules"][:]
        for st in app_type.get("sub-types", []):
            if st["reference"] == sub_type_ref:
                combined_modules.extend(st["modules"])
        combined_modules = sorted(combined_modules, key=lambda x: x['name'])
        if markdown:
            print("\nModules\n---")
            for module in combined_modules:
                print(f"* [{module['name']}]({get_module_discussion_url(module)}) (ref: {module['reference']})")
        else:
            print(f"\n{len(combined_modules)} Modules\n---")
            for module in combined_modules:
                print(f"{module['name']} (ref: {module['reference']})")
    else:
        if app_type.get("modules"):
            if markdown:
                print("\nModules\n---")
                for module in app_type["modules"]:
                    print(f"* [{module['name']}]({get_module_discussion_url(module)}) (ref: {module['reference']})")
            else:
                print(f"\n{len(app_type['modules'])} Modules\n---")
                for module in app_type["modules"]:
                    print(f"{module['name']} (ref: {module['reference']})")
        
        if app_type.get("sub-types"):
            if markdown:
                print("\nSub-types\n---")
                for sub_type in app_type["sub-types"]:
                    print(f"* Sub-type: {sub_type['reference']}")
                    if sub_type["modules"]:
                        for module in sub_type["modules"]:
                            print(f"  * {module['name']} (ref: {module['reference']})")
                    else:
                        print("Note: 0 associated modules for this sub-type")
            else:
                print("\nSub-types\n---")
                for sub_type in app_type["sub-types"]:
                    print(f"Sub-type: {sub_type['reference']}")
                    if sub_type["modules"]:
                        print(f"{len(sub_type['modules'])} associated modules:")
                        for module in sub_type["modules"]:
                            print(f"  {module['name']} (ref: {module['reference']})")
                    else:
                        print("  0 associated modules for this sub-type")


def get_app_type_from_ref(app_ref, app_types):
    return next((app for app in app_types if app["reference"] == app_ref), None)


def add_modules(app_type, app_types, app_mod_joins, modules):
    app_module_refs = [j['application-module'] for j in app_mod_joins if j["application-type"] == app_type['reference']]
    app_type["modules"] = get_modules(app_module_refs, modules)
    return app_type


def print_app_types_as_markdown_table(app_types):
    sorted_app_types = sorted(app_types, key=lambda x: x['name'])
    discussion_url = f"https://github.com/digital-land/planning-application-data-specification/discussions/"
    print("| Application Type | Notes |")
    print("|---|---|")
    for app in sorted_app_types:
        print(f"| [{app['name']}]({discussion_url}) | {app.get('notes', '')} |")


def print_sub_types(sub_types):
    sub_types_by_app_type = defaultdict(list)
    for sub_type in sub_types:
        app_type = sub_type["application-type"]
        sub_types_by_app_type[app_type].append(sub_type["reference"])

    for app_type, sub_type_refs in sub_types_by_app_type.items():
        print(f"Application Type: {app_type}")
        for sub_type_ref in sub_type_refs:
            print(f"  Sub-type: {sub_type_ref}")


def get_app_types_with_module(module_ref, app_mod_joins, app_types, sub_types):
    app_types_with_module = [join['application-type'] for join in app_mod_joins if join['application-module'] == module_ref and join['application-type']]
    sub_types_with_module = [join['application-sub-type'] for join in app_mod_joins if join['application-module'] == module_ref and join['application-sub-type']]
    return {
        "application-types": [app for app in app_types if app['reference'] in app_types_with_module],
        "sub-types": [app for app in sub_types if app['reference'] in sub_types_with_module]
    }


def add_modules_to_file(open_file, modules, modules_dir):
    if len(modules):
        for module in modules:
            module_file = os.path.join(modules_dir, f"{module['reference']}.md")
            if os.path.exists(module_file):
                with open(module_file, "r") as mf:
                    module_content = mf.read()
                print(f"adding {module['reference']} to application file")
                open_file.write(f"## {module['name']} ({module['reference']})\n\n")
                open_file.write(module_content)
                open_file.write("\n---\n\n")
            else:
                print(f"can't locate {module_file}")


def generate_application_markdown(application, sub_type_ref=None, modules_dir="../specification/module", output_dir="../specification/application"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{application['reference']}.md"
    if sub_type_ref:
        filename = f"{application['reference']}-{sub_type_ref}.md"
    output_file = os.path.join(output_dir, filename)
    
    with open(output_file, "w") as f:
        f.write(f"# {application['name']}\n")
        f.write(f"\n{application['description']}\n\n")
        if sub_type_ref:
            print(f'Generating markdown file for {application["name"]} -> {sub_type_ref}\n')
        else:
            print(f'Generating markdown file for {application["name"]}\n')
        
        sub_type = None
        if sub_type_ref:
            for st in application.get("sub-types", []):
                if st["reference"] == sub_type_ref:
                    sub_type = st
                    break
            if sub_type:
                f.write(f"## Sub-type: {sub_type['name']}\n\n")
        
        add_modules_to_file(f, application.get("modules", []), modules_dir)
        
        if sub_type_ref and sub_type:
            f.write("## Sub-type modules\n")
            f.write("The following modules are required for this sub-type.\n\n")
            add_modules_to_file(f, sub_type.get("modules", []), modules_dir)
