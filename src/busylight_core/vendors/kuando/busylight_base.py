"""Kuando Busylight Base Implementation"""

from functools import cached_property

from busylight_core.mixins import ColorableMixin

from .implementation import State
from .kuando_base import KuandoBase


class BusylightBase(ColorableMixin, KuandoBase):
    """Base Busylight implementation.

    Kuando devices require periodic keepalive packets to prevent the hardware
    from quiescing. This implementation automatically manages keepalive using
    the appropriate strategy (asyncio or threading) based on the calling context.
    """

    @cached_property
    def state(self) -> State:
        """The device state manager."""
        return State()

    def __bytes__(self) -> bytes:
        return bytes(self.state)

    def on(self, color: tuple[int, int, int], led: int = 0) -> None:
        """Turn on the Busylight with the specified color.

        Automatically starts keepalive using the best available strategy
        (asyncio or threading) based on the calling environment.

        :param color: RGB color tuple (red, green, blue) with values 0-255
        :param led: LED index (unused for Busylight devices)
        """
        self.color = color
        with self.batch_update():
            self.state.steps[0].jump(self.color)

        # Environment automatically chooses asyncio or threading!
        self.add_task("keepalive", _keepalive, interval=10)

    def off(self, led: int = 0) -> None:
        """Turn off the Busylight and stop keepalive.

        :param led: LED index (unused for Busylight devices)
        """
        self.color = (0, 0, 0)
        with self.batch_update():
            self.state.steps[0].jump(self.color)
        self.cancel_task("keepalive")


def _keepalive(light: BusylightBase, interval: int = 10) -> None:
    """Send keepalive packet - works in any context.

    This synchronous function can be called from either asyncio or
    threading contexts. The TaskableMixin automatically handles
    the appropriate scheduling strategy.

    :param light: The BusylightBase instance to send keepalive to
    :param interval: Keepalive interval in seconds (0-15)
    """
    with light.batch_update():
        light.state.steps[0].keep_alive(interval)
