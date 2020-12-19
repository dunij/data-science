import time
import pandas as pd
import numpy as np
import sys 
import tkinter as tk
from time import time 
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import *
from tkinter.ttk import *
from tkinter import font 

###***** Project Of Bike_share system*****###
### --- You need to adjust path of the image in first function __init__ ---### 
class bike_share:
    # city_data dictionary {}  of  3 files .csv , that we will filter data within them
    city_data = { 'chicago': 'chicago.csv',
                  'new york': 'new_york.csv',
                  'washington': 'washington.csv' }   

    def __init__(self):
        try:
          
    ### this function will appear once we start the project ###
    ### show screen window of project name ###
        # creating tkinter window 

        #try: # to avoid errors from image if it doesn't exists
            # take care if PROBLEM happened from root TK() try { root = Tk() | root = tk.Toplevel()}
            # TK() show only one window , toplevel shows 2 windows
            root = Tk()    # Adding widgets to the root window 
            root.title("Bike_share System") # the top title of sceen window
            root.configure(bg = "black")
            Title_Screen = tk.Label(root,
                                 text="Welcome in Bikeshare System",
                                 fg="grey",
                                 bg="black",
                                 font="Helevetica 25 bold",
                                 pady = "30",
                                 padx = "25",
                                 ).pack(side = TOP, pady = 50) 
            
            # Creating a photoimage object to use image 
            img = PhotoImage(file = r"./udacity_fwd.GIF") 
            
            # Resizing image to fit on button 
            photoimage = img.subsample(3, 3)   
                
            Button(root, text ="Click To Launch Bike_share System" , 
                  image = img, compound = BOTTOM, command = root.destroy ).pack(side = BOTTOM, pady = 10) 
            #Exteral paddign for the buttons
            
            """ that is a nice timer to close window automatically after 3 seconds"""
            start = time() 
            root.after(3000, root.destroy)              
            root.mainloop()                         
            end = time() # calculating end time 
            # in after method 5000 miliseconds 
            # is passed i.e after 5 seconds 
            # main window i.e root window will 
            # get destroyed         
            
        except:
            pass           
     
#-------- show message to close system or restart it --------#
    def restart(self):       
        
        start_end = input('keyword {start} or any keyword to restart , keyword {n} to close\n').lower().strip()         
        if start_end == 'n' or start_end == 'no':
            sys.exit()                   
        elif start_end == 'start' or start_end != 'n' or start_end != 'no':
            self.main()  
            
