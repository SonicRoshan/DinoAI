import keyboard




def key_check(key):
    if keyboard.is_pressed(key):
        return True
    return False


if __name__ == '__main__':
    key_check()

