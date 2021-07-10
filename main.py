#importing pygame module
import pygame

# initialize pygame
pygame.init()

# Define the dimensions of window object
win = pygame.display.set_mode((500,500))

# Giving the title to the window
pygame.display.set_caption("Character Animation")

# Loading the  right walking images and storing in a list
WalkRight = [pygame.image.load('NR1.png'),pygame.image.load('NR2.png'),
             pygame.image.load('NR3.png'),pygame.image.load('NR4.png')]
             
# Loading the  left walking images and storing in a list
WalkLeft = [pygame.image.load('NL1.png'),pygame.image.load('NL2.png'),
             pygame.image.load('NL3.png'),pygame.image.load('NL4.png')]

# Loading the background image for window
bg = pygame.image.load('bg.jpeg')

# Loading the standing image of character
stan = pygame.image.load('Nstanding.png')


Clock = pygame.time.Clock()

# Creating the variable for the dimension of the rectangle
x=50
y=400
width = 40 
height = 60

# creating a varible for updating the position after movement
speed = 10
run = True

# creating variables to find the direction of face
left = False
right = False
walkCount = 0

# Function to load the background image 
def redrawgamewindow():

    win.blit(bg,(0,0))
    #globalize the variable to track the last updated value
    global left
    global right
    global walkCount

    # Here we are using 6 because we want to show all the images for the duration of 2-2 images 
    # to reposition the list index of images to 0
    if walkCount+1 > 6:
        walkCount = 0
    
    # updating the character to pygame window from the left facing character list
    if left:
        win.blit(WalkLeft[walkCount//2],(x,y))
        walkCount +=1

    # updating the character to pygame window from the right facing character list  
    elif right:
        walkCount +=1
        win.blit(WalkRight[walkCount//2],(x,y))

    #updating the character if it is not moving 
    else:
        win.blit(stan,(x,y))


while run:
    # Providing the delay of 50ms for pygame processing
    pygame.time.delay(50)
    # checking the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            

    # storing the pressed key as a list
    keys = pygame.key.get_pressed()
    
    # checking for left arrow key pressed  and updating postion
    if keys[pygame.K_LEFT] and x > speed:
        x-=speed
        left = True
        right = False
    
    #checking for right arrow key pressed and updating position
    elif keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x+=speed
        left = False
        right = True

    else:
        left =False
        right = False
        walkCount=0
   
    redrawgamewindow()
    # Updating the window of pygame

    pygame.display.update()
    # Updating the background image
   

# terminating the pygame window
pygame.quit()