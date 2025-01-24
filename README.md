# micropython-ePaper-5in65-border-color
This project modifies the original driver to enable changing the border color of the ePaper display.

## Screenshots
!Black Image
!Red Image

## Features
- Change border color of the e-paper display
- Easy-to-use method for border color customization

## Requirements
- Raspberry Pi Pico
- Waveshare 5.65-inch e-paper display
- MicroPython

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/frederik-andersen/micropython-ePaper-5in65-border-color.git
    ```
2. Upload the files to your Raspberry Pi Pico.

## Usage - Demo
This is the included demo, showing how to use the modified epaper driver with the change_border_color method.
```python
# Epaper 5in65 border color demo.
# By Frederik Andersen
import utime
from pico_epaper_5in65 import EPD_5in65

epd = EPD_5in65()  # The screen
epd.fill(0xff)

epd.change_border_color('black')
epd.text('This is black border color.', 190, 200, epd.Black)
epd.EPD_5IN65F_Display(epd.buffer)

utime.sleep(5)

epd.change_border_color('red')
epd.text('But now its changed to red.', 190, 220, epd.Red)
epd.EPD_5IN65F_Display(epd.buffer)
# etc etc etc...

epd.Sleep()

# Available colors are: 'black', 'white', 'green', 'blue', 'red', 'yellow', 'orange'.
# See the change_border_color method in the EPD_5in65 class for more details on how it works.
# You could also hardcode the border color in the class init, if changing it several times is not needed.

```
## Hardcoding The Border Color
If changing the border color several times isnt necessary, you should hardcode it in the driver.
In the` __init__` method, change `self._border_color` to the desired color:
```python
self._border_colors = {
'black': 0x10,
'white': 0x30, # 0x37 is the default white from Waveshare, I don't see any difference with using 0x30 instead.
'green': 0x50,
'blue': 0x70,
'red': 0x90,
'yellow': 0xB0,
'orange': 0xD0
}

self._border_color = self._border_colors['white'] 
```

## Available Colors
The available colors for the border are:
- `black`
- `white`
- `green`
- `blue`
- `red`
- `yellow`
- `orange`

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Frederik Andersen

## Acknowledgments
- Waveshare team for the original e-paper driver code
