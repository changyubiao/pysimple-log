# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import re

with io.open('README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

with io.open("simplelog/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__\s*=\s*'(.*?)'", f.read()).group(1)


print(f"version = {version!r}")

setup(
    name="pysimple-log",
    license='Apache License 2.0',
    version=version,
    packages=find_packages("simplelog"),
    zip_safe=False,
    include_package_data=True,
    package_dir={"": "simplelog"},
    long_description=long_description,
    url='https://github.com/changyubiao/pysimple-log.git',
    author='frank',
    author_email='frank.chang@lexisnexis.com',
    description='simple log configuration',

    project_urls={
        "Code": "https://github.com/changyubiao/pysimple-log.git",
    },

    python_requires='>=3.0',
    install_requires=[
        "concurrent-log-handler>=0.9.16"

    ],

    classifiers=[

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache License 2.0',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
