# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

#Sounds
coiny = pygame.mixer.Sound("audio.WAV")
pygame.mixer.music.load("sounds/minecraft.ogg")

#Images
Stephen = pygame.image.load("Stephen.PNG")
chair = pygame.image.load("wheel.PNG")
chair = pygame.transform.scale(chair, (25, 25))
chair2 = pygame.transform.flip(chair, True, False)
atom = pygame.image.load("atom.PNG")
atom = pygame.transform.scale(atom, (25, 25))
#font
MY_FONT = pygame.font.Font(None, 50)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# stages
START = 0
PLAYING = 1
END = 2


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# make walls
wall3 =  [25, 0, 25, 25]
wall4 =  [75, 0, 25, 25]
wall5 =  [125, 0, 25, 25]
wall7 =  [175, 0, 25, 25]
wall8 =  [225, 0, 25, 25]
wall9 =  [275, 0, 25, 25]
wall0 =  [325, 0, 25, 25]
wall10 =  [375, 0, 25, 25]
wall13 =  [425, 0, 25, 25]
wall14 =  [475, 0, 25, 25]
wall15 =  [525, 0, 25, 25]
wall16 =  [575, 0, 25, 25]
wall17 =  [625, 0, 25, 25]
wall18 =  [675, 0, 25, 25]
wall19 =  [725, 0, 25, 25]
wall11 =  [775, 0, 25, 25]
wall20 =  [600, 100, 200, 25]
wall22 =  [575, 150, 200, 25]
wall21 =  [550, 75, 25, 500]
wall23 =  [600, 200, 200, 25]
wall24 =  [575, 250, 200, 25]
wall25 =  [600, 300, 200, 25]
wall26 =  [575, 350, 200, 25]
wall27 =  [600, 400, 200, 25]
wall28 =  [575, 450, 200, 25]
wall29 =  [600, 500, 200, 25]
wall30 =  [575, 550, 200, 25]
wall31 =  [575, 650, 200, 25]
wall32 =  [600, 600, 200, 25]
wall33 =  [575, 750, 200, 25]
wall34 =  [600, 700, 200, 25]
wall35 =  [575, 850, 200, 25]
wall36 =  [0, 100, 25, 25]
wall37 =  [0, 150, 25, 25]
wall38 =  [0, 200, 25, 25]
wall39 =  [0, 250, 25, 25]
wall40 =  [0, 300, 25, 25]
wall41 =  [0, 350, 25, 25]
wall42 =  [0, 400, 25, 25]
wall43 =  [0, 450, 25, 25]
wall44 =  [0, 500, 25, 25]
wall45 =  [0, 550, 25, 25]
wall46 =  [50, 125, 25, 25]
wall47 =  [50, 175, 25, 25]
wall48 =  [50, 225, 25, 25]
wall49 =  [50, 275, 25, 25]
wall50 =  [50, 325, 25, 25]
wall51 =  [50, 375, 25, 25]
wall52 =  [50, 425, 25, 25]
wall53 =  [50, 475, 25, 25]
wall54 =  [50, 525, 25, 25]
wall55 =  [50, 575, 25, 25]





wall12 =  [0, 50, 775, 25]
borderleft =  [-10, 0, 10, 600]
bordertop =  [0, -10, 800, 10 ]
borderright =  [0, 600, 800, 10]
borderbottom =  [800, 0, 10, 600]

walls = [wall3, wall4, wall5, wall7, wall8, wall9, wall10, wall0, wall11, wall12,
         borderleft, bordertop, borderright, borderbottom, wall13, wall14, wall15, wall16, wall17,
         wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26,
         wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35]

