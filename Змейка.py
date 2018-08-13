def draw_element(i, j):
    canvas.create_oval((i + 1) * 25, (j + 1) * 25, (i + 2) * 25, (j + 2) * 25, fill = "gold")
    
def draw_snake():
    global table_x, table_y
    i = 0
    while i < len(table_x):
        draw_element(table_x[i], table_y[i])
        i += 1
        
def draw_field():
    #canvas.create_rectangle(0, 0, (30 + 2) * 25, (20 + 2) * 25, fill = 'brown')
    canvas.create_rectangle(0, 0, (30 + 2) * 25, (20 + 2) * 25, fill = 'darkgreen')
    
def draw_bonus():
    global xb, yb
    canvas.create_oval((xb + 1) * 25, (yb + 1) * 25, (xb + 2) * 25, (yb + 2) * 25, fill = 'red')
     
def draw_all():
    draw_field()
    draw_snake()
    draw_bonus()
    canvas.update()
    
def left(event):
    global vx, vy
    vx = -1
    vy = 0
    
def right(event):
    global vx, vy
    vx = 1
    vy = 0
 
def up(event):
    global vx, vy
    vx = 0
    vy = -1
    
def down(event):
    global vx, vy
    vx = 0
    vy = 1
  
 
from tkinter import *
import time
import random
 
root = Tk()
canvas = Canvas(root, width = (30 + 2) * 25, height = (20 + 2) * 25)
canvas.pack()
 
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
 
table_x = [11, 12, 13, 14]
table_y = [3, 3, 3, 3]
xb = 17
yb = 17
 
win = True
vx = -1
vy = 0
 
while win:
    if (table_x[0] == 0) and (vx == -1): table_x[0] = 29
    if (table_x[0] == 29) and (vx == 1): table_x[0] = 0
    if (table_y[0] == 0) and (vy == -1): table_y[0] = 19
    if (table_y[0] == 19) and (vy == 1): table_y[0] = 0
    
    table_x = [table_x[0] + vx] + table_x
    table_y = [table_y[0] + vy] + table_y
        
    if (table_x[0] != xb) or (table_y[0] != yb):
        table_x.pop(-1)
        table_y.pop(-1)
    else:
        xb, yb = random.randint(0, 29), random.randint(0, 19)
    
    i = 1
    while i < len(table_x):    
        if (table_x[0] == table_x[i]) and (table_y[0] == table_y[i]): win = False
        i += 1
    
    draw_all()
    time.sleep(0.1)
    canvas.delete('all')
 
root.mainloop()