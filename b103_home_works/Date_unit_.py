while 1:
    day = int(input('enter day: '))
    month = int(input('enter month: '))
    year = int(input('enter year: '))
        

    if day == 1:
        day = 'pervovo'
    elif day == 2:
        day = 'vtorovo'
    elif day == 3:
        day ='trtiva'
    elif day == 4:
        day='chetvertovo'
    elif day == 5:
        day='pyatovo'
    elif day == 6:
        day='shestovo'
    elif day == 7:
        day='sedmovo'
    elif day == 8:
        day='vosmova'
    elif day == 9:
        day='devyatovo'
    elif day == 10:
        day='desyatovo'
    elif day == 11:
        day='odinadsetovo'
    elif day == 12:
        day='dvinadsetovo'
    elif day == 13:
        day='trinadsetovo'
    elif day == 14:
        day='chetirnadsetovo'
    elif day == 15:
        day='pyatnadsetovo'
    elif day == 16:
        day='shesnatsenovo'
    elif day == 17:
        day='semnadsetovo'
    elif day == 18:
        day='vosemnadsetovo'
    elif day == 19:
        day='devednatsetovo'
    elif day == 20:
        day='dvatsatovo'
    elif day == 21:
        day='dvadsat pervovo'
    elif day == 22:
        day='dvatsat vtorovo'
    elif day == 23:
        day='dvatsat tretevo'
    elif day == 24:
        day='dvadsat chetvertovo'
    elif day == 25:
        day='dvadsat pyatovo'
    elif day == 26:
        day='dvatsat shestovo'
    elif day == 27:
        day='dvatsat sedmovo'
    elif day == 28:
        day='dvatsat vosmova'
    elif day == 29:
        day= 'dvadsat devyatovo'
    elif day == 30:
        day ='tridsatovo'
    elif day == 31:
        day = 'tridset pervovo'



    if month == 1:
        month='yanvarya'
    elif month == 2:
        month='fevralya'
    elif month == 3:
        month='Marta'
    elif month == 4:
        month='Aprela'
    elif month == 5:
        month='Maya'
    elif month == 6:
        month='Iyuna'
    elif month == 7:
        month='Iyula'
    elif month == 8:
        month='Avgusta'
    elif month == 9:
        month='Sentabrya'
    elif month == 10:
        month='Oktebra'
    elif month == 11:
        month='Noyabrya'
    elif month == 12:
        month='Dekabrya'


    print(f'{day}.{month}.{year} goda.')
