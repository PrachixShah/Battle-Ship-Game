# Prachi Shah
# BattleShip: ISU Final 
# 2020-06-10

# First develop the grid, and 5 pre-set "ships"

import turtle
from random import randint
import random 
import string

t = turtle.Turtle()
t.speed(0)

s = turtle.Screen()
t.hideturtle()

def grid():
  t.color("#000000")
  t.penup()
  t.goto(-150,-100)

  t.pendown()
  t.forward(250)
  t.lt(90)
  t.forward(250)
  t.lt(90)
  t.forward(250)
  t.lt(90)
  t.forward(250)
  t.lt(90)

  for times in range(0, 2):
    t.forward(25)
    t.lt(90)
    t.forward(250)
    t.rt(90)
    t.forward(25)
    t.rt(90)
    t.forward(250)
    t.lt(90)
    t.forward(25)
    t.lt(90)
    t.forward(250)
    t.rt(90)
    t.forward(25)
    t.rt(90)
    t.forward(250)
    t.lt(90)
    t.forward(25)
  
  t.lt(180)
  t.forward(125)
  t.rt(90)
  t.forward(250)

  t.rt(90)
  t.forward(125)
  
  for times in range(0, 4):
    t.rt(90)
    t.forward(25)
    t.rt(90)
    t.forward(250)
    t.lt(90)
    t.forward(25)
    t.lt(90)
    t.forward(250)
  
  t.rt(90)
  t.forward(25)
  t.rt(90)
  t.forward(250)
grid()

def labelling_letters():
  t.penup()
  t.rt(90)
  t.forward(230)
  t.rt(90)
  t.forward(9)
  t.pendown()
  t.write('A')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('B')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('C')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('D')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('E')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('F')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('G')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('H')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('I')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('J')
labelling_letters()

t.penup()
t.goto(105,-100)

def labelling_no():
  t.penup()
  t.lt(90)
  t.forward(9)
  t.pendown()
  t.write('1')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('2')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('3')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('4')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('5')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('6')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('7')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('8')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('9')
  t.penup()
  t.forward(25)
  t.pendown()
  t.write('10')

labelling_no()

