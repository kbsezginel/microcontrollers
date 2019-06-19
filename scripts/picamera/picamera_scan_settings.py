"""
Scan picamera settings to see how they affect image and select prefered settings.
"""
import picamera


scan_settings = {'sharpness': range(0, 125, 25),
                 'contrast': range(0, 125, 25),
                 'brightness': range(0, 125, 25)
                 'saturation': range(0, 125, 25)}

for setting in scan_settings.keys():
    for values in settings:
        
camera = picamera.PiCamera()


camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
