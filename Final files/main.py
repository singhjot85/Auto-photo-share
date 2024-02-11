import sys
from imageCapture import detect_bounding_box, video_capture_script
from cmpImg import similar_images, image_resizer

x = int(input("Select option: \n"+ "1. Capture photo\n"+"2. Enter image path manually\n"))

if x is 1: captured_image = video_capture_script()
elif x is 2: captured_image = input("Enter image path\n")
else:
    print("Invalid input")
    sys.exit()

directory_path = r'C:\Users\SinghJot\OneDrive\Documents\GitHub\Projects\APS\Final files\Database'
similar_image_path = similar_images(captured_image,directory_path)

import os
import zipfile
with zipfile.ZipFile('SimilarImages.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    # add each image to the ZIP file
    for image_path in similar_image_path:
        zipf.write(os.path.basename(image_path)) # include only the image file name in the ZIP file
print("zip create success")

import pywhatkit
def complete_mobile_number(mobile_number):
    if mobile_number.startswith('+'):
        print("Mobile number already has a country code.")
        return mobile_number
    country_code = input("Enter your country code (e.g., US, UK, IN): ").upper()    
    country_codes = {'US': '+1','UK': '+44',
                     'IN': '+91','CA': '+1',}
    if country_code not in country_codes:
        print("!!!Invalid country code!!!")
        sys.exit()
    complete_number = country_codes[country_code] + mobile_number
    return complete_number

phone_number = input("Enter your mobile number: ")
complete_phone_number = complete_mobile_number(phone_number)
caption = "Extract this file to get images"
pywhatkit.sendwhats_image(complete_phone_number, 'SimilarImages.zip', caption=caption) # Send the file


