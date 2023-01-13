import pygame , time , math

from files.constants import *
from files.utils import SpriteSheet
from files.boat import Boat
from files.buoy import Buoy
from files.plastic import Plastic
from files.battery import Battery

boat_Texture    = []
boat_list       = []
plastic_list    = []
buoy_list       = []
battery_list    = []
current_count   = 0
battery_count   = 0

def loadLevel(current_level):
    global current_count    
    global battery_count    
    match current_level:
        case 0:
            boat_list.append(Boat(3,5,1))

            plastic_list.append(Plastic(6,5))

            current_count = 3            
        case 1:
            boat_list.append(Boat(5,5,0))
            boat_list.append(Boat(3,5,1))

            plastic_list.append(Plastic(7,3))

            current_count = 5           

        case 2:
            boat_list.append(Boat(3,9,0))
            boat_list.append(Boat(3,7,1))
            boat_list.append(Boat(3,4,1))

            plastic_list.append(Plastic(6,6))
            plastic_list.append(Plastic(6,3))

            current_count = 11

        case 3:
            boat_list.append(Boat(2,3,1))
            boat_list.append(Boat(4,3,2))
            boat_list.append(Boat(5,5,1))
            boat_list.append(Boat(6,6,0))

            plastic_list.append(Plastic(7,3))

            buoy_list.append(Buoy(6,3))

            current_count = 8 
        
        case 4:
            boat_list.append(Boat(3,5,1))

            plastic_list.append(Plastic(7,5))

            battery_list.append(Battery(5,5))

            current_count = 2
            battery_count = 2
        
        case 5:
            boat_list.append(Boat(3,4,1))
            boat_list.append(Boat(4,7,0))
            boat_list.append(Boat(5,6,2))
            boat_list.append(Boat(6,6,3))

            plastic_list.append(Plastic(5,5))

            battery_list.append(Battery(4,5))
            
            current_count = 2
            battery_count = 3

        case 6:
            boat_list.append(Boat(1,4,1))
            boat_list.append(Boat(1,7,0))
            boat_list.append(Boat(3,3,2))
            boat_list.append(Boat(4,6,1))
            boat_list.append(Boat(6,5,3))
            boat_list.append(Boat(6,6,0))

            plastic_list.append(Plastic(2,3))
            plastic_list.append(Plastic(5,6))
            plastic_list.append(Plastic(6,7))

            buoy_list.append(Buoy(1,3))
            battery_list.append(Battery(1,5))

            current_count = 12
            battery_count = 5
        
        case 7:
            boat_list.append(Boat(2,4,1))
            boat_list.append(Boat(2,7,0))
            boat_list.append(Boat(4,3,2))
            boat_list.append(Boat(4,5,1))
            boat_list.append(Boat(6,5,3))

            plastic_list.append(Plastic(1,7))
            plastic_list.append(Plastic(7,3))
            plastic_list.append(Plastic(7,5))

            battery_list.append(Battery(3,7))

            current_count = 12
            battery_count = 7

        case 8:
            boat_list.append(Boat(1,3,2))
            boat_list.append(Boat(1,6,1))
            boat_list.append(Boat(3,5,1))
            boat_list.append(Boat(4,7,0))
            boat_list.append(Boat(6,3,2))

            plastic_list.append(Plastic(3,7))
            plastic_list.append(Plastic(5,3))
            plastic_list.append(Plastic(8,6))

            battery_list.append(Battery(8,4))

            current_count = 11
            battery_count = 4

        case 9:
            boat_list.append(Boat(6,4,3))
            boat_list.append(Boat(6,5,3))
            boat_list.append(Boat(5,7,0))
            boat_list.append(Boat(3,6,1))

            plastic_list.append(Plastic(1,3))
            plastic_list.append(Plastic(1,4))
            plastic_list.append(Plastic(7,5))

            battery_list.append(Battery(8,5))

            current_count = 5
            battery_count = 7

        case 10:
            boat_list.append(Boat(1,4,1))
            boat_list.append(Boat(1,5,1))
            boat_list.append(Boat(1,6,1))
            boat_list.append(Boat(2,8,0))
            boat_list.append(Boat(4,3,2))
            boat_list.append(Boat(5,6,3))

            plastic_list.append(Plastic(3,5))
            plastic_list.append(Plastic(3,6))
            plastic_list.append(Plastic(3,7))
            plastic_list.append(Plastic(6,6))

            battery_list.append(Battery(2,3))

            current_count = 12
            battery_count = 6
        case 11:
            boat_list.append(Boat(1,4,1))
            boat_list.append(Boat(2,4,1))
            boat_list.append(Boat(3,4,1))
            boat_list.append(Boat(2,5,2))
            boat_list.append(Boat(2,6,2))
            boat_list.append(Boat(2,7,2))
            boat_list.append(Boat(5,4,3))
            boat_list.append(Boat(6,4,3))
            boat_list.append(Boat(7,4,3))
            boat_list.append(Boat(8,4,3))
            boat_list.append(Boat(5,7,3))
            boat_list.append(Boat(6,7,3))
            boat_list.append(Boat(7,7,3))
            boat_list.append(Boat(8,7,3))
            boat_list.append(Boat(7,6,1))
            boat_list.append(Boat(6,5,1))

            boat_list.append(Boat(1,2,1))

            plastic_list.append(Plastic(7,2))

            current_count = 6
    load_boundary()

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    global current_count
    global battery_count
    current_level = 0
    clicked_boat  = None

    #load textures
    for i in range(4):
        temp = pygame.image.load(TEX_DIR + str(i) + '.png')
        temp = pygame.transform.scale(temp,(48,48))
        boat_Texture.append(temp)

    pygame.display.set_caption("INTERCEPT THE PLASTIC")
    pygame.display.set_icon(boat_Texture[1])

    plastic_Texture     = pygame.image.load(PLASTIC_IMG)
    background_Texture  = pygame.image.load(BACK_IMG)
    background_overlay  = pygame.image.load(BACKOVR_IMG)
    buoy_Sprite         = pygame.image.load(BUOY_IMG)
    battery_Sprite      = pygame.image.load(BATTERY_IMG)
    border_Sprite       = pygame.image.load(BORDER_IMG)
    splash_texture      = pygame.image.load(TITLE_IMG)
    wave_texture        = pygame.image.load(WAVE_IMG)
    wave2_texture       = pygame.image.load(WAVE2_IMG)
    title_texture       = pygame.image.load(TITLE_TEXT)
    end_texture         = pygame.image.load(END_TEXT)

    plastic_Sprite = SpriteSheet(plastic_Texture).return_image_list(6 , 32 , 32 , 1.5 , BLUE)
    buoy_Sprite    = pygame.transform.scale(buoy_Sprite , (48,48))
    battery_Sprite = pygame.transform.scale(battery_Sprite , (48,48))
    battery_Sprite = pygame.transform.rotate(battery_Sprite , -45)


    #load sounds
    error_sound     = pygame.mixer.Sound(SFX_DIR + 'error.wav')
    restart_sound   = pygame.mixer.Sound(SFX_DIR + 'restart.wav')
    click_sound     = pygame.mixer.Sound(SFX_DIR + 'move.wav')
    pickup_sound    = pygame.mixer.Sound(SFX_DIR + 'pickup.wav')
    pickup_sound2   = pygame.mixer.Sound(SFX_DIR + 'pickup2.wav')
    starting_sound  = pygame.mixer.Sound(SFX_DIR + 'starting.wav')

    #load fonts
    font16         = pygame.font.Font(FONT_LOC , 16)
    font32         = pygame.font.Font(FONT_LOC , 32)
    font64         = pygame.font.Font(FONT_LOC , 64)

    splash_screen_timer = 0

    prev_time = time.time()
    starting_sound.play()
    while splash_screen_timer < 2.5:
        now = time.time()
        dt  = now - prev_time
        prev_time = now

        splash_screen_timer += dt

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                
        line_1 = font32.render('DEVELOPED BY VINAYAK aka VINDAY', True , (100,100,100))
        line_2 = font32.render('LEVEL DESIGN BY ASHISH', True , (100,100,100))
        
        screen.blit(splash_texture,(0,0))
        screen.blit(line_1 , (75 , 190))
        screen.blit(line_2 , (120 , 234))

        pygame.display.update()

    title_screen = True

    while title_screen:

        screen.blit(splash_texture , (0,0))
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                case pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case pygame.BUTTON_LEFT:
                            title_screen = False

        
        click_text = font64.render('Click to Start', True ,(100,100,100))
        
        screen.blit(title_texture,(25,35 + math.sin(time.time()*5)*6))
        screen.blit(wave2_texture,(-36 + math.sin(time.time()*5)*4,265 ))
        screen.blit(wave_texture, (-68,228 + math.sin(time.time()*5)*4))
        screen.blit(click_text , (100 , 360))
        pygame.display.update()
    
    pickup_sound.play()

    prev_time = time.time()
    timer = 0

    loadLevel(current_level)

    frame = 0
    next_frame = pygame.time.get_ticks()
    running = True
    while running:

        now = time.time()
        dt = now - prev_time
        prev_time = now

        timer += dt

        screen.blit(background_Texture,(0,0))
        screen.blit(background_overlay,(0,0 + math.sin(time.time()*5)*2 ))

        for event in pygame.event.get():
            match event.type :
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case pygame.BUTTON_LEFT:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            for boat in boat_list:
                                if (math.floor(x/48) == boat.int_pos.x) and (math.floor(y/48) == boat.int_pos.y):
                                    boat.Move = True
                                    clicked_boat = boat
                                    current_count -= 1
                                    click_sound.play()
                                    timer = 0
                            if (x > 213 and y > 10 and x < 213 + 64 and y < 10 + 32):
                                reset(current_level)
                                clicked_boat = None
                                restart_sound.play()
                            elif (x > 316 and y > 10 and x < 316 + 64 and y < 10 + 32):
                                current_level += 1
                                reset(current_level)
                                clicked_boat = None
                                pickup_sound.play()
                            

                            
        if clicked_boat:
            for boat_2 in boat_list:
                if clicked_boat != boat_2:
                    if clicked_boat.int_pos == boat_2.int_pos:
                        boat_2.shift(clicked_boat.direction)


        for boat in boat_list:
            boat.update(dt)

        for boat in boat_list:
            for buoy in buoy_list:
                if boat.int_pos == buoy.position:
                    boat.unshift(clicked_boat.direction)
                    if boat != clicked_boat:
                        clicked_boat.unshift(clicked_boat.direction)
                    error_sound.play()
            for battery in battery_list:
                if boat.int_pos == battery.position:
                    battery_list.remove(battery)
                    pickup_sound2.play()
                    current_count += battery_count

            

        for plastic in plastic_list:
            for boat in boat_list:
                if(plastic.position == boat.int_pos):
                    plastic_list.remove(plastic)
                    pickup_sound.play()


        if pygame.time.get_ticks() > next_frame:
            frame = (frame + 1)%6
            next_frame += 200

        for plastic in plastic_list:
            screen.blit(plastic_Sprite[frame],(plastic.position.x * 48 , plastic.position.y * 48 +  math.sin(time.time()*5)*2))

        
        for boat in boat_list:
            screen.blit(boat_Texture[boat.direction],(boat.real_pos.x * 48,boat.real_pos.y * 48 + math.sin(time.time()*5)*3))

        for buoy in buoy_list:
            screen.blit(buoy_Sprite , (buoy.position.x * 48, buoy.position.y * 48 +  math.sin(time.time()*5)*4))

        for battery in battery_list:
            screen.blit(battery_Sprite , (battery.position.x * 46, battery.position.y * 46 +  math.sin(time.time()*5)*6))

        if current_level < 12:
            screen.blit(border_Sprite , (120,10))
            screen.blit(border_Sprite , (400,10))
            screen.blit(border_Sprite , (213,10))
            screen.blit(border_Sprite , (316,10))

            level_tex = font16.render(' LEVEL  : ' + str(current_level + 1), True , WHITE)
            screen.blit(level_tex , (125,15))

            reset_tex = font16.render('    RESET ' , True , WHITE)
            screen.blit(reset_tex , (218,15))

            skip_tex = font16.render('     SKIP ' , True , WHITE)
            screen.blit(skip_tex , (323,15))

            moves_tex = font16.render('  BAT  : ' + str(current_count), True , WHITE)
            screen.blit(moves_tex , (405,15))
        else:
            screen.blit(end_texture,(38,118))

        if current_level == 11:
            support_tex = font32.render('KEEP UP THE GOOD WORK #TEAMSEAS' , True ,WHITE)
            screen.blit(support_tex , (1*48 , 8*48))

        if not len(plastic_list):
            if timer > 0.4:
                current_level += 1 
                reset(current_level)
                clicked_boat = None

        elif current_count < 1 and timer > 0.2:
            reset(current_level)
            clicked_boat = None
            restart_sound.play()
    
        pygame.display.update()

    pygame.quit()

def reset(current_level):
    boat_list.clear()
    plastic_list.clear()
    buoy_list.clear()
    battery_list.clear()
    loadLevel(current_level)

def load_boundary():
    for i in range(11):
        buoy_list.append(Buoy(-1,i))
        buoy_list.append(Buoy(10,i))
        buoy_list.append(Buoy(i , 10))


if __name__ == '__main__':
    main()