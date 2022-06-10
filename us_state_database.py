"""Lab 3: Make a list of the 50 states their capitals,
state flowers, population. Allow user to search, update
state pop and provide bar graph for top 5 pop states
showing population"""

import matplotlib.pyplot as plt

class State:
    '''State object with all required info as attributes'''
    def __init__(self, name, state_code, capital, population, flower, flower_photo):
        self.name = name
        self.state_code = state_code
        self.capital = capital
        self.population = population
        self.flower = flower
        self.flower_photo = flower_photo

    # Creating getters for display, not creating one for
    # state code because I only plan to use it for the user's
    # search

    def get_name(self):
        '''Getter to display state name'''
        return self.name

    def get_capital(self):
        '''Getter to display state capital'''
        return self.capital

    def get_population(self):
        '''Getter to display state population'''
        return self.population

    def get_flower(self):
        '''Getter to display state flower'''
        return self.flower

    def get_flower_photo(self):
        '''Getter to display photo of state flower'''
        photo_file = plt.imread(self.flower_photo)
        plt.imshow(photo_file)
        plt.show()

    def display_all_info(self):
        '''Function to display all info for a state'''
        print(self.name + " - Capital: " + self.capital +
              ", Population: " + str(self.population) + ", State Flower: ", self.flower)

    def set_population(self, population):
        '''Function to update a specific state's population'''
        self.population = population

# Declare Objects for Each State
al = State("Alabama", "AL", "Montgomery", 4918689, "Camelia",
           r"State Flowers/AL_Camelia.jpeg")
ak = State("Alaska", "AK", "Juneau", 727951, "Forget-Me-Not",
           "State Flowers/AK_ForgetMeNot.jpeg")
az = State("Arizona", "AZ", "Phoenix", 7399410, "Saguaro Cactus Blossom",
           "State Flowers/AZ_SaguaroCactusBlossom.jpeg")
ar = State("Arkansas", "AR", "Little Rock", 3025875, "Apple Blossom",
           r"State Flowers/AR_AppleBlossom.jpeg")
ca = State("California", "CA", "Sacramento", 39562858, "California Poppy",
           r"State Flowers/CA_CaliforniaPoppy.jpeg")
co = State("Colorado", "CO", "Denver", 5826185, "Rocky Mountain Columbine",
           r"State Flowers/CO_RockyMtnColumbine.jpeg")
ct = State("Connecticut", "CT", "Hartford", 3559054, "Mountain Laurel",
           r"State Flowers/CT_MtnLaurel.jpeg")
de = State("Delaware", "DE", "Dover", 982049, "Peach Blossom",
           r"State Flowers/DE_PeachBlossom.jpeg")
fl = State("Florida", "FL", "Tallahassee", 21711157, "Orange Blossom",
           r"State Flowers/FL_OrangeBlossom.jpeg")
ga = State("Georgia", "GA", "Atlanta", 10723715, "Cherokee Rose",
           r"State Flowers/GA_CherokeeRose.jpeg")
hi = State("Hawaii", "HI", "Honolulu", 1411151, "Yellow Hibiscus",
           r"State Flowers/HI_YellowHibiscus.jpeg")
idaho = State("Idaho", "ID", "Boise", 1823594, "Syringa",
           r"State Flowers/ID_Syringa.jpeg")
il = State("Illinois", "IL", "Springfield", 12620571, "Violet",
           r"State Flowers/IL_Violet.jpeg")
indiana = State("Indiana", "IN", "Indianapolis", 6768941, "Peony",
           r"State Flowers/IN_Peony.jpeg")
ia = State("Iowa", "IA", "Des Moines", 3161522, "Wild Rose",
           r"State Flowers/IN_WildRose.jpeg")
ks = State("Kansas", "KS", "Topeka", 2915269, "Wild Native Sunflower",
           r"State Flowers/KS_WildNativeSunflower.jpeg")
ky = State("Kentucky", "KY", "Frankfort", 4474193, "Goldenrod",
           r"State Flowers/KY_Goldenrod.jpeg")