# Make coins
coin1 = [50, 0, 25, 25]
coin2 = [100, 0, 25, 25]
coin3 = [150, 0, 25, 25]
coin4 = [200, 0, 25, 25]
coin5 = [250, 0, 25, 25]
coin6 = [300, 0, 25, 25]
coin7 = [350, 0, 25, 25]
coin8 = [400, 0, 25, 25]
coin9 = [450, 0, 25, 25]
coin10 = [500, 0, 25, 25]
coin11 = [550, 0, 25, 25]
coin12 = [600, 0, 25, 25]
coin13 = [650, 0, 25, 25]
coin14 = [700, 0, 25, 25]
coin15 = [750, 0, 25, 25]
coin16 = [575, 100, 25, 25]
coin17 = [775, 150, 150, 25]
coin18 = [575, 200, 25, 25]
coin19 = [775, 250, 25, 25]
coin20 = [575, 300, 25, 25]
coin21 = [775, 350, 25, 25]
coin22 = [575, 400, 25, 25]
coin23 = [775, 450, 25, 25]
coin24 = [575, 500, 25, 25]
coin25 = [775, 550, 25, 25]
coin26 = [0, 200, 25, 25]
coin27 = [342, 343, 25, 25]
coin28 = [232, 300, 25, 25]
coin29 = [100, 350, 25, 25]
coin30 = [150, 400, 25, 25]
coin31 = [367, 450, 25, 25]
coin32 = [123, 500, 25, 25]
coin33 = [200, 550, 25, 25]



coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11,
         coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22,
         coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33]

def setup():
    global player1, player2, stage, vel1, vel2, score1, score2, player1_speed, player2_speed, coins
    

    player1 = screen.blit(chair, [0,0])
    vel1 = [0, 0]
    player1_speed = 5
    score1 = 0
    player2 =  [0, 0, 25, 25]
    vel2 = [0, 0]
    player2_speed = 5
    score2 = 0
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11,
         coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22,
         coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33]

    stage = START


def splash():
    screen.blit(Stephen, [0,0])




# Game loop
setup()
pygame.mixer.music.play(-1)
done = False
thingy = False


while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                        stage = PLAYING
                elif event.key == pygame.K_r:
                        stage = START

            elif stage == PLAYING:
                ''' process player1 input '''
                pass
            
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    up2 = pressed[pygame.K_w]
    down2 = pressed[pygame.K_s]
    left2 = pressed[pygame.K_a]
    right2 = pressed[pygame.K_d]

    if left:
        vel1[0] = -player1_speed
        thingy = "Left"
    elif right:
        vel1[0] = player1_speed
        thingy = "Right"
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0

    ''' process player2 input '''
    if left2:
        vel2[0] = -player2_speed
    elif right2:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    if up2:
        vel2[1] = -player2_speed
    elif down2 :
        vel2[1] = player2_speed
    else:
        vel2[1] = 0



        
    # Game logic (Check for collisions, update points, etc.)


    ''' move the player in horizontal direction '''
    if stage == PLAYING:
        player1[0] += vel1[0]
        player2[0] += vel2[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    for w in walls:
        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    if stage == PLAYING:
        player1[1] += vel1[1]
        player2[1] += vel2[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]

    for w in walls:
        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]

    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coiny.play()
        
    if len(coins) == 0:
        stage = END





    for c in coins:
        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]

    
    for hit in hit_list2:
        coins.remove(hit)
        score2 += 1
        coiny.play()
        
    if len(coins) == 0:
        stage = END

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    font = pygame.font.Font(None, 48)
    text4 = font.render(str(score1), 1, WHITE)
    screen.blit(text4, [0, 572])
    text4 = font.render(str(score2), 1, GREEN)
    screen.blit(text4, [WIDTH - 50, 572])



    ''' begin/end'''
    if stage == START:
        screen.blit(Stephen, [0,0])
    elif stage == END:
        font = pygame.font.Font(None, 48)
        if score1 > score2:
            text = font.render("Hawking Wins!", 1 , WHITE)
            text2 = font.render("Press SPACE to restart", 1 , WHITE)
            text3 = font.render("Hawking:", 1 , WHITE)
        else:
            text = font.render("Blocky Wins!", 1, GREEN)
            text2 = font.render("Press SPACE to restart", 1, GREEN)
            text5 = font.render("Green:", 1, GREEN)
        screen.blit(text, [315, 200])
        screen.blit(text2, [230, 230])



    if PLAYING == False:
        splash()


    
    if stage == PLAYING:
        for w in walls:
            pygame.draw.rect(screen, RED, w)

        for c in coins:
            screen.blit(atom, c)
        if thingy =="Right":
            screen.blit(chair, player1)
        elif thingy == "Left":
            screen.blit(chair2, player1)
            

        pygame.draw.rect(screen, GREEN, player2)

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
