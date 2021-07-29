
from PIL import Image

im1 = Image.open("img2_RGB.jpg")
# convert to grey scale
img_grey = im1.convert("L")
# convert to HSV
img_hsv = im1.convert("HSV")
# convert to YCbCr
img_YCbCr = im1.convert("YCbCr")

# img_grey.show()
# img_hsv.show()
img_YCbCr.show()
