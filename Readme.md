buildozer android debug && adb install -r ./bin/kivy_test*.apk

adb shell
run-as com.heattheatr.kivy_test

adb logcat | grep python