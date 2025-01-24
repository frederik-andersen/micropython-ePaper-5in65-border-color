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