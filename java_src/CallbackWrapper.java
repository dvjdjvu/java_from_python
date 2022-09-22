package org.wherever.whatever;

// the wrapper interface
public interface CallbackWrapper {
    public boolean callback_call(String from);
    public void callback_call_end();
    public void callback_message(String from, String message);
}