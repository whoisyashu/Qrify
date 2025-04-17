[app]

# (str) Title of your application
title = Qrify

# (str) Package name
package.name = com.yash.Qrify

# (str) Package version
version = 1.0.0

# (str) Application description
description = A simple Kivy app for Android

# (list) Application requirements
# You can add more libraries if your app uses other dependencies
# For example: requirements = python3,kivy,someotherlibrary
requirements = python3,kivy

# (list) Application source includes (e.g., .py files, images, and other assets)
source.include_exts = py,png,jpg,kv,atlas

# (str) Path to your application source code
# If your main file is located in the current directory (i.e. where this spec is)
source.include_dirs = .

# (str) Application entry point. This is the name of the Python file that starts the app.
# For example, if your entry point file is "main.py", you would use:
# main.source = main.py
main.source = main.py

# (bool) Indicate whether the app requires a full-screen mode
fullscreen = 1

# (str) Icon for the app
# icon.filename = %(source.dir)/icon.png

# (str) The directory where the app will be packaged
# e.g., /path/to/app
# source.include_dirs = .

[buildozer]

# (str) The directory where the buildozer configuration file is located
# The default is where you execute buildozer command.
# buildozer.spec = buildozer.spec

# (str) The name of the directory where the build is created
# This is the directory containing the apk file once the build is complete
# output_dir = build

# (str) Path to the android SDK
# android.sdk_path = /path/to/sdk

# (str) Path to the android NDK
# android.ndk_path = /path/to/ndk

# (str) Android API version to target
# (use 'android.api = 29' for Android 10 or 'android.api = 21' for Android 5.0)
android.api = 29

# (int) Android NDK version to use
# (leave blank to let buildozer select the NDK version)
# android.ndk = 21b

# (str) Java package name
# android.package = org.mycompany.myapp

# (list) Android permissions required by the app
# android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (str) The minimum Android API the app is supported on
# android.minapi = 21

# (str) The target Android API the app should be built for
# android.target = 29

# (bool) Set to True to generate a debug APK instead of a release APK
android.debug = True

# (bool) Set to False to generate a release APK
# android.release = False

[dependencies]
# Add any external dependencies here
# dependencies = libpng, libjpeg, etc.

