import pygame
from math import sqrt
const_int_mod = int(10**4)
height = 1400
witd = 750
screen = pygame.display.set_mode((height,witd))

class COLORS:
    def __init__(self) -> None:
        self.BACKGROUND = (255,255,255)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREY = (192,192,192)
        self.RED = (255,0,0)
        self.GREEN = (0,102,51)
        self.BLUE = (0,0,153)
        self.YELLOW = (255,255,0)
        self.PURPLE = (255,0,255)
        self.SKY = (0,255,255)
        self.ORANGE = (255,125,25)
        self.GRAPE = (100,25,125)
        self.GRASS = (55,155,65)

class Draw_ox_oy:
    def __init__(self,ox1 : int, ox2 : int ,ox3 : int, ox4 : int , oy1 : int,oy2 : int,oy3 : int,oy4 : int, 
                 BLACK : tuple,
                 up : pygame.surface.Surface,
                 ngang : pygame.surface.Surface,
                 screen : pygame.surface.Surface) -> None:
        
        self.ox1 = ox1
        self.ox2 = ox2
        self.ox3 = ox3
        self.ox4 = ox4
        self.oy1 = oy1
        self.oy2 = oy2
        self.oy3 = oy3
        self.oy4 = oy4
        self.BLACK = BLACK
        self.up = up
        self.ngang = ngang
        self.screen = screen

    def show(self) -> None:
        pygame.draw.line(self.screen,self.BLACK,(self.ox1,self.ox2),(self.ox3,self.ox4),3)
        pygame.draw.line(self.screen,self.BLACK,(self.oy1,self.oy2),(self.oy3,self.oy4),3)    
        self.screen.blit(self.up,(44,32))    
        self.screen.blit(self.ngang,(1100,588))

class Show_mouse:
    def __init__(self,x_mouse : float , 
                 y_mouse : float ,
                 font_mouse : pygame.font.Font,
                 BLACK : tuple,
                 screen : pygame.surface.Surface) -> None:
                 
        self.x_mouse = x_mouse
        self.y_mouse = y_mouse
        self.font_mouse = font_mouse
        self.BLACK = BLACK    
        self.screen = screen

    def show(self) -> None:
        text_mouse = self.font_mouse.render("(" + "x = " + str((self.x_mouse - 50)) + "," + "y = " + str(abs(self.y_mouse-600)) + ")",True,self.BLACK)
        self.screen.blit(text_mouse, (self.x_mouse + 10, self.y_mouse))

class draw_rect_backgroud:
    def __init__(self, x : int, y : int, w : int, h : int, colors : COLORS) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colors = colors

    def show(self) -> None:
        pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
        pygame.draw.rect(screen,self.colors.WHITE,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))


def points_black_rect() -> list:
    rect_black = [(50,610,100,40),(50,655,100,40),(165,610,200,50),(375,610,200,50),(585,610,200,50),(790,610,200,50),(1000,610,90,50)]
    return rect_black

def points_white_circle() -> list:
    rect_white = [(55,615,90,30),(55,660,40,30),(170,615,190,40),(380,615,190,40),(590,615,190,40),(795,615,190,40),(1005,615,80,40)]
    return rect_white

def Linear_Search(arr : list , x : int) -> list:
    list_index = []
    for i in range(len(arr)):
        if (arr[i][0] == x):
            list_index.append(arr[i][1])
    return list_index

def Binary_Search(arr : list , x : int) -> int:
    ans = -1
    r = 0
    l = len(arr) - 1
    while l <= r:
        mid = int((l + r)/2)
        if (arr[mid][0] == x):
            return mid
        elif (arr[mid][0] < x):
            l = mid + 1
        else:
            r = mid - 1
    return ans

def check_value(arr1 : list , arr2 : list) -> int:
    label = -1
    for i in range(len(arr1)):
        min_distance = 10**9
        index = Binary_Search(arr2,arr1[i])
        if (min_distance > arr2[index][1]):
            min_distance = arr2[index][1]
            label = arr1[i]
    if (label != -1):
        return label

def array_counts(arr : list , K_NN : int) -> tuple:
    counts = [0]*const_int_mod
    labels = []
    check = set()
    distance_labels = []
    for i in range(K_NN):
        labels.append(arr[i][1])
        if (arr[i][1] not in check):
            distance_labels.append([arr[i][1],arr[i][0]])
            check.add(arr[i][1])
    
    begin = const_int_mod
    end = 0

    for i in range(len(labels)):
        counts[labels[i]] += 1
        begin = min(begin,labels[i])
        end = max(end,labels[i])

    return (begin,end,counts,distance_labels)


def lower_bound(arr : list , x : int) -> int:
    ans = -1
    l = 0
    r = len(arr) - 1
    if (arr[0] == 1):
        while l <= r:
            mid = int((l + r)/2)
            if (arr[mid] == x):
                ans = mid
                r = mid - 1
            elif (arr[mid] > x):
                l = mid + 1
            else:
                r = mid - 1
    else:
        while l <= r:
            mid = int((l + r)/2)
            if (arr[mid][0] == x):
                ans = mid
                r = mid - 1
            elif (arr[mid][0] < x):
                l = mid + 1
            else:
                r = mid - 1
    return ans


colors = COLORS()

def colors_init(colors : COLORS) -> dict:
    colorss = {0 : colors.GREEN,
                1 : colors.BLUE,
                2 : colors.YELLOW,
                3 : colors.PURPLE,
                4 : colors.SKY,
                5 : colors.ORANGE,
                6 : colors.GRAPE,
                7 : colors.GRASS}
    return colorss

def upper_bound(arr : list , x : int) -> int:
    ans = -1
    l = 0
    r = len(arr) - 1
    if (arr[0] == 1):
        while l <= r:
            mid = (l + r)//2
            if (arr[mid] == x):
                ans = mid
                l = mid + 1
            elif (arr[mid] < x):
                l = mid + 1
            else:
                r = mid - 1
    else:
        while l <= r:
            mid = (l + r)//2
            if (arr[mid][0] == x):
                ans = mid
                l = mid + 1
            elif (arr[mid][0] < x):
                l = mid + 1
            else:
                r = mid - 1
    return ans

def calc_distance(p1 : list , p2 : list) -> float:
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def search_and_distance(points : list , clusters : list) -> tuple:
    labels_values = []
    labels = []
    index_distance = []
    # print(points)
    for i in points: #O(n)
        min_points = []
        for c in clusters: # O(n)
            dis = calc_distance(i, c)
            min_points.append(dis)

        min_ans = min(min_points)
        index_labels = min_points.index(min_ans)
        labels_values.append([index_labels,i])
        labels.append(index_labels)
        index_distance.append([index_labels,min_points[index_labels]])
    return (labels_values, labels, index_distance)

def prefix_sum(arr : list) -> list:
    arr_new = [0]*len(arr)
    arr_new[0] = arr[0][1]
    for i in range(1,len(arr)):
        arr_new[i] = arr_new[i - 1] + arr[i][1]
    return arr_new      
