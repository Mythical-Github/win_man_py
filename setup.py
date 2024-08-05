from setuptools import setup, find_packages

setup(
    name='python_window_management',
    version='0.1',
    packages=find_packages(),  # This will automatically include the python_window_management package and subpackages
    install_requires=[
        'pygetwindow',
        'screeninfo',
        'python_logging @ git+https://github.com/Mythical-Github/python_logging.git',
    ],
    include_package_data=True,
    description='A Python module for managing and manipulating windows with advanced logging capabilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/python_window_management',  # Updated URL to match your current package
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL-3.0',
)
