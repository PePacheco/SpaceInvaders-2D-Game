from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Polygon import *
from AABB import *
from random import randint
import math

projectile = Polygon()
projArrow = Polygon()
enemyProj = Polygon()
cannon = Polygon()
cannon.insereVertice(0, 0, 0)
cannon.insereVertice(0, 16, 0)
cannon.insereVertice(8, 16, 0)
cannon.insereVertice(8, 0, 0)
enemies = loadEnemies()
buildings = loadBuildings()
enemiesHit = [False, False, False, False, False, False, False, False, False, False]
buildingsHit = [False, False, False, False, False, False, False, False, False, False]

power = 100
angle = 0
xCannon = 0
xEnemies = 0
lives = 3

cores = []
objetos = []

enemyShooting = False
animated = False
animationTime = 5 # time to cross the screen
animatedTime = 0
time = 0
enemySelectedIndex = randint(0, 9)

########################################
##### SPRITES INI
########################################

def loadSprites(path):
	with open(path) as f:
		file_data = f.readlines()
	return file_data

def parseSprites(path):
	file_data = loadSprites(path)
	cores_quant = int(file_data[1].replace("\n", ""))
	global cores
	global objetos
	cores = []
	objetos = []

	for x in range(1, cores_quant + 1):
		cor_raw = file_data[1 + x].split(" #")[0][2:].split(" ")
		cor = (int(cor_raw[0]), int(cor_raw[1]), int(cor_raw[2]))
		cores.append(cor)
	
	for x in range(len(file_data)):
		if "#OBJETO" in file_data[x]:
			obj = []
			obj_rows = int(file_data[x + 1].split(" ")[0])
			for y in range(obj_rows):
				row = file_data[x + y + 2].replace("\n", "").split(" ")
				int_row = [int(i) for i in row]
				obj.append(int_row)
			objetos.append(obj)

def DesenhaCelula(start_x, start_y):
	glBegin(GL_QUADS)
	glVertex2f(start_x + 0, start_y + 0)
	glVertex2f(start_x + 0, start_y + 1)
	glVertex2f(start_x + 1, start_y + 1)
	glVertex2f(start_x + 1, start_y + 0)
	glEnd()

def DesenhaMatriz(obj, start_x, start_y):
	#glPolygonMode(GL_FRONT,G)
	glPushMatrix()
	for i in range(len(obj)-1, -1, -1): # Altura = comprimento da matriz
		glPushMatrix()
		for j in range(len(obj[0])): # Largura = comprimento de uma lista da matriz
			pix = obj[i][j] # Pixel
			glColor3f(int(cores[pix][0]), int(cores[pix][1]), int(cores[pix][2])) # Pega corretamente a cor de cada pixel
			DesenhaCelula(start_x, start_y)
			#Ret1x1.desenhaPoligono()
			glTranslatef(1, 0, 0)
		glPopMatrix()
		glTranslatef(0, 1, 0)
	glPopMatrix()

########################################
##### SPRITES END
########################################

def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(Min.x-BordaX, Max.x+BordaX, Min.y-BordaY, Max.y+BordaY, 0.0, 1.0)
    #glOrtho(Min.x, Max.x, Min.y, Max.y, 0.0, 1.0)
    glOrtho(0, 100, 0, 100, 0.0, 1.0)
    #glOrtho(0, 55, -40, 40, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display():
    global projectile, projArrow, power, angle, xCannon, animated, xEnemies
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLineWidth(1)
    if lives == 0 or allEnemiesGone() or allBuildingsGone():
        os._exit(0)
    # glClearColor(255,255,255,255) # Background
    # drawBezier(xCannon, angle, power)
    drawCannon(xCannon, angle)
    if not enemiesHit[0]:
        drawEnemies1(10, 60, 0, xEnemies)
    if not enemiesHit[1]:
        drawEnemies2(30, 60, 1, xEnemies)
    if not enemiesHit[2]:
        drawEnemies3(50, 60, 2, xEnemies)
    if not enemiesHit[3]:
        drawEnemies1(70, 60, 3, xEnemies)
    if not enemiesHit[4]:
        drawEnemies2(90, 60, 4, xEnemies)
    if not enemiesHit[5]:
        drawEnemies3(85, 80, 5, xEnemies)
    if not enemiesHit[6]:
        drawEnemies1(15, 80, 6, xEnemies)
    if not enemiesHit[7]:
        drawEnemies2(35, 80, 7, xEnemies)
    if not enemiesHit[8]:
        drawEnemies3(55, 80, 8, xEnemies)
    if not enemiesHit[9]:
        drawEnemies3(75, 80, 9, xEnemies)
    if not buildingsHit[0]:
        drawBuilding(30, 0)
    if not buildingsHit[1]:
        drawBuilding(55, 1)
    if not buildingsHit[2]:
        drawBuilding(80, 2)
    if not buildingsHit[3]:
        drawHouse(40, 3)
    if not buildingsHit[4]:
        drawHouse(65, 4)
    if not buildingsHit[5]:
        drawHouse(87, 5)
    # drawBezier(xCannon, angle, power)
    drawArrow(angle, xCannon, power)
    if enemyShooting:
        drawEnemyProj()
    if animated:
        drawProjectile()
    glutSwapBuffers()

