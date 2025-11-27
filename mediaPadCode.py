# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# import media keys
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
#add media keys as an extension?
keyboard.extensions.append(MediaKeys())

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
# 6 - Play previous
# 7 - Stop
# 5 - play next
# 10 - play/pause
PINS = [board.D6, board.D7, board.D5, board.D10]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MEDIA_PREV_TRACK, KC.MEDIA_STOP	, KC.MEDIA_NEXT_TRACK, KC.MEDIA_PLAY_PAUSE,]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()