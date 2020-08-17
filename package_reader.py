import re
import os

def return_packages_info():
    packages_str = read_file_to_string(file_depending_on_os())
    all_packages_raw = packages_str.rstrip().split("\n\n")
    all_packages = []
    reverse_depends_dict = {}
    for package in all_packages_raw:
        name = extract_name(package)
        description = extract_description(package)
        depends = extract_dependencies(package)
        reverse_depends_dict = update_reverse_depends_dictionary(depends, name, reverse_depends_dict)
        all_packages.append({ 'name': name, 'description': description, 'depends': depends })
    return { 'packages': all_packages, 'reverse_depends_dict': reverse_depends_dict }

def file_depending_on_os():
    if os.name == 'nt':
        return 'status.real' #if on windows, use mock-data
    else:
        return '/var/lib/dpkg/status'

def read_file_to_string(filename):
    f = open(filename, 'r', encoding='utf8')
    packages_str = f.read()
    f.close()
    return packages_str

def extract_name(packageStr):
    match = re.search('(?<=Package: ).*', packageStr)
    return match.group(0)

def extract_description(packageStr):
    match = re.search('(?<=Description: ).*', packageStr)
    return match.group(0)

def extract_dependencies(packageStr):
    match = re.search('(?<=Depends: ).*', packageStr)
    dependencies = []
    if match is not None:
        depends_with_versions = match.group(0).split(',') 
        for dep in depends_with_versions:
            dependencies.append(dep.strip().split(' ')[0])
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