def animate():
    global animated, angle, xCannon, power, animatedTime, xEnemies, time, enemyShooting, enemySelectedIndex
    xEnemies -= 0.2
    if xEnemies < -98:
        xEnemies = 0
    glutPostRedisplay() 
    enemyShooting = True
    # print(animatedTime)
    if animatedTime > 5:
        animatedTime = 0
    if enemyShooting:
        time += 0.08
        if not enemiesHit[enemySelectedIndex]:
            enemyPol = enemies[enemySelectedIndex]
            animateBezierEnemy(230, 20, enemyPol)
        else:
            enemySelectedIndex = randint(0, 9)
    if animated:
        animateBezierProjectile(xCannon, angle, power)
        animatedTime += 0.08

def animateBezierProjectile(xCannon: int, angle: float, power: int):
    global animated, animationTime, projectile, animatedTime, enemiesHit
    t = animatedTime/animationTime
    startXProj = 8
    startYProj = 10
    xPower = math.cos(converterGrausParaRad(angle)) * power
    yPower = math.sin(converterGrausParaRad(angle)) * power
    distX = xPower + startXProj + xCannon 
    distY = yPower + startYProj + xCannon 
    halfX = (xPower/2) + startXProj + xCannon 
    if t > 0.98:
        animated = False
        projectile.translate = Point(startXProj + xCannon , startYProj, 0)
    p = calculateBezier3(Point(startXProj, startYProj, 0), Point(halfX, distY, 0), Point(distX, 0, 0), t)
    if p.x > 100 or p.y > 100:
        animated = False
        projectile.translate = Point(startXProj + xCannon , startYProj, 0)
        animatedTime = 0
    pol = Polygon()
    pol.insereVertice(p.x + xCannon, p.y, 0)
    pol.insereVertice(p.x + xCannon, p.y + 2, 0)
    pol.insereVertice(p.x + xCannon + 2, p.y + 2, 0)
    pol.insereVertice(p.x + xCannon + 2, p.y, 0)
    for i in range(10):
        if not enemiesHit[i]:
            if colision2Obj(enemies[i], pol):
                animated = False
                projectile.translate = Point(startXProj + xCannon , startYProj, 0)
                animatedTime = 0
                enemiesHit[i] = True
    projectile.translate = p

def animateBezierEnemy(angle: float, power: int, p: Polygon):
    global time, enemyShooting, enemyProj, enemySelectedIndex, cannon, lives
    LePontosDeArquivo("Projectile.txt", enemyProj)
    enemyProj.setTranslate(Point(p.translate.x, p.translate.y, 0))
    t = time/5
    startXProj = p.translate.x
    startYProj = p.translate.y
    xPower = math.cos(converterGrausParaRad(angle)) * power
    yPower = math.sin(converterGrausParaRad(angle)) * power
    distX = xPower + startXProj
    distY = yPower + startYProj
    halfX = (xPower/2) + startXProj
    p = calculateBezier3(Point(startXProj, startYProj, 0), Point(halfX, distY, 0), Point(distX, 0, 0), t)
    if t > 0.98:
        enemyShooting = False
        time = 0
        enemySelectedIndex = randint(0, 9)
    pol = Polygon()
    pol.insereVertice(p.x, p.y, 0)
    pol.insereVertice(p.x, p.y + 2, 0)
    pol.insereVertice(p.x + 2, p.y + 2, 0)
    pol.insereVertice(p.x + 2, p.y, 0)
    for i in range(5):
        if not buildingsHit[i]:
            if colision2Obj(pol, buildings[i]):
                enemyShooting = False
                time = 0
                enemySelectedIndex = randint(0, 9)
                buildingsHit[i] = True
    if colision2Obj(pol, cannon):
        lives -= 1
        enemyShooting = False
        time = 0
        enemySelectedIndex = randint(0, 9)
    enemyProj.translate = p

