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
        print("\nModules\n---")
        for module in app_type["modules"]:
            print(f"{module['name']} ({module['reference']})")
