from skimage import io
#from skimage import filters
#from matplotlib import pyplot as plt
from numpy import asarray, array_equal

screenshot = io.imread('IMG-1800.PNG')

graph = screenshot[760:1010, 30: 875]

print(type(graph[100][100]))

blue = asarray([10, 132, 255])
teal = asarray([100, 210, 255])
orange = asarray([255, 159, 10])

blue_count = 0
teal_count = 0
orange_count = 0

for x in range(len(graph)):
    for y in range(len(graph[x])):
        if array_equal(graph[x][y], blue):
            if blue_count < 5:
                print(x,y)
            blue_count += 1
        if array_equal(graph[x][y], teal):
            if teal_count < 5:
                print(x,y)
            teal_count += 1
        if array_equal(graph[x][y], orange):
            if orange_count < 5:
                print(x,y)
            orange_count += 1

print(type(graph))
print(graph.shape)

print('blue_count', blue_count)
print('teal_count', teal_count)
print('orange_count', orange_count)

io.imsave('graph.png', graph)