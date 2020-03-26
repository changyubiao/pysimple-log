# -*- coding: utf-8 -*-
from setuptools import setup, find_namespace_packages
import io
import re

with io.open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

with io.open("simplelog/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__\s*=\s*'(.*?)'", f.read()).group(1)

print(f"version = {version!r}")
# print(long_description)

setup(
    name="pysimple-log",
    license='Apache License 2.0',
    version=version,
    packages=find_namespace_packages(include=["simplelog.*", "simplelog"]),
    zip_safe=False,
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/changyubiao/pysimple-log.git',
    author='frank',
    author_email='15769162764@163.com',
    description='simple log configuration',

    project_urls={
        "Code": "https://github.com/changyubiao/pysimple-log.git",
    },

    python_requires='>=3.0',
    install_requires=[
        "concurrent-log-handler>=0.9.16"

    ],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Logging",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
