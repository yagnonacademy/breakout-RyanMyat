'''
Chapter 10 Homework
Breakout Project
Ryan Myat                      
Jan 23, 2020
'''

import pygame

# colors
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,  64,   0)
YELLOW = (255, 215,  77)
GREEN  = (128, 255,   0)

# drawing functions
def draw_ball(screen, x, y):
   pygame.draw.rect(screen, WHITE, [x, y, 14, 14])
   
def draw_paddle(screen, x, y):
   pygame.draw.rect(screen, WHITE, [x, y, 80, 14])

def draw_block1(screen, x, y):
   pygame.draw.rect(screen, RED, [x, y, 78, 15])

def draw_block2(screen, x, y):
   pygame.draw.rect(screen, YELLOW, [x, y, 78, 15])

def draw_block3(screen, x, y):
   pygame.draw.rect(screen, GREEN, [x, y, 78, 15])  

# main function
def main():
   
   # setup
   pygame.init()
    
   # width and height of the screen
   size = [600, 800]
   screen = pygame.display.set_mode(size)
    
   pygame.display.set_caption("B R E A K O U T")

   # game ends when user clicks close
   done = False
    
   # how fast the screen updates
   clock = pygame.time.Clock()

   # current position for ball
   x_ball = 293
   y_ball = 682

   # current position for paddle
   x_pad = 260
   y_pad = 700

   # speed in pixels per frame for ball
   b_xspeed = 0
   b_yspeed = 0

   # speed in pixels per frame for paddle
   p_xspeed = 0

   # game starts when user presses space key
   start = False

   # paddle starts moving after game starts
   move_paddle = False

   # position list for blocks
   position_1 = [[0,150],[87,150],[174,150],[261,150],
                [348,150],[435,150],[522,150],
                [0,174],[87,174],[174,174],[261,174],
                [348,174],[435,174],[522,174]]

   position_2 = [[0,198],[87,198],[174,198],[261,198],
                [348,198],[435,198],[522,198],
                [0,222],[87,222],[174,222],[261,222],
                [348,222],[435,222],[522,222]]

   position_3 = [[0,246],[87,246],[174,246],[261,246],
                [348,246],[435,246],[522,246],
                [0,270],[87,270],[174,270],[261,270],
                [348,270],[435,270],[522,270]]

   # lives
   life = 3

   # score
   score = 0

   # game over
   game_over = False

   # win game
   win_game = False

   # -------- Main Program Loop -------- #

   while not done:
      
      for event in pygame.event.get():
         # user clicks quit
         if event.type == pygame.QUIT:
            done = True

         # user presses down on a key
         elif event.type == pygame.KEYDOWN:
            if start == False:
               if event.key == pygame.K_SPACE:
                  # ball starts moving
                  b_xspeed = 5
                  b_yspeed = -5
                  # paddle starts moving
                  move_paddle = True
                  # prevents user from pressing space key again
                  start = True
            elif move_paddle == True:
               if event.key == pygame.K_LEFT:
                  p_xspeed = -6
               elif event.key == pygame.K_RIGHT:
                  p_xspeed = 6
               
         # user lets up on a key       
         elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               p_xspeed = 0

      # -------- Game Logic -------- #

      # move ball
      x_ball += b_xspeed
      y_ball += b_yspeed
      
      # move paddle 
      x_pad += p_xspeed

      # bounce ball off of walls and ceiling
      if x_ball >= 586 or x_ball <= 0:
         b_xspeed = -b_xspeed
      elif y_ball <= 150:
         b_yspeed = -b_yspeed
      elif y_ball >= 786:
         b_yspeed = 0
         b_xspeed = 0
         p_xspeed = 0
         x_ball = x_pad+33
         y_ball = 682
         life -= 1
         start = False

      # bounce ball off of blocks and delete blocks
      for i in range(len(position_3)):
         if y_ball <= position_3[i][1]+15 and y_ball+14 >= position_3[i][1]:
            if x_ball+14 >= position_3[i][0] and x_ball <= position_3[i][0]+78:
               b_yspeed = -b_yspeed
               del position_3[i]
               score += 1
               break
            
      for i in range(len(position_2)):
         if y_ball <= position_2[i][1]+15 and y_ball+14 >= position_2[i][1]:
            if x_ball+14 >= position_2[i][0] and x_ball <= position_2[i][0]+78:
               b_yspeed = -b_yspeed
               del position_2[i]
               score += 1
               break
         
      for i in range(len(position_1)):
         if y_ball <= position_1[i][1]+15 and y_ball+14 >= position_1[i][1]:
            if x_ball+14 >= position_1[i][0] and x_ball <= position_1[i][0]+78:
               b_yspeed = -b_yspeed
               del position_1[i]
               score += 1
               break

      # bounce ball off of paddle
      if y_ball <= y_pad and y_ball+14 >= y_pad+1:
         if x_ball+14 >= x_pad and x_ball <= x_pad+80:
            b_yspeed = -b_yspeed
      
      elif y_ball <= y_pad+14 and y_ball+14 >= y_pad:
         if x_ball+14 >= x_pad and x_ball <= x_pad+80:
            b_xspeed = -b_xspeed
      
      # stops paddle from going off-screen
      if x_pad < 0:
         x_pad = 0
      elif x_pad > 520:
         x_pad = 520

      # lose game
      if life == 0:
         start = True
         move_paddle = False
         game_over = True

      # win game
      if score == 42:
         start = True
         move_paddle = False
         b_xspeed = 0
         b_yspeed = 0
         win_game = True
         
      # -------- Drawing Code -------- #
         
      # color the screen black
      screen.fill(BLACK)
         
      # draw the ball
      draw_ball(screen, x_ball, y_ball)
      
      # draw the paddle
      draw_paddle(screen, x_pad, y_pad)

      # draw the blocks
      for i in range(len(position_1)):
         draw_block1(screen, position_1[i][0], position_1[i][1])

      for i in range(len(position_2)):
         draw_block2(screen, position_2[i][0], position_2[i][1])

      for i in range(len(position_3)):
         draw_block3(screen, position_3[i][0], position_3[i][1])
         
      # lives
      font = pygame.font.SysFont('Calibri', 35, True, False)
      text = font.render("LIFE : " + str(life), True, WHITE)
      screen.blit(text, [60, 85])
      
      # score
      font = pygame.font.SysFont('Calibri', 35, True, False)
      text = font.render("SCORE : " + str(score), True, WHITE)
      screen.blit(text, [360, 85])

      # win game
      if win_game == True:
         font = pygame.font.SysFont('Calibri', 50, True, False)
         text = font.render("CONGRATS", True, WHITE)
         screen.blit(text, [188, 350])

      # game over
      elif game_over == True:
         font = pygame.font.SysFont('Calibri', 50, True, False)
         text = font.render("GAME OVER", True, WHITE)
         screen.blit(text, [185, 350])
         
      # update the screen
      pygame.display.flip()

      # limit the frames per second
      clock.tick(60)

   # close the window and quit
   pygame.quit()

main ()
