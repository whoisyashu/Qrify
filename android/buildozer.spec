# This is the buildozer.spec file for your Kivy app

[app]
# (str) Title of your application
title = QRify

# (str) Package name (should be a unique name, in reverse domain notation)
package.name = qrify

# (str) Package domain (use your own domain, e.g., org.yash)
package.domain = org.yash

# (str) Application version
version = 1.0

# (list) Application requirements
# Example: "kivy", "pillow", "sqlalchemy", etc.
# Separate each dependency with a comma.
# Make sure to include all the libraries you need, e.g., kivy, kivymd, qrcode
requirements = python3,kivy,kivymd,qrcode

# (list) Source files to include in the package
# Include all your necessary files (like .kv files, .py, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (str) Icon for the application (must be a .png file)
icon.filename = %(source.dir)s/icon.png

# (str) Main python file (the entry point of your app)
# Make sure this is set to the file where your Kivy app starts
# For example, if your main file is `main.py`, you can leave it as it is.
source.include_patterns = main.py

[buildozer]
# (int) Target platform to build for
target = android

# (str) Android API level to target (e.g., 29 for Android 10, or 21 for Lollipop)
android.api = 29

# (str) Minimum Android API level to support (e.g., 21)
android.minapi = 21

# (str) Android SDK version (the default is 25)
android.sdk = 25

# (str) Android NDK version (the default is 19b)
android.ndk = 19b

# (bool) Whether to generate debug APKs or release APKs
# Set to True to generate debug APKs, False for release
android.debug = True

# (str) Path to the Java SDK
# This is generally set up automatically, but if you encounter issues,
# you can specify the path manually.
# android.javasdk = /path/to/java_sdk

# (str) Path to the Android SDK
# This is generally set up automatically, but if you encounter issues,
# you can specify the path manually.
# android.sdk_path = /path/to/android_sdk

# (str) Path to the Android NDK
# This is generally set up automatically, but if you encounter issues,
# you can specify the path manually.
# android.ndk_path = /path/to/android_ndk

# (str) Full path to the .apk file you want to generate
# This is where your APK will be saved after the build
# You generally don't need to change this path.
# android.apkanalysis = %(buildozer.dir)s/bin/

# (bool) Whether or not to include a splash screen
android.splashscreen = True

# (str) Full path to the .apk icon
android.icon = %(source.dir)s/icon.png

# (bool) Enable Android permissions required by your app
# For instance, if your app uses the camera or internet, you will need to add those permissions
android.permissions = INTERNET, CAMERA
