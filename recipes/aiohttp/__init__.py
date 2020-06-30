from pythonforandroid.recipe import CythonRecipe

class AioHTTPRecipe(CythonRecipe):
    version = '3.6.2'
    url = 'https://github.com/aio-libs/aiohttp/archive/v{version}.zip'
    depends = ['setuptools', 'multidict']
    python_depends = ['attrs', 'chardet', 'yarl', 'async-timeout']

    site_packages_name = 'aiohttp'
    call_hostpython_via_targetpython = False

recipe = AioHTTPRecipe()
