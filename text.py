import pygame
import time

pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Typewriter Text Effect")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

corbel = pygame.font.SysFont('Corbel', 35)
calibri = pygame.font.SysFont('Calibri', 35)
ariel = pygame.font.SysFont('Ariel', 35)
courier = pygame.font.SysFont('Courier',35)
# Define the font
#font = pygame.font.Font(None, 36)
font = courier

# Define the text to be displayed
text = "Hello, World! This is a typewriter text effect. And I am a super fricking genius. Also pretty sad bruh this might take a while."

# Define the starting position of the text



# Define the typing speed
typing_speed = 10

# Define the function to display the text with a typewriter effect
def typewriter(text):
    x, y = 50, 50
    formatted_text = text
    lines = text.split("\n")
    counter = 0
    # Iterate over each line
    for line in lines:
        # Iterate over each character in the line
        words = line.split(" ")
        for i in range(len(words)):
            words.insert((i*2-1), ' ')
        print(words)
        for word in words:
            
            # Render the character as a surface
            word_surface = font.render(word, True, WHITE)
            # Get the size of the surface
            word_width, word_height = word_surface.get_size()
                        
            # Move the position to the right for the next character
            if x + word_width > (screen_width-50):
                ##pygame.draw.circle(screen,(255,0,0),(x,y),5)
                ##pygame.display.update()
                print("LOOK")
                time.sleep(2)
                print([formatted_text[:counter]], [formatted_text[counter:]], word)
                formatted_text = formatted_text[:counter]+ '\n' + formatted_text[counter:]
                counter += 1
                x = 50
                y += word_height
                

##            screen.blit(word_surface, (x, y))
##            # Update the screen
##            pygame.display.update()
##            # Wait for the typing speed
##            time.sleep(1 / typing_speed)
            x += word_width
            counter += len(word)
            
        # Move the position to the next line
        x = 50
        y += word_height

    for i in range(len(formatted_text)):
        if i != 0 and i + 2 < len(formatted_text) and (formatted_text[i] == '\n' and formatted_text[i+1] == ' ') :
            formatted_text = formatted_text[:i+1]+formatted_text[i+2:]
            print(formatted_text)
        elif i != 0 and i + 2 < len(formatted_text) and (formatted_text[i] == ' ' and formatted_text[i+1] == '\n'):
            formatted_text = formatted_text[:i]+formatted_text[i+1:]
            print(formatted_text)

            
    print([formatted_text])
    
    x, y = 50, 50
    # Split the text into lines
    lines = formatted_text.split("\n")
    # Iterate over each line
    for line in lines:
        # Iterate over each character in the line
        for char in line:
            # Render the character as a surface
            char_surface = font.render(char, True, WHITE)
            # Get the size of the surface
            char_width, char_height = char_surface.get_size()
            # Blit the character surface onto the screen
            screen.blit(char_surface, (x, y))
            # Update the screen
            pygame.display.update()
            # Wait for the typing speed
            time.sleep(1 / typing_speed)
            # Move the position to the right for the next character
            x += char_width
        # Move the position to the next line
        x = 50
        y += char_height
    
    

# Set the background color
screen.fill(BLACK)

# Call the typewriter function to display the text
typewriter(text)

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the screen
    pygame.display.update()