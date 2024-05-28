class License:
    def __init__(self, pkg_name: str, pkg_version: str | None, license: str | None, licensetext: str | None):
        # name of package
        self.pkg_name: str = pkg_name
        # (release) version of package
        self.pkg_version: str | None = pkg_version
        # short description of license (e.g. GNU/GPL3, CC ZERO, MIT, ...)
        self.license: str | None = license
        # full license text
        self.licensetext: str | None = licensetext

    def __repr__(self):

        return (f'{type(self).__name__}(pkg_name={self.pkg_name}, pkg_version={self.pkg_version}, '
                f'license={self.license}, licensetext={None if not self.licensetext else f"\'...\'"})')