from busylight_core import Blynclight, Light

# Find audio-capable devices
audio_devices = []
for light in Light.all_lights():
    print("Checking device:", light, "with capabilities:", light.on.__annotations__)
    if hasattr(light, "on") and "sound" in light.on.__annotations__:
        audio_devices.append(light)

if audio_devices:
    device = audio_devices[0]

    # Control with sound (if supported)
    device.on((255, 0, 0), sound=True)  # Red with sound

    # Mute/unmute functions (if available)
    if hasattr(device, "mute"):
        device.mute()
    if hasattr(device, "unmute"):
        device.unmute()
