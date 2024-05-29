import re
import numpy

from setuptools import setup, find_packages
from setuptools.extension import Extension



def version_number(path: str) -> str:
    """Get the version number from the src directory"""
    print("verison path is", path)

    exp = r'__version__[ ]*=[ ]*["\']([^"\']+)["\']'
    version_re = re.compile(exp)


    with open(path, 'r') as file:
        content = file.read()

    match = version_re.search(content)
    if match:
        version = match.group(1)
        print("version is", version)
        return version
    else:
        raise ValueError("Version number not found in the specified file")
        #return None

def load_requirements(filename):
    r"""
    load requirement and return the list
    """
    with open(filename, 'r') as file:
        return file.read().splitlines()


def main() -> None:
    version_path = "qubitchem/__version__.py"
    __version__ = version_number(version_path)
    if __version__ is None:
        raise ValueError("Version information not found in " + version_path)

    setup(
        name='QubitChem',
        version=__version__,
        author='Yu Zhang',
        author_email='zhyhku@gmail.com',
        description='Quantum Chemistry solvers on qubits',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/TBA',
        packages=find_packages(exclude=["examples", "docs", "tests", "tools", "setup.py"]),
        python_requires='>=3.6',
        install_requires=load_requirements("requirements.txt"),
    )

if __name__ == "__main__":
    main()
