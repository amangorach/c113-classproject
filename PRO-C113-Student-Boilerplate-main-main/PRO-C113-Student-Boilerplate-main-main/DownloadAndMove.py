import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#variables
from_dir = "C:/Users/rahil/Downloads"
to_dir = "C:/Users/rahil/Documents/Downloaded_Files"
#the dict
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
# Event Hanlder Class
class FileMovementHandler(FileSystemEventHandler):
    #Student Activity1

    

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extention = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if extention in value:
                fileName = os.path.basename(event.src_path)
                print('downloaded' + fileName)
                path1 = from_dir + '/' + fileName
                path2 = to_dir + '/' + 'Downloaded_Files'
                path3 = to_dir + '/' + 'Downloaded_Files' + '/' + fileName
                if os.path.exists(path2):
                    print('directory exists')
                    print('moving' + fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print('making directory ')
                    os.makedirs(path2)
                    print('moving' + fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

#Student Activity2
try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print('stoped')
    observer.stop