from licenselib.utils import DataContainer
from licenselib.license import License
import requests
import base64


class Repository(DataContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name, self.owner = self.full_name.split('/')

    def get_license(self) -> DataContainer | None:
        url = f'https://api.github.com/repos/{self.owner}/{self.name}/license'
        response = requests.get(url)
        if response.status_code == 200:
            license = DataContainer(**response.json())
            license.content = None if not license.content else base64.b64decode(license.content.replace('\n', ''))
            return license
        return None

    @property
    def license(self) -> License | None:
        license = self.get_license()
        if not license:
            return None

        pkg_name = f'{self.owner}/{self.name}'
        pkg_version = None
        license_name = license.license.key
        license_text = license.content
        return License(pkg_name, pkg_version, license_name, license_text)



    @license.setter
    def license(self, value) -> None:
        pass



def get_repo(url: str | None = None, owner: str | None = None, name: str | None = None) -> Repository | None:
    """
    Get repository either using the url or owner and name

    :param url: reporisoty url
    :param owner: owner of the repository
    :param name: name of the repository
    :return: repository or None on if not found
    """
    if url:
        return get_repo_from_url(url)
    elif owner and name:
        return get_repo_from_owner(owner, name)
    raise ValueError('Either url or owner and name must be provided')


def get_repo_from_url(url: str) -> Repository | None:
    """
    Get repository from url

    :param url: repository url
    :return: repository or None on if not found
    """
    url = f'https://api.dalicc.net/githublicensechecker/dependencies?github_url={requests.utils.quote(url)}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if not data.get('error'):
            return Repository(**data)
    return None


def get_repo_from_owner(owner: str, name: str) -> Repository | None:
    """
    Get repository using owner name and repo name

    :param owner: owner of the repository
    :param name: name of the repository
    :return: repository or None on if not found
    """
    url = f'https://api.dalicc.net/githublicensechecker/dependencies/{requests.utils.quote(owner)}/{requests.utils.quote(name)}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if not data.get('error'):
            return Repository(**data)
    return None


if __name__ == '__main__':
    # run some tests
    from rich import print
    def test(i): print(f'\n[bold green]TESTCASE #{i}:[/]')

    test(1)
    #repo = get_repo(url='https://github.com/django/django')
    #print(repo.full_name)

    test(2)
    #repo = get_repo(owner='django', name='django')
    #print(repo.full_name)

    test(3)
    #print(get_repo(url='https://github.com/django/non_existent_repo'))

    test(4)
    #print(get_repo(owner='django', name='non_existent_repo'))

    test(5)
    repo = get_repo(url='https://github.com/django/django')
    print(dependency.name for dependency in repo.dependencies)

    test(6)
    #repo = get_repo(owner='TeamSmil3y', name='PigeonPost')
    #print(repo.license)

    test(7)
    repo = get_repo(owner='django', name='django')
    print(repo.license)