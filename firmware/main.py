from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.quickpin.pro_micro import pins

keyboard = KMKKeyboard()

# ---------- DIRECT KEYS ----------
keyboard.col_pins = ()
keyboard.row_pins = ()

keyboard.direct_pins = (
    pins.GP0,  # SW1
    pins.GP1,  # SW2
    pins.GP2,  # SW3
    pins.GP3,  # SW4
)

# ---------- KEYMAP ----------
keyboard.keymap = [
    [
        KC.MEDIA_PLAY_PAUSE,
        KC.MEDIA_PREV_TRACK,
        KC.MEDIA_NEXT_TRACK,
        KC.MEDIA_STOP,
    ]
]

# ---------- ROTARY ENCODER ----------
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (pins.GP4, pins.GP5),  # Encoder A, B
)

encoder.map = [
    ((KC.VOLUME_DOWN, KC.VOLUME_UP),),
]


#------------OLED-----------
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

oled = Display(
    display=SSD1306(
        sda=pins.GP6,
        scl=pins.GP7,
        i2c_addr=0x3C,
        width=128,
        height=32,
    ),
    entries=[
        TextEntry(text='Fajr Pad', y=0),
        TextEntry(text='Volume / Media', y=16),
    ],
)

keyboard.extensions.append(oled)

# ---------- GO ----------
if __name__ == '__main__':
    keyboard.go()