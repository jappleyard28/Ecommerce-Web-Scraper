from tkinter import *

# constants
BG_GRAY = "lightgray"
BG_COLOR = "white"
TEXT_COLOR = "black"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

window = Tk()
# window.state("zoomed") # makes full screen with title bar and taskbar
window.title("Ecommerce-Web-Scraper")

# creating grid for gui
frame_header = Frame(window, borderwidth=2, pady=2)
frame_centre = Frame(window, borderwidth=2, pady=5)
frame_bottom = Frame(window, borderwidth=2, pady=5)

frame_header.grid(row=0, column=0)
frame_centre.grid(row=1, column=0)
frame_bottom.grid(row=2, column=0)

header = Label(frame_header, text="Ecommerce Web Scraper", bg='grey', fg='black', height='3', width='50', font=("Helvetica 16 bold"))
header.grid(row=0, column=0)


window.configure(width=500, height=750, bg=BG_COLOR) # window.geometry("500x750")


# all widgets will be here
# Execute Tkinter
window.mainloop()