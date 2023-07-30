import numpy, cv2, functions as fc

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
    'cannyLow':24,
    'cannyHigh':24,
    'houghVotes':100,
    'houghMLL':250,
    'houghMLG':100,
    'bilateralD':15,
    'bilateralSigma':200,
    'bilateralColor':250
}

sourcePath = '1_2023-07-25-122526-0000.jpg'
source = cv2.imread(sourcePath)
def generateBoundLines(sourcePath):
    source = cv2.imread(sourcePath)
    sourceCopy = source
    source = fc.produceCanny(source,dpack)
    lineGroups = fc.getLines(source,dpack)
    pts = fc.getIntersections(lineGroups,source)
    newLines = [[],[],[],[]]
    for i in range(4):
        newRegion, offset = fc.enterROI(pts[i],pts[(i+1)%4],sourceCopy)
        newRegion = fc.produceCanny(newRegion,dpackROI)
        firstLine = fc.getLines(newRegion,dpackROI)[(i+1)%2][0]
        x1,y1,x2,y2 = fc.fixOffset(firstLine[0]+firstLine[1],offset)
        pt1,pt2 = fc.extendLine([x1,y1,x2,y2])
        newLines[i].append([(x1,y1),(x2,y2)])
        cv2.line(sourceCopy,pt1,pt2,((125*(i+1)%250),(25*(i+1)),(50*(i+1))))
    return newLines, sourceCopy

def generateDimensions(newLines,source):
    res = []
    pts = fc.getIntersections(newLines,source)
    for i in range(4):
        res.append(fc.getDist(pts[i]+pts[(i+1)%4]))
    return res












