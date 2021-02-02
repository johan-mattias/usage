from skimage import io
from numpy import asarray, array_equal
graph = io.imread('graph.png')

blue = asarray([10, 132, 255])
teal = asarray([100, 210, 255])
orange = asarray([255, 159, 10])
grey = asarray([58, 58, 60])


def find_width_by_color(color, graph):
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if array_equal(graph[y][x], color):
                x1 = x
                flag = True
                while flag:
                    if array_equal(graph[y][x1], color):
                        x1 += 1
                    else:
                        #print(x1-x)
                        return x1-x

def run():
    blue_width = find_width_by_color(blue, graph)
    teal_width = find_width_by_color(teal, graph)
    orange_width = find_width_by_color(orange, graph)
    grey_width = find_width_by_color(grey, graph)

    print('blue_width', blue_width, 'teal_width' ,teal_width,
          'orange_width', orange_width, 'grey_width', grey_width)
    
    





run()