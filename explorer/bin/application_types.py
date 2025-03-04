from bin.modules import get_modules

def print_all(app_types):
    print("===")
    print("All application types")
    print("===")
    for app in app_types:
        print(f"{app['name']} (ref: {app['reference']})")


def app_type_overview(app_type):
    print("Application type")
    print("===")
    print(f"{app_type['name']} (ref: {app_type['reference']})")

    print("\nDescription\n---")
    print(f"{app_type['description']}")

    print("\nLegislation\n---")
    legislation_urls = app_type['legislation'].split(";")
    for url in legislation_urls:
        print(url)

    if app_type.get("modules"):
        print(f"\n{len(app_type['modules'])} Modules\n---")
        for module in app_type["modules"]:
            print(f"{module['name']} (ref: {module['reference']})")
    
    if app_type.get("sub-types"):
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