#-------- Ask user to specify the way he wants to filter data by it --------#         
    def get_filters(self):
        
        """
        Asks user to specify a city, month, and day to analyze.
    
        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "not at all" to apply no month filter
            (str) day - name of the day of week to filter by, or "not at all" to apply no day filter
        """
        month, day = "both", "both"
        cities = ['chicago', 'new york', 'washington']
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        days = ['monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday','sunday']
        
        
        self.city = input("Would you like to see data for Chicago, New York, or Washington?...\n").lower().strip()      
        n_try = 1
        while (self.city not in cities) and (0< n_try< 3):
            # try errors for only 3 times then log out from program        
            city = input("Try agan ....{} tries remain\n".format (3- n_try)).lower().strip()
            n_try +=1
            if (n_try ==3 and city not in cities):
                print('Yoa had entered  many non available data ')
                self.restart()
                
            else:
                continue

        filter =input("Would you like to filter the data by month, day, both or not at all?\n").lower().strip()  
        while True:    
            if filter == 'month' or filter == 'both':      
                month =input("Which month - January, February, March, April, May, or June?\n").lower().strip()
                n_try =1 
                while (month not in months):
                     # try errors for only 3 times then log out from program  
                     month=input("Enter a valid data OF Month name \nTry again ....{} times remain\n".format (3- n_try)).lower().strip()
                                        
                     if (n_try ==2 and month not in month):  # tee number of errors data entering {1,2,3} then restart system                 
                         print('You had entered  many non available data ')
                         self.restart()
                     else:
                         n_try +=1 # increase each time by one and  continue loop untill restart of log out from loop to continue 
                         continue
                 
                               
            if filter == 'day' or filter == 'both':      
                day =input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n").lower().strip()
                n_try =1
                while (day not in days):
                     # try errors for only 3 times then log out from program  
                     day=input("Enter a valid data\nTry again ....{} times remain\n".format (3- n_try)).lower().strip()
                                        
                     if (n_try ==2 and day not in days):                       
                         print('Yoa had entered  many non available data ')
                         self.restart() 
                     else:
                        n_try +=1
                        continue
                    
            if filter == 'not at all' or filter == 'n': #states of restarts input conditions
                """ to skip function of filter and complete """
                df = self.load_data(self.city, month, day)
                self.time_stats(df)
                self.station_stats(df)
                self.trip_duration_stats(df)
                self.user_stats(df)
                self.display_row_data(df)
                sys.exit()
                 
                                    
            if filter not in ["month" ,"day" , "both" , "n" , "not at all"] :
                n_try =1
                while (filter not in ["month" , "day" , "both" , "n"  ,"not at all"]):
                     # try errors for only 3 times then log out from program  
                     filter =input("Enter a valid data\nTry again ....{} times remain\n".format (3- n_try)).lower().strip()
                                        
                     if (n_try ==2 and filter  not in ["month" , "day" , "both" , "n"  , "not at all"]):                         
                         print('Yoa had entered  many non available data ')
                         self.restart()
                     else:
                        n_try +=1
                        continue
                continue

            print('-'*40)
            return (self.city, month, day)     
            
         
    def load_data(self,city, month, day):
        """
        Loads data for the specified city and filters by month and day if applicable.
    
        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "not at all" to apply no month filter
            (str) day - name of the day of week to filter by or "not at all" to apply no day filter
        Returns:
            df - pandas DataFrame containing city data filtered by month and day
        """
        
        # load data file into a dataframe
        df = pd.read_csv(self.city_data[self.city])
    
        # convert the Start Time column to datetime
        df['Start Time'] =  pd.to_datetime(df['Start Time'])
        
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
    
        # filter by month if applicable
        if month != 'both':
            # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
        
            # filter by month to create the new dataframe
            df = df[df['month'] == month]
    
        # filter by day of week if applicable
        if day != 'both':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
              
        return df
     
    
    def time_stats(self,df):
        """Displays statistics on the most frequent times of travel."""
    
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time()
    
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])       
        
        """ Display the most common month """
        # extract month from the Start Time column to create a month column
        df['month'] = df['Start Time'].dt.month
        # the most common month
        popular_month = df['month'].mode()[0]
        print('Most common month:', popular_month)       
        
        """ Display the most common day of week """
        # extract day of weak from the Start Time column to create a day  column
        df['day'] = df['Start Time'].dt.day
        # the most common day
        popular_day = df['day'].mode()[0]
        print('Most common day:', popular_day)  
    
        """ Display the most common start hour """  
        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour  
        # the most common hour (from 0 to 23)
        popular_hour = df['hour'].mode()[0]
        print('Most Frequent Start Hour:', popular_hour)
        print ("Count: ", df['hour'].value_counts().max())
      
        print("\nThis took %s seconds." % (time() - start_time))
        print('-'*40)
        
        
        
    def station_stats(self,df):
        """Displays statistics on the most popular stations and trip."""
    
        print('\nCalculating The Most Popular Stations and Trip...')
        start_time = time()
        
        # display most commonly used Start Station
        popular_start_station = df['Start Station'].mode().to_string(index= False).strip()
        print('\nMost popular Start Station:\n',popular_start_station)
        print ("Count: ", df['Start Station'].value_counts().max())
        
        # display most commonly used End Station
        popular_end_station = df['End Station'].mode().to_string(index= False).strip()
        print('\nMost popular End Station:\n',popular_end_station)
        print ("Count: ", df['End Station'].value_counts().max())
        
        # most frequently combination of start station and end station
        trip_stations = (df['Start Station'] +"   " +df['End Station']).mode().to_string(index= False)

        print('\nMost common trip from start to end:\nStart Station  End Station\n',trip_stations)
     
        print("\nThis took %s seconds." % (time() - start_time))
        print('-'*40)    
        
        
    def trip_duration_stats(self,df):
        
        """Displays statistics on the total and average trip duration."""
          
        print('\nCalculating Trip Duration...\n')
        start_time = time()
    
        # display total travel time
        print("total Duration time:",df["Trip Duration"].sum()) 
        # display total count 
        print ("Count: ",df['Trip Duration'].value_counts().sum())
        # display mean travel time
        print("Average Duration time:",df["Trip Duration"].mean())
    
    
        print("\nThis took %s seconds." % (time() - start_time))
        print('-'*40)
      
    def user_stats(self,df):
        
        print('Calculating User Stats...')
        start_time = time()
        
        """Displays statistics on bikeshare users.""" 
        # print value counts for each user type
        user_types = df["User Type"].value_counts(dropna=False) 
        print("\ncounts of user types:\n", user_types)
        
        try:        
            """ print earliest, most recent, and most common year of birth """
            # print  earliest  Birth Year 
            print("\nThe earliest Birth Year:",df["Birth Year"].min()) 
            
            # print The most recent Birth Year 
            print("\nThe most recent Birth Year:",df["Birth Year"].max())
            
            # print The most common of Birth Year 
            print("\nThe most common of Birth Year:",df["Birth Year"].mode().to_string(index= False).strip()) 
            
            # print value counts for  Gender
            gender = df["Gender"].value_counts(dropna=True) 
            print("counts of gender:\n", gender)
                
        
            print("This took %s seconds." % (time() - start_time))
            print('-'*40)
            
        except:
              pass   
              
              
    def display_row_data(self,df):
        try:
        
            #buch of data defined to show as samples"

            """" Display 5 samples frequently while user wants"""
            
            if (self.city == "washington"):
                data = {"Start Time": df['Start Time'] , "End Time": df['End Time'] ,
                "Trip Duration": df['Trip Duration'], "Start Station": df['Start Station'] ,
                "End Station": df['End Station'] , "User Type":df['User Type']} 
                df2= pd.DataFrame(data)
                               
            else:
                 #buch of data defined to show as samples"
                data = {"Start Time": df['Start Time'] , "End Time": df['End Time'] ,
                "Trip Duration": df['Trip Duration'], "Start Station": df['Start Station'] ,
                "End Station": df['End Station'] , "User Type":df['User Type'],
                "Gender":df['Gender'], "Birth Year" :df['Birth Year']} 
                df2= pd.DataFrame(data)

            while True:    
                
                    ask_print = input ("Would you like to see individual trip data? Enter yes or no...\n").lower().strip()               
                    while(ask_print.lower() == 'yes' or ask_print.lower() == 'y'):
                        
                        """
                        code to sample data and show as dictionary
                    
                        """
                        # to display 6 samples at a time
                        data_samples = df2.sample(n=6)     # to show six samples at a time 
                        
                        dict_ = data_samples.to_dict('index')
                        dict_list = list(dict_.items())        # convert dictionary items to list             
                        samples_itr = dict(list(dict_.items()))  #with dict                  
                        sict_str = listToStr = ' '.join(map(str, dict_list))   # to convert list to string 
                        
                        # to Display samples from data , n =6 but with index integer
                        # its disadvantage that it can't show all data column in state of many samples
                        #print(data_samples.iloc[0:6])
                       # print(dict_list)
                        split_list = []
                        i =1       
                        """
                        while loop to display only samples after spliti items to each line
                        take cara that dictionary as index { dict_ = data_samples.to_dict('index')}
                        
                        """
                        while True:
                            split_list.append(sict_str.split(",")[i:i+1]) 
                        
                            if split_list[-1] == []:
                                break
                            else:
                                print(sict_str.split(",")[i:i+1])
                                i += 1
        
                        ask_print = input ("Would you like to see a nother individual trip data? Enter yes or no...\n").lower().strip()     
                        if(ask_print.lower() == 'no' or ask_print.lower() == 'n'):
                            self.restart()    
                        else:
                            continue# try many times to print
                            
                    if(ask_print.lower() == 'no' or ask_print.lower() == 'n'):
                        self.restart()  
                        
                    else:               
                        continue     # try if beginning is not yes or no or y or n            
        except:
            pass
        
    def end_screen(self):    
        try:         
            root = tk.Toplevel() # take care if PROBLEM happened from root TK() try {root = tk.Toplevel()}
            root.geometry("300x150") 
            root.title("Bike_share System")
            root.configure(bg = "black") 
            Label(root, text ='GOOD TIME', font = "50").pack(side = TOP, pady = 50)        
            start = time() 
            # in after method 5000 miliseconds 
            # is passed i.e after 5 seconds 
            # main window i.e root window will 
            # get destroyed 
            root.after(10000, root.destroy) 
            root.mainloop() 
            # calculating end time 
            end = time() 

            
        except:
            pass
                           
    def main(self):
        while True:
            print("\t\t❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀")
            print("\t\t❀Hello! Let\'s explore some US bikeshare data!❀")
            print("\t\t❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀❀")
            city, month, day = self.get_filters()
            df = self.load_data(city, month, day)
            self.time_stats(df)
            self.station_stats(df)
            self.trip_duration_stats(df)
            self.user_stats(df)
            self.display_row_data(df)
            self.end_screen() 
            sys.exit()
                    
# Instance of Class Main
bikeshare_obj = bike_share()   
bikeshare_obj.main()
if __name__ == "__main__":
    main()