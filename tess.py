from skimage import io
import pytesseract
time = io.imread('summary.png')
print(pytesseract.image_to_string(time))