### Bloc game
### Python Project
### 
import pygame
import random

# Class List
class Player:
    def __init__(self):
        self.score = 0
        self.health = 100
        self.money = 750
        self.actions = ["Place","Sell","Upgrade"]
        self.action = self.actions[0]
class Wave:
    def __init__(self,wave_number):
        self.number = wave_number
        self.extra = 0
        self.bossWave = False
        if(self.number <2):
            self.enemyRate = 30
            self.startEnemyCount = (50 + self.number)
            self.enemySpeed = 1
        if(self.number >=2 and self.number <5):
            self.enemyRate = 30
            self.startEnemyCount = (50 + self.number)
            self.enemySpeed = 2
        elif(self.number <10 and self.number>=5):
            self.enemyRate = 20
            self.startEnemyCount = (100 + self.number)
            self.enemySpeed = 4
        elif(self.number <15 and self.number>=10):
            self.enemyRate = 15
            self.startEnemyCount = (250 + self.number)
            self.enemySpeed = 5
        elif(self.number <17 and self.number>=15):
            self.enemyRate = 13
            self.startEnemyCount = (500 + self.number)
            self.enemySpeed = 10
        elif(self.number <18 and self.number>=17):
            self.enemyRate = 12
            self.startEnemyCount = (500 + self.number)
            self.enemySpeed = 10
        elif(self.number <20 and self.number>=18):
            self.enemyRate = 10
            self.startEnemyCount = (500 + self.number)
            self.enemySpeed = 10
        elif(self.number ==20):
            self.enemyRate = 5
            self.startEnemyCount = (3200 + self.number)
        if wave_number % 5 == 0:
            self.bossWave = True
            self.extra =  self.number
            self.startEnemyCount = (self.startEnemyCount + self.number) + (self.extra * 5)
            self.enemyRate = self.enemyRate - 5
            if(self.enemyRate < 1):
                self.enemyRate = 3
                self.enemySpeed = 4     
        self.enemyCount = self.startEnemyCount
        self.scoreMultiplier = self.number
        
