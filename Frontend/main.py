"""CSC110 Fall 2021 Final Project: Main File
===========================================================
This Python module holds all the functions that are required to run the program. This file also
contains code to run the tkinter window and its matplotlib interactive graphs.
"""

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from BackEnd import read_data, country_data

#############################################################
# constant variables
#############################################################

GOV_POLICIES = ["Cancellation of Public Events",
                "Public Gathering Rules",
                "Face Coverings",
                "Debt Relief",
                "Income Support",
                "Internal Movement",
                "International Travel",
                "Public Transport",
                "Public Campaigns",
                "School Closures",
                "Workplace Closures",
                "Stay At Home Restrictions",
                "Containment and Health Index",
                "Stringency Index",
                "Testing Policy",
                "Contact Tracing"]

SURVIVABILITY = ["Total Cases",
                 "Total Deaths",
                 "Total Testing",
                 "Total Vaccinations",
                 "New Cases",
                 "New Deaths",
                 "New Testing",
                 "New Vaccinations"]


####################################################################################################
# Functions used in code
####################################################################################################


def update(data: list) -> None:
    """ Updates the list box so it returns to default where all countries are listed
    Preconditions:
      - len(data) != 0
    """
    listbox.delete(0, 'end')

    # put new data
    for item in data:
        listbox.insert('end', item)


def check(event: tk.EventType) -> None:
    """ Updates the list box everytime the user searches for a country
    """
    val = event.widget.get()

    if val == '':
        data = country_list
    else:
        data = []
        for item in country_list:
            if val.lower() in item.lower():
                data.append(item)

    update(data)


def select() -> None:
    """ Adds the country to the set to display the country
    """
    for i in listbox.curselection():
        if listbox.get(i) in current_selection:
            continue
        else:
            current_selection.append(listbox.get(i))

    selected.config(text=("\n".join(current_selection)))


def split_string(words: str) -> str:
    """ Splits the variable name into a better formatted string
    Preconditions:
      - "_" in word and 0 < index("_") < len(word)

    >>> split_string("hello_world")
    'Hello World'

    """

    lst = words.split("_")
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    return " ".join(lst)


def delete() -> None:
    """ Deletes the country from the set of displayed countries
    """

    for i in listbox.curselection():
        if listbox.get(i) in current_selection:
            current_selection.remove(listbox.get(i))
    selected.config(text=("\n".join(current_selection)))


def clear() -> None:
    """Clears the currently selected countries from currently selected country list"""
    global current_selection
    current_selection = []
    listbox.selection_clear(0, tk.END)
    selected.config(text=("\n".join(current_selection)))


def store_category(e) -> None:
    """ Stores the category that the user selected from the tkinter widget"""
    global category
    category = menu_category.get()

    lst = category.split(" ")
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    category = "_".join(lst)


def store_policy(e) -> None:
    """ Stores the policy that the user selected from the tkinter widget"""
    global policy
    policy = menu_policy.get()

    lst = policy.split(" ")
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
    policy = "_".join(lst)


def graph(country_dct: dict) -> None:
    """ Graphs the data when user clicks the 'graph' button
    Preconditions:
      - len(country_dct) != 0
    """
    global policy
    global category

    # Lists used to store values
    policy_list = []
    category_list = []
    time_category_list = []
    time_policy_list = []
    index_policy_list = []
    survivability_category_list = []

    # Finds all selected countries and obtains the policy and category for each country
    for country in current_selection:
        obj_country = get_country(country, country_dct)
        policy_list.append(getattr(obj_country, policy).time_to_index)
        category_list.append(getattr(obj_country, category).time_to_index)

    # Separates the category list into a list of lists
    for i in category_list:
        time_category_list.append([day[0] for day in i if day[0][8:10] == '01'
                                   or day[0][8:10] == '07' or day[0][8:10] == '14'
                                   or day[0][8:10] == '23'])
        survivability_category_list.append([day[1] for day in i if day[0][8:10] == '01'
                                            or day[0][8:10] == '07' or day[0][8:10] == '14'
                                            or day[0][8:10] == '23'])

    # Separates the policy list into a list of lists
    for i in policy_list:
        time_policy_list.append([day[0] for day in i if day[0][8:10] == '01' or day[0][8:10] == '07'
                                 or day[0][8:10] == '14' or day[0][8:10] == '23'])
        index_policy_list.append([day[1] for day in i if day[0][8:10] == '01'
                                  or day[0][8:10] == '07' or day[0][8:10] == '14'
                                  or day[0][8:10] == '23'])

    # Creates a figure to plot
    fig = plt.figure(figsize=(screen_width * px * 2 / 3, screen_height * px * 8 / 9))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    # Plots the graphs onto the figure
    for i in range(len(current_selection)):
        ax1.plot(time_category_list[i], survivability_category_list[i], label=current_selection[i])
    for i in range(len(current_selection)):
        ax2.plot(time_policy_list[i], index_policy_list[i], label=current_selection[i])

    # set titles and legends
    ax1.set_title(f"{split_string(category)} as a Function of Time", fontsize=15)
    ax1.legend(loc='upper left')
    ax2.set_title(f"{split_string(policy)} as a Function of Time", fontsize=15)
    ax2.legend(loc='upper left')

    # rotate x ticks
    for tick1 in ax1.get_xticklabels():
        tick1.set_rotation(90)
    for tick2 in ax2.get_xticklabels():
        tick2.set_rotation(90)

    # for ax1 #########################
    # unclutter x ticks
    every_nth = 2
    for n, label in enumerate(ax1.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)

    # for ax2 #########################
    # unclutter x ticks
    every_nth = 2
    for n, label in enumerate(ax2.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    plt.close(fig)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=0, column=0)


