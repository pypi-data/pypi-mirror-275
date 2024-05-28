import cv2
import os
from pkg_resources import resource_filename

#Creating faces storing directory 
if not os.path.isdir('faces'):
    os.makedirs('faces')

# Load the cascade file
haar_cascade_path = resource_filename(__name__, 'data/haarcascade_frontalface_default.xml')

if not os.path.isfile(haar_cascade_path):
    raise FileNotFoundError(f"Haar cascade file not found at path: {haar_cascade_path}")

haar_face = cv2.CascadeClassifier(haar_cascade_path)

# face detecting functions
def detect(path):
    img = cv2.imread(path)
    if img is None:
        print(f"Error: Could not read image {path}")
        return 
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
    tFaces = 0 
    
    for x,y,w,h in face:
        name = str(tFaces)+'.jpg'
        cv2.imwrite('faces/'+name,img[y:y+h,x:x+w])
        tFaces += 1
        
    print(f'total faces detect: {tFaces}')
    cv2.waitKey(0)
    cv2.destroyAllWindows()