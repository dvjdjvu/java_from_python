package some.kivy_test;

// Подключение интерфейса CallbackWrapper из CallbackWrapper.java
import some.kivy_test.CallbackWrapper;


/**
	\brief Тестовый класс.

	Содержит набор методов, вызываемые из python и в python (main.py).
*/
public class Test {
    CallbackWrapper wrapper = null;

    /**
        Конструктор класса
        \param callback_wrapper указатель на callback_wrapper из main.py
        \return Сумму двух чисел, переданных в качестве аргументов
    */
    public Test(CallbackWrapper callback_wrapper) {
        this.wrapper = callback_wrapper;
    }

    /**
        Функция возврата строки
        \return Возвращает строку
    */
    public String hello() {
        return "Hello from Test.java";
    }

    /**
        Функция возврата строки
        \param arg1 строка
        \return Возвращает строку
    */
    public String hello2(String arg1) {
        return arg1;
    }

    /**
        Функция вызова callback1 из callback_wrapper (main.py)
    */
    public void callback1() {
        this.wrapper.callback1();
    }

    /**
        Функция вызова callback2 из callback_wrapper (main.py)
    */
    public void callback2() {
        this.wrapper.callback2("callback");
    }

    /**
        Функция вызова callback3 из callback_wrapper (main.py)
    */
    public void callback3() {
        this.wrapper.callback3(11, (byte) 22);
    }
}
