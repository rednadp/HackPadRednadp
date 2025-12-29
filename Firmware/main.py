# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation, MatrixScanner
from kmk.modules.rotary import RotaryEncoderModule
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.rotary import RotaryEncoder
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
cols = [board.D26, board.D27, board.D28]
rows = [board.D3, board.D4, board.D2]

scanner = MatrixScanner(
    row_pins=rows,
    col_pins=cols,
    diode_orientation=DiodeOrientation.COL2ROW
)
keyboard.modules.append(scanner)

keyboard.extensions.append(MediaKeys())

encoder = RotaryEncoder(
    pins=(board.D7, board.D8),
    clockwise=MediaKeys.volume_up,
    counter_clockwise=MediaKeys.volume_down,
)
keyboard.modules.append(encoder)

# 3. CONFIGURACIÓN DE LOS LEDS (16 SK6812 MINI-E)
# Conectados al pin D3
rgb = RGB(pixel_pin=board.D29, num_pixels=8, val_default=100)
keyboard.extensions.append(rgb)

# 4. CONFIGURACIÓN DE LA PANTALLA OLED (SSD1306)
# Pins D4 (SDA) y D5 (SCL) se detectan automáticamente por hardware I2C
display_driver = SSD1306(
    i2c=board.I2C(),
    device_address=0x3C,
)

display = Display(
    display_driver=display_driver,
    entries=[
        TextEntry(text='Hackpad v1.0', x=0, y=0),
        TextEntry(text='Layer: 0', x=0, y=12),
    ]
)
keyboard.extensions.append(display)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        [KC.A, KC.B, KC.C],    # ROW1
        [KC.D, KC.E, KC.F],    # ROW2
        [KC.G, KC.H, KC.I],    # ROW3
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()