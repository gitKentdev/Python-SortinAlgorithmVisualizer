import pygame, sys, random, time

res = 100
numbers = [x for x in range(res)]
random.shuffle(numbers)

def change_pos(array, pos1, pos2):
	container = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = container

def sorting_algorithm(array, line_color):
	for j in range(res):
		min_value = array[j]
		for i in range(j, res):
			if array[i] < min_value:
				min_value = array[i]
		change_pos(array, j, array.index(min_value))
		drawline(line_color, array)
		pygame.display.update()
		screen.fill((25, 25, 25))
		time.sleep(0.1)
	return array


#=====================================================================================
pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
GRID_HEIGHT = int(SCREEN_HEIGHT/res)
GRID_SIZE = int(SCREEN_WIDTH/res)
game_state = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SORTING ALGORITHM VISUALIZER')

def drawline(line_color, array):
	for index in range(res):
		pygame.draw.line(screen, line_color, (index*GRID_SIZE, SCREEN_HEIGHT), (index*GRID_SIZE, SCREEN_HEIGHT - (array[index] * GRID_HEIGHT)), GRID_SIZE)


while True:
	screen.fill((25, 25, 25))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if game_state:
		line_color = (255, 255, 255)
		newarray = sorting_algorithm(numbers, line_color)
		game_state = False
	else:
		line_color = (0, 255, 0)
		drawline(line_color, newarray)


	pygame.display.update()
	clock.tick(1)