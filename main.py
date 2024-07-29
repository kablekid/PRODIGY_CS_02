import getopt
import LoadImage,change
import sys
from PIL import Image


try:
    # Improved options and error handling
    short_options = "e:d:f:"
    long_options = ["encrypt=", "decrypt=", "filepath="]
    user_input = sys.argv[1:]  # Get user arguments after script name
    opts, args = getopt.getopt(user_input, short_options, long_options)


    for opt, arg in opts:
        if opt in ("-e", "--encrypt"):
            mode,key = "encrypt",int(arg)
            
        elif opt in ("-d", "--decrypt"):
            mode,key = "decrypt",int(arg)
            
        elif opt in ("-f", "--filepath"):
            filepath = arg
        else:
            raise ValueError("Invalid option:", opt)  # Raise specific error

except getopt.GetoptError as err:
    print(str(err))
    sys.exit(2)

# Check for missing required arguments
if not mode or not filepath:
    print("Usage: python main.py -[e|d] <key> -f <filepath>")
    sys.exit(2)

# Assuming LoadImage.start(...) is your image processing function
imgArray = LoadImage.start(filepath) # Pass  filepath

print(imgArray) 

if mode == "encrypt":
    modifiedImage = change.encrypt(imgArray,key)
elif mode == 'decrypt':
    modifiedImage = change.decrypt(imgArray,key)



image = Image.fromarray(modifiedImage, 'RGB')

# Save the image
image.save('output.png')