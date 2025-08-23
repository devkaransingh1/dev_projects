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
        print("\nWelcome to Netflix Data Analyzer 🎬")
        print("1. View dataset (first 10 rows)")
        print("2. Show dataset info")
        print("3. Search movie/show by title")
        print("4. Count movies vs TV shows")
        print("5. Top 10 countries with most content")
        print("6. Exit")
        
        # choice pallete
        choice=int(input("enter your choice in as index number = "))
        
        if choice == 1:
            print("firt 10 rows : \n",df.head(10))
            print("data loaded correctly 👍")
            
        if choice == 2:
            print("\ninfo\n",df.info())
            print("\nshape\n",df.shape)
            print("\ncolum names\n",df.columns)
            
        if choice == 6:
            print("Thankyou for using this tool made by dev karan singh.")
            print("tool closed succesfully.")
            break

        