def drawBezier(xCannon: int, angle: float, power: int):
    t = 0.0
    deltaT = 1.0/10
    glBegin(GL_LINE_STRIP)
    startXProj = 7
    startYProj = 6
    xPower = math.cos(converterGrausParaRad(angle)) * power
    yPower = math.sin(converterGrausParaRad(angle)) * power
    distX = xPower + startXProj + xCannon
    distY = yPower + startYProj
    halfX = (xPower/2) + startXProj + xCannon
    glColor3f(1,0,0)
    while t < 1.0:
        p = calculateBezier3(Point(startXProj + xCannon, startYProj, 0), Point(halfX, distY, 0), Point(distX, 0, 0), t)
        glVertex2f(p.x, p.y)
        t += deltaT
    glEnd()

def calculateBezier3(point1: Point, point2: Point, point3: Point, t: float) -> Point:
    oneMinusT = 1-t
    p = (point1 * oneMinusT * oneMinusT) + (point2 * 2* oneMinusT * t) + (point3 * t * t)
    return p

def allEnemiesGone() -> bool:
    global enemiesHit
    for i in enemiesHit:
        if not i:
            return False
    return True

def allBuildingsGone() -> bool:
    global buildingsHit
    for i in buildingsHit:
        if not i:
            return False
    return True

def drawProjectile():
    glPushMatrix() # PUSH
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(projectile.translate.x + xCannon, projectile.translate.y, 0)
    projectile.desenhaPoligono()
    glPopMatrix() # POP

def drawEnemyProj():
    glPushMatrix() # PUSH
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(enemyProj.translate.x , enemyProj.translate.y, 0)
    enemyProj.desenhaPoligono()
    glPopMatrix() # POP

