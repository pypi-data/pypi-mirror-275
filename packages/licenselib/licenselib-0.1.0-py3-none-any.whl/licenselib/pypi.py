from licenselib.license import License
from licenselib.utils import DataContainer
import piplicenses
import piplicenses_lib
import requests
import pip
import importlib


class Package(DataContainer):
    @property
    def dependencies(self) -> list | None:
        """
        Grab dependencies

        :return: List of dependencies or None if not found
        """
        if hasattr(self, 'info') and hasattr(self.info, 'requires_dist') and isinstance(self.info.requires_dist, list):
            return self.info.requires_dist
        else:
            return None


def api_call(pkg_name: str) -> dict | None:
    """
    Performs an api call to the PyPI API for the given package

    :param pkg_name: Name of the package
    :return: dict of json data or None on failure
    """
    url = f'https://pypi.org/pypi/{requests.utils.quote(pkg_name)}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    return None


def api_call_version(pkg_name: str, pkg_release: str) -> dict | None:
    """
    Performs an api call to the PyPI API for the given package and release

    :param pkg_name: Name of the package
    :param pkg_release: Release of the package
    :return: dict of json data or None on failure
    """

    pkg_data = api_call(pkg_name)
    if not pkg_data:
        return None

    return pkg_data['releases'].get(pkg_release)


def packages_installed(pkg_names: list[str]) -> list[bool]:
    """
    Checks whether given packages are installed

    :param pkg_names: Package names to check
    :return: List of states, whether a package is installed or not (True or False)
    """
    lower_pkg_names = [pkg_name.lower() for pkg_name in pkg_names]
    packages = [package.get('name').lower() for package in get_local_packages()]
    exists = list()
    for pkg_name in pkg_names:
        exists.append(pkg_name.lower() in lower_pkg_names)
    return exists



def get_licenses_unsafe(pkg_names: list[str], mute=False) -> list[License]:
    """
    .. Warning:: Installs packages for a brief period of time if not already installed!

    Attempts to retrieve the licenses for a package whether installed or not.
    Does this by installing packages not already installed and then calls get_local_licenses(...)

    :param pkg_names: Package names
    :return: List of licenses or None on failure
    """
    # check if package is installed
    exists = list()
    for pkg_name in pkg_names:
        exists.append(True if importlib.util.find_spec(pkg_name) else False)

    # install missing packages
    for pkg_name, pkg_exists in zip(pkg_names, exists):
        if not pkg_exists:
            if not mute: print(f'installing package {pkg_name} since it\'s not installed and unsafe function is called')
            pip.main(['install', '--user', '--break-system-packages', pkg_name])

    licenses = get_local_licenses(pkg_names=pkg_names)

    # uninstall packages
    for pkg_name, pkg_exists in zip(pkg_names, exists):
        if not pkg_exists:
            if not mute: print(f'uninstalling package {pkg_name} after gathering license data')
            pip.main(['uninstall', '-y', '--break-system-packages', pkg_name])

    return licenses


def get_local_licenses(pkg_names: list[str]) -> list[License]:
    """
    Attempts to retrieve the licenses for given local packages.

    :param pkg_names: Package names
    :return: List of local licenses or None on failure
    """
    lower_pkg_names = [pkg_name.lower() for pkg_name in pkg_names]
    packages = get_local_packages()
    licenses = list()
    for package in packages:
        if (name:=package.get('name')).lower() in lower_pkg_names:
            licenses.append(License(
                pkg_name=name,
                pkg_version=package.get('version'),
                license=package.get('license'),
                licensetext=package.get('licensetext')
            ))
    return licenses


def get_local_packages() -> list[dict]:
    """
    Retrieves a list of package data for all packages installed on the system.

    :return: list of package data
    """
    return list(piplicenses_lib.get_packages(from_source=piplicenses.FromArg.MIXED))


def get_package(pkg_name: str) -> Package | None:
    """
    Retrieves the package info from the PyPI API

    :param pkg_name: Name of the package
    :return: Package or None on failure
    """
    pkg_data = api_call(pkg_name)
    if not pkg_data:
        return None

    pkg = Package(name=pkg_name, **pkg_data)
    return pkg


if __name__ == '__main__':
    # run some tests
    from rich import print
    def test(i): print(f'\n[bold green]TESTCASE #{i}:[/]')

    test(1)
    pkg = get_package('PyDooray')
    print(pkg.dependencies)

    test(2)
    pkg = get_package('requests')
    print(pkg.dependencies)

    test(3)
    print(get_package('non_existent_package'))

    test(4)
    license: License = get_local_licenses(['requests'])[0]
    print(license)
    print(license.licensetext)

    test(5)
    license = get_licenses_unsafe(['django'])[0]
    print(license)
    print(license.licensetext)
