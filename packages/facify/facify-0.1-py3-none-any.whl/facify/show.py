import cv2

def show(path):
    filepath = path
    # Read the image from filepath
    image = cv2.imread(filepath)

    # Check if the image was successfully loaded
    if image is None:
        print("Could not load image.")
    else:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
