def get_module(ref, modules):
    matches = [module for module in modules if ref == module['reference']]
    if matches:
        return matches[0]
    return None


def get_modules(refs, modules):
    matched_modules = sorted([get_module(ref, modules) for ref in refs], key=lambda item: item['name'] if item else '')
    return matched_modules