def get_country(curr_country: str, countries: dict) -> country_data.Country:
    """ Returns the country as an object
    Preconditions:
      - curr_country != ''
      - len(countries) != 0
    """
    # for country in countries:
    #     # if countries[country].name == curr_country:
    #     #     return countries[country]
    return countries[curr_country]


if __name__ == '__main__':
    current_selection = []  # This is a list containing the country that user selects
    category = ""  # This is the category the user wants to view
    policy = ""  # This is the policy the user wants to view
    country_list = []
    country_dict = read_data.load_files()
    for c in country_dict:
        country_list.append(c)
    ################################################################################################
    # Making the Window
    ################################################################################################
    root = tk.Tk()
    root.title("Graphing COVID DATA")
    root.resizable(tk.FALSE, tk.FALSE)
    px = 1 / plt.rcParams['figure.dpi']
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(str(screen_width) + 'x' + str(int(screen_height * 9 / 10)))
    # Create Frames
    drop_down_frame = tk.Frame(root)
    scroll_frame = tk.Frame(root)  # This creates frame to hold the scroll bar

    # Creates a Listbox with a scrollbar attached
    scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL)  # This creates the scroll bar
    entry = tk.Entry(scroll_frame, font="Times 10")
    entry.bind('<KeyRelease>', check)
    listHeight = int((screen_height * 9 / 10 // 13) - 30)
    listbox = tk.Listbox(scroll_frame, width=30, height=listHeight, yscrollcommand=scrollbar.set,
                         selectmode=tk.MULTIPLE)  # Creates a listbox
    update(country_list)
    scrollbar.config(command=listbox.yview)

    # Creates a drop down list for policies
    menu_policy = tk.StringVar()
    menu_policy.set("Policies")
    drop_policy = tk.OptionMenu(drop_down_frame, menu_policy, *GOV_POLICIES, command=store_policy)
    drop_policy.config(width=30, bg="blue", fg="white")

    # Creates a drop down list for survivability factors
    menu_category = tk.StringVar()
    menu_category.set("Category")
    drop_category = tk.OptionMenu(drop_down_frame, menu_category, *SURVIVABILITY,
                                  command=store_category)
    drop_category.config(width=30, bg="blue", fg="white")

    # Creates Labels
    selected = tk.Label(drop_down_frame, text=("\n".join(current_selection)), font="Times 13")
    selected_country_label = tk.Label(drop_down_frame, text="Selected Countries:",
                                      font="Times 13 underline")
    country_label = tk.Label(scroll_frame, text="Select Country:", font="Times 16 underline")

    # Creates buttons for users
    button_select = tk.Button(drop_down_frame, width=15, text="Add Country", command=select)
    button_delete = tk.Button(drop_down_frame, width=15, text="Delete", command=delete)
    button_clear = tk.Button(drop_down_frame, width=15, text="Clear", command=clear)
    button_graph = tk.Button(drop_down_frame, width=15, text="Graph",
                             command=lambda: (graph(country_dict)))

    # Adds widgets to the scroll bar frame
    scrollbar.grid(row=2, column=1, sticky='ns')
    listbox.grid(row=2, column=0)
    entry.grid(row=1, column=0)
    drop_down_frame.grid(row=0, column=1, sticky="n")
    country_label.grid(row=0, column=0)

    # Adds widgets to the drop_down frame
    drop_category.grid(row=0, column=0)
    drop_policy.grid(row=1, column=0)
    button_graph.grid(row=2, column=0, pady=5)
    button_select.grid(row=3, column=0, pady=5)
    button_clear.grid(row=4, column=0, pady=5)
    button_delete.grid(row=5, column=0, pady=5)
    selected_country_label.grid(row=6, column=0, pady=(20, 0))
    selected.grid(row=7, column=0)

    # Adds frames to tk window
    scroll_frame.grid(row=0, column=0)
    drop_down_frame.grid(row=0, column=1, sticky="n")

    # Frame to hold both graphs
    graph_frame = tk.Frame(root)
    graph_frame.grid(row=0, column=2, sticky='nswe')

    root.mainloop()
