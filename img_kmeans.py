from init_class import pygame,COLORS
from sklearn.cluster import KMeans
import cv2
import os
import numpy as np

#test
path_test = "img"

file_img_test = "list_img/"
list_test = os.listdir(path_test)

stt_img = 1
def train_model(index : int , k : int):
    image = cv2.imread(path_test + "/" + list_test[index - 1])
    width = image.shape[0]
    height = image.shape[1]
    image = image.reshape(width*height,3)
    kmeans = KMeans(n_clusters=k).fit(image)

    labels = kmeans.predict(image)
    clusters = kmeans.cluster_centers_
    labels_reshaped = labels.reshape(width, height)
    img2 = clusters[labels_reshaped]
    img2 = list(img2)
    yield img2

def format_array(arr):
    return arr[len(arr) - 1]

file_file = os.listdir("img")

class draw_rect_backgroud:
    def __init__(self,x : int , y : int, w : int, h : int, colors : dict) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colors = colors

    def show(self) -> None:
        pygame.draw.rect(screen,self.colors.BLACK,(self.x,self.y, self.w, self.h))
        pygame.draw.rect(screen,self.colors.WHITE,(self.x + 5, self.y + 5, self.w - 10, self.h - 10))       
class Text:
    def __init__(self,
                 button_n_clusters : pygame.surface.Surface,
                button_plus : pygame.surface.Surface,
                button_tru : pygame.surface.Surface,
                button_run : pygame.surface.Surface,
                button_show : pygame.surface.Surface,
                button_selection : pygame.surface.Surface,
                ngang : pygame.surface.Surface):
        self.button_n_clusters = button_n_clusters
        self.button_plus = button_plus
        self.button_tru = button_tru
        self.button_run = button_run
        self.button_show = button_show
        self.button_selection = button_selection
        self.ngang = ngang

    def show_(self):
        screen.blit(self.button_n_clusters,(1230,25))
        screen.blit(self.button_plus,(1255,80))
        screen.blit(self.button_tru,(1225 + 80 + 10 + 30,70))
        screen.blit(self.button_run,(1280,145))
        screen.blit(self.button_show,(1235,205))
        screen.blit(self.button_selection,(1235,265))
        screen.blit(self.button_plus,(1225 + 60 + 15,260))
        screen.blit(self.button_tru,(1225 + 60 + 50 + 20,250))
        screen.blit(self.ngang,(650,338))

pygame.init()

colors = COLORS()
height = 1400
witd = 750
screen = pygame.display.set_mode((height,witd))
clock = pygame.time.Clock()
runing = True
font = pygame.font.SysFont('sans', 20)
font1 = pygame.font.SysFont('sans', 30)
font2 = pygame.font.SysFont('sans', 40)
font3 = pygame.font.SysFont('sans', 50) 
k = 0

list_ = []
shape = (500,500)

path1 = "img"
path2 = "list_img"

list_all = []
list_img_ = []

index = 0
run_img = False
run_kmeans = False

cnt = 1
index_img_dir = []
img_ouput = []

check111 = False

while runing:
    clock.tick(60)
    screen.fill(colors.BACKGROUND)
    x_mouse , y_mouse = pygame.mouse.get_pos()

    #Backgroud
    rect = draw_rect_backgroud(20,20,1200,700,colors)
    rect.show()

   
    #n_clusters
    rect = draw_rect_backgroud(1225,20,170,50,colors)
    rect.show()

    # + -
    rect = draw_rect_backgroud(1225,80,80,50,colors)
    rect.show()
    rect = draw_rect_backgroud(1225 + 80 + 10,80,80,50,colors)
    rect.show()

   
    #button run
    rect = draw_rect_backgroud(1225,140,170,50,colors)
    rect.show()

    #button show
    rect = draw_rect_backgroud(1225,200,170,50,colors)
    rect.show()
    
    #button selection
    rect = draw_rect_backgroud(1225,260,50,50,colors)
    rect.show()
    #+
    rect = draw_rect_backgroud(1225 + 60,260,50,50,colors)
    rect.show()
    #-
    rect = draw_rect_backgroud(1225 + 60 + 50,260,50,50,colors)
    rect.show()

    #Menu
    rect = draw_rect_backgroud(1225,320,170,400,colors)
    rect.show()
    
    button_plus = font2.render("+" , True, colors.BLACK)
    button_tru = font3.render("-" , True, colors.BLACK)
    button_run = font1.render("Run" , True, colors.BLACK)
    button_show = font1.render("Image Show" , True, colors.BLACK)
    pygame.draw.line(screen,colors.BLACK,(560,350),(650,350),3)
    ngang = font.render("►", True, colors.BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if (1225 <= x_mouse <= 1225 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k >= 0):
                    k += 1

            elif (1225 + 80 + 10 <= x_mouse <= 1225 + 80 + 10 + 80 and 80 <= y_mouse <= 80 + 50):
                if (k > 0):
                    k -= 1  

            elif (1225 <= x_mouse <= 1225 + 170 and 140 <= y_mouse <= 140 + 50):
                #format arr
                img2 = train_model(index,k)
                print(type(img2))
                img2 = list(img2)                
                img2 = format_array(img2)
                img2 = np.array(img2)

                name_img = list_test[index - 1]
                index_test = name_img.index(".")                
                cv2.imwrite(file_img_test + str(stt_img) + name_img[index_test:], img2)
                img_ouput.append(str(cnt) + name_img[index_test:])
                cnt += 1            
                stt_img += 1
                run_kmeans = True
                print("Run")

            elif (1225 <= x_mouse <= 1225 + 170 and 200 <= y_mouse <= 200 + 50):
                run_img = True

            elif (1225 + 60 <= x_mouse <= 1225 + 60 + 50 and 260 <= y_mouse <= 260 + 50):
                if (index >= 0):
                    index += 1
                run_img = False
                run_kmeans = False
                k = 0
                if (k == 0 and cnt != 0):
                    index_img_dir.append(cnt)
                print("+ menu")

            elif (1225 + 60 + 50 <= x_mouse <= 1225 + 60 + 50 + 50 and 260 <= y_mouse <= 260 + 50):
                if (index > 0):
                    index -= 1
                run_img = False
                print("- menu")
            else:
                ...
    if (run_img):
        if (index != 0 and k != -1):
            image = pygame.image.load(path1 + "/" + file_file[index - 1])
            image = pygame.transform.scale(image, shape)
            screen.blit(image, (60, 80))            
        else:
            pass
    if (run_kmeans):
        image1 = pygame.image.load(path2 + "/" + img_ouput[len(img_ouput) - 1])
        image1 = pygame.transform.scale(image1, shape)
        screen.blit(image1,(665, 80))
    else:
        pass
     
    button_selection = font1.render(str(index) , True, colors.BLACK)
    button_n_clusters = font1.render("n_clusters = " + str(k) , True, colors.BLACK)
    show_text = Text(button_n_clusters,
                     button_plus,
                     button_tru,
                     button_run,
                     button_show,
                     button_selection,
                     ngang
                     )
    show_text.show_()

    pygame.display.flip()
pygame.quit()
