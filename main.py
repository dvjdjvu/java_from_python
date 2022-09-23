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
# Класс оповещений событий из Java
##
class CallbackWrapper(PythonJavaClass):
    __javacontext__ = 'app'
    __javainterfaces__ = ['some/kivy_test/CallbackWrapper']

    def __init__(self):
        super().__init__()

    @java_method('()V')
    def callback1(self):
        print("Python: @java_method('()V')")

    @java_method('(Ljava/lang/String;)Z')
    def callback2(self, arg1):
        print("Python: @java_method('(Ljava/lang/String;)Z'), ", arg1)
        return True

    @java_method('(IB)I')
    def callback3(self, arg1, arg2):
        print("Python: @java_method('(IB)I'), ", arg1, arg2)
        return 555

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

    callback_wrapper = CallbackWrapper()
    test = Test(callback_wrapper)

    print("Python: ", test.hello())

    test.callback1()
    test.callback2()
    test.callback3()

    ButtonApp().run()
