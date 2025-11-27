# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
# import media keys
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
#add media keys as an extension?
#is this necessary? idk
keyboard.extensions.append(MediaKeys())

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
encoder_handler = EncoderHandler()
#none as third option (click) bcuz it's set as a key. 
encoder_handler.pins = ((board.GP9,board.GP8,None),)


# Define your pins here!
# 6 - Play previous
# 7 - Stop
# 5 - play next
# 10 - play/pause
PINS = [board.D6, board.D7, board.D5, board.D10]

encoder_handler.map = [
            ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN),),       
            ((KC.MW_UP, KC.MW_DN),),      
            ]

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