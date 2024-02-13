import random
import math
import pygame
from pygame import mixer
#intialize the pygame
pygame.init()
#creating a screen
screen = pygame.display.set_mode((720, 500))
#background
background=pygame.image.load('background.png')
#background sound 
mixer.music.load("background.wav")
mixer.music.play(-1)
#title &icon
pygame.display.set_caption("space shuttle")
icon= pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
#player

playerImg= pygame.image.load('arcade-game (1).png')
playerX=270 
playerY=380
playerX_change=0

#enemy
enemyImg= []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_enemies= 6
     #game over
for i in range(num_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
bulletImg= pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font("Pacifico.ttf",42)
testX=10
testY=10
# Game Over
over_font = pygame.font.Font('Pacifico.ttf', 64)
#game over music
game_over_music = pygame.mixer.Sound("game_over1.wav")

def show_score(X,Y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
   
    screen.blit(score,(X,Y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))    

def player(X,Y):
    screen.blit(playerImg, (X,Y))
def enemy(X,Y,i):
    screen.blit(enemyImg[i], (X,Y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bulletImg,(x+16,y+10)) 
def isCollision(enemyX,enemyY,bulletX, bulletY):
    distance=math.sqrt((math.pow(enemyX- bulletX,2))+(math.pow(enemyY- bulletY,2)))
    if distance<27:
        return True
    else:
       return False
def reset_game():
    global score, game_over
    score = 0
    game_over = False

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    def game_over_music():
        game_over_music.play()

# Create a reset button
reset_button = Button(340, 400, 100, 50, "Reset")

# game_over = True
# game_over_music()

running=True
while running:
    #RGB=red , green, blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_button.isCollision(event.pos):
                reset_game.action()
        if event.type == pygame.QUIT:
            running=False
    
#if keystroke is pressed check wheather its right or left
        if event.type ==pygame.KEYDOWN:
           
            if event.key ==pygame.K_RIGHT:
                playerX_change = 5
            if event.key== pygame.K_LEFT:
                playerX_change = -5
            if event.key==pygame.K_SPACE:
                bulletX=playerX
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser gun shot.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                

        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_RIGHT or event.type== pygame.K_LEFT:
                playerX_change=0
    
            
#checking for boundaries
    
    playerX +=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736 
#enemy movement
    for i in range(num_enemies):
     
            


        # Game Over
        if enemyY[i] > 450:
            for j in range(num_enemies):
                enemyY[j] = 2000
 
            game_over_text()
    # game_over = True
        
            
            reset_button.draw()
            
            game_over=True
            pygame.mixer.music.stop()  # Stop the background music
            game_over_music.play()
            # mouse_pos = pygame.MOUSEBUTTONDOWN.get_pos()
            # if reset_button.is_clicked(mouse_pos):
            #     reset_game

            


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        


# collision
        collision= isCollision(enemyX[i],enemyY[i],bulletX,bulletY) 
        if collision :
            explosionSound=mixer.Sound("bigboom.wav")
            explosionSound.play()
            bulletY=480
            bullet_state="ready"  
            score_value +=1    
            enemyX[i]=random.randint(0,800)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i)      
 #bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    player(playerX, playerY)
   
    show_score(testX,testY)
    
    # reset_button.draw()
    pygame.display.update()