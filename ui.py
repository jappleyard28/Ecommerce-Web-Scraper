from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from operator import itemgetter
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
    exit()

def search(search_value, sort_value):
    # get inputs to scrape
    # check what value has been inputted into the entry box
    # use that input to create the url to be passed into the scraper
    # start scraper function

    print("search_value: " + search_value)
    print("sort_value: " + sort_value)
    scraper1 = Scraper(url1 + search_value + url2) # concatenate strings to include search value
    data_list = scraper1.return_data()
    create_table(data_list, sort_value)

#data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list', 'Portal': 10000}, {'Geeks':10, 'For': 20, 'geeks': 30}]

def create_table(data_list, sort_value):
    # define columns
    columns = ('title', 'price', 'time_left', 'bids', 'link')

    tree = ttk.Treeview(frame_bottom, columns=columns, show='headings')

    # delete previous records
    for item in tree.get_children():
        tree.delete(item)

    # define headings
    tree.heading('title', text='Product Title')
    tree.heading('price', text='Price')
    tree.heading('time_left', text='Time Left')
    tree.heading('bids', text='Bids')
    tree.heading('link', text='Link')

    # generate sample data
    # soup[0] - DICT
    # soup - LIST
    
    # sort list
    sort_code = ""
    reverse_sort = False
    if (sort_value == "Default"):
        sort_code = "title"
    elif (sort_value == "Price: Low to high"):
        sort_code = "price"
    elif (sort_value == "Price: High to low"):
        sort_code = "price"
        reverse_sort = True
    elif (sort_value == "Time left"):
        sort_code = "time_left"
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
    window.state("zoomed") # makes full screen with title bar and taskbar
    window.title("Ecommerce-Web-Scraper")
    window.grid_columnconfigure(0, weight=1)
    # window.configure(background='purple')

    # creating grid for gui
    frame_header = Frame(window, borderwidth=2, pady=100, highlightthickness=2)
    frame_header.grid_columnconfigure(0, weight=1)
    # frame_header.configure(background='purple')
    
    frame_centre = Frame(window, borderwidth=2, pady=20)
    # frame_centre.configure(background='blue')

    frame_bottom = Frame(window, borderwidth=2, pady=50)
    # frame_bottom.configure(background='green')

    frame_header.grid(row=0, column=0, sticky="nsew") # sticky="nsew" makes it fill frame horizontally
    frame_centre.grid(row=1, column=0, sticky="nsew")
    frame_bottom.grid(row=2, column=0, sticky="nsew")

    header = Label(frame_header, text="Ecommerce Web Scraper", bg='grey', fg='black', font=("Helvetica 16 bold"))
    header.grid(row=0, column=0, columnspan=10)

    frame_main_1 = Frame(frame_centre, borderwidth=2, relief='sunken')
    frame_main_2 = Frame(frame_centre, borderwidth=2, relief='raised')

    search_product = Label(frame_main_1, text="Search product: ")
    
    # search entry box
    search_product_entry = Entry(frame_main_1, width=40) # width=40 changes the width of the entry box

    # sort by
    sort_by_list = ('Default', 'Price: Low to high', 'Price: High to low', 'Time left')
    sort_variable = StringVar(frame_main_1)
    sort_variable.set("Select an Option")
    question_menu = OptionMenu(frame_main_1, sort_variable, *sort_by_list)

    # search button with search value and sort by value inputted as arguments
    search_button = Button(frame_main_1, text="Search", command=lambda: search(str(search_product_entry.get()), str(sort_variable.get())), bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold')) # command=search_products - search_products is function

    # close button
    close_button = Button(frame_main_1, text="Close", command=close_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold')) # command=search_products - search_products is function

    # data = [{'title': 'car 1', 'price': '1', 'time_left': 'time 1', 'bids': "1", 'link': 'link test 1'}, {'title': 'car 2', 'price': '2', 'time_left': 'time 2', 'bids': "2", 'link': 'link test 2'}] 
    data = []
    create_table(data, "default")


    # adding widgets to the grid
    frame_main_1.pack(fill='x', pady=2)
    frame_main_2.pack(fill='x', pady=2)
    search_product.pack(side='left')
    search_product_entry.pack(side='left', padx=1)
    question_menu.pack(side='left', padx=1)
    search_button.pack(side='left', padx=1)
    close_button.pack(side='left', padx=1)

    window.mainloop()