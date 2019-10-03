import dlib
import os
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt

files = []
path = '/content/drive/My Drive/ID_Photo'


def detect_faces(image):
    
    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]
    

    return face_frames

# Load image
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpeg' in file:
            files.append(os.path.join(r, file))



#img_path = '/content/drive/My Drive/RupeeGo/15/panind/SRINIVASA_SANATHKUMAR_PAN_1.jpeg'
for f in files:
  image = io.imread(f)


# Detect faces
  detected_faces = detect_faces(image)

# Crop faces and plot
  for n, face_rect in enumerate(detected_faces):
    
      face = Image.fromarray(image).crop(face_rect)
      plt.subplot(1, len(detected_faces), n+1)
      #plt.axis('off')
      plt.imshow(face)
