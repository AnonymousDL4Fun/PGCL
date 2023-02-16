import PIL.Image
import numpy as np
from torchvision import transforms

#Dummy image as placeholder
image = PIL.Image.fromarray(np.zeros(224, 224, 3))

# For generation StainAug set
image = transforms.functional.adjust_hue(image, 0.40)
