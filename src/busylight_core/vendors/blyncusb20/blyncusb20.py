"""Embrava Blynclight BLYNCUSB20 Support

Support for early Blynclight models with VID 0x1130.
These use different protocols from the newer Embrava Blynclight devices.

Three variants are supported:
- BLYNCUSB10 (PID 0x0001, 0x0002): Uses blynux 8-byte protocol with feature report
- BLYNCUSB20 (PID 0x1E00): Uses TENX20 2-byte protocol on interface 1

Protocol information from:
- https://github.com/ticapix/blynux (for PID 0x0001)
- Decompiled Blynclight.dll SDK (for PID 0x1E00 TENX20 protocol)
"""

from enum import IntEnum
from typing import TYPE_CHECKING, ClassVar

from busylight_core.light import Light

from .blyncusb20_base import (
    BLYNCUSB20_COLOR_TO_RGB,
    Blyncusb20Base,
    Blyncusb20Color,
    rgb_to_blyncusb20_color,
)

if TYPE_CHECKING:

    from busylight_core.hardware import Hardware


class Blyncusb10(Blyncusb20Base):
    """Embrava Blynclight BLYNCUSB10 (PID 0x0001, 0x0002) USB status light.

    This is an early Blynclight model (TENX10 chipset) that uses the
    blynux 8-byte USB control transfer protocol. It supports 7 predefined
    colors plus off.

    Device specifications:
    - VID: 0x1130
    - PID: 0x0001 or 0x0002
    - Interface: 1
    - Protocol: 8-byte USB HID feature report (blynux protocol)
    - Colors: 7 predefined + OFF
    """

    supported_device_ids: ClassVar[dict[tuple[int, int], str]] = {
        (0x1130, 0x0001): "Blynclight BLYNCUSB10",
        (0x1130, 0x0002): "Blynclight BLYNCUSB10",
    }

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


# Backwards compatibility alias
Blyncusb20 = Blyncusb10


class Tenx20Color(IntEnum):
    """Color codes for TENX20 chipset (PID 0x1E00).

    These are single-byte color codes used in the TENX20 protocol.
    The protocol sends 0x73 (reset) first, then the color code.
    """

    RED = 0x60
    GREEN = 0xD8
    BLUE = 0x35
    YELLOW = 0x40
    MAGENTA = 0x20
    WHITE = 0x07
    CYAN = 0x17
    OFF = 0x73  # Also used as reset command


# Map Blyncusb20Color to Tenx20Color
BLYNCUSB20_TO_TENX20: dict[Blyncusb20Color, Tenx20Color] = {
    Blyncusb20Color.RED: Tenx20Color.RED,
    Blyncusb20Color.GREEN: Tenx20Color.GREEN,
    Blyncusb20Color.BLUE: Tenx20Color.BLUE,
    Blyncusb20Color.YELLOW: Tenx20Color.YELLOW,
    Blyncusb20Color.MAGENTA: Tenx20Color.MAGENTA,
    Blyncusb20Color.WHITE: Tenx20Color.WHITE,
    Blyncusb20Color.CYAN: Tenx20Color.CYAN,
    Blyncusb20Color.OFF: Tenx20Color.OFF,
}


class Blyncusb30(Light):
    """Embrava Blynclight BLYNCUSB30 (PID 0x1E00) USB status light.

    This variant uses the TENX20 chipset with a different protocol:
    - 65-byte HID write on interface 1
    - Two-step command: send 0x73 (reset), then color code
    - Simple single-byte color codes (not the blynux bit-shifted format)

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

    # TENX20 protocol uses 65-byte buffer (1 report ID + 64 data bytes)
    _BUFFER_SIZE = 65

    @staticmethod
    def vendor() -> str:
        """Return the vendor name for BLYNCUSB30 devices."""
        return "Embrava"

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Initialize the BLYNCUSB30 device."""
        super().__init__(*args, **kwargs)
        self._current_color: Blyncusb20Color = Blyncusb20Color.OFF
        self._rgb_color: tuple[int, int, int] = (0, 0, 0)

    @classmethod
    def claims(cls, hardware: "Hardware") -> bool:
        """Check if this class can control the given hardware device.

        The BLYNCUSB30 requires interface 1 for control.

        :param hardware: Hardware instance to test for compatibility
        :return: True if this class can control the hardware device
        """
        return (
            hardware.device_id in cls.supported_device_ids
            and hardware.interface_number == 1
        )

    def _make_command(self, code: int) -> bytes:
        """Create a 65-byte command buffer with the given control code.

        :param code: The control code byte
        :return: 65-byte command buffer
        """
        return bytes([0x00, code] + [0] * 63)

    def __bytes__(self) -> bytes:
        """Return the device state as bytes for USB communication.

        Note: The TENX20 protocol uses a two-step command sequence,
        so this returns the color command (step 2). The update() method
        handles sending both commands in sequence.
        """
        tenx20_color = BLYNCUSB20_TO_TENX20.get(
            self._current_color, Tenx20Color.OFF
        )
        return self._make_command(tenx20_color)

    def update(self) -> None:
        """Write the current state to the hardware device.

        The TENX20 protocol requires a two-step command:
        1. Send 0x73 (reset/prepare)
        2. Send color code
        """
        # Step 1: Send reset command
        self.hardware.handle.write(self._make_command(0x73))

        # Step 2: Send color code
        tenx20_color = BLYNCUSB20_TO_TENX20.get(
            self._current_color, Tenx20Color.OFF
        )
        self.hardware.handle.write(self._make_command(tenx20_color))

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

        Note: The device only supports 7 predefined colors.
        The RGB color will be mapped to the nearest available color.

        :param color: RGB color tuple (red, green, blue)
        :param led: LED index (not used by this device)
        """
        self.color = color
        self.update()

    def reset(self) -> None:
        """Reset the device to its default state (off)."""
        self.blyncusb20_color = Blyncusb20Color.OFF
        self.update()
