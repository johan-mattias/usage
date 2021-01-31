from matplotlib import image
from matplotlib import pyplot
from numpy import asarray, array_equal
# load image as pixel array
img = image.imread('IMG_1802.jpg')
# summarize shape of the pixel array
#print(img.dtype)
#print(img.shape)
# display the array of pixels as an img
pyplot.imshow(img)
pyplot.show()

data = asarray(img)
#print(type(data))
# summarize shape
#print(data.shape)
#print(data)

#print("Before trimming:",img.shape)
day = img[370:410, 30:350]
time = img[415:480, 30:240]
graph = img[760:1010, 30: 875]

### these are going to move around
#cat_1
#cat_2
#cat_3

#print("After trimming:",day.shape)
pyplot.imshow(graph)

#pyplot.savefig('graph.png', bbox_inches='tight', pad_inches=0)

data = asarray(graph)
#print(type(data))
# summarize shape
#print(data.shape)
#print(data)

#print(type(data[0][0]))
blue = asarray([9, 135, 249])
teal = asarray([100, 206, 253])
orange = asarray([253, 158, 11])
#print(type(blue))

#print(list(blue))

#print(data[0][0] == blue.all())
#print(array_equal(data[0][0], blue))


'''
blue
9 133 247
17 130 249
teal
104 207 252
98 209 255
orange
253 158 11
252 159 12
grej
67 51 64
black
28 28 30


'''

def compare_range(pixel, color):
    pixel = list(pixel)
    color= list(color)
    flag = False
    margin = 12

    if(abs(pixel[0] - color[0]) < margin):
        if(abs(pixel[1] - color[1]) < margin):
            if(abs(pixel[2] - color[2]) < margin):
                flag = True
    return flag
        


print(img[395][137])

blue_count = 0
teal_count = 0
orange_count = 0
for x in range(len(data)):
    for y in range(len(data[x])):
        if compare_range(data[x][y], blue):
            if blue_count < 5:
                print(x,y)
            blue_count += 1
        if compare_range(data[x][y], teal):
            if teal_count < 5:
                print(x,y)
            teal_count += 1
        if compare_range(data[x][y], orange):
            if orange_count < 5:
                print(x,y)
            orange_count += 1

print('blue_count', blue_count)
print('teal_count', teal_count)
print('orange_count', orange_count)
