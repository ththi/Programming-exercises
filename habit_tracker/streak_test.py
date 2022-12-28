#### unittest file for habit tracker functions

""" This script will execute a unitttest for one of the function
    from the habit tracker analytics module.
"""

import unittest

import os

######
day_to_date={}
hab_dic={}

### empty dictionaries to fill with dates
date_dic_day={}
date_dic_week={}
date_dic_first={}



### check if habit file already exists (check correct name !!!)

file_name="track_data.csv"
if os.path.exists(file_name):
    #print(" Found Habit file...\n")

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
        ###line_split is now list of , has still newline!
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


### create habit class

class Habit:
  def __init__(self, name, period):
    self.name = name
    self.period = period

# loop through pre-defined or acquired list of habits

objs_list = list()

for names in hab_dic:
    #print(names,hab_dic[names])
    #habit objects are stores seuqnrially in list
    objs_list.append(Habit(names,hab_dic[names]))


####

def list_all_streaks(input_xx,input_day,input_week):
    """ Lists longest streak per Habit and overall best streak.
        Input is the object list and two dictionaries (weeks, days)
        containing the dates when tasks were completed.
    """
    streak_dic={"daily":[],"weekly":[]}

    for xx in input_xx:

        last_num=0
        streak_cou=0
        long_st=0

        if xx.period =="daily":
            str_perio="Days"
            for zz in input_day[xx.name]:

                if last_num==0:
                    last_num=int(zz)
                elif int(zz)==last_num+1:
                    streak_cou+=1

                    if streak_cou >long_st:
                        long_st=streak_cou

                elif int(zz)!=last_num+1:
                    streak_cou=0

                #print("  ",zz,last_num,streak_cou,long_st)
                last_num=int(zz)

        if xx.period =="weekly":
            str_perio="Weeks"
            for zz in input_week[xx.name]:

                if last_num==0:
                    last_num=int(zz)
                elif int(zz)==last_num+1:
                    streak_cou+=1

                    if streak_cou >long_st:
                        long_st=streak_cou

                elif int(zz)!=last_num+1 and int(zz)!=last_num:
                    streak_cou=0


                #print("  ",zz,last_num,streak_cou,long_st)
                last_num=int(zz)

        #print(">",xx.name,"Streak:",long_st,str_perio)
        streak_dic[xx.period].append([long_st,xx.name])

    #print("\nLongest streaks overall: ")
    return(sorted(streak_dic["daily"],)[-1][0],sorted(streak_dic["daily"],)[-1][1]
    ,sorted(streak_dic["weekly"],)[-1][0],sorted(streak_dic["weekly"],)[-1][1])


###

### actual testing will follow

class Test_streak(unittest.TestCase):
    def test_streak_done(self):
        actual = list_all_streaks(objs_list,date_dic_day,date_dic_week)
        expected = (5,"Meditate",4,"Walk 10k")
        self.assertEqual(actual, expected)
