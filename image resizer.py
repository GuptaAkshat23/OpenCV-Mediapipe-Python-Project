from PIL import Image

def resize_image(size1,size2):
    image = Image.open('')
    
    print(f"Current size : {image.size}")
    
    resized_image = image.resize((size1,size2))
    
    resized_image.save(''+str(size1)+'.jpeg')
    
size1 = int(input("Enter width"))
size2 = int(input("enter length"))

resize_image(size1, size2)
    
    
