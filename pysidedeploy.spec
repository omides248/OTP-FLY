[app]
# title of your application
title = OTPFLY
# project directory. the general assumption is that project_dir is the parent directory
# of input_file
project_dir = .
# source file path
input_file = D:\w_omid_old\Projects\otp-fly\app.py
# directory where exec is stored
exec_directory = .
# path to .pyproject project file
#project_file = 
# application icon
icon = D:\w_omid_old\Projects\otp-fly\otpfly.ico

[python]
# python path
python_path = D:\w_omid_old\Projects\venv3.11\Scripts\python.exe
# python packages to install
# ordered-set = increase compile time performance of nuitka packaging
# zstandard = provides final executable size optimization
packages = nuitka==1.8.0,ordered_set,zstandard,pyotp==2.9.0,cryptography==42.0.5
# buildozer = for deploying Android application
android_packages = buildozer==1.5.0,cython==0.29.33

[qt]
# comma separated path to qml files required
# normally all the qml files required by the project are added automatically
# excluded qml plugin binaries
excluded_qml_plugins = QtCharts,QtQuick3D,QtSensors,QtTest,QtWebEngine
qml_files = app.qml,lib\view\AccountDelegate.qml,lib\view\AddAccountDialog.qml,lib\view\DeleteAccountDialog.qml,lib\view\ProgressCircle.qml,lib\view\menu_bar\MenuBar.qml,lib\view\menu_bar\MyToolBar.qml,test\downloader2\App.qml

[android]
# path to pyside wheel
#wheel_pyside = 
# path to shiboken wheel
#wheel_shiboken = 
# plugins to be copied to libs folder of the packaged application. comma separated
#plugins = platforms_qtforandroid

[nuitka]
# (str) specify any extra nuitka arguments
# eg = extra_args = --show-modules --follow-stdlib
extra_args = --quiet --noinclude-qt-translations --disable-console
# --include-data-files = view\*.qml

[buildozer]
# build mode
# possible options = [release, debug]
# release creates an aab, while debug creates an apk
mode = debug
# contrains path to pyside6 and shiboken6 recipe dir
recipe_dir = 
# path to extra qt android jars to be loaded by the application
jars_dir = 
# if empty uses default ndk path downloaded by buildozer
ndk_path = 
# if empty uses default sdk path downloaded by buildozer
sdk_path = 
# modules used. comma separated
modules = 
# other libraries to be loaded. comma separated.
# loaded at app startup
local_libs = plugins_platforms_qtforandroid
# architecture of deployed platform
# possible values = ["aarch64", "armv7a", "i686", "x86_64"]
arch = 

