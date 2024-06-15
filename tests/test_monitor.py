from pynput.keyboard import Key, Listener, HotKey


def show(key):

    print("\nYou Entered {0}".format(key))

    if key == Key.delete:
        # Stop listener
        return False


def on_activated():
    print("Hot key pressed!")


def for_canonical(f):
    return lambda k: f(hot_key_listener.canonical(k))


hotkey = HotKey(keys=HotKey.parse("<ctrl>+<alt>+h"), on_activate=on_activated)

# Collect all event until released
# common_key_listener = Listener(on_press=show)
# hot_key_listener = Listener(on_press=hotkey.press)

with Listener(on_press=show) as common_key_listener:
    with Listener(on_press=for_canonical(hotkey.press)) as hot_key_listener:
        common_key_listener.join()
        hot_key_listener.join()

# fadfafafa
