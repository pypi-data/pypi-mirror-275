# LicenseLib
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Library for fetching licenses and dependencies.

# Install
```bash
python3 -m pip install --user licenselib
```

# Usage
Retrieve package info from PyPI:
```python
from licenselib import pypi, License

pkg = pypi.get_package('licenselib')
print(pkg) # all pkg data

dependencies = pkg.dependencies
print(dependencies) # pkg dependencies as list including version

# for locally installed packages you may use:
license: License = get_local_licenses(['requests'])[0]
print(license) # license metadata
print(license.licensetext) # full licensetext

# for remote packages you could use: (note: this will install the package temporarily though!)
license: License = get_licenses_unsafe(['django'])[0]
print(license)
print(license.licensetext)
```
Retrieve packages from GitHub
```python
from licenselib import github, License

# get github repo
repo = github.get_repo(owner='django', name='django') # like this
repo = github.get_repo(url='https://github.com/django/django') # or like this

dependencies = repo.dependencies
print(dependencies) # repo dependencies
print(dependency.name for dependency in repo.dependencies) # repo dependencies names as list

# get license
license: License = repo.license
print(license)
print(license.licensetext)

# or get even more data
license_data = repo.get_license()
print(license_data) # all license data
```
