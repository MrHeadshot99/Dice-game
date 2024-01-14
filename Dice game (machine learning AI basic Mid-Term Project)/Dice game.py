from tkinter import * # 그림 그리는 라이브러리
from PIL import Image, ImageTk # 이미지 물러와서 처리하고 tkinter형식으로 변환
import random 
from datetime import datetime
import keyboard
import time
class Dice_game:
    def __init__(self,img,x_coordinate,y_coordinate,distance_x = 114 ,distance_y = 114, velocity_x = 190, velocity_y = 192):
   
        self.img = img # dice들의 이름
        self.value = 0 
        self.value_num = 0
        self.value_total = 0
        self.distance_x = distance_x
        self.distance_y = distance_y
        self.velocity_x = velocity_x  
        self.velocity_y = velocity_y
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.img_id =None
         
    def roll(self):
        self.value_num = self.dice_throw()
        self.value = self.distance_x * self.value_num
        self.value_total += self.value
        
    def dice_throw(self):
        return random.randint(1,6)   
    
    def progress(self):
        global t_0
        if self.img_id is None:  # 이미지 객체가 없으면 생성
            self.img_id = cvs.create_image((self.x_coordinate, self.y_coordinate), image=self.img)

        if self.value_total <= self.distance_x * 6:
            requirement = True
            t_now = datetime.now()
            t_delta = (t_now - t_0).total_seconds()
            p_delta = round(self.velocity_x * t_delta)
            while requirement:
                p = (self.x_coordinate + p_delta, self.y_coordinate)
                cvs.coords(self.img_id, p)
                cvs.pack()
                win.update()
                if p_delta >= self.value:
                    p = (self.x_coordinate+self.value, self.y_coordinate)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    requirement = False
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_x * t_delta)
            self.x_coordinate = self.x_coordinate + self.value

        elif self.value_total > self.distance_x * 6 and self.value_total <= self.distance_x * 6 + self.distance_y * 6:
            
            if self.x_coordinate < 620 + self.distance_x * 6: 
                self.value = self.value - (620 + self.distance_x * 6 - self.x_coordinate) # 이거 중요함
                requirement = True
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_x * t_delta)
                while requirement:
                    p = (self.x_coordinate + p_delta, self.y_coordinate)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    if p[0] >= 620 + self.distance_x * 6:
                        self.x_coordinate = 620 + self.distance_x * 6
                        p = (self.x_coordinate, self.y_coordinate)
                        cvs.coords(self.img_id, p)
                        cvs.pack()
                        win.update()
                        requirement = False
                    t_now = datetime.now()
                    t_delta = (t_now - t_0).total_seconds()
                    p_delta = round(self.velocity_x * t_delta)
                t_0 = datetime.now()
                      
            requirement = True
            t_now = datetime.now()
            t_delta = (t_now - t_0).total_seconds()
            p_delta = round(self.velocity_y * t_delta)
    
            while requirement:
                p = (self.x_coordinate, self.y_coordinate + p_delta)
                cvs.coords(self.img_id, p)
                cvs.pack()
                win.update()
                if p_delta >= self.value:
                    p = (self.x_coordinate, self.y_coordinate+self.value)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    requirement = False
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_y * t_delta)
            self.y_coordinate = self.y_coordinate + self.value
        
        elif self.value_total > self.distance_x * 6 + self.distance_y * 6 and self.value_total <= self.distance_x * 12 + self.distance_y * 6:

            if self.y_coordinate < 200 + self.distance_y * 6:
                self.value = self.value - (200 + self.distance_y * 6 - self.y_coordinate)
                requirement = True
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_y * t_delta)
                while requirement:
                    p = (self.x_coordinate,self.y_coordinate + p_delta)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    if p[1] >= 200 + self.distance_y * 6:
                        self.y_coordinate = 200 + self.distance_y * 6
                        p = (self.x_coordinate , self.y_coordinate)
                        cvs.coords(self.img_id, p)
                        cvs.pack()
                        win.update()
                        requirement = False

                    t_now = datetime.now()
                    t_delta = (t_now - t_0).total_seconds()
                    p_delta = round(self.velocity_y * t_delta)
                t_0 = datetime.now()
            
            requirement = True
            t_now = datetime.now()
            t_delta = (t_now - t_0).total_seconds()
            p_delta = round(self.velocity_x * t_delta)  
            while requirement:
                p = (self.x_coordinate - p_delta , self.y_coordinate)
                cvs.coords(self.img_id, p)
                cvs.pack()
                win.update()
                if p_delta >=  self.value:
                    p = (self.x_coordinate - self.value ,self.y_coordinate)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    requirement = False

                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_x * t_delta)
            self.x_coordinate = self.x_coordinate - self.value 
        
        elif self.value_total > self.distance_x * 12 + self.distance_y * 6 and self.value_total <= self.distance_x * 12 + self.distance_y * 12:

            if self.x_coordinate > 620: 
                self.value = self.value - (self.x_coordinate - 620)
                requirement = True
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_x * t_delta)
                while requirement:
                    p = (self.x_coordinate - p_delta , self.y_coordinate)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    if p[0] < 620:
                        self.x_coordinate = 620
                        p = (self.x_coordinate , self.y_coordinate)
                        cvs.coords(self.img_id, p)
                        cvs.pack()
                        win.update()
                        requirement = False

                    t_now = datetime.now()
                    t_delta = (t_now - t_0).total_seconds()
                    p_delta = round(self.velocity_x * t_delta)
                
                t_0 = datetime.now()

            requirement = True
            t_now = datetime.now()
            t_delta = (t_now - t_0).total_seconds()
            p_delta = round(self.velocity_y * t_delta)  
            while requirement:
                p = (self.x_coordinate, self.y_coordinate - p_delta)
                cvs.coords(self.img_id, p)
                cvs.pack()
                win.update()
                if p_delta >= self.value:
                    p = (self.x_coordinate ,self.y_coordinate - self.value)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    requirement = False
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_y * t_delta)
            self.y_coordinate = self.y_coordinate - self.value

        elif self.value_total > self.distance_x * 12 + self.distance_y * 12:

            if self.y_coordinate > 200: 
                self.value = self.value - (self.y_coordinate - 200)
                requirement = True
                t_now = datetime.now()
                t_delta = (t_now - t_0).total_seconds()
                p_delta = round(self.velocity_y * t_delta)    
                while requirement:
                    p = (self.x_coordinate , self.y_coordinate - p_delta)
                    cvs.coords(self.img_id, p)
                    cvs.pack()
                    win.update()
                    if p[1] < 200:
                        self.y_coordinate = 200
                        p = (self.x_coordinate , self.y_coordinate)
                        cvs.coords(self.img_id, p)
                        cvs.pack()
                        win.update()
                        requirement = False
                    t_now = datetime.now()
                    t_delta = (t_now - t_0).total_seconds()
                    p_delta = round(self.velocity_y * t_delta)
                
                t_0 = datetime.now()

