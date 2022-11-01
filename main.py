import pyaudio
import pygame
import sys
import array
import math

def log_viz(datarray, i):
	color = pygame.Color(0,0,0)
	color.hsva = (i, 100, 100)
	screen.fill((230,230,230), special_flags=pygame.BLEND_MULT)
	pygame.draw.lines(screen, color, False, list(zip(t, [math.copysign(math.log(abs(x) + 1, 2)*20,x) + 320 for x in datarray])))

def circle_viz(datarray, i):
	color = pygame.Color(0,0,0)
	color.hsva = (i, 100, 100)
	screen.fill((230,230,230), special_flags=pygame.BLEND_MULT)
	pygame.draw.aalines(screen, color, False, [((x[1] + 5000)*math.cos(x[0]*math.pi/512)/128 + 512,(x[1] + 5000)*math.sin(x[0]*math.pi/512)/128 + 320) for x in zip(t, datarray)])
	
def simple_viz(datarray, i):
	color = pygame.Color(0,0,0)
	color.hsva = (i, 100, 100)
	screen.fill((230,230,230), special_flags=pygame.BLEND_MULT)
	pygame.draw.lines(screen, color, False, list(zip(t, [x/100 + 320 for x in datarray])))

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1

pygame.init()
screen = pygame.display.set_mode((1024,640), flags=pygame.FULLSCREEN | pygame.SCALED)

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
data = 0
datarray = array.array('h')
t = range(0, 1024)
i = 1
try:
	while True:
		i += 2
		i = i%360
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		data = stream.read(CHUNK)
		datarray.frombytes(data)
		
		circle_viz(datarray, i)
		
		pygame.display.flip()
		datarray = array.array('h')
finally:
	print("* done recording")
	stream.stop_stream()
	stream.close()
	p.terminate()

