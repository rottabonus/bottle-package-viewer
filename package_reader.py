import re
import os

def return_packages_info():
    packages_str = read_file_to_string()
    all_packages_raw = packages_str.rstrip().split("\n\n")
    all_packages = {}
    reverse_depends_dict = {}
    for package in all_packages_raw:
        name = extract_name(package)
        description = extract_description(package)
        depends = extract_dependencies(package)
        reverse_depends_dict = update_reverse_depends_dictionary(depends, name, reverse_depends_dict)
        all_packages[name] = { 'description': description, 'depends': depends }
    return { 'packages': all_packages, 'reverse_depends_dict': reverse_depends_dict }

def read_file_to_string():
    if os.name == 'nt':
        f = open('status.real', 'r', encoding='utf8') #use mock data and encoding ut8 on windows
    else:
        f = open('/var/lib/dpkg/status', 'r')
    packages_str = f.read()
    f.close()
    return packages_str

def extract_name(packageStr):
    match = re.search('(?<=^Package: ).*', packageStr, re.MULTILINE)
    return match.group(0)

def extract_description(packageStr):
    search = 'Description: '
    split_integer = packageStr.find(search)
    splitted_string = packageStr[(split_integer+len(search)):len(packageStr)]
    line_array = splitted_string.split("\n")
    descriptions = []
    for line in line_array:
        if re.search('(^\w+)', line) is None:
            descriptions.append(line)
    return descriptions
    
def extract_dependencies(packageStr):
    match = re.search('(?<=^Depends: ).*', packageStr, re.MULTILINE)
    dependencies = []
    if match is not None:
        depends_with_versions = match.group(0).split(',')
        for dep in depends_with_versions:
            alt_deps = dep.split('|')
            for d in alt_deps:
                dependencies.append(d.strip().split(' ')[0])
    else:
        return []
    return set(dependencies)

def update_reverse_depends_dictionary(depends, current_package, dictionary):
    for depend in depends:
        if depend in dictionary.keys():
            dictionary[depend].append(current_package)
        else:
            dictionary[depend] = [current_package]
    return dictionary

print(return_packages_info())
