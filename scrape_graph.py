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

def search_start_point(graph, color_list):
    for x in range(len(graph[0])):
        for y in range(len(graph)):
            if array_equal_set(graph[y][x], color_list):
                return(x, y)


def find_base(graph, color_list):
    gaps = []
    tops = []
    starts = []
    x, y = search_start_point(graph, color_list)
    #print(x, y)
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
    starts.append(x)
    #go right all the way to end

    #TODO: detect end of graph
    while x < 475:
        #print('x', x)
        x1 = x
        flag = True
        while flag:
            if array_equal_set(graph[y1][x1], color_list):
                x1 += 1
            else:
                #print(x1, y1)
                flag = False
        x2 = x1
        flag = True
        while flag:
            if not array_equal_set(graph[y1][x2], color_list):
                #print('x2', x2)
                x2 += 1
            else:
                #print(x2, y1)
                #print(x2-x1)
                gaps.append(x2-x1)
                starts.append(x2)
                flag = False

        y2 = y1
        flag = True
        while flag:
            if array_equal_set(graph[y2][x2], color_list):
                #print('y2', y2)
                y2 -= 1
            else:
                #print(x2, y2)
                #print(y1-y2)
                tops.append(y1-y2)
                flag = False
        x = x2
    return(gaps, tops, starts)   



def run():
    blue_width = find_width_by_color(blue, graph)
    teal_width = find_width_by_color(teal, graph)
    orange_width = find_width_by_color(orange, graph)
    grey_width = find_width_by_color(grey, graph)

    print('blue_width', blue_width, 'teal_width' ,teal_width,
          'orange_width', orange_width, 'grey_width', grey_width)
    assert(blue_width == teal_width == orange_width == grey_width)

    width = blue_width

    gaps, tops, starts = find_base(graph, color_list)
    print('gaps', len(gaps), gaps)
    print('tops', len(tops), tops)
    print('starts', len(starts), starts)
    
    print(list(zip(starts, tops)))

    areas = []

    for top in tops:
        areas.append(top*15)

    print(areas)

    sum = 0

    for area in areas:
        sum += area
    print('area:', sum)
    #417 minutes
    print('pixels per minute', round(sum/417))

    pix_per_min = round(sum/417)

    times = []
    for area in areas:
        times.append(round(area/pix_per_min))
    print(times)

    hours = []
    x = 0
    index = 0
    print('start')
    for gap in gaps:
        print(gap)
        #TODO calculate max gap
        if gap > 10:
            length = gap
            while length > 0:
                print('len',length)
                hours.append(0)
                #TODO calculate constant
                length -= 30
        hours.append(times[index])
        index += 1
        x = x + gap
        #print(x, gap)
        print('hours',hours)
    print(len(hours))


        






run()