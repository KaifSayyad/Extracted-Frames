# Program To Read video
# and Extract Frames
import cv2


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ImagesApp.settings")
django.setup()
from django.core.files import File
from base.models import Image  # Import your model
from django.conf import settings


def insert_image(image_path, title):
    with open(image_path, 'rb') as f:
        image_file = File(f)
        new_image = Image(title=title)
        new_image.image.save(os.path.basename(image_path), image_file)
        new_image.save()



def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite("media/images/frame%d.jpg" % count, image)
        image_path = "media/images/frame%d.jpg" % count
        title= "frame%d.jpg" % count
        insert_image( image_path, title)
        count += 1


# Driver Code
if __name__ == '__main__':

	# Calling the function
	FrameCapture("C:/Riot Games/VALORANT/live/ShooterGame/Content/Movies/Menu/HomePage_Gekko.mp4")
