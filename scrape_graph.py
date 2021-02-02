from skimage import io
from numpy import asarray, array_equal
graph = io.imread('graph.png')

blue = asarray([10, 132, 255])
teal = asarray([100, 210, 255])
orange = asarray([255, 159, 10])
grey = asarray([58, 58, 60])

color_list = [blue, teal, orange, grey]


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
                        return x1-x

def array_equal_set(graph_point, color_list):
    for color in color_list:
        if array_equal(graph_point, color):
            return True
    return False

def find_base(graph, color_list):
    gaps = []
    tops = []
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if array_equal_set(graph[y][x], color_list):
                print(x, y)
                #go down
                y1 = y
                flag = True
                while flag:
                    if array_equal_set(graph[y1][x], color_list):
                        y1 += 1
                    else:
                        y1 -= 1
                        flag = False
                tops.append(y1-y)
                gaps.append(x)
                #go right all the way to end

                while x < 520:
                    print('x', x)
                    x1 = x
                    flag = True
                    while flag:
                        if array_equal_set(graph[y1][x1], color_list):
                            x1 += 1
                        else:
                            print(x1, y1)
                            flag = False
                    x2 = x1
                    flag = True
                    while flag:
                        if not array_equal_set(graph[y1][x2], color_list):
                            print('x2', x2)
                            x2 += 1
                        else:
                            print(x2, y1)
                            print(x2-x1)
                            gaps.append(x2-x1)
                            flag = False

                    y2 = y1
                    flag = True
                    while flag:
                        if array_equal_set(graph[y2][x2], color_list):
                            print('y2', y2)
                            y2 -= 1
                        else:
                            print(x2, y2)
                            print(y1-y2)
                            tops.append(y1-y2)
                            flag = False
                    x = x2
                    print(gaps)
                    print(tops)

    return(gaps, tops)   



def run():
    blue_width = find_width_by_color(blue, graph)
    teal_width = find_width_by_color(teal, graph)
    orange_width = find_width_by_color(orange, graph)
    grey_width = find_width_by_color(grey, graph)

    print('blue_width', blue_width, 'teal_width' ,teal_width,
          'orange_width', orange_width, 'grey_width', grey_width)
    assert(blue_width == teal_width == orange_width == grey_width)

    width = blue_width

    gaps, tops = find_base(graph, color_list)
    print(gaps)
    print(tops)
    
    





run()