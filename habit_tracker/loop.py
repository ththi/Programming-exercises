### Habit tracker
### written by Thorsten Thiergart (2022)

""" A habittracker with 4 Main functions:
    - check predefined habits
    - add new habits
    - delete existing habits
    - analyze habits, using the func_mod module
    - script will check for existing habit file (test_data.csv)
 """

import datetime
import os

# import analytics module with functions...
import func_mod

### get current date
day_to_date={}
date_x = datetime.datetime.now()

full_date=[date_x.strftime("%A"),date_x.strftime("%d"),date_x.strftime("%m"),date_x.strftime("%Y")]
day_num=date_x.strftime("%j")
week_num=date_x.strftime("%U")
exact_date=full_date[0]+" "+full_date[1]+" "+full_date[2]+" "+full_date[3]

day_to_date[day_num]=[exact_date,week_num]

###

print("\n Welcome to your habit tracker, today is:",exact_date)
print(" Checking for habit file:")

### empty dictionary to fill with habits
hab_dic={}

### empty dictionaries to fill with dates
date_dic_day={}
date_dic_week={}
date_dic_first={}


### check if habit file already exists (check correct name !!!)

file_name="track_data.csv"
if os.path.exists(file_name):
    print(" Found Habit file...\n")

    ### read test file
    habit_file = open(file_name, "r")
    for line in habit_file:
        #rstrip removes trailing character at end of string
        line=line.rstrip("\n")
        line_split=line.split(",")

        #skip "first" line
        if line_split[0] == "Day":
            continue

        exact_date=line_split[0]+" "+line_split[1]+" "+line_split[2]+" "+line_split[3]
        hab_dic[line_split[6]]=line_split[7]

        day_to_date[line_split[4]]=[exact_date,line_split[5]]

        #save dates for each habit in dictionary... (append if already exists)
        if line_split[6] in date_dic_day:

            date_dic_day[line_split[6]].append(line_split[4])
            date_dic_week[line_split[6]].append(line_split[5])

        else:
            date_dic_day[line_split[6]]=[line_split[4]]
            date_dic_week[line_split[6]]=[line_split[5]]
            date_dic_first[line_split[6]]=[exact_date]

        #print(line)

    habit_file.close()
    ### end, read test file

 #if no file exists create 5 sample habits !
else:
    print(" No Habit file found...\n")
    # add predefined habits here
    hab_dic["Walk 10k"]="weekly"
    hab_dic["Exercise"]="weekly"
    hab_dic["Meditate"]="daily"
    hab_dic["Learn new stuff"]="daily"
    hab_dic["Call Friends"]="daily"

    #initialize empty dics
    date_dic_day={"Walk 10k":[],"Exercise":[],"Meditate":[],"Learn new stuff":[],"Call Friends":[]}
    date_dic_week={"Walk 10k":[],"Exercise":[],"Meditate":[],"Learn new stuff":[],"Call Friends":[]}
    date_dic_first={"Walk 10k":[],"Exercise":[],"Meditate":[],"Learn new stuff":[],"Call Friends":[]}

### create habit class

class Habit:
  def __init__(self, name, period):
    self.name = name
    self.period = period

# loop through pre-defined or acquired list of habits

objs_list = list()

for names in hab_dic:

    #habit objects are stores sequentially in list
    objs_list.append(Habit(names,hab_dic[names]))

####

### start endless loop, until 5 is choosen as input

# check variable for new entries or deleted habits
check_for_new=0

while True:

    print("\nPlease Choose one of the following Tasks (Select by Number):\n")
    print("1. Add a new Habit\n2. Check habits\n3. Analyze habits")
    print("4. Delete habits\n5. Exit\n")

    user_choice=input()

    # block for adding new habits
    if user_choice == "1":
        print("\nPlease add name for new Habit\n")
        new_hab_nam=input()

        print("\nPlease add period for new Habit , 1 for daily, 2 for weekly\n")
        new_hab_per=input()

        date_dic_first[new_hab_nam]=[exact_date]


        if new_hab_per =="1":
            objs_list.append(Habit(new_hab_nam,"daily"))
            date_dic_day[new_hab_nam]=[]
        elif new_hab_per =="2":
            objs_list.append(Habit(new_hab_nam,"weekly"))
            date_dic_week[new_hab_nam]=[]
        else:
            print("WRONG INPUT\n")

    # block for checking habits
    if user_choice == "2":
        print("\nPlease choose Habit to check (from list)\n")
        l_cou=0
        for xx in objs_list:
            l_cou+=1
            print(">",l_cou,xx.name)

        to_check=input()
        if to_check.isdigit():
            if int(to_check) <= l_cou:
                check_dump=objs_list[int(to_check)-1]
                print("\nYou completed your task",check_dump.name,"on",exact_date)

                check_for_new=1

                date_dic_week[check_dump.name].append(week_num)
                date_dic_day[check_dump.name].append(day_num)

            else:
                print("WRONG INPUT\n")
        else:
            print("WRONG INPUT\n")

    # block for analyzing habits
    if user_choice == "3":
        print("What do you want to Analyze?\n")
        print("1. List all habits\n2. Longest streak for each Habit")
        print("3. List all habits with same period\n")

        user_choice_an=input()

        if user_choice_an == "1":
            func_mod.list_all_habs(objs_list)

        if user_choice_an == "2":

            func_mod.list_all_streaks(objs_list,date_dic_day,date_dic_week)

        if user_choice_an == "3":
            func_mod.list_habs_by_period(objs_list)

        if user_choice_an != "1" and user_choice_an != "2" and user_choice_an != "3":
            print("Wrong input c")

    # block for deleting habits
    if user_choice == "4":
        print("\nPlease choose Habit to delete (from list)\n")
        l_cou=0
        for xx in objs_list:
            l_cou+=1
            print(">",l_cou,xx.name)

        to_del=input()
        if to_del.isdigit():
            if int(to_del) <= l_cou:
                del objs_list[int(to_del)-1]
                check_for_new=1
            else:
                print("WRONG INPUT\n")
        else:
            print("WRONG INPUT\n")


    # block for wrong input from main text
    if user_choice != "1" and user_choice != "2" and user_choice != "3" and user_choice != "4" and user_choice != "5":
        print("\nPlease choose one of the Numbers (1-5) !\n")

    # block for exit choice
    if user_choice == "5":
        break

print("\nGoodbye")
###end, loop


### open new file if new entries are there or habits were deleted...
if check_for_new ==1:

    """ A new/updated tracking file will be created if habits are
    completed or deleted. Note: old data might get lost!
    (although a copy was created)
    """

    # make copy of old file
    os.system('cp track_data.csv track_data_copy.csv')

    # create updated new file
    exit_file = open("track_data.csv", "w")

    print("Day,Date_day,Date_month,Year,Day_count,Week_count,Habit_name,Habit_period",file=exit_file)

    for xx in objs_list:

        # check if new habit was added , but has no dates yet
        if xx.name in date_dic_day:
            for date_entry in date_dic_day[xx.name]:
                dump_string=day_to_date[date_entry][0].replace(" ",",")
                print (dump_string,date_entry,day_to_date[date_entry][1],xx.name,xx.period,file=exit_file,sep=",")



#### end of script
