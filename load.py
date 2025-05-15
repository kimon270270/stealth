from PIL import Image
import os

def load_image():
    
    try:
        image_path = "DOG.png"
        
        if (os.path.exists(image_path)):
            image = Image.open(image_path)
            image.show()
    
    except:
        pass

load_image()