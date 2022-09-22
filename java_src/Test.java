package some.kivy_test;

import some.kivy_test.CallbackWrapper;

public class Test {
    CallbackWrapper wrapper = null;

    public Test(CallbackWrapper callback_wrapper) {
        this.wrapper = callback_wrapper;
    }

    public String hello() {
        return "Hello from Test.java";
    }

    public void callback1() {
        this.wrapper.callback1();
    }

    public void callback2() {
        this.wrapper.callback2("callback");
    }

    public void callback3() {
        this.wrapper.callback3(11, '@');
    }

    public void callback4() {
        this.wrapper.callback4(11, (byte) 22);
    }
}
