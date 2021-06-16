from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font 

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
    helpWindow.geometry("500x500")
    #help frames set up
    help_page1= tk.Frame(helpWindow, height = '500', width = '500')
    help_page1.grid(row=0, column=0, sticky=tk.NSEW)
    help_page2 = tk.Frame(helpWindow, height = '500', width = '500')
    help_page3 = tk.Frame(helpWindow, height = '500', width = '500')
    #first frame header 
    h_page1_header=tk.Label(help_page1, text='Step 1', font=large_font)
    h_page1_header.grid(row=0, column=0, sticky=tk.N)
    #second frame header
    h_page2_header=tk.Label(help_page2, text='Step 2', font=large_font)
    h_page2_header.grid(row=0, column=0, sticky=tk.N)
    #third frame header
    h_page3_header=tk.Label(help_page3, text='Step 3', font=large_font)
    h_page3_header.grid(row=0, column=0, sticky=tk.N)

##    #instructions for frame 1
##    h_page1_instructions=tk.Text(help_page1, textvariable='', font=small_font)
##    h_page1_instructions.grid(row=1, column=0, sticky=tk.N)
##    #instructions for frame 2
##    h_page2_instructions=tk.Text(help_page2, textvariable='', font=small_font)
##    h_page2_instructions.grid(row=1, column=0, sticky=tk.N)
##    #instructions for frame 3
##    h_page3_instructions=tk.Text(help_page3, textvariable='', font=small_font)
##    h_page3_instructions.grid(row=1, column=0, sticky=tk.N)
    
    #next buttons
    def next_button():
        help_page1.grid_forget()
        help_page2.grid(row=0, column=0, sticky=tk.NSEW)

    def next_button2():
        help_page2.grid_forget()
        help_page3.grid(row=0, column=0, sticky=tk.NSEW)
    
    #next button for first page
    btn_next1 = tk.Button(help_page1, text="Next", font=small_font, command=next_button)
    btn_next1.grid(row=3, column=4,sticky=tk.W)

    #next button for second page
    btn_next2 = tk.Button(help_page2, text="Next", font=small_font, command=next_button2)
    btn_next2.grid(row=3, column=4,sticky=tk.W)
    
    #back buttons
    def back_button():
        help_page2.grid_forget()
        help_page1.grid(row=0, column=0, sticky=tk.NSEW)

    def back_button2():
        help_page3.grid_forget()
        help_page2.grid(row=0, column=0, sticky=tk.NSEW)

    #back button for first page 
    btn_back1 = tk.Button(help_page2, text="Back", font=small_font, command = back_button)
    btn_back1.grid(row=3, column=0, sticky=tk.E)

    #back button for second page 
    btn_back2 = tk.Button(help_page3, text="Back", font=small_font, command = back_button2)
    btn_back2.grid(row=3, column=0,sticky=tk.E)

#creates help button for setup_page
help_btn=tk.Button(setup_frame, text="HELP", font=small_font, command=help_window)
help_btn.grid(row=0, column=3, sticky=tk.NW)

##def help_button2():
    ##create a small demo with screenshots and arrows of second page
    
#creates help button for heatmap_page
##help_btn(heatmap_frame, text="HELP", font=small_font, command=help_button2)
##help_btn.grid(row=1, column=0, sticky=tk.SE)

root.mainloop()
