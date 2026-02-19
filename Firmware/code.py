import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
#from kmk.modules.layers import Layers # Por si quieres luces que cambien con capas
from kmk.extensions.rgb import RGB

# Configuración del teclado
keyboard = KMKKeyboard()

# 1. BUS DE DATOS (I2C)
# D5 suele ser SCL y D4 suele ser SDA en el XIAO
i2c_bus = busio.I2C(board.D5, board.D4)

# 2. CONFIGURACIÓN DE PANTALLA
# Pasamos los objetos directamente sin etiquetas para evitar el TypeError
display_driver = SSD1306(i2c=i2c_bus, device_address=0x3C)

estado_teclado = {
    'volumen': 50
}

volumen_display = TextEntry(text='Vol: 50%', x=0, y=12)

# Aquí le pasamos (driver, [lista de textos])
display_extension = Display(display_driver, [
    TextEntry(text="Rednadp's hackpad", x=0, y=0),
    volumen_display,
], flip=True)


keyboard.extensions.append(display_extension)

# 1. PINES DE LA MATRIZ (Corregidos para XIAO RP2040)
# Ajusta estos pines si los soldaste en otros agujeros
keyboard.col_pins = (board.D0, board.D1, board.D2) 
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. EXTENSIONES
keyboard.extensions.append(MediaKeys())

# 3. ENCODER (Giro y Click)
encoder_handler = EncoderHandler()
# Pines D0 y D1 para el giro, D3 para el click (ajusta si es necesario)
encoder_handler.pins = ((board.D7, board.D6, None, False),)
keyboard.modules.append(encoder_handler)

# 4. MAPA DE TECLAS (3x3)
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I,
    ]
]

# 5. MAPA DEL ENCODER (Volumen y Silencio)

class VolumenKey(Key):
    def __init__(self, incremento, **kwargs):
        super().__init__(**kwargs)
        self.incremento = incremento

    def on_press(self, keyboard, coord_int=None):
        # 1. Calculamos el nuevo volumen
        nuevo_vol = estado_teclado['volumen'] + self.incremento
        nuevo_vol = max(0, min(100, nuevo_vol))
        estado_teclado['volumen'] = nuevo_vol
        
        # 2. Actualizamos el texto de la pantalla
        volumen_display.text = f'VOL: {nuevo_vol}%'
        
        # 3. Mandamos la señal al ordenador
        if self.incremento > 0:
            keyboard.tap_key(KC.AUDIO_VOL_UP)
        else:
            keyboard.tap_key(KC.AUDIO_VOL_DOWN)
        print(volumen_display.text)
        

# Creamos las dos teclas que usaremos en el encoder
VOL_SUBIR = VolumenKey(incremento=2)
VOL_BAJAR = VolumenKey(incremento=-2)

encoder_handler.map = [
    ((VOL_SUBIR, VOL_BAJAR, KC.MUTE),)
]

# rgb = RGB(
#     pixel_pin=board.D3,      # Pin donde conectaste los LEDs
#     num_pixels=1,            # Cambia este número por cuántos LEDs soldaste
#     val_default=100,         # Brillo (de 0 a 255)
#     hue_default=0,           # Color inicial (0 es rojo)
#     sat_default=255,         # Saturación
#     rgb_order=(0, 1, 2),     # Orden de colores (GRB suele ser el estándar)
# )
# keyboard.extensions.append(rgb)


# --- CONFIGURACIÓN RGB LIMPIA ---
# rgb = RGB(
#     pixel_pin=board.D3,
#     num_pixels=9,
#     val_default=50, # Empezamos con brillo bajo por si acaso
#     rgb_order=(1, 0, 2), # Prueba GRB, que es el estándar de estos pequeñines
# )
# 
# keyboard.extensions.append(rgb)



if __name__ == '__main__':
    keyboard.go()