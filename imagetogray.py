from PIL import Image
def comandlineprogram():
    try: 
        a = Image.open(input("Image rout and name: "))
        uv =a.size[1]
        av =a.size[0]
        new_image = a.resize((int(av),int(uv))).convert("L")
        for i in range(new_image.size[0]):
            for j in range(new_image.size[1]):  
                gray = new_image.getpixel((i,j))    
                if gray > 205:
                    new_image.putpixel((i,j),255)
                elif gray > 155:
                    new_image.putpixel((i,j),180)
                elif gray > 105:
                    new_image.putpixel((i,j),105)
                elif gray > 55:
                    new_image.putpixel((i,j),80)
                else:
                    new_image.putpixel((i,j),30)
        new_image.save('alahuakbar.jpg')
        new_image.putpixel((i,j),230)
    except FileNotFoundError:
        print("File not found")