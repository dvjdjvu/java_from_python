package some.kivy_test;

// Обертка для python callback-ов
public interface CallbackWrapper {
    public void callback1();
    public boolean callback2(String arg1);
    public int callback3(int arg1, byte arg2);
}