"""Embrava Blynclight BLYNCUSB10/BLYNCUSB20/BLYNCUSB30 Support

Support for early Blynclight models with VID 0x1130:
- BLYNCUSB10 (PID 0x0001, 0x0002): Uses blynux 8-byte feature report protocol
- BLYNCUSB20/30 (PID 0x1E00): Uses TENX20 2-byte HID write protocol on interface 1

These use a predefined color palette instead of full RGB control.

Protocol sources:
- https://github.com/ticapix/blynux (for PID 0x0001)
- Decompiled Blynclight.dll SDK (for PID 0x1E00)
"""

from .blyncusb20 import (
    Blyncusb10,
    Blyncusb20,
    Blyncusb30,
    Tenx20Color,
)
from .blyncusb20_base import (
    BLYNCUSB20_COLOR_TO_RGB,
    Blyncusb20Base,
    Blyncusb20Color,
    rgb_to_blyncusb20_color,
)

# Backwards compatibility
Blyncusb20Lights = Blyncusb20Base

__all__ = [
    "BLYNCUSB20_COLOR_TO_RGB",
    "Blyncusb10",
    "Blyncusb20",
    "Blyncusb20Base",
    "Blyncusb20Color",
    "Blyncusb20Lights",
    "Blyncusb30",
    "Tenx20Color",
    "rgb_to_blyncusb20_color",
]
