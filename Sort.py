# Python Project to move files from the Download Folder to Drive D


#task1 : 
# to sort files into executeable, compressed,audio, videos, and others folders


#task 2:
#to move the files from Download directory to E:/ directory

import os
import shutil
from os import listdir
from os.path import isfile,join
from Tkinter import *
pathToExtract = "C:\\Users\\keshav-2\\Downloads"
pathToDrop = 'D:\\'


applications = ['executeable']
audio = ['audio']
compressed = ['compressed']
videos = ['videos']
textual = ['texts']
others = ['others']

files = [f for f in listdir(pathToExtract) if isfile(join(pathToExtract,f))]
for i in xrange(len(files)):
	files2 = files[i].split('.')
	if(files2[-1] == "exe"):
		applications.append(join(pathToExtract,files[i]))

	elif(files2[-1] == 'txt'):
		textual.append(join(pathToExtract,files[i]))

	elif(files2[-1] == 'mp3'):
		audio.append(join(pathToExtract,files[i]))

	elif(files2[-1] == 'zip'):
		compressed.append(join(pathToExtract,files[i]))
	
	elif(files2[-1] == 'mp4' or files2[-1] == 'flv' or files2[-1] == 'mkv' or  files2[-1] == 'wmv' or files2[-1] == 'mpg') :
		videos.append(join(pathToExtract,files[i]))
	
	else:
		others.append(join(pathToExtract,files[i]))



def create_dir(directory):
	if not os.path.exists(directory):
		print 'Creating the directory ', directory
		os.makedirs(directory)


def move_files(type,pathToDrop):

	for i in xrange(1,len(type)):
		
		shutil.move(type[i],pathToDrop)

def begin(type,pathToDrop):

	if (len(type) > 1):
		path_this = join(pathToDrop,type[0]) 
		create_dir(path_this)
		move_files(type,path_this)



begin(applications, pathToDrop)
begin(audio, pathToDrop)
begin(videos, pathToDrop)
begin(textual, pathToDrop)
begin(others, pathToDrop)

root = Tk()
root.title('Task done!')
moved = str(len(applications) + len(videos) + len(audio) + len(textual) + len(others) - 5)
text = "Number of files moved : " +  moved

label1 = Label(root, text = text)
label1.pack()

frame = Frame(root)
frame.pack()

quitbutton = Button(frame, text = "OK", command = frame.quit)
quitbutton.pack()

root.mainloop()