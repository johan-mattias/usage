from skimage import io
import pytesseract
import glob


time = io.imread('IMG-1800.PNG')

images = glob.glob('usage/*.PNG')

print(images)

dates = []

def check_days_of_week(text):
    if ',' in text:
        line_split = text.split()
        day = line_split[0].replace(',', '')
        if day == 'Monday':
            return True
        elif day == 'Tuesday':
            return True
        elif day == 'Wednesday':
            return True
        elif day == 'Thursday':
            return True
        elif day == 'Friday':
            return True
        elif day == 'Saturday':
            return True
        elif day == 'Sunday':
            return True    
    return False

def check_time(text):
    text = text.split()
    if(len(text) == 2):
        if 'h' in text[0] and 'm' in text[1]:
            return True
    return False

def get_date(text):
    text = text.split('\n')

    day = ""
    time = ""

    for line in text:
        if line:
            if check_days_of_week(line):
                day = line
            elif check_time(line):
                time = line
                break
    return (day, time)

for image_path in images:
    pic = io.imread(image_path)
    text = pytesseract.image_to_string(pic)

    date = get_date(text)
    dates.append(date)


    image_name = image_path.split('/')
    image_path = image_name[1].replace('.PNG', '.txt')
    with open('out/'+image_path, "w") as file:
        file.write(text)

#print(pytesseract.image_to_string(time))