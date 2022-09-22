#!/usr/bin/python3
#-*- coding: utf-8 -*-

import kivy
kivy.require("2.1.0")
from kivy.app import App
from kivy.uix.button import Button

import jnius
from jnius import cast
from jnius import autoclass, PythonJavaClass, java_method

System = autoclass('java.lang.System')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
currentActivity = cast('android.app.Activity', PythonActivity.mActivity)

# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text ="Push Me !",
                   font_size ="20sp",
                   background_color = (1, 1, 1, 1),
                   color = (1, 1, 1, 1),
                   size_hint = (.2, .1),
                   pos_hint = {'x':.4, 'y':.45})

        # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        return btn

    # callback function tells when button pressed
    def callback(self, event):
        currentActivity.finishAndRemoveTask();
        System.exit(0);

##
#  Старт.
##
if __name__ == "__main__":
    # печать функций python
    print("Python: Hello world!")
    # Вызов метода печати из класса System.
    System.out.println('I/python: Java: Hello world!')

    # Вызов методов класса Test из Test.java
    Test = autoclass('some.kivy_test.Test')

    print("Python: ", Test().hello())

    ButtonApp().run()