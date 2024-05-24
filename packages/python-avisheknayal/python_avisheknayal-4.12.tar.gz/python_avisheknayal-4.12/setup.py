from setuptools import setup, find_packages
setup(
    name="python_avisheknayal",
    version="4.12",
    packages=find_packages(),
    install_requires=[
        #Add dependencies
    ],
    py_modules=["sample"],
    package_dir={'':'sample/src'},
)