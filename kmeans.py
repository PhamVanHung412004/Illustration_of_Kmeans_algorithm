# import pygame
print("scussflully")
from random import randint
from sklearn.cluster import KMeans
from init_class import Draw_ox_oy,Show_mouse,pygame,COLORS,upper_bound,lower_bound,colors_init,points_black_rect,points_white_circle,search_and_distance,prefix_sum,draw_rect_backgroud,screen

colors = COLORS()
rect_black = points_black_rect()
rect_white = points_white_circle()
COLORS_LABELS = colors_init(colors)
const = int(1e4)

# def solve():
class Draw_point:
    def __init__(self,point: int, WHITE : tuple,BLACK: tuple ,label : list, COlOR : dict) -> None:
        self.point = point
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.label = label
        self.COlOR = COlOR

    def draw_points_panel(self) -> None:
        points = self.point
        color = self.COlOR
        labels = self.label

        for i in range(len(points)):
            pygame.draw.circle(screen,self.BLACK,(points[i][0] + 50, 600 - points[i][1]),8)
            if (len(labels) == 0):
                pygame.draw.circle(screen,self.WHITE,(points[i][0] + 50,600 - points[i][1]),7)
            else:
                pygame.draw.circle(screen,color[labels[i]],(points[i][0] + 50,600 - points[i][1]),8)

class Name_button:
    def __init__(self,random : pygame.surface.Surface,
                 algorithm : pygame.surface.Surface,
                 error : pygame.surface.Surface,
                 reset : pygame.surface.Surface,
                 k_button : pygame.surface.Surface,
                 run_button : pygame.surface.Surface, 
                 dau_cong : pygame.surface.Surface,
                 dau_tru : pygame.surface.Surface) -> None:
        self.random = random
        self.algorithm = algorithm
        self.error = error
        self.reset = reset
        self.k_button = k_button
        self.run_button = run_button
        self.dau_cong = dau_cong
        self.dau_tru = dau_tru
    
    def show_name_button(self) -> None: 
        screen.blit(self.k_button,(1230,25))
        screen.blit(self.dau_cong,(1255,80))
        screen.blit(self.dau_tru,(1225 + 80 + 10 + 30,70)) 
        screen.blit(self.random,(1250,145))
        screen.blit(self.algorithm,(1235,265))
        screen.blit(self.error,(1235,330))
        screen.blit(self.reset,(1270,385))
        screen.blit(self.run_button,(1280,205))

class Draw_clusters:
    def __init__(self,cluster : list, COLOR : dict) -> None:
        self.cluster = cluster
        self.COLOR = COLOR

    def draw_clusters(self) -> None:
        clusters = self.cluster
        COLORS = self.COLOR
        for i in range(len(clusters)):
            # pygame.draw.circle(screen,COLORS[i],(clusters[i][0] + 50, 600 - clusters[i][1]),8)
            pygame.draw.rect(screen,COLORS[i],(clusters[i][0] + 50, 600 - clusters[i][1],15,15))

def cacl_point_mid(x : float ,y : float, cnt : int) -> float:
    value = [x / cnt, y / cnt]
    return value

pygame.init()
clock = pygame.time.Clock()
runing = True
points = []
clusters = []
labels = []
labels_values = []
k = 0
error = 0
prefix_sum_x = []
prefix_sum_y = []
index_distance = []
arr1 = []
arr2 = []
arr3 = [] 
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 

