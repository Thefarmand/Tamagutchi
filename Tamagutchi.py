from sense_hat import SenseHat
sense = SenseHat()
import time
import random

s = SenseHat()
#s.low_light = True

red = 0
blue = 0
green = 255
foreground = (red, green, blue)
background = (0, 0, 0)
minimum = -50
maximum = 50

def change_random_color():
    global red
    global green
    global blue
    color_number = random.randint(1,3) # random number between 1 and 3
    if color_number == 1: red = clamp(red + random.randint(minimum, maximum), 0, 255)
    elif color_number == 2: green = clamp(green + random.randint(minimum, maximum), 0, 255)
    else: blue = clamp(blue + random.randint(minimum, maximum), 0, 255)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def tamagotchi_face_happy():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, F, F, B, B, F, F, B,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, F, B, F, F, B, F, B,
    B, F, B, B, B, B, F, B,
    B, B, F, F, F, F, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return image
    
def tamagotchi_face_happy_reverse():
    B = background
    F = foreground
    image = [ 
    F, F, F, F, F, F, F, F,
    F, B, B, F, F, B, B, F,
    F, F, B, F, F, B, F, F,
    F, F, F, F, F, F, F, F,
    F, B, F, B, B, F, B, F,
    F, B, F, F, F, F, B, F,
    F, F, B, B, B, B, F, F,
    F, F, F, F, F, F, F, F,
    ]
    return image

def tamagotchi_face_unhappy():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    F, F, B, B, B, B, F, F,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, F, F, B, B, B,
    B, B, B, B, B, B, B, B,
    B, F, F, F, F, F, F, B,
    F, B, B, B, B, B, B, F,
    ]
    return image
    
def tamagotchi_face_unhappy_reverse():
    B = background
    F = foreground
    image = [ 
    F, F, F, F, F, F, F, F,
    B, B, F, F, F, F, B, B,
    F, F, B, F, F, B, F, F,
    F, F, F, F, F, F, F, F,
    F, F, F, B, B, F, F, F,
    F, F, F, F, F, F, F, F,
    F, B, B, B, B, B, B, F,
    B, F, F, F, F, F, F, B,
    ]
    return image

def brown():
  sense.clear(139,69,19)

while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        s.set_pixels(tamagotchi_face_happy())
      elif event.direction == "down":
        s.set_pixels(tamagotchi_face_unhappy())
      elif event.direction == "left": 
        s.set_pixels(tamagotchi_face_happy_reverse())
      elif event.direction == "right":
        s.set_pixels(tamagotchi_face_unhappy_reverse())
      elif event.direction == "middle":
        sense.show.brown("M")      # Enter key
    
  change_random_color()
  foreground = (red,green,blue)
  #s.set_pixels(images[count % len(images)]())
  #count += 1
  time.sleep(1)
  sense.clear()