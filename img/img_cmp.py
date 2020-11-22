from PIL import Image,ImageChops

# reading two image
img1 = Image.open('img1.jpg')
img2 = Image.open('img2.jpg')

# checking difference
d = ImageChops.difference(img1,img2)

# showing image
print(d)
d.show()