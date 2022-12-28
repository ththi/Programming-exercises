### Habit tracker, functions
### written by Thorsten Thiergart (2022)

""" Functions for analyzing habits, use together with loop.py """

###
def list_all_habs(input_dat):
    """ Lists all habits, from object list as input """
    for entrie in input_dat:
        print(">",entrie.name)

    print("\n")

###
def list_habs_by_period(input_dat):
    """ Lists all habits by period, from object list as input """
    print("Daily habits:")
    for entrie in input_dat:
        if entrie.period =="daily":
            print(">",entrie.name,entrie.period)

    print("\nWeekly habits:")
    for entrie in input_dat:
        if entrie.period =="weekly":
            print(">",entrie.name,entrie.period)

    print("\n")

###
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

                last_num=int(zz)

        print(">",xx.name,"Streak:",long_st,str_perio)
        streak_dic[xx.period].append([long_st,xx.name])

    print("\nLongest streaks overall: ")
    for yy in streak_dic:
        print(yy,sorted(streak_dic[yy],)[-1][0],"in",sorted(streak_dic[yy],)[-1][1])

###