coordinates = {
  
  'A_10': (-137.5, 137.5),
  'A_9' : (-137.3, 112.5),
  'A_8' : (-137.5, 87.5),
  'A_7' : (-137.5, 62.5),
  'A_6' : (-137.5, 37.5),
  'A_5' : (-137.5, 12.5),
  'A_4' : (-137.5, -12.5),
  'A_3' : (-137.5, -37.5),
  'A_2' : (-137.5, -62.5),
  'A_1' : (-137.5, -87.5),

  'B_10': (-112.5, 137.5),
  'B_9' : (-112.5, 112.5),
  'B_8' : (-112.5, 87.5),
  'B_7' : (-112.5, 62.5),
  'B_6' : (-112.5, 37.5),
  'B_5' : (-112.5, 12.5),
  'B_4' : (-112.5, -12.5),
  'B_3' : (-112.5, -37.5),
  'B_2' : (-112.5, -62.5),
  'B_1' : (-112.5, -87.5),

  'C_10': (-87.5, 137.5),
  'C_9' : (-87.5, 112.5),
  'C_8' : (-87.5, 87.5),
  'C_7' : (-87.5, 62.5),
  'C_6' : (-87.5, 37.5),
  'C_5' : (-87.5, 12.5),
  'C_4' : (-87.5, -12.5),
  'C_3' : (-87.5, -37.5),
  'C_2' : (-87.5, -62.5),
  'C_1' : (-87.5, -87.5),

  'D_10': (-62.5, 137.5),
  'D_9' : (-62.5, 112.5),
  'D_8' : (-62.5, 87.5),
  'D_7' : (-62.5, 62.5),
  'D_6' : (-62.5, 37.5),
  'D_5' : (-62.5, 12.5),
  'D_4' : (-62.5, -12.5),
  'D_3' : (-62.5, -37.5),
  'D_2' : (-62.5, -62.5),
  'D_1' : (-62.5, -87.5),

  'E_10' : (-37.5, 137.5),
  'E_9' : (-37.5, 112.5),
  'E_8' : (-37.5, 87.5),
  'E_7' : (-37.5, 62.5),
  'E_6' : (-37.5, 37.5),
  'E_5' : (-37.5, 12.5),
  'E_4' : (-37.5, -12.5),
  'E_3' : (-37.5, -37.5),
  'E_2' : (-37.5, -62.5),
  'E_1' : (-37.5, -87.5),

  'F_10': (-12.5, 137.5),
  'F_9' : (-12.5, 112.5),
  'F_8' : (-12.5, 87.5),
  'F_7' : (-12.5, 62.5),
  'F_6' : (-12.5, 37.5),
  'F_5' : (-12.5, 12.5),
  'F_4' : (-12.5, -12.5),
  'F_3' : (-12.5, -37.5),
  'F_2' : (-12.5, -62.5),
  'F_1' : (-12.5, -87.5),

  'G_10': (12.5, 137.5),
  'G_9' : (12.5, 112.5),
  'G_8' : (12.5, 87.5),
  'G_7' : (12.5, 62.5),
  'G_6' : (12.5, 37.5),
  'G_5' : (12.5, 12.5),
  'G_4' : (12.5, -12.5),
  'G_3' : (12.5, -37.5),
  'G_2' : (12.5, -62.5),
  'G_1' : (12.5, -87.5),

  'H_10': (37.5, 137.5),
  'H_9' : (37.5, 112.5),
  'H_8' : (37.5, 87.5),
  'H_7' : (37.5, 62.5),
  'H_6' : (37.5, 37.5),
  'H_5' : (37.5, 12.5),
  'H_4' : (37.5, -12.5),
  'H_3' : (37.5, -37.5),
  'H_2' : (37.5, -62.5),
  'H_1' : (37.5, -87.5),

  'I_10' : (62.5, 137.5),
  'I_9' : (62.5, 112.5),
  'I_8' : (62.5, 87.5),
  'I_7' : (62.5, 62.5),
  'I_6' : (62.5, 37.5),
  'I_5' : (62.5, 12.5),
  'I_4' : (62.5, -12.5),
  'I_3' : (62.5, -37.5),
  'I_2' : (62.5, -62.5),
  'I_1' : (62.5, -87.5),

  'J_10': (87.5, 137.5),
  'J_9' : (87.5, 112.5),
  'J_8' : (87.5, 87.5),
  'J_7' : (87.5, 62.5),
  'J_6' : (87.5, 37.5),
  'J_5' : (87.5, 12.5),
  'J_4' : (87.5, -12.5),
  'J_3' : (87.5, -37.5),
  'J_2' : (87.5, -62.5),
  'J_1' : (87.5, -87.5)
}

# if target == ship then turn red circle. otherwise smaller black dot/circle

def game():
  print("Hello! This is a battleship game, made by Prachi Shah. The game will continue until you have sunk all three of the enemy battleships. Good luck Captain.") 

  ship_x = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
  ship_y = random.randint(1,10)

  ship_x2 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
  ship_y2 = random.randint(1,10)

  ship_x3 = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
  ship_y3 = random.randint(1,10)

  if (ship_x == ship_x2 and ship_y == ship_y2) or (ship_x == ship_x3 and ship_y == ship_y3): 
    if ship_y < 10: 
      ship_y + 1
    else:
      ship_y - 1
  if ship_x2 == ship_x3 and ship_y2 == ship_y3:
    if ship_y2 > 1: 
      ship_y2 -1
    else: 
      ship_y2 + 1

  print(ship_x, ship_y)
  print(ship_x2, ship_y2)
  print(ship_x3, ship_y3)

  while True: 
    try: 
      user_x =( input("Please enter the letter of your coordinate:  ")).upper()
      user_y = int(input("Please enter the number of your coordinate:  "))
          
      user_xy = (user_x + '_' + str(user_y))
      user_guess = coordinates[user_xy]
      
      if (user_x == ship_x and user_y == ship_y) or (user_x == ship_x2 and user_y == ship_y2) or (user_x == ship_x3 and user_y == ship_y3):
        t.penup()
        t.goto(user_guess)
        t.pendown()
        t.dot(5, "red")
        wins + 1
      else:
        t.penup()
        t.goto(user_guess)
        t.pendown()
        t.dot(5, "blue")
    except KeyError: 
      print("Try again. I need a proper input to continue")
    except ValueError: 
      print("Your input doesn't make sense. Let's try again.")

    
  print("Great job captain! Mission was a success!")


game()