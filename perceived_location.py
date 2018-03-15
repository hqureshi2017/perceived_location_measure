# Perceived Location Script

'''
This code allows you to move a simple object left and right and then give 
you the end location of the object. This might be useful for perceived loc
measure in psychophysical testing.
'''

import pygame
from pygame_helper import print_at
import datetime

pygame.init()

white = [255,255,255]
black = [0,0,0]
red = [255,0,0]

screen = pygame.display.set_mode([800,600])

pygame.display.set_caption('perceived_location')

lead_x = 300
lead_y = 300

# Setting up the text file
text_file = open('text_file.txt', 'w')
text_file = open('text_file.txt', 'a')
now = datetime.datetime.now()
text_file.write(now.strftime('\n' + "%Y-%m-%d %H:%M"))
text_file.write('\n' +'\n' + '-'*10+'\n' + 'RESULTS'+ '\n'+'-'*10)
text_file.write('\n' +'\n' + "This is the results summary of my perceived location " +
                'measure')


# Command to begin program
#command = input('Are you ready to begin? Press spacebar + enter to continue')
#if command == ' ':
gameExit = False

# Event handling
while not gameExit:
            
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        # the question
                          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
# Only works with the big Enter key
            if event.key == pygame.K_RETURN:
                print(event)
                per_loc = lead_x
                print(per_loc)
                text_file = open('text_file.txt', 'a')
                text_file.write('\n'*5 + 'Perceived location of the right hand is: %s ' % (per_loc))
#                text_file.write("Purchase Amount: %s price %f" % (TotalAmount, price))
#                text_file.write('\n' + per_loc)
#                text_file.write('The right hand is perceived at ' + per_loc)
                               
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
        
    # White background
    screen.fill(white)
    
    # Adding the question
    print_at(screen, (200,100), 'What is the location of the right hand? ', 30, (0,0,0) )
    
    
    print_at(screen, (700,580), 'Press Q to quit ', 20, (0,0,0) )
    # Make object
    # can insert an image from inkscape OR you can make an object with code
    pygame.draw.rect(screen, black, [lead_x,lead_y,10,100])
    pygame.draw.rect(screen, red, [lead_x,lead_y+100,10,10])
        
    pygame.display.update()
    text_file.close()
           
pygame.display.update()

pygame.quit()
quit()




