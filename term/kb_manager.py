from pynput import keyboard
pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)

    # Ctrl gauche ou droit + q
    if (
        (keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys)
        and hasattr(key, 'char')
        and key.char == 'q'
    ):
        return False
    # elif (
    #     (keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys)
    #     and hasattr(key, 'char')
    #     and key.char == 'w'
    # ):


def on_release(key):
    pressed_keys.discard(key)

def start_kb_listening():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
