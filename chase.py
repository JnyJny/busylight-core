from busylight_core import BlinkStickSquare

l = BlinkStickSquare.first_light()

import itertools
import time

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 0)]

p = 0.05

while True:
    for a, b in itertools.pairwise(itertools.cycle(colors)):
        l.on(a)
        time.sleep(p)
        for led in range(1, l.nleds + 1):
            l.on(b, led=led)
            time.sleep(p)
