import os
import zipfile

# list of image paths
image_paths = ['gurr.jpg',r'C:\Users\SinghJot\OneDrive\Documents\OTHERS\Projects\APS\Gurjot 4.png', 'send_button.png']

# specify the full path of the ZIP file
zip_file_path =r'D:\whts_send'

# create a ZIP file at the specified location
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # add each image to the ZIP file
    for image_path in image_paths:
        # include only the image file name in the ZIP file
        zipf.write(os.path.basename(image_path))

print("zip create sucess")