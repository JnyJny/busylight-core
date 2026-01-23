"""Embrava Blynclight BLYNCUSB20 base class.

This is an early variant of the Blynclight, using USB control transfers
with a predefined color palette instead of full RGB control.

Device specifications from https://github.com/ticapix/blynux:
- VID:PID: 0x1130:0x0001
- 8-byte command payload
- Predefined color palette (8 colors including OFF)
"""

from enum import IntEnum
from typing import TYPE_CHECKING

from busylight_core.light import Light

if TYPE_CHECKING:
    from collections.abc import Callable


class Blyncusb20Color(IntEnum):
    """Predefined color values for BLYNCUSB20 devices.

    The BLYNCUSB20 uses a 4-bit color mask that maps to
    predefined colors. Full RGB control is not available.
    """

    WHITE = 0x8
    CYAN = 0x9
    MAGENTA = 0xA
    BLUE = 0xB
    YELLOW = 0xC
    GREEN = 0xD
    RED = 0xE
    OFF = 0xF


def rgb_to_blyncusb20_color(red: int, green: int, blue: int) -> Blyncusb20Color:
    """Map an RGB color to the nearest BLYNCUSB20 predefined color.

    Since the BLYNCUSB20 device only supports 7 colors plus OFF,
    this function attempts to find the best match based on
    the RGB values provided.

    :param red: Red component (0-255)
    :param green: Green component (0-255)
    :param blue: Blue component (0-255)
    :return: The closest Blyncusb20Color match
    """
    # If all components are very low, return OFF
    if red < 32 and green < 32 and blue < 32:
        return Blyncusb20Color.OFF

    # Determine dominant colors
    max_val = max(red, green, blue)
    threshold = max_val * 0.5  # 50% of max to be considered "on"

    r_on = red >= threshold
    g_on = green >= threshold
    b_on = blue >= threshold

    # Map RGB combinations (r_on, g_on, b_on) to Blyncusb20 colors
    color_map = {
        (True, True, True): Blyncusb20Color.WHITE,
        (True, True, False): Blyncusb20Color.YELLOW,
        (True, False, True): Blyncusb20Color.MAGENTA,
        (False, True, True): Blyncusb20Color.CYAN,
        (True, False, False): Blyncusb20Color.RED,
        (False, True, False): Blyncusb20Color.GREEN,
        (False, False, True): Blyncusb20Color.BLUE,
    }

    return color_map.get((r_on, g_on, b_on), Blyncusb20Color.OFF)


# Reverse mapping from Blyncusb20Color to approximate RGB values
BLYNCUSB20_COLOR_TO_RGB: dict[Blyncusb20Color, tuple[int, int, int]] = {
    Blyncusb20Color.WHITE: (255, 255, 255),
    Blyncusb20Color.CYAN: (0, 255, 255),
    Blyncusb20Color.MAGENTA: (255, 0, 255),
    Blyncusb20Color.BLUE: (0, 0, 255),
    Blyncusb20Color.YELLOW: (255, 255, 0),
    Blyncusb20Color.GREEN: (0, 255, 0),
    Blyncusb20Color.RED: (255, 0, 0),
    Blyncusb20Color.OFF: (0, 0, 0),
}


class Blyncusb20Base(Light):
    """Base class for Embrava Blynclight BLYNCUSB20 devices.

    The BLYNCUSB20 uses a different protocol than newer Embrava Blynclights:
    - 8-byte USB control transfer command
    - Predefined color palette (7 colors + OFF)
    - No audio support

    Command structure:
    - Bytes 0-6: Header (0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02)
    - Byte 7: Color mask (color_value << 4) | 0x0f
    """

    # Base command payload from blynux C code
    _BASE_COMMAND = bytes([0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02, 0x0F])

    @staticmethod
    def vendor() -> str:
        """Return the vendor name for BLYNCUSB20 devices."""
        return "Embrava"

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the BLYNCUSB20 device."""
        super().__init__(*args, **kwargs)
        self._current_color: Blyncusb20Color = Blyncusb20Color.OFF
        self._rgb_color: tuple[int, int, int] = (0, 0, 0)

    def __bytes__(self) -> bytes:
        """Return the device state as bytes for USB communication.

        The command format for the original BLYNCUSB20 (0x0001) is:
        - 7 header bytes: 0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02
        - 1 color byte: (color_mask << 4) | 0x0f

        Uses send_feature_report for USB control transfers.
        """
        color_byte = (self._current_color.value << 4) | 0x0F
        return bytes([0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02, color_byte])

    @property
    def write_strategy(self) -> "Callable[[bytes], None]":
        """The write method used by this light.

        The original BLYNCUSB20 (0x0001) uses send_feature_report.
        """
        return self.hardware.handle.send_feature_report

    @property
    def color(self) -> tuple[int, int, int]:
        """Tuple of RGB color values (approximated from BLYNCUSB20 color)."""
        return self._rgb_color

    @color.setter
    def color(self, value: tuple[int, int, int]) -> None:
        """Set the RGB color values (mapped to nearest BLYNCUSB20 color)."""
        self._rgb_color = value
        self._current_color = rgb_to_blyncusb20_color(*value)

    @property
    def blyncusb20_color(self) -> Blyncusb20Color:
        """Get the current BLYNCUSB20 color value."""
        return self._current_color

    @blyncusb20_color.setter
    def blyncusb20_color(self, value: Blyncusb20Color) -> None:
        """Set the BLYNCUSB20 color directly."""
        self._current_color = value
        self._rgb_color = BLYNCUSB20_COLOR_TO_RGB.get(value, (0, 0, 0))

    def on(self, color: tuple[int, int, int], led: int = 0) -> None:
        """Turn on the device with the specified color.

        Note: The BLYNCUSB20 only supports 7 predefined colors.
        The RGB color will be mapped to the nearest available color.

        :param color: RGB color tuple (red, green, blue)
        :param led: LED index (not used by BLYNCUSB20 devices)
        """
        self.color = color
        self.update()

    def reset(self) -> None:
        """Reset the device to its default state (off)."""
        self.blyncusb20_color = Blyncusb20Color.OFF
        self.update()