win = Tk() # 창 만드는 함수
win.geometry("1920x1080") # 해상도 
win.title("Chainssoman Dice Game_by subinkimcs99") 

# 그림 그리는 위젯 삽입  
cvs = Canvas(win) 
cvs.config(width = 1920, height =1080, bd = 0,highlightthickness = 0 ) # 화면과 해상도 일치시키기
cvs.configure(background="white")

# scarybackground 
p0 = (960,540)
img0 = Image.open("scarybackground4.jpg")
img0 = img0.resize((1920, 1080), Image.ANTIALIAS)
img0 = ImageTk.PhotoImage(img0, master = win)
cvs.create_image(p0, image = img0)
cvs.pack() 
# gameboard
p1 = (960,540)
img = Image.open("board.jpg") # png파일 불러오기
img = img.resize((800, 800), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img, master = win) # tkinter 파일로 변환
cvs.create_image(p1, image = img) # image 만들기기

cvs.pack() #위젯 창에 배치

# background3
p10 = (960,540)
img10 = Image.open("flower.png")
img10 = img10.resize((800-240, 800-240), Image.ANTIALIAS)
img10 = ImageTk.PhotoImage(img10, master = win)
cvs.create_image(p10, image = img10)
cvs.pack()

# pochita(사용자 플레이어)
p2 = (620+114*2,200+114*3)
img2 = Image.open("pochita2.png")
img2 = img2.resize((100, 100), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2, master = win)
cvs.create_image(p2, image = img2)

