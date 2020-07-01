from __future__ import absolute_import

from os import getenv
from os.path import exists, join

from pythonforandroid.recipe import PythonRecipe, current_directory
from sh import cp, mkdir


class OpenWalletRecipe(PythonRecipe):
    """
    Python-for-Android OpenWallet recipe
    """

    url = 'git+https://github.com/TimSpeelman/ow-android.git'

    depends = ['ipv8']

    patches = []

    python_depends = []

    site_packages_name = 'openwallet'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(OpenWalletRecipe, self).postbuild_arch(arch)

        print("OpenWalletRecipe postbuild")

        # Copy static files (should not be needed right?)
        cp('-rf', join(self.get_build_dir(arch.arch), 'ow_service', 'static'),
           join(self.ctx.get_python_install_dir(), 'ow_service', 'static'))

        # Copy openwallet_service.py
        cp('-rf', join(self.get_build_dir(arch.arch), 'ow_service.py'),
           self.ctx.get_python_install_dir())


recipe = OpenWalletRecipe()
