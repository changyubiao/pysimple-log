#!/usr/bin/env bash

# activate your virtual environment

# 检查打包文件
echo " begin  python setup.py check  "
python setup.py  check

# 打包
echo " begin  python setup.py sdist bdist_wheel "
python setup.py sdist bdist_wheel

# 发布包
echo " begin twine upload dist/*  "
twine upload dist/*


