# MAX7219 MicroPython Driver

Driver for a single MAX7219-based 8x8 LED dot-matrix module over SPI. Handles the chip's setup registers (decode mode, scan limit, intensity) and gives you basic drawing — pixels, text, and brightness control — backed by MicroPython's built-in `framebuf.FrameBuffer`. Single module only (no daisy-chaining multiple matrices).

## Install

Copy `max7219.py` onto your board's filesystem (e.g. via [Open Maker Studio](https://openmakerstudio.com)'s Library Manager, Thonny, or `mpremote cp`).

## Usage

```python
from machine import Pin, SPI
from max7219 import Matrix8x8

spi = SPI(1, baudrate=10_000_000, sck=Pin(14), mosi=Pin(13))
matrix = Matrix8x8(spi, Pin(15, Pin.OUT))

matrix.brightness(7)
matrix.text("A", 0, 0)
matrix.show()
```

## License

MIT — see [LICENSE](LICENSE).
