import subprocess
import sys
import getopt
import os
import wand.image
import img2pdf

FILE_LIST = []
PNG_FILE_LIST = []
image_extensions = ('.png', '.jpg', '.jpeg')

def hasAlpha(image_path):
    with wand.image.Image(filename=image_path) as img:
        #print(dir(img))
        alpha = img.alpha_channel
        return alpha

def removeAlpha(image_path, new_image_path):
    with wand.image.Image(filename=image_path) as img:
        img.alpha_channel = 'remove' #close alpha channel   
        img.background_color = wand.image.Color('white')
        img.save(filename=new_image_path)

def handle_file(file_path):
    trash, extension = os.path.splitext(file_path)
    use_this = file_path.replace('\\', '\\\\')
    use_this = use_this.replace(' ', '\\ ')
    # print('a', use_this)
    if extension in image_extensions:
        FILE_LIST.append(str(file_path))
    if extension == image_extensions[0]:
        PNG_FILE_LIST.append(str(file_path))

def recursive_file_search(paths):
    paths.sort()
    for path in paths:
        if os.path.isdir(path):
            for file_ in os.listdir(path):
                if os.path.isdir(os.path.join(path, file_)):
                    recursive_file_search([os.path.join(path, file_)])
                elif os.path.isfile(os.path.join(path, file_)):
                    handle_file(os.path.join(path, file_))
        elif os.path.isfile(path):
            handle_file(path)
        elif os.path.exists(path):
            print("{} Path isn't an image file or directory".format(path))

def make_pdf(output_path, file_paths):
    with open(output_path,"wb") as f:
	    f.write(img2pdf.convert(file_paths))

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'o:')
output_path = opts[0][1]
recursive_file_search(args)
print('FILE LIST:')
for file_path in FILE_LIST:
    print(file_path)
print('PNG FILE LIST:')
for file_path in PNG_FILE_LIST:
    print(file_path)
# subprocess.call(['remove_alpha.sh', *PNG_FILE_LIST], shell=True)
for file_path in PNG_FILE_LIST:
    if hasAlpha(file_path):
        removeAlpha(file_path, file_path)
make_pdf(output_path, FILE_LIST)
# subprocess.call(['convert_images_to_pdf.sh', output_path, *FILE_LIST], shell=True)
