from PIL import Image, ImageGrab
import time

ref = str(time.time())[0:10]

time.sleep(1)

img = ImageGrab.grab()
img.save('screen_{}.png'.format(ref), 'png')
print("Done")