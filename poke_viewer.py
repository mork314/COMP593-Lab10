from tkinter import ttk
from tkinter import *
import os
import inspect
import image_lib
from PIL import ImageTk, Image
import poke_api
import ctypes

root = Tk()

root.title('Pokemon Viewer')


script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
script_dir = os.path.dirname(script_path)

#Make default window image
    
win_image_data = image_lib.download_image(r'https://2.bp.blogspot.com/-nnriC7RO7dM/VOuR_46Eb_I/AAAAAAAAAVs/u5J-XjN79SY/s1600/Pokeball.png')

win_image_path = script_dir + '\window_default.jpg'

image_lib.save_image_file(win_image_data, win_image_path)

    #turns the image into a .ico photoimage thingy

ico = Image.open(win_image_path)

    #Sets the window icon

ico.save(win_image_path, format='ICO')

root.iconbitmap(False, win_image_path)

window_handle = ctypes.windll.user32.GetParent(root.winfo_id())

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Tkinter_id")

ctypes.windll.user32.SetClassLongW(window_handle, -14, ctypes.windll.shell32.Shell_GetCachedImageIndexW(win_image_path, 0, 0x00000000))

#Set up frames
frame = Frame(root)
frame.grid(column=0, row=0, padx = 10, pady = 10, sticky = "nsew")
frame.rowconfigure(0, weight = 100)
frame.columnconfigure(0, weight = 100)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(500, 600)


#Set default image

#Downloads the desired default image

image_data = image_lib.download_image(r'https://2.bp.blogspot.com/-nnriC7RO7dM/VOuR_46Eb_I/AAAAAAAAAVs/u5J-XjN79SY/s1600/Pokeball.png')

image_path = script_dir + '\default_img.jpg'

image_lib.save_image_file(image_data, image_path)

#Displays selected image

img_to_display = ImageTk.PhotoImage(file=win_image_path)

img_label = Label(frame, image = img_to_display)

img_label.grid(column = 0, row=0, padx = 10, pady = 10, sticky = "nsew")

#Create desktop button

def desk_button_click():
    image_lib.set_desktop_background_image(image_path)


desk_button = ttk.Button(frame, text = "Set as Desktop Image", command=desk_button_click)
desk_button.grid(row=2, column=0, padx = 10, pady = 10, sticky = "nsew")

#disable desktop button
desk_button.state(['disabled'])

#Make Combobox handler

poke_list = sorted(poke_api.fetch_all_names())

n = StringVar()

n.set('Choose a Pokemon')

choose_img = ttk.Combobox(frame, values = poke_list, textvariable = n, state='readonly')

choose_img.grid(column=0, row = 1, padx = 10, pady = 10, sticky = "nsew")

def handle_box_sel(event):
    
    desk_button.state(['!disabled'])
    
    selected_index = choose_img.current()
    
    poke_selected = poke_list[selected_index]
    
    global image_path

    image_path = poke_api.get_poke_image(poke_selected)

    img_to_display = ImageTk.PhotoImage(file=image_path)

    img_label.new_image = img_to_display

    img_label.configure(image=img_to_display)



choose_img.bind('<<ComboboxSelected>>', handle_box_sel)



root.mainloop()