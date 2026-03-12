"""Embrava Blynclight BLYNCUSB10 Support (VID 0x1130, PID 0x0001/0x0002)

Early Blynclight using the blynux 8-byte USB feature report protocol.
Supports 7 predefined colors plus OFF.

Protocol source: https://github.com/ticapix/blynux

Command format:
- Bytes 0-6: Header (0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02)
- Byte 7: (color_mask << 4) | 0x0F
"""

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


class Blyncusb10(Light):
    """Embrava Blynclight BLYNCUSB10 (PID 0x0001, 0x0002) USB status light.

    Uses the blynux 8-byte USB control transfer protocol. Supports 7
    predefined colors plus off. No audio, flash, or dim capability.

    Device specifications:
    - VID: 0x1130
    - PID: 0x0001 or 0x0002
    - Interface: 1
    - Protocol: 8-byte USB HID feature report (blynux)
    """

    supported_device_ids: ClassVar[dict[tuple[int, int], str]] = {
        (0x1130, 0x0001): "Blynclight BLYNCUSB10",
        (0x1130, 0x0002): "Blynclight BLYNCUSB10",
    }

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

        The BLYNCUSB10 requires interface 1 for control.

        :param hardware: Hardware instance to test for compatibility
        :return: True if this class can control the hardware device
        """
        return (
            hardware.device_id in cls.supported_device_ids
            and hardware.interface_number == 1
        )

    def __bytes__(self) -> bytes:
        """Return the device state as bytes for USB communication.

        Command format: 7 header bytes + 1 color byte.
        Color byte: (color_mask << 4) | 0x0F
        """
        color_byte = (self._current_color.value << 4) | 0x0F
        return bytes([0x55, 0x53, 0x42, 0x43, 0x00, 0x40, 0x02, color_byte])

    @property
    def write_strategy(self) -> Callable[[bytes], None]:
        """The write method used by this light.

        The BLYNCUSB10 uses send_feature_report for USB control transfers.
        """
        return self.hardware.handle.send_feature_report

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
