import cv2
import os

while True:

    file = input(" \nEnter File name: ")
    fpath = str(file + '.jpg')

    print("\nA. Colored B. Grayscale")
    flag = input("\nEnter Flag Values: ")

    if flag == "A" or flag == "a":
        if os.path.exists(fpath):
            img= cv2.imread(fpath,1)
            if file == 'kitty':
                cv2.imshow("HELLO KITTY", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            
            if file == 'panda':
                cv2.imshow("PANDA", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

        else:
            print("Imported invalid file type ! ! !")

    elif flag == "B" or flag == "b":
        if os.path.exists(fpath):
            img = cv2.imread(fpath,0)
            if file == 'kitty':
                cv2.imshow("HELLO KITTY", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

            if file == 'panda':
                cv2.imshow("PANDA", img)
                cv2.waitKey(0)  
                cv2.destroyAllWindows()
                break

        else:
            print("\nImported invalid file type ! ! !")

    else:
        print("\nEntered invalid flag values ! ! !")