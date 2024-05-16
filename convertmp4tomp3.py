#------------------------------------------------------------
# 2021/12/12 created by issarak 
# This program will convert file type ,mp4/mkv/.mov to mp3
#
# 2021/12/14 Added
#   f = open("unique_filename.txt", "w") -104-106 
#   f.write("file contents....") -function main
#   f.close() -140
#   Modified:
#       change function name from text--> text_msg line 90
#       and addone more parameter called status ("GOOD", "BAD")
#       add if/else statements
# 2021/12/15 load testing and final review
#-------------------------------------------------------------
#import
import os 
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
from tkinter.font import Font
import sys

#variable
#setting the max length of the file name 
Max_File_len = 20

window = Tk()
window.title("MP4 to MP3")
window.geometry("800x500")
window.configure(bg="#0000FF")

#def Platform
def platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def which_slash():
    if platform() == "Windows":
        slash_is = "\\"
    else:
        slash_is = "/"
    return slash_is

#file and uniquw name 

#This is the function create to convert file_type mp4 to mp3
def converting_Mp4(src_File, mp3_File):
    cmd = "ffmpeg -i {} -vn {}".format(src_File, mp3_File)
    os.system(cmd) 

#this is the function create to convert file_type mkv to mp3
def converting_Mkv(src_File, mp3_File):
    cmd = "ffmpeg -i {} -vn -ar 44100 -ac 2 -ab 128k -f mp3 {}".format(src_File, mp3_File)
    os.system(cmd) 

#this is the function create to convert file_type mov to mp3
def converting_Mov(src_File, mp3_File):
    cmd = "ffmpeg -i {} -map 0:a {}".format(src_File, mp3_File)
    os.system(cmd) 

#unique name and dir for mp3
def get_unique_name() :
    import time
    return time.strftime("%Y%m%d-%H%M%S")


def create_directory_for_mp3(source_location, dir_name):
    mp3_directory_name = source_location + which_slash() + dir_name
    os.mkdir(mp3_directory_name)
    return mp3_directory_name

#to check and control filename
def assignfile(each_file, get_file, mp3_location):
    if len(each_file) >= Max_File_len:
        mp3_File = each_file[:Max_File_len] + ".mp3"
    else:
        mp3_File = each_file[:len(each_file)-4] + ".mp3"
        
    src_File = '"' + get_file + which_slash() +  each_file + '"'
    mp3_File = '"' + mp3_location + which_slash() + mp3_File + '"'
    return src_File, mp3_File


#
#just a text that tells us that the file is done converting 
def text_msg(each_file, mp3_location, status): #get_folder_dir):
    text_box = tk.Text(window,height="1", width="50")
    text_box.config(state="normal")
    if status == 'GOOD' :
        text_box.insert(tk.INSERT,  "{} is Done. The file location is in {}".format(each_file, mp3_location))
    else:
        text_box.insert(tk.INSERT,  "      {} This file type cannot be converted".format(each_file))
    text_box.config(state="disabled")
    text_box.pack()


#main program
def main():
    get_file = filedialog.askdirectory()
    unique_name = get_unique_name()
    mp3_location = create_directory_for_mp3(get_file, unique_name)
    
    #ask user to select folder
    read_file = os.listdir(get_file)

    for each_file in read_file:

        #convert mp4 to mp3
        if each_file.endswith(".mp4") or each_file.endswith(".MP4"):
            src_File, mp3_File = assignfile(each_file, get_file, mp3_location)
            converting_Mp4(src_File, mp3_File)    
            text_msg(each_file, mp3_location , "GOOD")
            
        # convert mkv to mp3
        elif each_file.endswith(".mkv") or each_file.endswith(".MKV"):
            src_File, mp3_File = assignfile(each_file, get_file, mp3_location)
            converting_Mkv(src_File, mp3_File)        
            text_msg(each_file, mp3_location , "GOOD")
            
        # convert mov to mp3
        elif each_file.endswith(".mov") or each_file.endswith(".MOV"):
            src_File, mp3_File = assignfile(each_file, get_file, mp3_location)
            converting_Mov(src_File, mp3_File)    
            text_msg(each_file, mp3_location, "GOOD")

            
        # file type that is not mp4,mkv,mov will not be converted
        else:
            text_msg(each_file, mp3_location, "BAD")
            
 
#label
#design
#
my_font = Font(
    family="Helvetica",
    size=30,

)
my_font1 = Font(
    family="helvetica",
    size="12"
)
#
#title
title = Label(window, text ="Convert file To MP3", font = my_font)
title.pack(pady=20)
#button
button1 = tk.Button(window, text="open MP4 folder", font = my_font1)
button1.config(command=main)
button1.pack(pady=10)
#end
window.mainloop()