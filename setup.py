from distutils.core import setup
import pathlib


with open('README.md') as file:
    readme = file.read()


setup(name='Py Natural Simulation',
    version='0.1.0',
    description="Python version of Khan Academy's Advanced JS: Natural Simulations Course",
    author='Jay Ess',
    url='https://github.com/jay3ss/py-natural-simulations',
    license='GPL3',
    py_modules=['walker'],
    long_description=readme
)
