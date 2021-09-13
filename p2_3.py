import matplotlib.pyplot as plt
from PIL import Image
  
# Opening the primary image (used in background)
img1 = Image.open(r"path/jungle.jpg")
  
# Opening the secondary image (overlay image)
img2 = Image.open(r"path/car_new_transparent.png")
  
# Pasting img2 image on top of img1 
# starting at coordinates (0, 0)
img1.paste(img2, (300,465), mask = img2)
  

plt.imshow(img1)
img1.save("path/pic3.png", "PNG")
