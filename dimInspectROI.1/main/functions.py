import cv2, numpy, math 


dpack = {
    "gaussTile":(9,9),
    'gaussSigma':6,
    'claheTile':(2,2),
    'cannyLow':30,
    'cannyHigh':30,
    'houghVotes':100,
    'houghMLL':150,
    'houghMLG':100,
    'bilateralD':10,
    'bilateralSigma':200,
    'bilateralColor':200
}

dpackROI = {
    "gaussTile":(9,9),
    'gaussSigma':6,
    'claheTile':(2,2),
    'cannyLow':40,
    'cannyHigh':40,
    'houghVotes':100,
    'houghMLL':250,
    'houghMLG':100,
    'bilateralD':10,
    'bilateralSigma':200,
    'bilateralColor':200
}

def enterROI(pt1, pt2,source):
    point1,point2 = pt1, pt2
    minX,maxX = min(point1[0],point2[0]), max(point1[0],point2[0])
    minY, maxY = min(point1[1],point2[1]), max(point1[1],point2[1])
    minX -= 25
    minY -= 25
    maxX += 25
    maxY += 25
    newRegion = source[minY:maxY,minX:maxX]
    offSet = (minX,minY)
    return newRegion,offSet

def getIntersections(lineGroups,source):
    pts = []
    for i in range(4):
        pt = intersect(lineGroups[i][0],lineGroups[(i+1)%4][0],source)
        pts.append(pt)
    return pts

def generateROI(pts,source):
    rt = []
    for i in range(4):
        newRegion, offSet = enterROI(pts[i],pts[(i+1)%4],source)
        cv2.imshow(str(i),newRegion)
        rt.append((newRegion,offSet))
    return rt

def produceCanny(source,dpack):     
    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    claheObject = cv2.createCLAHE(clipLimit=2.0,tileGridSize=dpack.get('claheTile',(2,2)))
    claheObject.apply(source)
    source = cv2.bilateralFilter(source, dpack.get('bilateralD',0),dpack.get('bilateralSigma',0),dpack.get('bilateralColor',0))
    source = cv2.Canny(source,dpack.get('cannyLow',20),dpack.get('cannyHigh',40))
    return source

#Taken code, find original author
def intersect(line1,line2,source):
    pt1, pt2 = line1
    pt3, pt4 = line2
    px1,py1 = pt1
    px2, py2 = pt2
    dx1, dy1 = pt3
    dx2, dy2 = pt4
    xdiff = (px1 - px2, dx1 - dx2)
    ydiff = (py1 - py2, dy1 - dy2)
    line1 = ((px1,py1),(px2,py2))
    line2 = ((dx1, dy1),(dx2,dy2))
    def determinant(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = determinant(xdiff, ydiff)
    if div == 0:
        print(f"ERROR {xdiff} {ydiff}")
        return False

    d = (determinant(*line1), determinant(*line2))
    x = int(determinant(d, xdiff) / div)
    y = int(determinant(d, ydiff) / div)
    cv2.circle(source,(x,y),3,(255,255,0),2)
    return x, y

def getLines(source,dpack,):
    lines = cv2.HoughLinesP(source, 1, numpy.pi/180, threshold=dpack.get('houghVotes',150),minLineLength=dpack.get('houghMLL',100),maxLineGap=dpack.get('houghMLG',100))
    source = cv2.cvtColor(source,cv2.COLOR_GRAY2BGR)
    lineGroups = [[],[],[],[]]
    for line in lines:
        x1,y1,x2,y2 = line[0]
        convLine = [(x1,y1),(x2,y2)]
        deg1 = math.degrees(math.atan2(abs(y1-y2),abs(x1-x2)))
        if 80 < deg1 < 100:
            if x1 < 640:
                lineGroups[0].append(convLine)
            else:
                lineGroups[2].append(convLine)
        else:
            if y1 < 480:
                lineGroups[1].append(convLine)
            else:
                lineGroups[3].append(convLine)
    return lineGroups

def extendLine(line):
    x1,y1,x2,y2 = line
    xdiff, ydiff = x2-x1,y2-y1
    nx1, nx2 = x1 + xdiff * 1000, x1 - xdiff * 1000
    ny1, ny2 = y1 + ydiff * 1000, y1 - ydiff * 1000

    return((nx1,ny1),(nx2,ny2))

def getDist(line):
    x1,y1,x2,y2 = line
    return (abs(x2-x1)**2+abs(y2-y1)**2)**(0.5)

def drawLine(line, source, colour=(255,0,0) ):
    x1,y1,x2,y2 = line
    cv2.line(source,(x1,y1),(x2,y2),colour)

def fixOffset(line,offset):
    x1,y1,x2,y2 = line
    x1 += offset[0]
    x2 += offset[0]
    y1 += offset[1]
    y2 += offset[1]
    return x1,y1,x2,y2







