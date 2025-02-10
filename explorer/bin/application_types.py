def print_all(app_types):
    print("===")
    print("All application types")
    print("===")
    for app in app_types:
        print(f"{app['name']} (ref: {app['reference']})")


def overview(app_type):
    print("Application type")
    print("===")
    print(f"{app_type['name']} (ref: {app_type['reference']})")

    print("\nDescription")
    print("===")
    print(f"{app_type['description']}")

    print("\nLegislation")
    print("===")
    legislation_urls = app_type['legislation'].split(";")
    for url in legislation_urls:
        print(url)
