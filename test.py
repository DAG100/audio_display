import array
import pygame

pygame.init()
screen = pygame.display.set_mode((800,640))
screen.fill((0,0,0))
#thelist = [(0, 400), (200,200), (400,0)]

thelist = list(zip(range(400), range(400, 0, -1)))
color = pygame.Color(0,0,0)
color.hsva = (90, 100, 100)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	pygame.draw.lines(screen, color, False, thelist)
	pygame.display.flip()

datarray = array.array('h')
data = b'\x12\x34\x56\x78'
datarray.frombytes(data)
print(datarray)