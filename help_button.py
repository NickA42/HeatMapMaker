from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import os
from pathlib import Path
#from PIL import Image, ImageTk

root=tk.Tk()
##help_frame=tk.Frame(root)
root.title("Help Button demo")
root.geometry("1920x1080")

#frame set up
setup_frame = tk.Frame(root)
setup_frame.grid(row=0, column=0, sticky=tk.NSEW)
heatmap_frame = tk.Frame(root)

#fonts to use 
large_font = font.Font(family='Arial', size='25', weight='bold')
medium_font = font.Font(family='Arial', size='16')
small_font = font.Font(family='Arial', size='12')

#headers for each frame
setup_header = tk.Label(setup_frame, text='Setup Page', font=large_font)
setup_header.grid(row=0, column=0, sticky=tk.N)

heatmap_header = tk.Label(heatmap_frame, text='Heatmap Page', font=large_font)
heatmap_header.grid(row=0, column=0, sticky=tk.N)   

#next button function: place packs/grids in there
#and whatever you want to unpack/ungrid
def next_button():
    setup_frame.grid_forget()
    heatmap_frame.grid(row=0, column=0, sticky=tk.NSEW)

#next button
btn_next = tk.Button(setup_frame, text="Next", font=small_font, command=next_button)
btn_next.grid(row=1, column=0, sticky=tk.SE)

#back button function: place packs/grids in there
#and whatever you want to unpack/ungrid
def back_button():
    heatmap_frame.grid_forget()
    setup_frame.grid(row=0, column=0, sticky=tk.NSEW)

#back button
btn_back = tk.Button(heatmap_frame, text="Back", font=small_font, command = back_button)
btn_back.grid(row=1, column=0, sticky=tk.SW)

##################      GRAB STUFF DOWN HERE!!!!!!


def help_window():
    ##creates a window when help button is clicked 
    helpWindow=tk.Toplevel(setup_frame)
    helpWindow.geometry("1920x1080")
    #help frames set up
    help_page1= tk.Frame(helpWindow, height = '1080', width = '1920')
    help_page1.grid(row=0, column=0, sticky=tk.NSEW)
    help_page2 = tk.Frame(helpWindow, height = '1080', width = '1920')
    help_page3 = tk.Frame(helpWindow, height = '1080', width = '1920')
    help_page4 = tk.Frame(helpWindow, height = '1080', width = '1920')

    #first frame header 
    h_page1_header=tk.Label(help_page1, text='Step 1', font=large_font)
    h_page1_header.grid(row=0, column=0, sticky=tk.N)

    #first frame instructions
    h_page1_text=tk.Label(help_page1, text="First, click browse file as seen below.", font=medium_font)
    h_page1_text.grid(row=2, column=0, sticky=tk.N)
    #second frame header
    h_page2_header=tk.Label(help_page2, text='Step 2', font=large_font)
    h_page2_header.grid(row=0, column=0, sticky=tk.N)

    #second frame instructions
    h_page2_text=tk.Label(help_page2, text="Second, browse through your directory to the location of your intended file.", font=medium_font)
    h_page2_text.grid(row=2, column=0, sticky=tk.N)
    
    #third frame header
    h_page3_header=tk.Label(help_page3, text='Step 3', font=large_font)
    h_page3_header.grid(row=0, column=0, sticky=tk.N)

    #third frame instructions
    h_page3_text=tk.Label(help_page3, text="Third, choose your intended file and then select 'Open'.", font=medium_font)
    h_page3_text.grid(row=2, column=0, sticky=tk.N)
    
    #fourth frame header
    h_page4_header=tk.Label(help_page4, text='Step 4', font=large_font)
    h_page4_header.grid(row=0, column=0, sticky=tk.N)
    
    #fourth frame instructions
    h_page3_text=tk.Label(help_page4, text="Finally, once your file is selected, choose whether or not you want to include 0's into your calculation and then select 'Next' to continue.", font=medium_font)
    h_page3_text.grid(row=2, column=0, sticky=tk.N)
    
    #next buttons
    def next_button():
        help_page1.grid_forget()
        help_page2.grid(row=0, column=0, sticky=tk.NSEW)
        
        #image for page 2
        step2_path = Path('setup_page2.png').absolute()
        canvas2 = Canvas(help_page2, width=500, height=500)
        canvas2.grid(row=3, column=0, sticky=tk.NSEW)
        screenshot2 = PhotoImage(file=step2_path)  #python file is not in "folder" but "folder" is in your python file directory
        canvas2.create_image(250, 250, image=screenshot2)

    def next_button2():
        help_page2.grid_forget()
        help_page3.grid(row=0, column=0, sticky=tk.NSEW)
        
        #image for page 3
        step3_path = Path('setup_page3.png').absolute()
        canvas3 = Canvas(help_page3, width=500, height=500)
        canvas3.grid(row=3, column=0, sticky=tk.NSEW)
        screenshot3 = PhotoImage(file=step3_path)  #python file is not in "folder" but "folder" is in your python file directory
        canvas3.create_image(250, 250, image=screenshot3)

    def next_button3():
        help_page3.grid_forget()
        help_page4.grid(row=0, column=0, sticky=tk.NSEW)
        
        #image for page 4
        step4_path = Path('setup_page4.png').absolute()
        canvas4 = Canvas(help_page4, width=500, height=500)
        canvas4.grid(row=3, column=0, sticky=tk.NSEW)
        screenshot4 = PhotoImage(file=step4_path)  #python file is not in "folder" but "folder" is in your python file directory
        canvas4.create_image(250, 250, image=screenshot4)

    
    #next button for page 1
    btn_next1 = tk.Button(help_page1, text="Next", font=small_font, command=next_button)
    btn_next1.grid(row=4, column=4,sticky=tk.W)

    #next button for page 2
    btn_next2 = tk.Button(help_page2, text="Next", font=small_font, command=next_button2)
    btn_next2.grid(row=4, column=4,sticky=tk.W)

    #next button for page 3
    btn_next3 = tk.Button(help_page3, text="Next", font=small_font, command=next_button3)
    btn_next3.grid(row=4, column=4,sticky=tk.W)
    
    #back button for page 2 (function)
    def back_button():
        help_page2.grid_forget()
        help_page1.grid(row=0, column=0, sticky=tk.NSEW)

    #back button for page 3 (function)
    def back_button2():
        help_page3.grid_forget()
        help_page2.grid(row=0, column=0, sticky=tk.NSEW)

    #back button for page 4 (function)
    def back_button3():
        help_page4.grid_forget()
        help_page3.grid(row=0, column=0, sticky=tk.NSEW)

    #back button for page 2
    btn_back1 = tk.Button(help_page2, text="Back", font=small_font, command = back_button)
    btn_back1.grid(row=4, column=0, sticky=tk.E)

    #back button for page 3  
    btn_back2 = tk.Button(help_page3, text="Back", font=small_font, command = back_button2)
    btn_back2.grid(row=4, column=0,sticky=tk.E)

    #back button for page 4
    btn_back3 = tk.Button(help_page4, text="Back", font=small_font, command = back_button3)
    btn_back3.grid(row=4, column=0,sticky=tk.E)

    #exit button for page 4 (function)
    def exit_button():
        helpWindow.destroy()

     #exit button for page 4
    btn_exit = tk.Button(help_page4, text="Exit", font=small_font, command = exit_button)
    btn_exit.grid(row=4, column=4, sticky=tk.W)

    

