# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# from __future__ import absolute_import
# from __future__ import unicode_literals
# import os

# from setuptools import setup, find_packages

# try:
#     with open('README.rst') as f:
#         readme = f.read()
# except IOError:
#     readme = ''

# def _requires_from_file(filename):
#     return open(filename).read().splitlines()

# # version
# here = os.path.dirname(os.path.abspath(__file__))
# version = next((line.split('=')[1].strip().replace("'", '')
#                 for line in open(os.path.join(here,
#                                               'reverse_string003',
#                                               '__init__.py'))
#                 if line.startswith('__version__ = ')),
#                '0.0.dev0')

# setup(
#     name="pypipkg",
#     version=version,
#     url='https://github.com/haru0039633/reverse_string',
#     author='haruuuu003',
#     author_email='s2222101@stu.musashino-u.ac.jp ',
#     maintainer='haruuuu003',
#     maintainer_email='s2222101@stu.musashino-u.ac.jp ',
#     description='Package Dependency: Validates package requirements',
#     long_description=readme,
#     packages=find_packages(),
#     install_requires=_requires_from_file('requirements.txt'),
#     license="MIT",
#     classifiers=[
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.3',
#         'Programming Language :: Python :: 3.4',
#         'License :: OSI Approved :: MIT License',
#     ],
#     entry_points="""
#       # -*- Entry points: -*-
#       [console_scripts]
#       pkgdep = pypipkg.scripts.command:main
#     """,
# )

from setuptools import setup, find_packages

setup(
    name='my_reverse_string',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    author='haruuuu003',
    author_email='s2222101@stu.musashino-u.ac.jp',
    description='Function to invert a string',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/haru0039633/my_reverse_string',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

