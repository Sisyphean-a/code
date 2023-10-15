@echo off
::编码方式设置为utf-8
chcp 65001
::升级pip
echo 正在获取pip版本，若版本过低，会自动升级
python -m pip install --upgrade pip
echo.
:while
echo 正在获取需要升级的包。。。
echo.
::获取需要升级包的列表
pip list --outdated 
echo.
set /p input="请输入要升级的包:"
echo.
pip install --upgrade -i https://pypi.douban.com/simple  %input%
echo.
echo.
goto while

::pip-review --auto