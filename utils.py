import pygame
def scale_image(img, factor):
    return pygame.transform.scale(img, (round(img.get_width() * factor), round(img.get_height() * factor)))

# NOTE: working of this function:
# this function is used to handle the rotation of the image. Rotating the image at a particular angle which is achieved by the first line of the function.
# The second line defines a new rectangle, which serves as a border for the rotated image.
# What essentially happens is that after rotating the image, it's dimensions do not fit the original rectangle, so we need to make it a new recantgle to fit that rotated image 
# While doing this we need to make sure that the centre of the car before rotation is assigned to the new rectangle  
def blit_rotate_centre(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = top_left).center)
    win.blit(rotated_image, new_rect.topleft)

#        width/2       
# # ---------|---------
#   |   .....|.....
#   |_ _ _ _ |        |
#   |                 |   
#   |_________________|
# we want to render text from the dots above, so what we need to do is calculate the starting position of the leftmoset dot
# which is done by subtracting the width_of_screen/2 - width_of_text/2
# so the leftmost dot will be the starting position of the text
def blit_text_center(win, font, text):
    renderS = font.render(text, 1, (1,0,0)) # text, antialiasing - always put 1, color
    win.blit(renderS, (win.get_width()/2.1 - renderS.get_width()/2, win.get_height()/2.2 - renderS.get_height()/2)) 