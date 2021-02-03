from skimage import io
import pytesseract
import glob


time = io.imread('IMG-1800.PNG')

images = glob.glob('usage/*.PNG')

print(images)


for image_path in images:
    pic = io.imread(image_path)
    text = pytesseract.image_to_string(pic)

    image_name = image_path.split('/')
    image_path = image_name[1].replace('.PNG', '.txt')
    with open('out/'+image_path, "w") as file:
        file.write(text)

#print(pytesseract.image_to_string(time))