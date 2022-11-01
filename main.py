import pyaudio
import pygame
import sys
import array

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
color = pygame.Color(0,0,0)
try:
	while True:
		i += 5
		i = i%360
		color.hsva = (i, 100, 100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		data = stream.read(CHUNK)
		datarray.frombytes(data)
		
		screen.fill((240,240,240), special_flags=pygame.BLEND_MULT)
		pygame.draw.lines(screen, color, False, list(zip(t, [x/100 + 320 for x in datarray])))
		pygame.display.flip()
		datarray = array.array('h')
finally:
	print("* done recording")
	stream.stop_stream()
	stream.close()
	p.terminate()

