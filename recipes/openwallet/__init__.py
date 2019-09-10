from __future__ import absolute_import

from os import getenv
from os.path import exists, join

from pythonforandroid.recipe import PythonRecipe, current_directory
from sh import cp, mkdir


class OpenWalletRecipe(PythonRecipe):
    """
    Python-for-Android OpenWallet recipe
    """

    url = 'git+https://github.com/TimSpeelman/OpenWallet.git'

    depends = ['ipv8', 'python2', 'twisted']

    patches = []

    python_depends = ['requests', 'tinydb']

    site_packages_name = 'openwallet'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(OpenWalletRecipe, self).postbuild_arch(arch)

        # # Install twistd plugins
        # cp('-rf', join(self.get_build_dir(arch.arch), 'twisted', 'plugins'),
        #    join(self.ctx.get_python_install_dir(), 'twisted'))

        # # Copy ipv8_service.py
        # cp('-rf', join(self.get_build_dir(arch.arch), 'ipv8_service.py'),
        #    self.ctx.get_python_install_dir())


recipe = OpenWalletRecipe()
