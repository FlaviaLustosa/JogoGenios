import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('tests.jpg')
imgplot = plt.imshow(img)
plt.show()
