import cv2, numpy, pandas as pd, functions as fc, os, time, process as pr

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

imageDirSource = 'trial1'

m = {}
for i,imageFileName in enumerate(os.listdir(imageDirSource)):
    if i == 50:
        break
    f = os.path.join(imageDirSource,imageFileName)
    if os.path.isfile(f):
        start = time.perf_counter()
        print(f)
        newLines, sourceCopy = pr.generateBoundLines(f)
        res = pr.generateDimensions(newLines,sourceCopy)
        end = time.perf_counter()
        m[f] = res + [end-start] + [res[0]-res[2]] + [res[1] - res[3]]
        cv2.imwrite(f"w{f}",sourceCopy)
df = pd.DataFrame(m)
df = df.transpose()
df.to_csv('results2.csv',header=['TopSideMeasure','LeftSideMeasure','BottomSideMeasure','RightSideMeasure','Time','hDiff','vDiff'])    

    
cv2.waitKey()