while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse,y_mouse = pygame.mouse.get_pos()
    
    x = font.render("X", True, colors.BLACK)
    y = font.render("Y", True, colors.BLACK)
    O = font.render("0", True, colors.BLACK)
    screen.blit(x, (1100, 605))
    screen.blit(y, (30, 35))
    screen.blit(O, (35, 590))

    dau_cong = font2.render("+", True, colors.BLACK)
    dau_tru = font3.render("-", True, colors.BLACK)
    random_button = font1.render("RANDOM", True, colors.BLACK)
    algorithm_button = font1.render("ALGORITHM", True, colors.BLACK)
    reset_button = font1.render("RESET" , True, colors.BLACK)
    run_button = font1.render("RUN" , True, colors.BLACK)
    img_button = font1.render("IMG" , True, colors.BLACK)

    title = font3.render("Illustration of kmeans algorithm",True,colors.BLACK)
    screen.blit(title,(200,600))


    #Font
    up = font.render("▲", True, colors.BLACK)
    ngang = font.render("►", True, colors.BLACK)

    #draw ox,oy,up,ngang
    draw_ox_oy = Draw_ox_oy(50, 50, 50, 600, 50, 600, 1100, 600, colors.BLACK, up, ngang,screen)
    draw_ox_oy.show()

    # Show mouse
    show_mouse = Show_mouse(x_mouse, y_mouse, font,colors.BLACK,screen)
    if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
        show_mouse.show()

    #n_clusters
    rect = draw_rect_backgroud(1225,20,170,50,colors)
    rect.show()

    # + -
    rect = draw_rect_backgroud(1225,80,80,50,colors)
    rect.show()
    rect = draw_rect_backgroud(1225 + 80 + 10,80,80,50,colors)
    rect.show()

   
    #button random
    rect = draw_rect_backgroud(1225,140,170,50,colors)
    rect.show()

    #button run
    rect = draw_rect_backgroud(1225,200,170,50,colors)
    rect.show()
    
    #button thuat toan
    rect = draw_rect_backgroud(1225,260,170,50,colors)
    rect.show()
    
    #button error
    rect = draw_rect_backgroud(1225,320,170,50,colors)
    rect.show()

    #button reset
    rect = draw_rect_backgroud(1225,380,170,50,colors)
    rect.show()    

    #Event mouse
    for event in pygame.event.get():
        #Button quit
        if (event.type == pygame.QUIT):
            runing = False  

        #Mouse button down
        if (event.type == pygame.MOUSEBUTTONDOWN):
            #button down
            if (50 <= x_mouse <= 1100 and 50 <= y_mouse <= 600):
                labels = []
                x = float(x_mouse - 50)
                y = float(abs(y_mouse - 600))
                point = [x,y]
                points.append(point)

            # += 1 clusters
            if (1225 <= x_mouse <= 1225 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k >= 0 and k < 8):
                    k += 1
            # -= 1 clusters
            if (1225 + 80 + 10 <= x_mouse <= 1225 + 80 + 10 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k > 0):
                    k -= 1
            
            #button random
            if (1225 <= x_mouse <= 1225 + 170 and 140 <= y_mouse <= 140 + 50):
                T = k
                clusters = []
                test_mid = []
                while(T > 0):
                    cluster = [randint(50,1110) - 50, abs(randint(50,600) - 600)]
                    clusters.append(cluster)
                    test_mid.append(cluster)
                    T -= 1

            #button run   
            if (1225 <= x_mouse <= 1225 + 170 and 200 <= y_mouse <= 200 + 50):
                try:
                    print("Run")
                    labels = []
                    labels_values = []
                    prefix_sum_x = []
                    prefix_sum_y = []
                    index_distance = []
                    error = 0                    

                    if (len(clusters) == 0):
                        continue
                    
                    (labels_values, labels, index_distance) = search_and_distance(points,clusters)
                    
                    #=> O(n^2)
                    labels_values.sort() # O(nlog(n))
                    index_distance.sort() # O(nlog(n))
                    value_init = labels_values[0][1]

                    prefix_sum_x = [0] * len(labels_values) # O(n)
                    prefix_sum_y = [0] * len(labels_values) # O(n)

                    prefix_sum_x[0] = value_init[0]
                    prefix_sum_y[0] = value_init[1] 

                    for i in range(1,len(labels_values)): # O(n)
                        value = labels_values[i][1]
                        prefix_sum_x[i] = prefix_sum_x[i - 1] + value[0] 
                        prefix_sum_y[i] = prefix_sum_y[i - 1] + value[1]
                        index_distance[i][1] += index_distance[i - 1][1]
                        
                    for i in range(0,7): # O(m)
                        first_value = lower_bound(labels_values,i) # O(log(n))
                        second_value = upper_bound(labels_values,i) # O(log(n))
                        
                        if (first_value != -1 and second_value != -1 and second_value - first_value + 1 > 0):
                            if (first_value == 0):
                                ans = cacl_point_mid(
                                    prefix_sum_x[second_value],
                                    prefix_sum_y[second_value],
                                    second_value - first_value + 1
                                )
                                error += index_distance[second_value][1]
                                clusters[i] = ans
                            else:
                                ans = cacl_point_mid(
                                    prefix_sum_x[second_value] - prefix_sum_x[first_value - 1],
                                    prefix_sum_y[second_value] - prefix_sum_y[first_value - 1],
                                    second_value - first_value + 1
                                )
                                error += index_distance[second_value][1] - index_distance[first_value - 1][1]
                                clusters[i] = ans
                except:
                    print("Error")
                    break

            #Button ALGORITHM
            if (1225 <= x_mouse <= 1225 + 170 and 260 <= y_mouse <= 260 + 50):
                try:
                    error = 0
                    arr1 = []
                    arr2 = []
                    arr3 = [] 
                    print("\nAlgorithm")
                    kmeans = KMeans(n_clusters=k).fit(points)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                    
                    (arr1, arr2, arr3) = search_and_distance(points,clusters)
                    arr3.sort()
                    arr2 = list(set(arr2))

                    total_error = prefix_sum(arr3)
                    for i in range(len(arr2)):
                        l = lower_bound(arr3,arr2[i])
                        r = upper_bound(arr3,arr2[i])
                        if (l != -1 and r != -1):
                            if (l == 0):
                                error += total_error[r]
                            else:
                                error += total_error[r] - total_error[l - 1]
                except:
                    print("Error")
                    break
                    
            if (585 <= x_mouse <= 785 and 610 <= x_mouse <= 660):
                continue
            
            #Button reset
            if (1225 <= x_mouse <= 1225 + 170 and 380 <= y_mouse <= 380 + 50):
                try: 
                    points = []
                    clusters = []
                    labels = []
                    index_distance = []
                    prefix_sum_x = []
                    prefix_sum_y = []
                    error = 0
                    k = 0
                    arr1 = []
                    arr2 = []
                    arr3 = []
                except:
                    print("Error")
                    break

            #button IMG
            # elif (1225 <= x_mouse <= 1225 + 170 and 440 <= y_mouse <= 440 + 50):
            #     import img_kmeans
            #     print("IMG")

            # else:
            #     print("Error")
            #     continue
    k_button = font1.render("n_clusters = " + str(k), True, colors.BLACK)         
    error_button = font.render("ERROR = "  + str(int(error)), True, colors.BLACK)
    
    name_button = Name_button(random_button,
                              algorithm_button,
                              error_button,
                              reset_button,
                              k_button,
                              run_button,
                              dau_cong,
                              dau_tru)
    
    name_button.show_name_button()
    draw_clusters = Draw_clusters(clusters, COLORS_LABELS)
    draw_clusters.draw_clusters()

    draw_points = Draw_point(points, colors.WHITE, colors.BLACK,labels,COLORS_LABELS)
    draw_points.draw_points_panel()
    
    pygame.display.flip()
pygame.quit()
