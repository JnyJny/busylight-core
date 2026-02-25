"""Conftest for pytest-markdown-docs.

Provides mock light infrastructure so doc code examples can run
without physical USB hardware connected.
"""

from unittest.mock import Mock, patch

import busylight_core
from busylight_core.hardware import ConnectionType, Hardware
from busylight_core.light import Light


def _make_mock_hardware(vendor_id=0x2C0D, product_id=0x0001, name="MockLight"):
    """Create a mock Hardware instance."""
    hw = Mock(spec=Hardware)
    hw.device_id = (vendor_id, product_id)
    hw.device_type = ConnectionType.HID
    hw.path = b"/dev/mock0"
    hw.product_string = name
    hw.vendor_id = vendor_id
    hw.product_id = product_id
    hw.manufacturer_string = "Mock Manufacturer"
    hw.serial_number = "MOCK001"
    hw.handle = Mock()
    hw.handle.read = Mock(return_value=b"\x00" * 8)
    hw.handle.write = Mock()
    hw.acquire = Mock()
    hw.release = Mock()
    return hw


class StatefulMockLight:
    """A mock light that tracks state for doc examples.

    Not a real Light subclass -- just has the same interface
    so doc examples work.
    """

    def __init__(self, name="MockLight", vendor_name="Mock"):
        self.name = name
        self._vendor_name = vendor_name
        self.color = (0, 0, 0)
        self._is_lit = False
        self.hardware = _make_mock_hardware(name=name)
        self.path = "/dev/mock0"
        self._is_button = False
        self._button_on = False
        self._tasks = {}

    def vendor(self):
        return self._vendor_name

    def on(self, color, led=0):
        self.color = color
        self._is_lit = True

    def off(self):
        self.color = (0, 0, 0)
        self._is_lit = False

    @property
    def is_lit(self):
        return self._is_lit

    def reset(self):
        self.off()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"

    # Embrava features
    def dim(self):
        pass

    def bright(self):
        pass

    def flash(self, color, speed=None):
        self.color = color
        self._is_lit = True

    def stop_flashing(self):
        pass

    # BlynclightPlus audio
    def play_sound(self, music=0, volume=1, repeat=False):
        pass

    def stop_sound(self):
        pass

    def mute(self):
        pass

    def unmute(self):
        pass

    # Button devices
    @property
    def is_button(self):
        return self._is_button

    @property
    def button_on(self):
        return self._button_on

    # Task management
    def add_task(self, name, func, interval=1.0):
        self._tasks[name] = func

    def cancel_task(self, name):
        self._tasks.pop(name, None)

    def cancel_tasks(self):
        self._tasks.clear()


def _make_light(name="MockLight", vendor="Mock", button=False):
    light = StatefulMockLight(name=name, vendor_name=vendor)
    if button:
        light._is_button = True
        light._button_on = True
    return light


def _mock_first_light(name="MockLight", vendor="Mock", button=False):
    def first_light(*args, **kwargs):
        return _make_light(name=name, vendor=vendor, button=button)

    return first_light


def _mock_all_lights(name="MockLight", vendor="Mock", count=1, button=False):
    def all_lights(*args, **kwargs):
        return [
            _make_light(name=name, vendor=vendor, button=button) for _ in range(count)
        ]

    return all_lights


# Build patchers that stay active for all doc tests
_patches = []


def _setup_patches():
    """Create all patches for doc testing."""
    global _patches

    # Core Light class
    _patches.append(patch.object(Light, "first_light", side_effect=_mock_first_light()))
    _patches.append(
        patch.object(Light, "all_lights", side_effect=_mock_all_lights(count=2))
    )

    # Hardware.enumerate
    _patches.append(
        patch.object(
            Hardware,
            "enumerate",
            return_value=[
                _make_mock_hardware(),
                _make_mock_hardware(
                    vendor_id=0x27B8, product_id=0x01ED, name="blink(1)"
                ),
            ],
        )
    )

    # Vendor-specific classes - patch first_light and all_lights on each
    vendor_configs = {
        "EmbravaLights": {"name": "Blynclight", "vendor": "Embrava"},
        "BlynclightPlus": {"name": "Blynclight Plus", "vendor": "Embrava"},
        "KuandoLights": {"name": "Busylight Omega", "vendor": "Kuando"},
        "BusylightAlpha": {"name": "Busylight Alpha", "vendor": "Kuando"},
        "BusylightOmega": {"name": "Busylight Omega", "vendor": "Kuando"},
        "Flag": {"name": "Flag", "vendor": "Luxafor"},
        "BlinkStickSquare": {"name": "BlinkStick Square", "vendor": "Agile Innovative"},
        "BlinkStickPro": {"name": "BlinkStick Pro", "vendor": "Agile Innovative"},
        "AgileInnovativeLights": {"name": "BlinkStick", "vendor": "Agile Innovative"},
        "Blink1": {"name": "blink(1)", "vendor": "ThingM"},
        "ThingMLights": {"name": "blink(1)", "vendor": "ThingM"},
        "MuteMe": {"name": "MuteMe", "vendor": "MuteMe", "button": True},
        "MuteMeLights": {"name": "MuteMe", "vendor": "MuteMe", "button": True},
        "EPOSLights": {"name": "EPOS Busylight", "vendor": "EPOS"},
        "PlantronicsLights": {"name": "Status Indicator", "vendor": "Plantronics"},
        "CompuLabLights": {"name": "fit-statUSB", "vendor": "CompuLab"},
        "LuxaforLights": {"name": "Flag", "vendor": "Luxafor"},
    }

    for cls_name, cfg in vendor_configs.items():
        cls = getattr(busylight_core, cls_name, None)
        if cls is None:
            continue
        btn = cfg.get("button", False)
        _patches.append(
            patch.object(
                cls,
                "first_light",
                side_effect=_mock_first_light(
                    name=cfg["name"], vendor=cfg["vendor"], button=btn
                ),
            )
        )
        _patches.append(
            patch.object(
                cls,
                "all_lights",
                side_effect=_mock_all_lights(
                    name=cfg["name"], vendor=cfg["vendor"], button=btn
                ),
            )
        )

    # Luxafor Mute (imported from submodule)
    from busylight_core.vendors.luxafor import Mute

    _patches.append(
        patch.object(
            Mute,
            "first_light",
            side_effect=_mock_first_light(name="Mute", vendor="Luxafor", button=True),
        )
    )
    _patches.append(
        patch.object(
            Mute,
            "all_lights",
            side_effect=_mock_all_lights(name="Mute", vendor="Luxafor", button=True),
        )
    )

    # Start all patches
    for p in _patches:
        p.start()


def _teardown_patches():
    for p in _patches:
        p.stop()
    _patches.clear()


# Start patches at import time (pytest-markdown-docs imports conftest once)
_setup_patches()

import atexit

atexit.register(_teardown_patches)


def pytest_markdown_docs_globals():
    """Inject globals available to all markdown code blocks."""

    return {
        # These are injected but most blocks do their own imports.
        # Having them here handles any blocks that rely on prior context.
        "time": __import__("time"),
        "asyncio": __import__("asyncio"),
    }
