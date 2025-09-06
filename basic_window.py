from tkinter import * #importing everything from tkinter
from PIL import Image, ImageTk #for images
import requests

gui = Tk() #our base

#kintone app info
DOMAIN = "yqozl5nyoqxf.kintone.com"
API_TOKEN = "3cQQP4Wy2XZ2Zj8UUkaUUqf3GnmwpxPnycDhfiio"
APP_ID = "2"


numpel = IntVar(value=0) #for button incrementation, default value = 0
def remove_pellet():
    global numpel
    numpel.set(numpel.get()-1) #removing one
    if numpel.get() <= 0: #have to get the number since you're getting int
        numpel.set(value=0)

def add_pellet():
    global numpel
    numpel.set(numpel.get()+1) #adding one


status_label = Label(gui, text="")
status_label.grid(row=4, column=2)

def submit_to_kintone():
    pellets = numpel.get()

    url = f"https://{DOMAIN}/k/v1/record.json" 
    
    headers = {
        "X-Cybozu-API-Token": API_TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "app": APP_ID,
        "record": {
            "Number": {"value": pellets}
        }
    }


    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        status_label.config(text="Successfully sent to Kintone", fg="green")
    except Exception as e:
        status_label.config(text=f"Failed: {e}", fg="red")
        print(e)





gui.title("AquaSitter")
gui.geometry("420x350")#wxh
Label(gui, text="").grid(row=1, column=2)
label = Label(gui, text="Welcome to AquaSitter! Add/remove the number of pellets below.")
label.grid(row=0,column=2)

img = Image.open("IMG_3347.jpg")

#resize of screen
max_width = 200
max_height = 150
img.thumbnail((max_width, max_height))

#image of betta!
img = ImageTk.PhotoImage(img)
display = Label(image=img)
display.grid(row=2, column=2)





#pellet button to add num of pellets
btn_add = Button(gui, text="+", command=add_pellet)
btn_add.place(x=260, y=220)

#remove button pellets
btn_remove = Button(gui, text="-", command=remove_pellet)
btn_remove.place(x=100, y=220)

#submit buton
btn_submit = Button(gui, text="Submit", command=submit_to_kintone)
btn_submit.place(x=160, y=250)

#label for number of pellets
count_label = Label(gui, textvariable=numpel)
count_label.place(x=190, y=220)

gui.mainloop()

