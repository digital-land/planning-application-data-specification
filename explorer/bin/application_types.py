import os
import csv
from collections import defaultdict
from bin.modules import get_modules, get_module_discussion_url
from bin.utils import slugify


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
    
    # Get codelists required for the modules
    all_modules = get_all_modules_for_application(app_type, sub_type_ref)
    codelists = get_codelists_for_modules(all_modules)
    if codelists:
        print("\nCodelists\n---")
        for codelist in codelists:
            print(f"{codelist['name']} (ref: {codelist['reference']})")


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
                open_file.write(f"### {module['name']} ({module['reference']})\n\n")
                if module.get("description"):
                    open_file.write(f"{module['description']}\n\n")
                else:
                    open_file.write("_To do: add description for module_\n\n")
                open_file.write(module_content)
                open_file.write("\n---\n\n")
            else:
                print(f"can't locate {module_file}")


def get_codelists_for_modules(modules, codelists_file="../data/codelists.csv"):
    """Get all codelists that reference any of the given modules"""
    if not modules:
        return []
        
    module_refs = {m['reference'] for m in modules if m.get('reference')}
    required_codelists = []
    
    with open(codelists_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get('end-date'):  # Only include active codelists
                codelist_modules = [m.strip() for m in row.get('modules', '').split(';') if m.strip()]
                if any(m in module_refs for m in codelist_modules):
                    required_codelists.append(row)
                    
    return sorted(required_codelists, key=lambda x: x['name'])


def get_all_modules_for_application(application, sub_type_ref=None):
    """Get all modules for an application type, including sub-type modules if specified"""
    all_modules = application.get("modules", [])
    if sub_type_ref:
        for st in application.get("sub-types", []):
            if st["reference"] == sub_type_ref:
                all_modules.extend(st.get("modules", []))
    return all_modules


def add_codelist_content_to_file(open_file, codelist, codelist_dir):
    """Add a codelist's markdown content to the output file"""
    codelist_file = os.path.join(codelist_dir, f"{codelist['reference']}.md")
    if os.path.exists(codelist_file):
        with open(codelist_file, "r") as cf:
            codelist_content = cf.read()
        print(f"adding {codelist['reference']} codelist content to application file")
        open_file.write(f"### {codelist['name']} ({codelist['reference']})\n\n")
        if codelist.get("description"):
            open_file.write(f"{codelist['description']}\n\n")
        else:
            open_file.write("_To do: add description for codelist_\n\n")
        open_file.write(codelist_content)
        open_file.write("\n---\n\n")
    else:
        print(f"can't locate codelist file: {codelist_file}")


def generate_contents_section(application, sub_type=None):
    """Generate a contents section for the markdown file"""
    contents = ["## Contents\n"]
    
    # Add link to application model
    contents.append("* [Application data specification](#application-data-specification)\n")
    
    # Add modules section
    contents.append("### Modules\n")
    
    # Add main application modules with slugged anchors
    for module in sorted(application.get("modules", []), key=lambda x: x['name']):
        slug = slugify(module['name'])
        contents.append(f"* [{module['name']}](#{slug}-{module['reference']})")
    
    # Add sub-type modules if present
    if sub_type and sub_type.get("modules"):
        contents.append("\n### Sub-type modules\n")
        for module in sorted(sub_type.get("modules", []), key=lambda x: x['name']):
            slug = slugify(module['name'])
            contents.append(f"* [{module['name']}](#{slug}-{module['reference']})")
            
    # Get codelists for this application/sub-type
    all_modules = get_all_modules_for_application(application, sub_type_ref=sub_type['reference'] if sub_type else None)
    codelists = get_codelists_for_modules(all_modules)
    
    if codelists:
        contents.append("\n### Required codelists\n")
        for codelist in sorted(codelists, key=lambda x: x['name']):
            slug = slugify(codelist['name'])
            contents.append(f"* [{codelist['name']}](#{slug}-{codelist['reference']})")
    
    return "\n".join(contents) + "\n\n---\n\n"


def add_specification_content_to_file(open_file, spec_file="../specification/application.md"):
    """Add the main application specification content to the file"""
    if os.path.exists(spec_file):
        with open(spec_file, "r") as sf:
            spec_content = sf.read()
        print(f"adding application specification content")
        open_file.write("## Application data specification\n\n")
        open_file.write(spec_content)
        open_file.write("\n---\n\n")
    else:
        print(f"can't locate specification file: {spec_file}")


def prepare_application_data(application, sub_type_ref=None, app_mod_joins=None, modules=None):
    """Prepare application data by loading modules and finding sub-types"""
    # Get modules for application type if not already loaded
    if app_mod_joins and modules and not application.get("modules"):
        app_module_refs = [j['application-module'] for j in app_mod_joins 
                        if j["application-type"] == application['reference'] and not j.get("end-date")]
        application["modules"] = get_modules(app_module_refs, modules)
    
    # Find matching sub-type if specified
    sub_type = None
    if sub_type_ref:
        for st in application.get("sub-types", []):
            if st["reference"] == sub_type_ref:
                # Get modules for sub-type if not already loaded
                if app_mod_joins and modules and not st.get("modules"):
                    st_module_refs = [j['application-module'] for j in app_mod_joins 
                                    if j["application-sub-type"] == st['reference'] and not j.get("end-date")]
                    st["modules"] = get_modules(st_module_refs, modules)
                sub_type = st
                break
                
    return application, sub_type


def generate_application_markdown(application, sub_type_ref=None, modules_dir="../specification/module", output_dir="../specification/application", codelist_dir="../specification/codelist", app_mod_joins=None, modules=None):
    """Generate markdown file for an application type and optionally a sub-type"""
    # Prepare the data
    application, sub_type = prepare_application_data(application, sub_type_ref, app_mod_joins, modules)

    # Setup output
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{application['reference']}-{sub_type_ref}.md" if sub_type_ref else f"{application['reference']}.md"
    output_file = os.path.join(output_dir, filename)
    
    print(f"\nGenerating markdown for {application['name']}{f' -> {sub_type_ref}' if sub_type_ref else ''}")
    
    # Generate the file
    with open(output_file, "w") as f:
        f.write(f"# {application['name']}\n")
        f.write(f"\n{application['description']}\n\n")
        
        if sub_type:
            f.write(f"## Sub-type: {sub_type['name']}\n\n")
        
        # Add contents section
        f.write(generate_contents_section(application, sub_type))
        
        # Add application specification content
        add_specification_content_to_file(f)
        
        # Add modules sections
        f.write(f"## Modules\n\n")
        f.write(f"These modules are all required for this application type\n\n")
        add_modules_to_file(f, application.get("modules", []), modules_dir)
        
        if sub_type:
            f.write("## Sub-type modules\n")
            f.write("The following modules are required for this sub-type.\n\n")
            add_modules_to_file(f, sub_type.get("modules", []), modules_dir)

        # Add codelists section
        all_modules = get_all_modules_for_application(application, sub_type_ref)
        codelists = get_codelists_for_modules(all_modules)
        print("\nCodelists\n---")
        if codelists:
            f.write("\n## Required codelists\n\n")
            f.write("The following codelists are required by modules in this application type:\n\n")            
            for codelist in codelists:
                add_codelist_content_to_file(f, codelist, codelist_dir)

    return output_file


def prepare_and_generate_application(application, app_mod_joins, modules, sub_types=None):
    """Prepare and generate markdown for an application and its sub-types"""
    # Get modules for this application type
    app_module_refs = [j['application-module'] for j in app_mod_joins 
                    if j["application-type"] == application['reference'] and not j.get("end-date")]
    application["modules"] = get_modules(app_module_refs, modules)
    
    # Get any sub-types for this application
    app_sub_types = [s for s in sub_types if s["application-type"] == application['reference']] if sub_types else []
    application['sub-types'] = []
    
    try:
        if app_sub_types:
            # If app has sub-types, only generate those
            print(f"\nGenerating markdown for {application['name']} sub-types")
            for st in app_sub_types:
                print(f"  -> {st['name']}")
                # Get modules for this sub-type
                st_module_refs = [j['application-module'] for j in app_mod_joins 
                                if j["application-sub-type"] == st['reference'] and not j.get("end-date")]
                st["modules"] = get_modules(st_module_refs, modules)
                application['sub-types'].append(st)
                generate_application_markdown(application, sub_type_ref=st['reference'])
        else:
            # Only generate base application markdown if no sub-types
            print(f"\nGenerating markdown for {application['name']}")
            generate_application_markdown(application)
            
        return None  # Success
    except Exception as e:
        return f"Error processing {application['name']}: {str(e)}"  # Return error message
