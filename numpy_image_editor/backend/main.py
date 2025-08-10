#importing required libraries
import cv2
import numpy as np


# image loading funtion
def loadimage(path):
    img=cv2.imread(path)
    if img is None:
        print("image import is failed , 1 - check file path , 2 - make sure that the file exist.")
        return None
    print("image imported succesfully and ready to be operated.")
    return img


# show image funtion
def showimage(path):
    a=int(input(("enter time for showing of image in seconds = (0 for forever opening) = ")))
    cv2.imshow("image provided by user",path)
    cv2.waitKey(a*1000)
    cv2.destroyAllWindows()
    

# increase brightness funtion
def incbright(img):
    value = int(input(("enter Brightness value scale: 0 (no change) to 255 (maximum brightening) = ")))
    bright= img.astype(np.int16) + value
    showimage(np.clip(bright,0,255).astype(np.uint8))
    save(bright)
        

    # decrease brightness funtion
def decbright(img):
    value = int(input(("enter Brightness decrease scale: 0 (no change) to 255 (maximum darkening) = ")))
    dark= img.astype(np.int16) - value
    showimage(np.clip(dark,0,255).astype(np.uint8))
    save(dark)
    

# greyscale funtion
def greyscale(img):
    grey=0.299*img[:,:,2]+0.587*img[:,:,1]+0.114*img[:,:,0]
    showimage(grey.astype(np.uint8))
    save(grey)
    
  
# edited image saving funition
def save(value):
    a=str(input(("do you want to save this edited image = y/n = ")))
    if a=='y' or a=='Y':
        cv2.imwrite(r"C:\Users\krishna\OneDrive\Desktop\coding\dev_projects\numpy_image_editor\backend\outputedited_image.jpg", np.clip(value, 0, 255).astype(np.uint8))
        print("image saved succesfully at output folder, check.") 
    elif a=='n' or a=='N':
        print("image not saved.")
    else:
        print("invalid input, image not saved.")
        
         

#  main code from here--
print("this is a mini and basic image editor for showing practical knowledge of numpy library of python made by Dev")
print("\n")
path=input("enter your image path here for editing = ")
img=loadimage(path)
print("\n")


# command line interface for choices
if img is not None:
    print("enter 1 for pre view of your loaded image before editing. (optional)")
    print("enter 2 for increasing brightness of image.")
    print("enter 3 for decreasing brightness of image.")
    print("enter 4 to convert the image into greyscale")
    print("enter 5 for closing the image editor.")
    print("\n")
    

# choice input by user
while img is not None:
    choice=int(input("enter your operation as index number = "))
    if(choice==1):
        showimage(img)
        
    elif choice==2:
        incbright(img)
        
    elif choice==3:
        decbright(img)
        
    elif choice==4:
        greyscale(img)
        
    elif choice==5:
        print("image editor closed succesfully.")
        break
    
    else:
        print("enter a valid number associated with a operation.")
# program exicuted succesfully
# END





        
    
    
    
    
    
    
    
    
    
    
    
    





















    