la = State("Louisiana", "LA", "Baton Rouge", 4637898, "Magnolia",
           r"State Flowers/LA_Magnolia.jpeg")
me = State("Maine", "ME", "Augusta", 1349367, "White Pine Cone and Tassle",
           r"State Flowers/ME_WhitePineConeTassle.jpeg")
md = State("Maryland", "MD", "Annapolis", 6055558, "Black-Eyed Susan",
           r"State Flowers/MD_BlackEyedSusan.jpeg")
ma = State("Massachusetts", "MA", "Boston", 6902371, "Mayflower",
           r"State Flowers/MA_Mayflower.jpeg")
mi = State("Michigan", "MI", "Lansing", 9989642, "Apple Blossom",
           r"State Flowers/MI_AppleBlossom.jpeg")
mn = State("Minnesota", "MN", "St. Paul", 5673015, "Pink and White Lady Slipper",
           r"State Flowers/MN_PinkWhiteLadySlipper.jpeg")
ms = State("Mississippi", "MS", "Jackson", 2971278, "Coreopsis",
           r"State Flowers/MS_Coreopsis.jpeg")
mo = State("Missouri", "MO", "Jefferson City", 6153233, "White Hawthorn Blossom",
           r"State Flowers/MO_WhiteHawthornBlossom.jpeg")
mt = State("Montana", "MT", "Helena", 1076891, "Bitterroot",
           r"State Flowers/MT_Bitterroot.jpeg")
ne = State("Nebraska", "NE", "Lincoln", 1943202, "Goldenrod",
           r"State Flowers/NE_Goldenrod.jpeg")
nv = State("Nevada", "NV", "Carson City", 3132971, "Sagebrush",
           r"State Flowers/NV_Sagebrush.jpeg")
nh = State("New Hampshire", "NH", "Concord", 1365957, "Pink Lady Slipper",
           r"State Flowers/NH_PinkLadySlipper.jpeg")
nj = State("New Jersey", "NJ", "Trenton", 8878355, "Violet",
           r"State Flowers/NJ_Violet.jpeg")
nm = State("New Mexico", "NM", "Santa Fe", 2100917, "Yucca",
           r"State Flowers/NM_Yucco.jpeg")
ny = State("New York", "NY", "Albany", 19376771, "Rose",
           r"State Flowers/NY_Rose.jpeg")
nc = State("North Carolina", "NC", "Raleigh", 10594553, "Dogwood",
           r"State Flowers/NC_Dogwood.jpeg")
nd = State("North Dakota", "ND", "Bismarck", 766044, "Wild Prarie Rose",
           r"State Flowers/ND_WildPrarieRose.jpeg")
oh = State("Ohio", "OH", "Columbus", 11701859, "White Trillium",
           r"State Flowers/OH_WhiteTrillium.jpeg")
ok = State("Oklahoma", "OK", "Oklahoma City", 3973707, "Mistletoe",
           r"State Flowers/OK_Mistletoe.jpeg")
oregon = State("Oregon", "OR", "Salem", 4253588, "Oregon Grape",
           r"State Flowers/OR_OregonGrape.jpeg")
pa = State("Pennsylvania", "PA", "Harrisburg", 12803056, "Mountain Laurel",
           r"State Flowers/PA_MountainLaurel.jpeg")
ri = State("Rhode Island", "RI", "Providence", 1060435, "Violet",
           r"State Flowers/RI_Violet.jpeg")
sc = State("South Carolina", "SC", "Columbia", 5213272, "Yellow Jessamine",
           r"State Flowers/SC_YellowJessamine.jpeg")
sd = State("South Dakota", "SD", "Pierre", 890621, "American Pasque",
           r"State Flowers/SD_AmericanPasque.jpeg")
tn = State("Tennessee", "TN", "Nashville", 6886717, "Passionflower",
           r"State Flowers/TN_PassionFlower.jpeg")
tx = State("Texas", "TX", "Austin", 29363096, "Ennis",
           r"State Flowers/TX_Ennis.jpeg")
ut = State("Utah", "UT", "Salt Lake City", 3258366, "Sego Lily",
           r"State Flowers/UT_SegoLily.jpeg")
