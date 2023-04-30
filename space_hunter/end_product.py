"""

CREATE MULTIPLE ENEMY
display score
add sound


"""

"""
Adding Background IMage
as well as shooting bullet while press the space button

make fuction called collision

make score variable to show colision

and show score of the users

 

"""
import pygame
import random
import math
from pygame import mixer


pygame.init()

user_score=0
running = True
# (width,height)
screen = pygame.display.set_mode((800, 800))


#adding caption
pygame.display.set_caption("Space craft")

#set icon
# 1) load image in a var
icon = pygame.image.load('element/spaceship.png')

#2 use image
pygame.display.set_icon(icon)


"""
adding backgorund imgae
"""
background = pygame.image.load('element/space.jpg')
background = pygame.transform.scale(background, (800, 800))




"""
use the code written below the space ship will created
the Initial Position will be (400,600) on the screen

"""
player_img = pygame.image.load('element/spaceship.png')
#resize image
image = pygame.transform.scale(player_img, (70, 90))
player_x = 400
player_y = 600
player_x_chnage = 0
player_y_chnage = 0



#adding music
mixer.music.load('element/xyz.mp3')
# -1 will make it infine
mixer.music.play(-1)


def player(x, y):
    #blit use to Draw Image
    screen.blit(image, (x, y))

"""

Adding the enemy on the the screen and,
the event will random values that means the postion of enemey always chnage

"""

"""
create multiple enemy by following logic

make a list contain all property of enemy

pass the list theought the loop

"""
enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_x_chnage=[] 
enemy_y_chnage=[]

enemy_no=8

for i in range(enemy_no):
    enemy_img.append(pygame.image.load('element/bacteria1.png'))
    enemy_x.append(random.randint(50, 700))
    enemy_y.append(random.randint(50, 150))
    enemy_x_chnage.append(0.8)
    enemy_y_chnage.append(100)


"""

insert enemy into our game

"""

def enemy(x, y, i):
        screen.blit(enemy_img[i], (x, y))





"""
add bullet
"""

"""
we will add two state in Bullet one is fire other is stope

1) ready:-state this is the state when bullet is not fired we can move our space ship also you can't see the bullet

2) fire:- this is the sate when we fire the bullet and we have to stop and do nothing, bullet is moving

"""
bullet = pygame.image.load('element/bullet.png')
bullet = pygame.transform.rotate(bullet, 90)
bullet = pygame.transform.scale(bullet, (40, 70))
bulletX = 0
bulletY = 480
bullet_x_chnage = 0
bullet_y_chnage =-5
bullet_state = 'ready'


""""
creating score text in game screen

"""
user_score=0

#creating fonrt in pygame
font=pygame.font.Font('freesansbold.ttf',30 )

#set x and y coordinate
textX=10
textY=10

def show_score(x,y):
    score=font.render("Score:"+str(user_score),True,(255,255,255))
    screen.blit(score,(x,y))

over_font=pygame.font.Font('freesansbold.ttf',400)

def game_over_text():
    over_font=font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_font,(300,300))







# define bullet contrl
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x+12, y+150))



"""
this fuction is helpful to detect the collision and 
"""

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False

    


while running:

    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        """
        
        key stroke is a event in Window chnage postion of player over key pressed
        
        """
        # if event.type==pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         print('LEFT KEY PRESSED')
        #     if event.key==pygame.K_RIGHT:
        #         print("right key pressed")
        # if event.type ==pygame.KEYUP:
        #     if event.key==pygame.K_LEFT:
        #         print('key released')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_chnage -= 1
            if event.key == pygame.K_RIGHT:
                player_x_chnage += 1

            #fire bullet
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('element/laser1.wav')
                    bullet_sound.play()
                    #we store the initial value so it will be static and would not be chnaged
                    #get the current x co-ordinate
                    bulletX=player_x
                    fire_bullet(bulletX,bulletY)



        if event.type == pygame.KEYUP:
            player_x_chnage = 0


    """
    setting the state of bullet bullet reach at zero reset at it's initial postion
    and change the state.

    
    
    """
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'

    """
    Bullet movement and appearence
    """
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY += bullet_y_chnage
        
        


    """
    created enemy using fuction
    
    """
    
   #boundry of enemy
    for i in range(enemy_no):
        #game over
        if enemy_y[i]>600:
            for j in range(enemy_no):
                enemy_y[j]=2000
                #after enemy reach at end 
                #text will show the game is over
            game_over_text()
            break
            
        if enemy_x[i] <= 10:
            enemy_x_chnage[i] = 1
            enemy_y[i] += enemy_y_chnage[i]
        elif enemy_x[i] >= 730:
            enemy_x_chnage[i] = -0.5
            enemy_y[i] += enemy_y_chnage[i]

        # movemeent of emenmy
        enemy_x[i] += enemy_x_chnage[i]
        enemy(enemy_x[i], enemy_y[i],i)
       
        collision=iscollision(enemy_x[i],enemy_y[i],bulletX,bulletY)
        if collision:
            bullet_sound=mixer.Sound('element/explosion.wav')
            bullet_sound.play()
            bulletY=480
            bullet_state='ready'
            user_score +=1
            enemy_x[i] = random.randint(100, 700)
            enemy_y[i] = random.randint(50, 150)

        """
    this collision is going to store the value if collision Occurs or Not.
    """

    """
    if collision occurs 
    1) make bullet at it's initial postion
    2) chnage state fire -> redy
    3) increase score by 1
    4) reswap the enemy's position
    
    """

        
   


    """
    
    create bullet 

    """

    """
    code for Player

    """

    if player_x <= 10:
        player_x = 10
    elif player_x >= 730:
        print(player_x)
        player_x = 730

    player_x += player_x_chnage


    """
    var for collision
    """

    

    """

    create the player

    """
    player(player_x, player_y)


    show_score(textX,textY)
    pygame.display.update()


 
