from datetime import datetime
import os
import csv
from pathlib import Path


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


def check_modules(modules, modules_dir, app_mod_joins):
    modules_with_refs = [m for m in modules if m.get("reference")]
    modules_with_end_date = [m for m in modules if m.get("end-date")]
    
    print(f"\nModule Statistics\n---")
    print(f"Total modules: {len(modules)}")
    print(f"Modules with references: {len(modules_with_refs)}")
    print(f"Modules with end dates: {len(modules_with_end_date)}")
    
    # Check for ended modules still referenced in active joins
    print(f"\nChecking module joins\n---")
    ended_module_refs = {m['reference'] for m in modules_with_end_date if m.get('reference')}
    problematic_joins = [join for join in app_mod_joins 
                        if not join.get('end-date') and  # Join is still active
                        join['application-module'] in ended_module_refs]  # References an ended module
    
    if problematic_joins:
        print("\nWARNING: Found active joins referencing ended modules:")
        for join in problematic_joins:
            print(f"  {join['reference']}: {join['application-type']} -> {join['application-module']}")
    else:
        print("All module joins are valid")
    
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


def check_codelists(modules, codelist_file="../data/codelists.csv", codelist_dir="../specification/codelist"):
    print("\nChecking codelists\n---")
    
    # Get all module references
    valid_module_refs = {m['reference'] for m in modules if m.get('reference')}
    
    missing_modules = []
    invalid_module_refs = []
    missing_markdown = []
    
    with open(codelist_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        for row in rows:
            if not row.get('end-date'):  # Only check active entries
                # Check for markdown file
                if row.get('reference'):
                    markdown_file = os.path.join(codelist_dir, f"{row['reference']}.md")
                    if not os.path.exists(markdown_file):
                        missing_markdown.append(row)

                modules_str = row.get('modules', '').strip()
                
                # Check if modules field is empty
                if not modules_str:
                    missing_modules.append({
                        'codelist': row.get('name'),
                        'reference': row.get('reference')
                    })
                    continue
                
                # Check each module reference is valid
                module_refs = [ref.strip() for ref in modules_str.split(';') if ref.strip()]
                invalid_refs = [ref for ref in module_refs if ref not in valid_module_refs]
                
                if invalid_refs:
                    invalid_module_refs.append({
                        'codelist': row.get('name'),
                        'reference': row.get('reference'),
                        'invalid_refs': invalid_refs
                    })
    
    if missing_modules:
        print("\nCodelist(s) missing module references:")
        for item in missing_modules:
            print(f"  Codelist: {item['codelist']}, Ref: {item['reference']}")
            
    if invalid_module_refs:
        print("\nCodelist(s) with invalid module references:")
        for item in invalid_module_refs:
            print(f"  Codelist: {item['codelist']}, Ref: {item['reference']} - Invalid module(s) = {', '.join(item['invalid_refs'])}")

    if missing_markdown:
        print("\nCodelist(s) missing markdown files:")
        for item in missing_markdown:
            print(f"  Codelist: {item['name']}, Ref: {item['reference']}")

    if not missing_modules and not invalid_module_refs and not missing_markdown:
        print("All codelists are valid!")
