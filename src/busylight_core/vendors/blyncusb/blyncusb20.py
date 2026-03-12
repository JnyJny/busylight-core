"""Embrava Blynclight BLYNCUSB20 Support (VID 0x1130, PID 0x1E00)

Early Blynclight using the TENX20 chipset with a 2-step HID write protocol.
Supports 7 predefined colors plus OFF.

Protocol source: decompiled Blynclight.dll SDK

Command format:
- 65-byte HID write on interface 1
- Byte 0: Report ID (0x00)
- Byte 1: Control code
- Bytes 2-64: Padding (0x00)

The TENX20 requires a two-step sequence: reset (0x73), then color code.
This is handled via write_strategy so the base Light.update() method
retains exclusive access and platform handling.
"""

from enum import IntEnum
from typing import TYPE_CHECKING, ClassVar

from collections.abc import Callable

from busylight_core.light import Light

from .colors import (
    BLYNCUSB_COLOR_TO_RGB,
    BlyncusbColor,
    rgb_to_blyncusb_color,
)

if TYPE_CHECKING:
    from busylight_core.hardware import Hardware


class Tenx20Color(IntEnum):
    """Color codes for TENX20 chipset (PID 0x1E00).

    Single-byte color codes used in the TENX20 protocol.
    """

    RED = 0x60
    GREEN = 0xD8
    BLUE = 0x35
    YELLOW = 0x40
    MAGENTA = 0x20
    WHITE = 0x07
    CYAN = 0x17
    OFF = 0x73


BLYNCUSB_TO_TENX20: dict[BlyncusbColor, Tenx20Color] = {
    BlyncusbColor.RED: Tenx20Color.RED,
    BlyncusbColor.GREEN: Tenx20Color.GREEN,
    BlyncusbColor.BLUE: Tenx20Color.BLUE,
    BlyncusbColor.YELLOW: Tenx20Color.YELLOW,
    BlyncusbColor.MAGENTA: Tenx20Color.MAGENTA,
    BlyncusbColor.WHITE: Tenx20Color.WHITE,
    BlyncusbColor.CYAN: Tenx20Color.CYAN,
    BlyncusbColor.OFF: Tenx20Color.OFF,
}


class Blyncusb20(Light):
    """Embrava Blynclight BLYNCUSB20 (PID 0x1E00) USB status light.

    Uses the TENX20 chipset with a two-step HID write protocol:
    1. Send 0x73 (reset/prepare)
    2. Send color code

    The two-step sequence is encapsulated in write_strategy so that
    Light.update() handles exclusive access and platform specifics
    without modification.

    Device specifications:
    - VID: 0x1130
    - PID: 0x1E00
    - Interface: 1
    - Protocol: TENX20 (65-byte HID write, 2-step command)
    - Colors: 7 predefined + OFF
    """

    supported_device_ids: ClassVar[dict[tuple[int, int], str]] = {
        (0x1130, 0x1E00): "Blynclight BLYNCUSB20",
    }

    RESET_CODE: ClassVar[int] = 0x73
    BUFFER_SIZE: ClassVar[int] = 65

    @staticmethod
    def vendor() -> str:
        """Return the vendor name."""
        return "Embrava"

    def __init__(self, *args: object, **kwargs: object) -> None:
        """."""
        super().__init__(*args, **kwargs)
        self._current_color: BlyncusbColor = BlyncusbColor.OFF
        self._rgb_color: tuple[int, int, int] = (0, 0, 0)

    @classmethod
    def claims(cls, hardware: "Hardware") -> bool:
        """Check if this class can control the given hardware device.

        The BLYNCUSB20 requires interface 1 for control.

        :param hardware: Hardware instance to test for compatibility
        :return: True if this class can control the hardware device
        """
        return (
            hardware.device_id in cls.supported_device_ids
            and hardware.interface_number == 1
        )

    @staticmethod
    def _make_command(code: int) -> bytes:
        """Create a 65-byte command buffer with the given control code.

        :param code: The control code byte
        :return: 65-byte command buffer
        """
        return bytes([0x00, code] + [0x00] * 63)

    def __bytes__(self) -> bytes:
        """Return the color command as bytes for USB communication.

        Returns only the color-setting command (step 2). The reset
        command (step 1) is handled by write_strategy.
        """
        tenx20_color = BLYNCUSB_TO_TENX20.get(self._current_color, Tenx20Color.OFF)
        return self._make_command(tenx20_color)

    @property
    def write_strategy(self) -> Callable[[bytes], None]:
        """Write strategy that implements the TENX20 two-step protocol.

        Sends the reset command (0x73) before writing the color command.
        This keeps the two-step protocol private to the device
        implementation without overriding Light.update().
        """
        handle = self.hardware.handle

        def tenx20_write(color_command: bytes) -> None:
            handle.write(self._make_command(self.RESET_CODE))
            handle.write(color_command)

        return tenx20_write

    @property
    def color(self) -> tuple[int, int, int]:
        """Tuple of RGB color values (approximated from palette color)."""
        return self._rgb_color

    @color.setter
    def color(self, value: tuple[int, int, int]) -> None:
        """Set the RGB color values (mapped to nearest palette color)."""
        self._rgb_color = value
        self._current_color = rgb_to_blyncusb_color(*value)

    def on(self, color: tuple[int, int, int], led: int = 0) -> None:
        """Turn on the device with the specified color.

        The RGB color will be mapped to the nearest available palette color.

        :param color: RGB color tuple (red, green, blue)
        :param led: LED index (not used by this device)
        """
        self.color = color
        self.update()

    def reset(self) -> None:
        """Reset the device to its default state (off)."""
        self._current_color = BlyncusbColor.OFF
        self._rgb_color = (0, 0, 0)
        self.update()