cvs.pack() 

# makima(컴퓨터 플레이어)
p3 = (620+114*4, 200+114*3)
img3 = Image.open("makima3.png")
img3 = img3.resize((100, 110), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3, master = win)
cvs.create_image(p3, image = img3)
cvs.pack()

# background
p4 = (190,540)
img4 = Image.open("scary.png")
img4 = img4.resize((350, 800), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(img4, master = win)
cvs.create_image(p4, image = img4)
cvs.pack()

# background2
p5 = (1730,540)
img5 = Image.open("scary2.png")
img5 = img5.resize((350, 800), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(img5, master = win)
cvs.create_image(p5, image = img5)
cvs.pack()



win.update()

# dice images
        
# 메인 함수
while True:
    if keyboard.read_key() == "space": 

        # 플레이어 start 지점에 배치
        cvs.delete(img2)
        cvs.delete(img3)
        win.update()

        p2 = (620,200)
        img2 = Image.open("pochita2.png")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2, master = win)
        cvs.create_image(p2, image = img2)
        cvs.pack() 

        p3 = (620,200)
        img3 = Image.open("makima3.png")
        img3 = img3.resize((100, 110), Image.ANTIALIAS) 
        img3 = ImageTk.PhotoImage(img3, master = win)
        cvs.create_image(p3, image = img3)
        cvs.pack()

        # 객체 정의  
        D1 = Dice_game(img2,p2[0],p2[1])
        D2 = Dice_game(img3,p3[0],p3[1]) 
        Dice = [D1,D2]

        img6 = Image.open("white.png")
        img6 = img6.resize((110, 110), Image.ANTIALIAS)
        img6 = ImageTk.PhotoImage(img6, master = win)
        cvs.create_image((620, 200), image=img6)
        cvs.pack()

        # dice images
        dice_image = ['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png']

        # 주사위 굴리기 
        loop =True
        while loop:
            for i in Dice:
                i.roll()
                if i.value_num == 1:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[0]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()
                if i.value_num == 2:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[1]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()
                if i.value_num == 3:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[2]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()
                if i.value_num == 4:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[3]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()    
                if i.value_num == 5:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[4]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()
                if i.value_num == 6:
                    p9 = (1080,560)
                    img9 = Image.open(dice_image[5]) 
                    img9 = img9.resize((200, 200), Image.ANTIALIAS)
                    img9 = ImageTk.PhotoImage(img9, master = win)
                    cvs.create_image(p9, image = img9)
                    cvs.pack()


                t_0 = datetime.now()
                i.progress()
                time.sleep(1)

            # 게임 종료 조건    
            if D1.value_total >= 12 * D1.distance_x + 12 * D1.distance_y:
                loop = False
                p7 = (960,540)
                img7 = Image.open("pochitawin.png")  
                img7 = img7.resize((800, 800), Image.ANTIALIAS)
                img7 = ImageTk.PhotoImage(img7, master = win)
                cvs.create_image(p7, image = img7)
                cvs.pack()

            elif D2.value_total >= 12 * D2.distance_x + 12 * D2.distance_y:
                loop = False
                p8 = (960,540)
                img8 = Image.open("makaima vs pochita.png") 
                img8 = img8.resize((800, 800), Image.ANTIALIAS)
                img8 = ImageTk.PhotoImage(img8, master = win)
                cvs.create_image(p8, image = img8)
                cvs.pack()

        break 


win.mainloop()
