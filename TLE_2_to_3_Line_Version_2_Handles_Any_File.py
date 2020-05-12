import os
import pprint
import Tkinter
import time
import Tkinter, Tkconstants, tkFileDialog
from Tkinter import Tk
import tkMessageBox
import tkSimpleDialog
from datetime import datetime
import subprocess
import sys

now = datetime.now()
now_correct = now.strftime("%Y_%m_%d_%H_%M_%S")

root = Tk()
root.wm_attributes('-topmost', 1)


#####
result = tkMessageBox.askyesno("Python","Hello, welcome to the 2 Line Element Set to 3 Line Element set program developed by Joshua Vaughan, TSOC Instructor \
\n\nThis Program is meant to convert the two line element sets from ISSA into 3 line element sets including a satellite name. \
\nBy using this program it will append the name onto the up to date information from ISSA so you can more easily import satellites into STK \
\nWithout needing to airgap new 3 line element sets from the UNCLASSIFIED internet very often, so if you need to use STK in an austere or secured environment \
\nthis program will make that much easier than it has been in the past. \
\n\nYou will need to have several things in order to proceed. \n\nYou will need: \nA current 3 Line Element set from Celestrak.com or Space-Track.org \
\nA newly updated ISSA 2 Line Element set saved as a .txt file. To get that you will need to open the Current.ELM file \
That is downloaded in the ISSA database and save it as a .txt file.  \nYou need to have both of these files and be able to \
Navigate to them in your harddrive.  \n\nIf at any time the program is not working as expected please press ctrl+c and that will \
Keyboard Interrupt the program killing it. \n\nDo you understand and have all the needed files?")

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, Please get the requisite files and run this program again. Thank You.")
    os._exit(0)

result = tkMessageBox.askyesno("File Directory",'You will now select where you want your new TLE file to be saved. \
\nWhen you click "Yes" a box will pop up and you will use that to select where you want your new TLE file to be saved. \
\nIf you do not understand click "No" and the program will be terminated.')

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, Please get the requisite understanding of file directory selection and run this program again. Thank You.")
    os._exit(0)


directory = tkFileDialog.askdirectory()

os.chdir(directory)

result = tkMessageBox.askyesno("2 Line Element Set Selection",'You will now select your 2 Line Element Set TLE from ISSA.  You will need to take the current.ELM file in the ISSA database and make a copy and save \
\nthat copy as a .txt for you to be able to select it for use in this program.  Once you have that new .txt file from ISSA you can proceed with the selection. \
\n\nDO YOU UNDERSTAND and have your 2 line element set saved and ready for use?')

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, Please get the requisite two line element set and run this program again. Thank You.")
    os._exit(0)

two_line_file = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

result = tkMessageBox.askyesno("3 Line Element Set Selection",'You will now select your 3 line element set from either Celestrak.com or Space-Track.org. \
\nPlease note that the orbital characteristics will be pulled from the 2 line element set.  Thus you will only need to airgap an UNCLASSIFIED full 3 line element set \
\nevery once in a while, really only to account for new space launches occuring over time. \
\nDo you understand and have the needed 3 line element set from Celestrak.com or Space-Track.org?')

if result == True:
    pass
else:
    tkMessageBox.showinfo ("Program Aborted","You have chosen No, Please get the requisite three line element set and run this program again. Thank You.")
    os._exit(0)


three_line_file = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))

answer1 = tkSimpleDialog.askstring('New TLE File Name', '''Please Enter the name for your new and exciting TLE file, if you leave it empty an automatically chosen name will be generated.\n
Do not enter in the file extension Example: ".txt" or the program will break, simply enter in the name of the file you would prefer.''')

if answer1 != '':
    pass
else:
    answer1 = 'new_three_line_TLE' + str(now_correct)

write_file = open(str(answer1) + '.txt', 'a')






###

two_list = []
two_list_second = []
three_list_names = []
three_list_firstline = []
two_list_index = []

with open(two_line_file, 'r+') as h:
    two_line = h.readlines()

with open(three_line_file, 'r+') as g:
    three_line = g.readlines()

for item in two_line[::2]:
    two_list.append(item)

for item in two_line[1::2]:
    two_list_second.append(item)

for item in two_list:
    two_list_index.append(item[2:7])

for item in three_line[::3]:
    three_list_names.append(item)

for item in three_line[1::3]:
    three_list_firstline.append(item)

three_line_index = []

for item in three_list_firstline:
    three_line_index.append(item[2:7])

two_line_search_index = []
three_line_search_index = []

#pprint.pprint(two_line[::2][0:30])



for item in two_list_index:
    if item in three_line_index:
        two_line_search_index.append(two_list_index.index(item))



for item in three_line_index:
    if item in two_list_index:
        three_line_search_index.append(three_line_index.index(item))
title_list = []
first_line_list = []
second_line_list = []



for i in three_line_search_index:
    title_list.append(three_list_names[i])

for i in two_line_search_index:
    first_line_list.append(two_list[i])
    second_line_list.append(two_list_second[i])

final_write_list = []

for n in range(0, len(three_line_search_index)):
    final_write_list.append(title_list[n])
    final_write_list.append(first_line_list[n])
    final_write_list.append(second_line_list[n])

for s in final_write_list:
    write_file.write(s)



write_file.close()

root.destroy()

tkMessageBox.showinfo("Program Completed",'''The program is now complete.  If you are seeing this message that means it all went well
and there will be a new 3 line element set sitting in the directory you chose at the beginning of this program.
The directory you chose was: \n\n''' + directory + '''\n\nPlease look there for your brand new and crispy TLE file.  
Please click ok to close this program.''')

os._exit(0)


###






