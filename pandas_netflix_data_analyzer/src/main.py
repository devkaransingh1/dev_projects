import pandas as pd

# command line user interface.
print("This is a netflix data analyzer tool")
print("made by dev karan singh for showing practical knowledge of pandas library of python.")

# taking file path as input from user.
try:
    a=input("\nenter you file path (format should be CSV , remove quotes from path if have.) = ")
    df = pd.read_csv(a)
except FileNotFoundError:
    print("\nentered file does not exists or typo in file path, Recheck PATH and rerun the program.")
    df = None

# CLI UI
if df is not None:
    while True:
        print("\nWelcome to Netflix Data Analyzer ")
        print("1. View dataset (first 10 rows)")
        print("2. Show dataset info")
        print("3. Search movie/show by title")
        print("4. Count movies vs TV shows")
        print("5. Top 10 countries with most content")
        print("6. Generate random recommendation")
        print("7. Exit")
        
        # choice pallete
        choice=int(input("enter your choice in as index number = "))
        
        if choice == 1:
            print("firt 10 rows : \n",df.head(10))
            print("data loaded correctly 👍")
            
        if choice == 2:
            print("\ninfo\n",df.info())
            print("\nshape\n",df.shape)
            print("\ncolum names\n",df.columns)
            
        if choice == 3:
            title=input("enter moive / show name  = ")
            result = df[df['title'].str.contains(title , case = False , na = False)]
            
            if result is not False:
                if not result.empty:
                    print(result[['title' , 'release_year' , 'duration' , 'listed_in']])
                else:
                    print("no match found for this entry.")
                    
        if choice == 4:
            counts=df['type'].value_counts()
            print("count of movies vs TV shows = ")
            print(counts)
            
        if choice == 5:
            top=df['country'].value_counts().head(10)
            print("top 10 countries are given below \n")
            print(top)
            
        if choice == 6:
            random=df.sample(n=1)
            print("we recommend you the content with title = ", random['title'])
            
        if choice == 7:
            print("Thankyou for using this tool made by dev karan singh.")
            print("tool closed succesfully.")
            break
        

        


