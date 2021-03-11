from graphics import *

def gameIntro(win):
	title = Text(Point(10,25), "Maze Game")
	title.setTextColor("blue")
	title.setSize(20)
	title.draw(win)
	Line(Point(7,24), Point(13,24)).draw(win)
	instruction = "In this game you will find the shortest path to the blue square. In order to move your square press w to move up, a to move left, s to move down or d to move right. Make sure you don't go out of bounds or hit an obstacle. Hint: Knowing python will surely get you into the #1 spot in our leaderboards"
	instructions1 = Text(Point(10,20), instruction[0:65])
	instructions2 = Text(Point(10,19), instruction[65:130])
	instructions3 = Text(Point(10,18), instruction[130:221])
	instructions4 = Text(Point(10,17), instruction[221::1])
	instructions1.draw(win)
	instructions2.draw(win)
	instructions3.draw(win)
	instructions4.draw(win)
	continue1 = Text(Point(10,5), "Click to continue")
	continue1.setSize(20)
	continue1.draw(win)
	handleClick(win)
	instructions1.undraw()
	instructions2.undraw()
	instructions3.undraw()
	instructions4.undraw()

	return continue1

def getInfo(win, continue1):
	name_label = Text(Point(10,17), "Name:").draw(win)
	entry = Entry(Point(10,15), 20).draw(win)
	handleClick(win)
	name = entry.getText()
	name_label.undraw()
	entry.undraw()
	continue1.undraw()

	return name

def setGame(win):
	Rectangle(Point(2,2), Point(18,18)).draw(win)
	goal = Rectangle(Point(17,2), Point(18,3))
	goal.setFill("blue")
	goal.draw(win)
	player = Rectangle(Point(2,18),Point(3,17))
	player.setFill('red')
	player.draw(win)
	obs = createObs(14)
	makeObs(obs, win)
	count = 0
	movement = [0,0]

	return count, movement, player

def runGame(win, movement, count, player):
	while True:
		movement = handleKey(win, player, movement)
		count += 1
		if movement[0] < 0 or movement[0] > 15:
			Text(Point(10,20), "Out of Bounds! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[1] > 0 or movement[1] < -15:
			Text(Point(10,20), "Out of Bounds! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 1 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 4 and movement[1] < 0 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 6 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 9 and movement[1] < 0 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 11 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 14 and movement[1] < 0 and movement[1] > -15:
			Text(Point(10,20), "You've hit an obstacle! Click the screen to exit").draw(win)
			count = -1
			break
		elif movement[0] == 15 and movement[1] == -15 and count > 31:
			Text(Point(10,20), "Congrats on reaching the goal. You could still improve your score! Click to exit.").draw(win)
			break
		elif movement[0] == 15 and movement[1] == -15 and count == 30:
			Text(Point(10,20), "You found the Easter Egg. You are a Python Master! Click to exit").draw(win)
			break
	return count
	
def handleKey(win, player, movement):
	key = win.getKey()
	if key == 'w':
		player.move(0,1)
		movement[1] += 1
	elif key == 'a':
		player.move(-1,0)
		movement[0] += -1
	elif key == 's':
		player.move(0,-1)
		movement[1] += -1
	elif key =='d':
		player.move(1,0)
		movement [0] += 1
	else:
		pass
	
	return movement

def handleClick(win):
	win.getMouse()
	pass

def makeObs(obs, win):
	for x in range(0,len(obs)):
		obs[x].setFill("green")
		obs[x].draw(win)

def createObs(quantity):
	obs = []
	for x in range(0,quantity, 5):
		obs.append(Rectangle(Point(x+3, 18), Point(x+4, 3)))
	for x in range(3,quantity, 5):
		obs.append(Rectangle(Point(x+3, 2), Point(x+4, 17)))
	return obs

def updateLeaderboard(name, score):
	file = open("scores.txt", "a")
	line_to_append = "Name: "+name+" Moves to Win: "+str(score)+"\n"
	file.write(line_to_append)
	file.close()


def main():


	win = GraphWin("Maze Game", 500, 500)
	win.setCoords(0,0,20,30)
	win.setBackground("lightblue")
	continue1 = gameIntro(win)
	name = getInfo(win, continue1)
	count, movement, player = setGame(win)
	count = runGame(win, movement, count, player)
	handleClick(win)
	updateLeaderboard(name, count)
	



main()
