from PIL import Image, ImageOps

img = Image.open('01.png')
img2 = Image.open('02.png')

gray_image = ImageOps.grayscale(img)
gray2_image = ImageOps.grayscale(img2)
gray_image.save('gray_image.png')
gray2_image.save('gray2_image.png')

img.show()
img2.show()
