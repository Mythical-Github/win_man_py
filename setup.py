from setuptools import setup, find_packages

setup(
    name='win_man_py',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pygetwindow',
        'screeninfo',
        'log_py @ git+https://github.com/Mythical-Github/log_py.git',
    ],
    include_package_data=True,
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mythical-Github/win_man_py',
    author='Mythical',
    author_email='mythicaldata.com',
    license='GPL-3.0',
)
