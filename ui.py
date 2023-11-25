from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from operator import itemgetter
import webbrowser
from scraper import Scraper

# constants
BG_COLOR = "skyblue"
FONT = "Helvetica 12"
url1 = "https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw="
url2 = "&_sacat=0&rt=nc&LH_Auction=1"

def close_app():
    exit()

def open_link(url):
    webbrowser.open_new(r"https://www.google.co.uk")
    
def search(search_value, sort_value):
    # get inputs to scrape
    # check what value has been inputted into the entry box
    # use that input to create the url to be passed into the scraper
    # start scraper function

    scraper1 = Scraper(url1 + search_value + url2) # concatenate strings to include search value
    data_list = scraper1.return_data()
    create_table(data_list, sort_value)

def create_table(data_list, sort_value):
    # define columns
    columns = ('title', 'price', 'time_left', 'bids', 'link')

    tree = ttk.Treeview(frame_bottom, columns=columns, show='headings')
    
    tree.column("# 1",anchor=CENTER, stretch=YES)
    tree.heading("# 1", text="Product Title")

    tree.column("# 2", anchor=CENTER, stretch=YES)
    tree.heading("# 2", text="Price")

    tree.column("# 3", anchor=CENTER, stretch=YES)
    tree.heading("# 3", text="Time Left")

    tree.column("# 4", anchor=CENTER, stretch=YES)
    tree.heading("# 4", text="Bids")

    tree.column("# 5", anchor=CENTER, stretch=YES)
    tree.heading("# 5", text="Link")

    style = ttk.Style(frame_bottom)
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=(None, 15), background="blueviolet", foreground="white")

    # generate sample data
    # soup[0] - DICT
    # soup - LIST
    
    # sort list
    sort_code = ""
    reverse_sort = False
    if (sort_value.lower() == "default"):
        sort_code = "title"
    elif (sort_value.lower() == "price: low to high"):
        sort_code = "price"
    elif (sort_value.lower() == "price: high to low"):
        sort_code = "price"
        reverse_sort = True
    elif (sort_value.lower() == "bids: low to high"):
        sort_code = "bids"
    elif (sort_value.lower() == "bids: high to low"):
        sort_code = "bids"
        reverse_sort = True
    else:
        sort_code = "title"
    
    products = sorted(data_list, key=itemgetter(sort_code), reverse=reverse_sort)

    sorted_products = []
    for i in range(len(data_list)):
        sorted_products.append((products[i].get('title'), "£" + str(products[i].get('price')), products[i].get('time_left'), products[i].get('bids'), products[i].get('link')))

    # add data to the treeview
    for product in sorted_products:
        tree.insert('', END, values=product)

    tree.grid(row=0, column=0, sticky='nsew') # adds table to the grid

    # add a scrollbar
    scrollbar = ttk.Scrollbar(frame_bottom, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # ---------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    window = Tk()
    # window.state("zoomed") # makes full screen with title bar and taskbar
    window.title("Ecommerce-Web-Scraper")
    window.grid_columnconfigure(0, weight=1)
    window.configure(background=BG_COLOR)

    # creating grid for gui
    frame_header = Frame(window, borderwidth=2, pady=50, highlightthickness=2)
    frame_header.grid_columnconfigure(0, weight=1)
    
    frame_centre = Frame(window, borderwidth=2, pady=20)
    frame_centre.grid_columnconfigure(0, weight=1)
    frame_centre.configure(background=BG_COLOR)

    frame_bottom = Frame(window, borderwidth=2, pady=50)
    frame_bottom.grid_columnconfigure(0, weight=1)
    frame_bottom.configure(background=BG_COLOR)

    frame_header.grid(row=0, column=0, sticky="nsew") # sticky="nsew" makes it fill frame horizontally
    frame_centre.grid(row=1, column=0, sticky="nsew")
    frame_bottom.grid(row=2, column=0, sticky="nsew")

    # header frame
    header = Label(frame_header, text="Ecommerce Web Scraper", fg='black', font=("Helvetica 28 bold"))
    header.grid(row=0, column=0, columnspan=10)

    # main frame
    frame_main = Frame(frame_centre, borderwidth=2, relief='sunken')
    search_product = Label(frame_main, text="Search product: ", font=(FONT))
    
    # search entry box
    search_product_entry = Entry(frame_main, width=50, font=(FONT)) # width=40 changes the width of the entry box

    # sort by
    sort_by_list = ('Default', 'Price: Low to high', 'Price: High to low', 'Bids: Low to high', 'Bids: High to low')
    sort_variable = StringVar(frame_main)
    sort_variable.set("Sort by")
    question_menu = OptionMenu(frame_main, sort_variable, *sort_by_list)
    question_menu.config(font = ("Helvetica 10"), width=14)

    # search button with search value and sort by value inputted as arguments
    search_button = Button(frame_main, text="Search", command=lambda: search(str(search_product_entry.get()), str(sort_variable.get())), bg='dark green', fg='white', width=10, font=(FONT))

    # close button
    close_button = Button(frame_main, text="Close", command=close_app, bg='dark green', fg='white', width=10, font=(FONT))

    # bottom frame
    data = []
    create_table(data, "default")


    # adding widgets to the grid
    frame_main.pack(pady=2)
    search_product.pack(side='left')
    search_product_entry.pack(side='left', padx=10)
    question_menu.pack(side='left', padx=1)
    search_button.pack(side='left', padx=1)
    close_button.pack(side='left', padx=1)

    window.mainloop()