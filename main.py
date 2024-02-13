import pygame
import random
import time
from pygame import mixer
pygame.init()     #  class object init initializing pygame

                       
red=(255,0,0)                #colors
white = (255, 255, 255)
black=(0,0,0)    
green=(0,255,0) 
yellow= (255,255,0)
blue=(0,0,255)


text = green                # setting the colour variable
background = black
snake=yellow



gameWindow = pygame.display.set_mode((900, 600))    # windiw size

pygame.display.set_caption("bhukkad snake")            # setting title of a screen as caption 
pygame.display.update()                              # making screen as updatable and () shows update full screen 
clock = pygame.time.Clock()                          #  for movemovement of snake
font = pygame.font.SysFont(None, 55)                 # setting the font style,font size of a text on screen
gameWindow.fill(pygame.Color(background))

#background sound 
mixer.music.load("stranger-things-124008.wav")
mixer.music.play(-1)
gameover_music=pygame.mixer.Sound("gameover music.wav")

def text_screen(text, color, x, y):                 # ending game function
    screen_text = font.render(text, True, color)    # creating text surface
    gameWindow.blit(screen_text, [x,y])             # setting the position of the text


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.circle(gameWindow, color,(x,y), 10)  # snake structure 

        

# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    gameover_music.play()
    snake_x = 45   #from where snake starts
    snake_y = 85
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    x=True
    global background,text,snake

    food_x = random.randint(20, 900-50)
    food_y = random.randint(60, 600 -50)
    score = 0
    init_velocity = 5
    snake_size = 20 
    fps = 60                                  # fps = frames per second
    while not exit_game:
        
        if game_over:
            gameWindow.fill(background)           # game over screen color
            text_screen('''Game Over! Press space To Continue score: '''+str(score * 10), text, 23, 250)   # game over function call 
            pygame.mixer.music.stop()  # Stop the background music
            gameover_music.play()
        
            for event in pygame.event.get():            # taking a event when game is over
                if event.type == pygame.QUIT:           # x button to close window
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:      # taking a escape button to exit
                        exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:     # taking space button to start again
                        gameloop()
                        

        else:

            for event in pygame.event.get():            # at the time of game screen
                if event.type == pygame.QUIT:           # x button for close window
                    exit_game = True
                    
                        # '-' is according to the coordinates of the screen (0,0) starts from top of the screen
                if event.type == pygame.KEYDOWN:        # right button to move snake right
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:      # left button to move snake left
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:        # up button to move snake up
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:      # down button to move snake down
                        velocity_y = init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_ESCAPE:    # escape button to close game screen 
                        exit_game = True
                        
                    if event.key==pygame.K_c:
                        if x==True:
                            background=white
                            text=blue
                            snake=red
                            x=False
                        else:
                                text = green                # setting the colour variable
                                background = black
                                snake=yellow
                                x=True
                    if event.key == pygame.K_SPACE:    
                        time.sleep(10)

                        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:       # sensitivity to take the point ofthe soze
                score +=1
                food_x = random.randint(20, 900 - 50)                       # ramdomly food pop up
                food_y = random.randint(60, 600 - 50)
                snk_length +=15                                             # setting the size increament of snake
                snakeSound=mixer.Sound("snake-hiss-95241.wav")
                snakeSound.play()
            gameWindow.fill(background)
            text_screen("Score: " + str(score * 10)+"  " +"press space to pause for 10sec" , text,5, 5)           # score updating on screen
            pygame.draw.circle(gameWindow, text, (food_x, food_y),7)
            pygame.draw.line(gameWindow, text, (0,40), (900,40),5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:            #changing the position of snake
                del snk_list[0]

            if head in snk_list[:-1]:               #self collide of snake
                game_over = False

            if snake_x<0 or snake_x>900-20 or snake_y<50 or snake_y>600-20:         # out of the screen
                game_over = True
                
                # pygame.mixer.music.stop()  # Stop the background music
                # gameover_music.play()
        
                
            plot_snake(gameWindow, snake, snk_list, snake_size)        #again plotting the snake after del of snk_list
        pygame.display.update()                                         #updating on screen
        clock.tick(fps)                                                 #making again as movable
    pygame.quit()                                                       #execting the screen
gameloop()