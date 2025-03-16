from datetime import datetime
import os


def get_module(ref, modules):
    matches = [module for module in modules if ref == module['reference']]
    if matches:
        return matches[0]
    return None


def get_modules(refs, modules):
    matched_modules = sorted([get_module(ref, modules) for ref in refs], key=lambda item: item['name'] if item else '')
    return matched_modules


# a join helper to making sure we have all the right app-types and modules joins
def get_expected_joins(app_type, modules_in_form, all_modules):
    exp_app_mod_joins = []
    for module in modules_in_form:
        if module.get('reference') and not module.get('replaced-by'):
            exp_app_mod_joins.append((app_type, module['reference'], "original"))
        else:
            # check if replacement is in list of all modules
            if module.get('replaced-by') in [m['reference'] for m in all_modules]:
                exp_app_mod_joins.append((app_type, module['replaced-by'], "replaced"))
            else:
                print(f"Don't not recognise replacement module: {module.get('name')} replaced by {module.get('replaced-by')}")
    return exp_app_mod_joins


def get_module_discussion_url(module):
    discussion_number = module['discussion-number'].lstrip('#')
    return f"https://github.com/digital-land/planning-application-data-specification/discussions/{discussion_number}"


def join_data_maker(expected_joins, all_joins):
    today = datetime.today().strftime('%Y-%m-%d')
    matched_joins = []
    missing_joins = []
    # make sure we have all the expected joins
    for exp_join in expected_joins:
        match_found = False
        for existing_join in all_joins:
            if exp_join[0] == existing_join['application-type'] and exp_join[1] == existing_join['application-module']:
                matched_joins.append(existing_join)
                match_found = True
                break
        if not match_found:
            missing_joins.append(exp_join)
    print(f"\n----------\n{len(matched_joins)} existing joins\n")
    print(f"{len(missing_joins)} missing joins\n")
    for _join in missing_joins:
        print(f"{_join[0]}-{_join[1]},{_join[0]},{_join[1]},{today},,")
    return


def check_modules(modules, modules_dir):
    modules_with_refs = [m for m in modules if m.get("reference")]
    modules_with_end_date = [m for m in modules if m.get("end-date")]
    
    print(f"\nModule Statistics\n---")
    print(f"Total modules: {len(modules)}")
    print(f"Modules with references: {len(modules_with_refs)}")
    print(f"Modules with end dates: {len(modules_with_end_date)}")
    
    print(f"\nChecking markdown files\n---")
    missing_files = []
    for module in modules_with_refs:
        expected_file = os.path.join(modules_dir, f"{module['reference']}.md")
        if not os.path.exists(expected_file):
            missing_files.append(module['reference'])
            
    if missing_files:
        print(f"\nMissing markdown files ({len(missing_files)}):")
        for ref in missing_files:
            print(f"  {ref}.md")
    else:
        print("All modules with references have corresponding markdown files")
