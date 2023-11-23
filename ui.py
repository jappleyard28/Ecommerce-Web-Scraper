from tkinter import *
from scraper import Scraper

# constants
BG_GRAY = "lightgray"
BG_COLOR = "white"
TEXT_COLOR = "black"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
url1 = "https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw="
url2 = "&_sacat=0&rt=nc&LH_Auction=1"

def close_app():
    window.destroy()

def search():
    # get inputs to scrape
    # check what value has been inputted into the entry box
    # use that input to create the url to be passed into the scraper
    # start scraper function
    search_product1 = str(search_product_entry.get()) # perfume
    print("search: " + search_product1)
    scraper1 = Scraper(url1 + search_product1 + url2) # concatenate strings to include search value
    scraper1.run()


window = Tk()
window.state("zoomed") # makes full screen with title bar and taskbar
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

frame_main_1 = Frame(frame_centre, borderwidth=2, relief='sunken')
frame_main_2 = Frame(frame_centre, borderwidth=2, relief='raised')

search_product = Label(frame_main_1, text="Search product: ")
# NEED TO ADD SEND BUTTON
search_product1 = StringVar() # ??
search_product_entry = Entry(frame_main_1, textvariable = search_product1, width=40) # width=40 changes the width of the entry box
search_button = Button(frame_main_1, text="Search", command=search, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold')) # command=search_products - search_products is function


#adding send button
close_button = Button(frame_bottom, text="Close", command=close_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold')) # command=search_products - search_products is function
close_button.grid(column=0, row=0, sticky='w', padx=100, pady=2)
# adding widgets to the grid
frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x', pady=2)
search_product.pack(side='left')
search_product_entry.pack(side='left', padx=1)
search_button.pack(side='left', padx=1)


window.configure(width=500, height=750, bg=BG_COLOR) # window.geometry("500x750")


# all widgets will be here
# Execute Tkinter
window.mainloop()