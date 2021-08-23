from typing import Text
import pygame
from sudokualgorithm import solve,possible
import time
pygame.font.init()
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Grid:
    board=[[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9],
     ]
    def __init__(self,rows,cols,width,height):
        self.rows=rows
        self.cols=cols
        self.cubes=[[Cube(self.board[i][j],i,j,width,height) for j in range(cols)]for i in range(rows)]
        self.width=width
        self.height=height
        self.model=None
        self.selected=None
    def draw(self,win):
        gap=self.width/9
        for i in range(self.rows+1):
            thick=1 if i%3 else 4
            pygame.draw.line(win,(0,0,0),(0,i*gap),(self.width,i*gap),thick)
            pygame.draw.line(win,(0,0,0),(i*gap,0),(i*gap,self.height),thick)
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)
    
    def click(self,pos):
        if pos[0]<self.width and pos[1]<self.height:
            gap=self.width/9
            x=pos[0]//gap
            y=pos[1]//gap
            return int(y),int(x)
        else:
            return None
    def select(self,row,col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected=False
        self.cubes[row][col].selected=True
        self.selected=(row,col)

class Cube:
    rows=9
    cols=9
    def __init__(self,value,row,col,width,height):
        self.value=value
        self.temp=0
        self.row=row
        self.col=col
        self.width=width
        self.height=height
        self.selected=False

    def draw(self,win):
        fnt=pygame.font.SysFont('comicsans',40)
        gap=self.width/9
        x=self.col*gap
        y=self.row*gap
        if self.temp!=0 and self.value==0:
            text=fnt.render(str(self.temp),1,(128,128,128))
            win.blit(text,(x+5,y+5))
        elif self.value!=0:
            text=fnt.render(str(self.value),1,(0,0,0))
            win.blit(text,(x+(gap/2-text.get_width()/2),y+(gap/2-text.get_width()/2)))
        if self.selected:
            pygame.draw.rect(win,(255,0,0),(x,y,gap,gap),3)



    
    


def redraw_window(win,board,time,strikes):
    #white background
    win.fill((255,255,255))
    #draw time
    fnt=pygame.font.SysFont('comicsans',40)
    text=fnt.render("Time:"+format_time(time),1,(0,0,0))
    win.blit(text,(560-210,560))
    text=fnt.render('X'*strikes,1,(255,0,0))
    win.blit(text,(20,560))
    board.draw(win)

def format_time(seconds):
    hr=seconds//3600
    mts=(seconds%3600)//60
    sec=((seconds%3600)%60)
    Time=f' {hr} : {mts} : {sec}'
    return Time

def main():
    win=pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board=Grid(9,9,540,540)
    strikes=0
    start=time.time()
    run=True
    while run:
        play_time=round(time.time()-start)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run =False
            #if event.type==pygame.KEYDOWN:
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                clicked=board.click(pos)
                if clicked:
                    board.select(clicked[0],clicked[1])
                    key=None
        redraw_window(win,board,play_time,strikes)
        pygame.display.update()
main()
pygame.quit()

