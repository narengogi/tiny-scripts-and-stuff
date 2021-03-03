from PIL import Image, ImageEnhance
from math import ceil

img = Image.open("./media/vennela.JPG")
img = img.resize((100, 100))
img = img.convert("L")
img = ImageEnhance.Contrast(img).enhance(3)
print(img.size)
width, height = img.size
for i in range(height-2):
    for j in range(width-2):
        W = img.getpixel((j, i))
        W2 = 0
        if W > 128:
            W2 = 255
        img.putpixel((j, i), (W2))
        quantError = W-W2
        img.putpixel(
            (j+1, i+1), int((int(img.getpixel((j+1, i+1))) + quantError*7/16)))
        img.putpixel(
            (j-1, i), int((int(img.getpixel((j-1, i))) + quantError*3/16)))
        img.putpixel(
            (j, i+1), int((int(img.getpixel((j, i+1))) + quantError*5/16)))
        img.putpixel(
            (j+1, i+1), int((int(img.getpixel((j+1, i+1))) + quantError*1/16)))

newHeight = height + height - 1 + (ceil((height + height - 1)/3) - 1)*3
newWidth = width + width - 1 + (ceil((width + width - 1)/3) - 1)*3
new = Image.new("L", (newWidth, newHeight))

for i in range(newHeight-1):
    if i % 4 != 0:
        for j in range(newWidth-1):
            if j % 4 != 0:
                new.putpixel((j, i), (img.getpixel(
                    (int((j+4)/4), int((i+4)/4)))))
            else:
                new.putpixel((j, i), (1))

# finalHeight = newHeight + int(((newHeight/9)-1)*7)
# finalWidth = newWidth + int(((newWidth/9)-1)*7)
# final = Image.new("L", (finalWidth, finalHeight))

# for i in range(finalHeight-1):
#     if (i//4) % 2 == 0:
#         for j in range(finalWidth-1):
#             if (j//4) % 2 == 0:
#                 final.putpixel((j, i), (new.getpixel(
#                     (int(9*(j+7)/16), int(9*(i+7)/16)))))

# print(img.getpixel((100, 100)))
# final = final.resize((1000, 1000))
new = new.resize((1000, 1000))
new.show()