##    #DOESNT WORK YET: finds image files and sets them to a variable for further use
##    def find_files(filename, search_path):
##        result = []
##
##        # Walking top-down from the root
##        for root, dir, files in os.walk(search_path):
##            if filename in files:
##               result.append(os.path.join(root, filename))
##        return result
##
##    print(find_files("setup_page1.png","D:"))

    #gets relative path and assigns it to the load image section
    

##    ##testing load image
##    directory_path = os.path.dirname('setup_page1.png')
##    file_path = os.path.join(directory_path, 'GUI testing/setup_page1.png')


##    curr_dir = os.getcwd()
##    abs_pathname = os.path.join(curr_dir, "setup_page1.png")
    #image for page 1

##    test_file = os.path.join(os.path.dirname(__file__), 'setup_page1.png')
##
##
    
    step1_path = Path('setup_page1.png').absolute()
    #abs_path = open(step1_path) #this line doesnt work. 
    print(step1_path)
    canvas1 = Canvas(help_page1, width=500, height=500)
    canvas1.grid(row=3, column=0, sticky=tk.NSEW)
    screenshot = PhotoImage(file = 'step1_path')  #python file is not in "folder" but "folder" is in your python file directory
    canvas1.create_image(250, 250, image=screenshot)

    
    

#creates help button for setup_page
help_btn=tk.Button(setup_frame, text="Help", font=small_font, command=help_window)
help_btn.grid(row=0, column=3, sticky=tk.NW)

###finds image files and sets them to a variable for further use
##def find_files(filename, search_path):
##   result = []
##
### Walking top-down from the root
##   for root, dir, files in os.walk(search_path):
##      if filename in files:
##         result.append(os.path.join(root, filename))
##   return result
##
##print(find_files("smpl.htm","D:"))


##def help_button2():
    ##create a small demo with screenshots and arrows of second page
    
#creates help button for heatmap_page
##help_btn(heatmap_frame, text="HELP", font=small_font, command=help_button2)
##help_btn.grid(row=1, column=0, sticky=tk.SE)

root.mainloop()
