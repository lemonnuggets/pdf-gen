import subprocess
import sys
import getopt
import os
FILE_LIST = []
PNG_FILE_LIST = []
image_extensions = ('.png', '.jpg', '.jpeg')
def recursive_file_search(paths):
    paths.sort()
    for path in paths:
        if os.path.isdir(path):
            for file_ in os.listdir(path):
                if os.path.isdir(os.path.join(path, file_)):
                    recursive_file_search([os.path.join(path, file_)])
                elif os.path.isfile(os.path.join(path, file_)):
                    trash, extension = os.path.splitext(file_)
                    if extension in image_extensions:
                        FILE_LIST.append(os.path.join(path, file_))
                    if extension == image_extensions[0]:
                        PNG_FILE_LIST.append(os.path.join(path, file_))
        elif os.path.isfile(path):
            trash, extension = os.path.splitext(path)
            if extension in image_extensions:
                FILE_LIST.append(path)
            if extension == image_extensions[0]:
                PNG_FILE_LIST.append(path)
        elif os.path.exists(path):
            print("{} Path isn't an image file or directory")

args = sys.argv[1:]
opts, args = getopt.getopt(args, 'o:')
print(opts, args)
output_path = opts[0][1]
recursive_file_search(args)
print('FILE LIST:')
for file_path in FILE_LIST:
    print(file_path)
print('PNG FILE LIST:')
for file_path in PNG_FILE_LIST:
    print(file_path)
# subprocess.call('remove_alpha.sh', shell=True)
subprocess.call(['remove_alpha.sh', *PNG_FILE_LIST])
# os.system('remove_alpha.sh ')