"""Embrava Early Blynclight Support (VID 0x1130)

Support for early Blynclight models predating the Embrava rebrand:
- BLYNCUSB10 (PID 0x0001, 0x0002): Uses blynux 8-byte feature report protocol
- BLYNCUSB20 (PID 0x1E00): Uses TENX20 2-byte HID write protocol on interface 1

These use a predefined color palette instead of full RGB control.

Protocol sources:
- https://github.com/ticapix/blynux (for PID 0x0001/0x0002)
- Decompiled Blynclight.dll SDK (for PID 0x1E00)
"""

from .blyncusb10 import Blyncusb10
from .blyncusb20 import Blyncusb20
from .colors import (
    BLYNCUSB_COLOR_TO_RGB,
    BlyncusbColor,
    rgb_to_blyncusb_color,
)

BlyncusbLights = Blyncusb10  # backwards compat alias

__all__ = [
    "BLYNCUSB_COLOR_TO_RGB",
    "Blyncusb10",
    "Blyncusb20",
    "BlyncusbColor",
    "BlyncusbLights",
    "rgb_to_blyncusb_color",
]