def drawArrow(angle: float, xCannon: int, power: int):
    glPushMatrix() # PUSH
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(projArrow.translate.x+ xCannon, projArrow.translate.y, 0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glScalef(1 + 0.05*power, 1, 1)
    projArrow.desenhaPoligono()
    glPopMatrix() # POP

def drawBullet():
    glPushMatrix() # PUSH
    glColor3f(1.0, 0.0, 0.0)
    projectile.desenhaPoligono()
    glPopMatrix() # POP

def drawCannon(xCannon: int, angle: float):
    glPushMatrix() # PUSH
    glColor3f(1,1,0); # R, G, B  [0..1]
    # glRotatef(angle, xCannon + 4, 9, 1)
    cannon.translate = Point(xCannon, 0, 0)
    glTranslatef(xCannon, 0, 0)
    DesenhaMatriz(objetos[0], 0, 0)
    glPopMatrix() # POP

def drawBuilding(x: int, i: int):
    glPushMatrix() # PUSH
    glTranslatef(x, 0, 0)
    buildings[i].translate = Point(x, 0, 0)
    glColor3f(1,1,0); # R, G, B  [0..1]
    DesenhaMatriz(objetos[4], 0, 0)
    glPopMatrix() # POP

def drawHouse(x: int, i: int):
    glPushMatrix() # PUSH
    glTranslatef(x, 0, 0)
    buildings[i].translate = Point(x, 0, 0)
    glColor3f(1,1,0); # R, G, B  [0..1]
    DesenhaMatriz(objetos[5], 0, 0)
    glPopMatrix() # POP

def drawEnemies1(x: int, y: int, i: int, xEnemies: int):
    newX = xEnemies + x
    if newX < 0:
        newX += 98
    elif newX > 98:
        newX -= 98
    glPushMatrix() # PUSH
    glTranslatef(newX, y, 0)
    glColor3f(0,0,1); # R, G, B  [0..1]
    enemies[i].translate = Point(newX, y, 0)
    DesenhaMatriz(objetos[2], 0, 0)
    glScalef(0.4, 0.4, 0)
    glPopMatrix() # POP

def drawEnemies2(x: int, y: int, i: int, xEnemies: int):
    newX = xEnemies + x
    if newX < 0:
        newX += 98
    elif newX > 98:
        newX -= 98
    glPushMatrix() # PUSH
    glTranslatef(newX, y, 0)
    glColor3f(1,1,0); # R, G, B  [0..1]
    enemies[i].translate = Point(newX, y, 0)
    glScalef(0.4, 0.4, 0)
    DesenhaMatriz(objetos[3], 0, 0)
    glPopMatrix() # POP

def drawEnemies3(x: int, y: int, i: int, xEnemies: int):
    newX = xEnemies + x
    if newX < 0:
        newX += 98
    elif newX > 98:
        newX -= 98
    glPushMatrix() # PUSH
    glTranslatef(newX, y, 0) 
    glColor3f(1,1,0); # R, G, B  [0..1]
    enemies[i].translate = Point(newX, y, 0)
    glScalef(0.4, 0.4, 0)
    DesenhaMatriz(objetos[1], 0, 0)
    glPopMatrix() # POP

def colision2Obj(p1: Polygon, p2: Polygon) -> bool:
    minP1, maxP1 = p1.getLimits()
    minP2, maxP2 = p2.getLimits()
    p1AABB = createBoundingBox(minP1.x + p1.translate.x, maxP1.x + p1.translate.x, minP1.y + p1.translate.y, maxP1.y + p1.translate.y)
    p2AABB = createBoundingBox(minP2.x + p2.translate.x, maxP2.x + p2.translate.x, minP2.y + p2.translate.y, maxP2.y + p2.translate.y)
    return hasCollision(p1AABB, p2AABB)

def converterGrausParaRad(numero):
    rad = (numero/180)*math.pi
    return rad

# ESCAPE = '\033'
ESCAPE = b'\x1b'
def keyboard(*args):
    global power, angle, xCannon, animated
    #special(*args)
    if args[0] == GLUT_KEY_LEFT:
        print("ESQUERDA")
    if args[0] == b'q':
        if angle < 160:
            angle += 5
    if args[0] == b'e':
        if angle != 0:
            angle -= 5
    if args[0] == ESCAPE:
        os._exit(0)
    if args[0] == b' ':
        animated = True
    if args[0] == b'd':
        xCannon += 0.5
        if xCannon > 90:
            xCannon = 90
    if args[0] == b'a':
        xCannon -= 0.5
        if xCannon < 0:
            xCannon = 0
    if args[0] == b'0':
        power += 30
        if power > 300:
            power = 300
    if args[0] == b'9':
        power -= 10
        if power < 10:
            power = 10

def LePontosDeArquivo(Nome, P):
    infile = open(Nome)
    line = infile.readline()
    for line in infile:
        words = line.split() # Separa as palavras na linha
        x = float (words[0])
        y = float (words[1])
        P.insereVertice(x,y,0)
    infile.close()

def ObtemMaximo (P1, P2):
    Max = copy.deepcopy(P1)
    
    if (P2.x > Max.x):
        Max.x = P2.x

    if (P2.y > Max.y):
        Max.y = P2.y

    if (P2.z > Max.z):
        Max.z = P2.z

    return Max

def ObtemMinimo (P1, P2):
    Min = copy.deepcopy(P1)
    
    if (P2.x < Min.x):
        Min.x = P2.x
    
    if (P2.y < Min.y):
        Min.y = P2.y
    
    if (P2.z < Min.z):
        Min.z = P2.z

    return Min

def createBoundingBox(minX: int, maxX: int, minY: int, maxY: int) -> AABB:
    P = Polygon()
    P.insereVertice(minX, minY, 0)
    P.insereVertice(minX, maxY, 0)
    P.insereVertice(maxX, maxY, 0)
    P.insereVertice(maxX, minY, 0)
    halfWidthX = (maxX-minX)/2
    halfWidthY = (maxY-minY)/2
    center = Point( halfWidthX+ minX, halfWidthY+minY, 0)
    halfWidth = Point(halfWidthX, halfWidthY, 0)
    boundingBox = AABB(center, halfWidth)
    return boundingBox

def hasCollision(E1: AABB, E2: AABB):
    if abs(E1.center.x - E2.center.x) > E1.halfWidth.x + E2.halfWidth.x :
        return False
    if abs(E1.center.y - E2.center.y) > E1.halfWidth.y + E2.halfWidth.y :
        return False
    if abs(E1.center.z - E2.center.z) > E1.halfWidth.z + E2.halfWidth.z :
        return False

    return True

def init():
    global cannon, projectile, projArrow  # Variáveis usadas para definir os limites da Window
    
    LePontosDeArquivo("Projectile.txt", projectile)
    projectile.setTranslate(Point(8, 10, 0))

    LePontosDeArquivo("ProjectileArrow.txt", projArrow)
    projArrow.setTranslate(Point(8, 10, 0))
    
def special(*args):
    print (args)
    if args[0] == GLUT_KEY_LEFT:
        print("ESQUERDA")

if __name__ == '__main__':
    parseSprites("objects.txt")
    init()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1000, 500)
    glutInitWindowPosition(400, 300)
    wind = glutCreateWindow("Lancador de Projeteis")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)

    try:
        glutMainLoop()
    except SystemExit:
        pass