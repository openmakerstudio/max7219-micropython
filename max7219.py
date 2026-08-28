"""Minimal MAX7219 8x8 LED matrix driver for MicroPython (single module only).

Published from Open Maker Studio's own reference driver for the MAX7219
Blockly block. Backed by MicroPython's built-in `framebuf.FrameBuffer` for
drawing primitives — talks to the chip over a plain `machine.SPI` instance,
no other dependency needed.
"""
import framebuf


class Matrix8x8:
    def __init__(self, spi, cs, num=1):
        self.spi = spi
        self.cs = cs
        self.cs.value(1)
        self.buffer = bytearray(8)
        self.fb = framebuf.FrameBuffer(self.buffer, 8, 8, framebuf.MONO_HLSB)
        self._cmd(0x0F, 0x00)
        self._cmd(0x0B, 0x07)
        self._cmd(0x09, 0x00)
        self._cmd(0x0A, 0x03)
        self._cmd(0x0C, 0x01)
        self.fill(0)
        self.show()

    def _cmd(self, reg, data):
        self.cs.value(0)
        self.spi.write(bytearray([reg, data]))
        self.cs.value(1)

    def brightness(self, value):
        self._cmd(0x0A, value & 0x0F)

    def fill(self, c):
        self.fb.fill(c)

    def pixel(self, x, y, c=1):
        self.fb.pixel(x, y, c)

    def text(self, s, x, y, c=1):
        self.fb.text(s, x, y, c)

    def show(self):
        for row in range(8):
            self.cs.value(0)
            self.spi.write(bytearray([row + 1, self.buffer[row]]))
            self.cs.value(1)