class Bloc(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.level = 1
        self.imageGallery = []
        self.imageGallery.append(pygame.image.load("img/greenbloc.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire1.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire2.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire3.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire4.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl2.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl2_fire1.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl2_fire2.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl2_fire3.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire4.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl3.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl3_fire1.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl3_fire2.png"))
        self.imageGallery.append(pygame.image.load("img/greenblocl3_fire3.png"))
        self.imageGallery.append(pygame.image.load("img/greenbloc_fire4.png"))
        self.imageGallery.append(pygame.image.load("img/radius1.png"))
        self.imageGallery.append(pygame.image.load("img/radius1w.png"))
        self.imageGallery.append(pygame.image.load("img/radius2.png"))
        self.imageGallery.append(pygame.image.load("img/radius2w.png"))
        self.imageGallery.append(pygame.image.load("img/radius3.png"))
        self.imageGallery.append(pygame.image.load("img/radius3w.png"))
        self.image_index = ((self.level - 1) *5)
        self.image = self.imageGallery[self.image_index]
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.x = self.position[0] -15
        self.rect.y = self.position[1] -15
        self.target = None
        self.target_list = None
        self.fireBuffer = 0
        if self.level == 1:
            self.radiusImage = self.imageGallery[15]
            self.radiusImageW = self.imageGallery[16]
            self.offset = 60
            self.upgradeCost = 750
            self.radius = 68
            self.fireRate = 80
        elif self.level == 2:
            self.radiusImage = self.imageGallery[17]
            self.radiusImageW = self.imageGallery[18]
            self.offset = 135
            self.upgradeCost = 1500
            self.radius = 143
            self.fireRate = 60
        elif self.level == 3:
            self.radiusImage = self.imageGallery[19]
            self.radiusImageW = self.imageGallery[20]
            self.offset = 135
            self.radius = 143
            self.fireRate = 30
    def fire(self,target,player):
        self.image = self.imageGallery[self.image_index]
        # Final hit check
        shoot_sound.play()
        if(pygame.sprite.collide_circle(self,target)):
            target.isHit = True
            
    def update(self,baddy_list):
        if self.level == 1:
            self.radiusImage = self.imageGallery[15]
            self.radiusImageW = self.imageGallery[16]
            self.offset = 60
            self.upgradeCost = 750
            self.radius = 68
            self.fireRate = 80
        elif self.level == 2:
            self.radiusImage = self.imageGallery[17]
            self.radiusImageW = self.imageGallery[18]
            self.offset = 135
            self.upgradeCost = 1500
            self.radius = 143
            self.fireRate = 60
        elif self.level == 3:
            self.radiusImage = self.imageGallery[19]
            self.radiusImageW = self.imageGallery[20]
            self.offset = 135
            self.radius = 143
            self.fireRate = 30
        self.target_list = pygame.sprite.spritecollide(self, baddy_list, False, pygame.sprite.collide_circle)
        if self.target_list: # Treats list as boolean. Returns True if there are items in the list
             # Specifically target first item in list.
            self.target = self.target_list[0]
        if self.target != None:
            self.fireBuffer += 1
            if self.fireBuffer > (self.fireRate - 5):
                if self.level ==1:
                    if self.image_index < 4:
                        self.image_index += 1
                    else:
                        self.image_index = 0
                    self.image = self.imageGallery[self.image_index];
                elif self.level == 2:
                    if self.image_index < 9:
                        self.image_index += 1
                    else:
                        self.image_index = 5
                    self.image = self.imageGallery[self.image_index];
                elif self.level == 3:
                    if self.image_index < 14 and self.image_index >= 10:
                        self.image_index += 1
                    else:
                        self.image_index = 10
                    self.image = self.imageGallery[self.image_index];
            if(self.fireBuffer == self.fireRate):
                self.fireBuffer = 0
                self.fire(self.target,player)
                self.target = None
        self.image = self.imageGallery[self.image_index]
class Baddy(pygame.sprite.Sprite):
    def __init__(self,path,wave):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/baddy.png")
        self.rect = self.image.get_rect()
        self.path = path
        self.pathCounter = 1
        self.position = self.path[0]
        self.destination = self.path[self.pathCounter]
        # Centering off 0,0
        self.destination = (int(self.destination[0] - 7),int(self.destination[1] - 7))
        self.rect.x = (self.position[0] - 7)
        self.rect.y = (self.position[1] - 7)
        self.madeIt = False
        self.speed = wave.enemySpeed
        self.isHit = False
    def update(self,player,wave):
        self.position = (self.rect.x ,self.rect.y)
        if self.isHit:
            play_kill = kill_sound[random.randint(0,1)]
            play_kill.play()
            self.kill()
            wave.enemyCount -= 1
            player.money += 6
            player.score += (1 +wave.scoreMultiplier)
        if(self.position == self.destination):
            if(self.pathCounter == 10):
                self.madeIt = True
                player.health -= 1
                self.kill()
                wave.enemyCount -= 1 
            else:
                self.pathCounter += 1
                self.destination = self.path[self.pathCounter]
                # Centering off 0,0
                self.destination = (int(self.destination[0] - 7),int(self.destination[1] - 7))
        if(self.rect.x == self.destination[0]):
            if(self.rect.y < self.destination[1]):
                #increase y
                self.rect.y += self.speed
            elif(self.rect.y > self.destination[1]):
                #decrease y
                self.rect.y -= self.speed
        else:
            if(self.rect.x < self.destination[0]):
                #increase x
                self.rect.x += self.speed
            elif(self.rect.x > self.destination[0]):
                #decrease x
                self.rect.x -= self.speed
class Button(pygame.sprite.Sprite):
    def __init__(self, action):
        pygame.sprite.Sprite.__init__(self)
        self.action = action
        if(self.action == "Place"):
            self.image = pygame.image.load("img/button_place.png")
            self.rect = self.image.get_rect()
            self.rect.x = 295
            self.rect.y = 25
        if(self.action == "Sell"):
            self.image = pygame.image.load("img/button_sell.png")
            self.rect = self.image.get_rect()
            self.rect.x = 360
            self.rect.y = 25
        if(self.action == "Upgrade"):
            self.image = pygame.image.load("img/button_upgrade.png")
            self.rect = self.image.get_rect()
            self.rect.x = 425
            self.rect.y = 25
    def clicked(self, player):
        player.action = self.action
        click_sound.play()
        

# Constant definitions
FPS = 35
# Colour Bank
WHITE = ( 255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BBLUE = (87,197,255)

# Load background images
bg = pygame.image.load("img/bg.png")
bgr = pygame.image.load("img/bgr.png")
bgy = pygame.image.load("img/bgy.png")
bgg = pygame.image.load("img/bgg.png")
bgw = pygame.image.load("img/bgw.png")

# PATH - Defines path of baddy
# PATHRECTS - Used to stop illegal bloc placement on path.
PATH = [(0,300),(100,300),(100,500),(200,500),(200,100),(300,100),(300,500),(400,500),(400,100),(500,300),(600,300)]
PATHRECTS =[(pygame.Rect(0,285,100,30)),
 (pygame.Rect(85,285,30,200)),
 (pygame.Rect(85,485,100,30)),
 (pygame.Rect(185,85,30,430)),
 (pygame.Rect(215,85,70,30)),
 (pygame.Rect(285,85,30,400)),
 (pygame.Rect(285,485,100,30)),
 (pygame.Rect(385,85,30,430)),
 (pygame.Rect(415,85,100,30)),
 (pygame.Rect(485,85,30,200)),
 (pygame.Rect(485,285,115,30))]

# Pygame initialisation

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

start = False
#titles = pygame.movie.Movie("img/titles.mpeg")
#titles.set_display(screen,(0,0,600,600))
#titles.play()
title_image = pygame.image.load("img/title.png")
pygame.mixer.music.load("snd/og.ogg")
pygame.mixer.music.play(-1)
# Main loop bool
done = False

while not start:
    #while not titles.get_busy():
    screen.fill(WHITE)
    screen.blit(title_image,(0,0))
    pygame.display.flip()
    
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            start = True
            done = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
            break
    
pygame.mixer.music.stop()

# Main Menu event loop

# Menu items
menu_tab = pygame.image.load("img/tab.png")
menu = pygame.Rect(0,0,600,55)
button_list = pygame.sprite.Group()
button_place = Button("Place")
button_sell = Button("Sell")
button_upgrade = Button("Upgrade")
button_list.add(button_place)
button_list.add(button_sell)
button_list.add(button_upgrade)

pygame.display.set_caption("Bloc")
font = pygame.font.Font("Font/Calibri.ttf",25)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Set start wave number
wave_number = 0

# Instansiate Player
player = Player()

bloc_list = pygame.sprite.Group()

hover_list = []
hover_list.append(pygame.image.load("img/greenhover.png"))
hover_list.append(pygame.image.load("img/redhover.png"))
hover_list.append(pygame.image.load("img/sellhover.png"))
hover_list.append(pygame.image.load("img/uphover.png"))

# Sound loads
pygame.mixer.music.load("snd/chon.ogg")
#SFX
wave_sound = pygame.mixer.Sound("snd/sfx/321wave.ogg")
win_sound = pygame.mixer.Sound("snd/sfx/win.ogg")
error_sound = pygame.mixer.Sound("snd/sfx/nope.ogg")
build_sound = pygame.mixer.Sound("snd/sfx/build.ogg")
sell_sound = pygame.mixer.Sound("snd/sfx/sell.ogg")
upgrade_sound = pygame.mixer.Sound("snd/sfx/up.ogg")
click_sound = pygame.mixer.Sound("snd/sfx/click.ogg")
shoot_sound = pygame.mixer.Sound("snd/sfx/shoot.ogg")
kill_sound = []
kill_sound.append(pygame.mixer.Sound("snd/sfx/kill1.ogg"))
kill_sound.append(pygame.mixer.Sound("snd/sfx/kill2.ogg"))

win_sound.set_volume(0.05)
wave_sound.set_volume(0.05)
build_sound.set_volume(0.10)
sell_sound.set_volume(0.15)
upgrade_sound.set_volume(0.15)
kill_sound[1].set_volume(0.25)
shoot_sound.set_volume(0.5)
click_sound.set_volume(0.05)
pygame.mixer.music.set_volume(0.05)

# Hints
hint_list = []
hint_list.append("Weaker Blocs work better in corners!")
hint_list.append("Place your Blocs carefully, money can be slow!")
hint_list.append("Every 5 waves, it gets more difficult.")
hint_list.append("Wave 20 is said to be nearly impossible... nearly.")
hint_list.append("Upgrades are expensive. Choose wisely.")
hint_list.append("Keep missing? Try upgrading some Blocs.")
hint_list.append("Health does not regenerate.")
hint_list.append("Selling Blocs a lot will hurt funds in the long term.")
hint_list.append("Upgrading level 1 Blocs makes them see further.")
hint_list.append("Upgrading level 2 Blocs makes them shoot faster.")
hint_list.append("Try not to lose")
hint_list.append("Building more Blocs will result in wider coverage.")
hint_list.append("Price per Bloc: 250 - LvlUp - 750 -- 1500")
hint_list.append("Save up money, you will need it later.")


# -------- Main Program Loop -----------
while not done:

    winner = False
    gameOver = False
    wave_number += 1
    #(Re) Set wave
    if wave_number > 1:
        win_sound.play()
    intermission = True
    intermissionTimer = 5
    intermissionBuffer = 0
    wave_start_pause = False
    waveMessageBuffer = 120
    wave_hint = hint_list[random.randint(0,13)]

    baddy_list = pygame.sprite.Group()
    
    # Reset variables
    spawnCounter = 0
    frameBuffer = 0
    errorBuffer = 0
    errorMessage = False
    # Instansiate the round
    wave = Wave(wave_number)
    
    # Music selection
    if(wave.number == 1):
        pygame.mixer.music.play(-1)
    if(wave.number == 5):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("snd/og.ogg")
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play(-1)
    if(wave.number == 10):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("snd/bubble.ogg")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
    if(wave.number == 12):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("snd/missles.ogg")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
    if(wave.number == 15):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("snd/puddle.ogg")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
    if(wave.number == 20):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("snd/boss.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    if(wave.number == 21):
        done = True
        winner = True
        gameOver = True
        
    # Wave loop
    while wave.enemyCount > 0:
        # --- Main event loop
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True
            # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if rect collide point for buttons
                for button in button_list:
                    if button.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
                        button.clicked(player)
                if not menu.collidepoint(mouse_pos[0],mouse_pos[1]):
                    if player.action == "Place":
                         # Conditionals for placing a tower
                        bloc = Bloc(mouse_pos)
                        if pygame.sprite.spritecollideany(bloc, bloc_list, collided = None) != None:
                        ## if collides with other
                            errorMessage = True
                            errorBuffer = 15
                            error_text = font.render("Bloc placement blocked!",True,RED)
                            errorRise = 1
                        elif not pygame.sprite.spritecollideany(bloc, button_list, collided = None) != None:
                            rect = pygame.Rect((bloc.rect.x),(bloc.rect.y),30,30)
                            collide = False
                            if(rect.colliderect(menu)):
                                collide = True
                            for path in PATHRECTS:
                                if (rect.colliderect(path)):
                                    collide = True
                                    errorMessage = True
                                    errorBuffer = 15
                                    errorRise = 1
                                    error_text = font.render("Can't build on the path!",True,RED)
                            if not collide:
                                if len(bloc_list.sprites()) == 10:
                                    errorMessage = True
                                    errorBuffer = 15
                                    errorRise = 1
                                    error_text = font.render("10/10 Blocs built!",True,RED)
                                else:
                                    if player.money >= 250:
                                        bloc_list.add(bloc)
                                        player.money -= 250
                                        build_sound.play()
                                    else:
                                        errorMessage = True
                                        errorBuffer = 15
                                        errorRise = 1
                                        error_text = font.render("You can't afford that!",True,RED)
                    elif player.action == "Sell":
                        for bloc in bloc_list:
                            if bloc.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
                                if(bloc.level == 1):
                                    player.money += 125
                                elif(bloc.level == 2):
                                    player.money += 375
                                elif(bloc.level == 3):
                                    player.money += 750
                                sell_sound.play()
                                bloc.kill()
                    elif player.action == "Upgrade":
                        for bloc in bloc_list:
                            if bloc.rect.collidepoint(mouse_pos[0],mouse_pos[1]):
                                if bloc.level < 3:
                                    if player.money>=bloc.upgradeCost:
                                        player.money -= bloc.upgradeCost
                                        bloc.level += 1
                                        bloc.image_index = ((bloc.level - 1) *5)
                                        bloc.target = None
                                        bloc.fireBuffer = 0
                                        upgrade_sound.play()
                                    else:
                                        errorMessage = True
                                        errorBuffer = 15
                                        errorRise = 1
                                        error_text = font.render("You can't afford that!",True,RED)
                                else:
                                    errorMessage = True
                                    errorBuffer = 15
                                    errorRise = 1
                                    error_text = font.render("Bloc at max level!",True,RED)
                            
        # First, if user selected Quit, exit
        if done:
            break

        # If Player is killed:
        if player.health == 0 or player.health < 0:
            done = True
            gameOver = True
            
        # If in intermission, count seconds
        if intermission:
            if intermissionTimer > 0:
                intermissionBuffer += 1
                if intermissionBuffer == FPS:
                    intermissionBuffer = 0
                    intermissionTimer -= 1
                if intermissionTimer == 3:
                    wave_sound.play()
            else:
                intermission = False
                wave_start_pause = True
        else:
            if wave_start_pause:
                if waveMessageBuffer > 0:
                    waveMessageBuffer -= 1
                else:
                    wave_start_pause = False
            # Spawns enemies
            frameBuffer += 1       
            if(spawnCounter < wave.startEnemyCount):
                if(frameBuffer == wave.enemyRate):
                    frameBuffer = 0
                    baddy = Baddy(PATH,wave)
                    baddy_list.add(baddy)
                    spawnCounter += 1
                
        # Update enemies 
        for baddy in baddy_list:
            baddy.update(player,wave)

        # Update blocs
        for bloc in bloc_list:
            bloc.update(baddy_list)

        # Hoverbox selection for cursor
        if(player.action == "Place"):
            hover = hover_list[0]
        elif(player.action == "Sell"):
            hover = hover_list[2]
        elif(player.action == "Upgrade"):
            hover = hover_list[3]
        hoverbox = pygame.Rect(mouse_pos[0]-15,mouse_pos[1]-15,30,30)
        
        # Drawing
        #########
        
        screen.fill(WHITE)
        # bg
        if wave.number >= 0 and wave.number < 5:
            screen.blit(bg,(0,0))
        elif wave.number >= 4 and wave.number < 10:
            screen.blit(bgr,(0,0))
        elif wave.number >= 10 and wave.number < 15:
            screen.blit(bgy,(0,0))
        elif wave.number >= 14 and wave.number < 20:
            screen.blit(bgg,(0,0))

            
        # Radius
        for bloc in bloc_list:
            rect = pygame.Rect(bloc.rect.x,bloc.rect.y,30,30)
            if(rect.collidepoint(mouse_pos[0],mouse_pos[1])):
               screen.blit(bloc.radiusImage,((bloc.rect.x - bloc.offset),(bloc.rect.y - bloc.offset)))
        # bgw - ReDisplay for trans effect on path with radius image.
        screen.blit(bgw,(0,0))
        
        # Draw blocs and baddies
        bloc_list.draw(screen)
        baddy_list.draw(screen)

        # ReDraw a radius and other hover-over-bloc basics
        for bloc in bloc_list:
            rect = pygame.Rect(bloc.rect.x,bloc.rect.y,30,30)
            if(rect.collidepoint(mouse_pos[0],mouse_pos[1])):
               screen.blit(bloc.radiusImageW,((bloc.rect.x - bloc.offset),(bloc.rect.y - bloc.offset)))
            if(player.action =="Place"):
                if(hoverbox.colliderect(rect)):
                    hover = hover_list[1]
            if(player.action =="Sell"):
                if(rect.collidepoint(mouse_pos[0],mouse_pos[1])):
                    if(bloc.level == 1):
                        hover_text = font.render("Sell for: 125",True,BLUE)
                    elif(bloc.level == 2):
                        hover_text = font.render("Sell for: 375",True,BLUE)
                    elif(bloc.level == 3):
                        hover_text = font.render("Sell for: 750",True,BLUE)
                    screen.blit(hover_text,(mouse_pos[0]-40,mouse_pos[1]-40))
            if(player.action =="Upgrade"):
                if(rect.collidepoint(mouse_pos[0],mouse_pos[1])):
                    if(bloc.level == 1):
                        hover_text = font.render("Upgrade for: 750",True,BLUE)
                    elif(bloc.level == 2):
                        hover_text = font.render("Upgrade for: 1500",True,BLUE)
                    elif(bloc.level == 3):
                        hover_text = font.render("",True,BLUE)
                        hover = hover_list[1]
                    screen.blit(hover_text,(mouse_pos[0]-40,mouse_pos[1]-40))
        # Draw menu tab and buttons           
        screen.blit(menu_tab,(0,0))
        button_list.draw(screen)

        # Hoverbox collision
        if(hoverbox.colliderect(menu)):
                hover = hover_list[1]
        if(player.action == "Place"):
            for path in PATHRECTS:
                if (hoverbox.colliderect(path)):
                    hover = hover_list[1]
            if(player.money<250):
                hover = hover_list[1]
                
        # Draw Hoverbox
        screen.blit(hover,(hoverbox.x,hoverbox.y))

        # Draw PATHRECTS (Restricted path area)
        #for path in PATHRECTS:
        #   pygame.draw.rect(screen,RED,path,0)
        
        # Menu text
        health_number = font.render(str(player.health),True,WHITE)
        score_number = font.render(str(player.score),True,WHITE)
        money_number = font.render(str(player.money),True,WHITE)
        wave_number_text = font.render(str(wave.number), True, WHITE)

        # Info text
        info_bloc = font.render("/10 Blocs",True,BBLUE)
        info_bloc_amount = font.render(str(len(bloc_list.sprites())),True,BBLUE)
        info_enemyLeft = font.render("Enemy Left:",True,BBLUE)
        info_enemyLeft_amount = font.render(str(wave.enemyCount),True,BBLUE)

        # Intermission text
        if intermission:
            intermission_text = font.render("Next wave in:", True, BBLUE)
            if(wave.bossWave):
                intermission_text = font.render("Boss wave in:", True, BBLUE)
                warning_text = font.render("Get ready!", True, BLUE)
                screen.blit(warning_text,(250,57))
            if(wave.number == 20):
                warning_text = font.render("Final wave!", True, BLUE)
                screen.blit(warning_text,(250,157))
            intermission_timer = font.render(str(intermissionTimer), True, BLACK)
            screen.blit(intermission_text,(15,57))
            screen.blit(intermission_timer,(155,57))
            hint_mark = font.render("Hint:", True, BLUE)
            hint = font.render(wave_hint, True, BLUE)
            screen.blit(hint_mark,(245,430))
            screen.blit(hint,(55,460))
        # Next wave text
        if wave_start_pause:
            wave_incoming = font.render("Wave:", True, BLACK)
            wave_incoming_value = font.render(str(wave_number), True, BLACK)
            screen.blit(wave_incoming,(250,270))
            screen.blit(wave_incoming_value,(330,270))
            
        # Draw menu text
        screen.blit(health_number,(27,27))
        screen.blit(score_number,(130,27))
        screen.blit(money_number,(210,27))
        screen.blit(wave_number_text,(540,27))

        # Draw info text
        screen.blit(info_bloc,(500,570))
        screen.blit(info_bloc_amount,(478,570))
        screen.blit(info_enemyLeft,(10,570))
        screen.blit(info_enemyLeft_amount,(135,570))
        
        # Draw error
        if errorMessage:
            errorPos = pygame.mouse.get_pos()
            if errorBuffer == 10:
                error_sound.play()
            if errorBuffer > 0:
                errorBuffer -= 1
                errorRise += 3
                screen.blit(error_text,(errorPos[0],errorPos[1]-errorRise))
            else:
                errorMessage == False
        
        # Updates displays
        pygame.display.flip()

        # --- Limit to 40 frames per second
        clock.tick(FPS)

if(gameOver == True):
    end = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load("snd/main.ogg")
    pygame.mixer.music.play(-1)

    screen.fill(BLACK)
    if(winner == True):
        gameOver_text = font.render("YOU WON!",True,WHITE)
    else:
        gameOver_text = font.render("GAME OVER!",True,WHITE)
    gO_score = font.render("Your score was: ",True,BBLUE)
    gO_score_amount = font.render(str(player.score),True,BBLUE)
    gO_wave = font.render("You reached wave:",True,BBLUE)
    gO_wave_number = font.render(str(wave.number),True,BBLUE)
    gO_continue = font.render("Click anywhere to exit",True,BBLUE)

    screen.blit(gameOver_text,(235,155))
    screen.blit(gO_score,(225,255))
    screen.blit(gO_score_amount,(295,285))
    screen.blit(gO_wave,(205,355))
    screen.blit(gO_wave_number,(295,385))
    screen.blit(gO_continue,(200,455))
    mouse_pos = pygame.mouse.get_pos()
    while not end:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                end = True
            # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                end = True
        pygame.display.flip()
        clock.tick(FPS)
    
pygame.quit()




        
