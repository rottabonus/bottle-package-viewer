def return_packages_list():
    f = open('/var/lib/dpkg/status', 'r')
    packages_str = f.read()
    f.close()
    all_packages = packages_str.split("\n\n")
    return len(all_packages)
