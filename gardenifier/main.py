# Importing Requirements

from PIL import Image, ImageEnhance
from math import ceil, floor

# Initiation

img = Image.open("./media/vennela.JPG")
img = img.resize((200, 200))
img = img.convert("L")
img = ImageEnhance.Contrast(img).enhance(1)

# Floyd-Steinberg Dithering

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


# Clubbing 3X3 pixels together for greater clarity

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

# Clubbing 3 each of the aforementioned 3X3 blocks to form the game of life blocks

temp = [[0]]*newHeight
for i in range(newHeight):
    for j in range(newWidth):
        temp[i] = temp[i] + [new.getpixel((j, i))]

stack = []
for i in range(len(temp)):
    stack.append([0])
    for j in range(len(temp[0])):
        if (j-1) % 12 == 0 and j != 0:
            stack[i].append(0)
            stack[i].append(0)
            stack[i].append(0)
            stack[i].append(0)
            stack[i].append(0)
            stack[i].append(temp[i][j])
        else:
            stack[i].append(temp[i][j])

stack2 = []
for i in range(len(stack)):
    if i % 12 == 0 and i != 0:
        stack2.append([0]*len(stack[0]))
        stack2.append([0]*len(stack[0]))
        stack2.append([0]*len(stack[0]))
        stack2.append([0]*len(stack[0]))
        stack2.append([0]*len(stack[0]))
        stack2 += [stack[i]]
    else:
        stack2 += [stack[i]]

final = Image.new("L", (len(stack2[0]), len(stack2)))
for i in range(len(stack2)):
    for j in range(len(stack2[0])):
        final.putpixel((j, i), (stack2[i][j]))

# Rendering the image

final.show()

