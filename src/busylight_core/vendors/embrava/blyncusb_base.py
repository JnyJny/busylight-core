"""Embrava early Blynclight (Blyncusb) family base class."""

from typing import TYPE_CHECKING

from .embrava_base import EmbravaBase
from .implementation import BlyncusbColor, rgb_to_blyncusb_color

if TYPE_CHECKING:
    from busylight_core.hardware import Hardware


class BlyncusbBase(EmbravaBase):
    """Base class for early Blynclight devices (VID 0x1130).

    Provides shared behavior for BLYNCUSB10 and BLYNCUSB20 devices
    including palette-based color management and interface claiming.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        """."""
        super().__init__(*args, **kwargs)
        self._current_color: BlyncusbColor = BlyncusbColor.OFF
        self._rgb_color: tuple[int, int, int] = (0, 0, 0)

    @classmethod
    def claims(cls, hardware: "Hardware") -> bool:
        """Check if this class can control the given hardware device.

        Early Blynclight devices require interface 1 for control.

        :param hardware: Hardware instance to test for compatibility
        :return: True if this class can control the hardware device
        """
        return (
            hardware.device_id in cls.supported_device_ids
            and hardware.interface_number == 1
        )

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
