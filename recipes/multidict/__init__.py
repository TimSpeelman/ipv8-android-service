from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class MultidictRecipe(CompiledComponentsPythonRecipe):
    version = '4.7.5'
    url = 'https://github.com/aio-libs/multidict/archive/v{version}.zip'
    depends = ['setuptools']

    site_packages_name = 'multidict'
    call_hostpython_via_targetpython = False


recipe = MultidictRecipe()