vt = State("Vermont", "VT", "Montpelier", 623620, "Red Clover",
           r"State Flowers/VT_Clover.jpeg")
va = State("Virginia", "VA", "Richmond", 8569752, "American Dogwood",
           r"State Flowers/VA_AmericanDogwood.jpeg")
wa = State("Washington", "WA", "Olympia", 7705917, "Coast Rhododendron",
           r"State Flowers/WA_CoastRhododendron.jpeg")
wv = State("West Virginia", "WV", "Charleston", 1780003, "Rhododendron",
           r"State Flowers/WV_Rhododendron.jpeg")
wi = State("Wisconsin", "WI", "Madison", 5837462, "Wood Violet",
           r"State Flowers/WI_WoodViolet.jpeg")
wy = State("Wyoming", "WY", "Cheyenne", 579917, "Indian Paintbrush",
           r"State Flowers/WY_IndianPaintbrush.jpeg")

# List Containing All States
states = [al, ak, az, ar, ca, co, ct, de, fl, ga, hi, idaho, il, indiana, ia, ks,
          ky, la, me, md, ma, mi, mn, ms, mo, mt, ne, nv, nh, nj, nm, ny, nc, nd,
          oh, ok, oregon, pa, ri, sc, sd, tn, tx, ut, vt, va, wa, wv, wi, wy]

def display_all_states():
    '''Function to display all statet and attributes'''
    for i in states:
        i.display_all_info()

def display_one_state(state_code):
    '''Function to display specific state and its attributes + photo'''
    if len(state_code) != 2 or state_code.isdigit(): # Validating user input
        new_code = input("Please enter valid two letter code:\n")
        display_one_state(new_code)

    found = False
    for i in states:
        if state_code.upper() in i.state_code:
            print("Displaying info and opening photo in new window.")
            found = True
            return i.display_all_info(), i.get_flower_photo()

    if found is False:
        display_one_state(input("Not found, try again.\n"))

def display_population_graph():
    '''Function to display bar graph of top 5 populations'''

    populations = []
    for i in states:
        populations.append(i.population)

    populations.sort(reverse=True) # Reverse sorting list of populations
    top_five = populations[:5] # Taking top 5 largest populations

    # For loop to create a new list of the names correlating with top 5 pops
    names = []
    for i in top_five:
        for j in states:
            if i == j.population:
                names.append(j.name)

    # Creating the bar graph
    plt.figure(figsize=(6,6))
    plt.bar(names,top_five)
    plt.xlabel("States")
    plt.ylabel("Populations x 10 Mil")
    plt.title("States with the Five Highest Populations")

    plt.show()

def update_population(code):
    '''Function to update a state's population'''
    if len(code) != 2 or code.isdigit(): # Validating user input
        new_code = input("Please enter valid two letter code:\n")
        update_population(new_code)
    for i in states:
        if code.upper() in i.state_code:
            new_pop = int(input("Enter your new population:\n"))
            i.set_population(new_pop)

# Menu for the program:
choice = 0
while choice != 5:
    choice = input("Welcome to the U.S. State Database.\n"
                   "Enter a number to choose:\n"
                   "1. Display all U.S. States with capitals, population, & state flower.\n"
                   "2. Display a single state with capital, population, & state flower w/ photo.\n"
                   "3. Provide a bar graph of the top 5 populated states.\n"
                   "4. Update a specific state's population.\n"
                   "5. Exit.\n")
    try: #Validating that choice is an int
        int(choice)
    except ValueError:
        print("That is not a number.")

    if int(choice) == 1:
        display_all_states()
    elif int(choice) == 2:
        code = input("Enter the two letter code for the state you'd like to see:\n")
        display_one_state(code)
    elif int(choice) == 3:
        display_population_graph()
    elif int(choice) == 4:
        pop_code = input("Enter the two letter code for the state you'd like to update:\n")
        update_population(pop_code)
    elif int(choice) > 5 or int(choice) < 1:
        print("Please enter a valid number between 1 & 5.\n")
