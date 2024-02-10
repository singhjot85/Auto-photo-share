import os
import sys
import zipfile
import pywhatkit

def complete_mobile_number(mobile_number):
    
    country_codes = {
        'US': '+1',
        'UK': '+44',
        'IN': '+91',
        'CA': '+1',
    }

    if mobile_number.startswith('+'):
        print("Mobile number already has a country code.")
        return mobile_number
    
    country_code = input("Enter your country code (e.g., US, UK, IN): ").upper()

    if country_code not in country_codes:
        print("!!!Invalid country code!!!")
        sys.exit()

    complete_number = country_codes[country_code] + mobile_number
    return complete_number

# list of image paths
image_paths = ['gurr.jpg',r'C:\Users\SinghJot\OneDrive\Documents\OTHERS\Projects\APS\Gurjot 4.png', 'send_button.png']

# create a ZIP file at the specified location
with zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    # add each image to the ZIP file
    for image_path in image_paths:
        # include only the image file name in the ZIP file
        zipf.write(os.path.basename(image_path))
        
print("zip create sucess")

caption = "Extract this file to get images"

phone_number = input("Enter your mobile number: ")
complete_phone_number = complete_mobile_number(phone_number)

# Send the file
pywhatkit.send_file(complete_phone_number, 'images.zip', caption=caption)
