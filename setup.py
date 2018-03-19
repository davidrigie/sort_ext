from setuptools import setup

setup(      name='sort_ext',
            version='0.1',
            description='sort folder by file extension',
            author='David Rigie',
            license='MIT',
            packages=['sort_ext'],
            entry_points = {
                  'console_scripts': ['sort_ext=sort_ext.command_line:main'],
            },
            zip_safe=False
    )