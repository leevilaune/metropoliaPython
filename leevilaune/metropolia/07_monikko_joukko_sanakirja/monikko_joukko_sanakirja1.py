def get_season(month):
    if(month>12):
        return "Invalid Month"
    seasons = ("talvi", "kevät", "kesä", "syksy")
    """
    negative indexing to account for winter months
    #[-4,0]= talvi
    #[-3]  = kevät
    #[-2]. = kesä
    #[-1]  = syksy
    month is divided by 3 to account for months in a season
    4 is subtracted from that to get negative index for the month
    12/3-4=4-4=0 is december/winter
    8/3-4=2-4=-2 is august/summer
    """
    season_num = (month//3)-4
    print(season_num)
    season = seasons[season_num]
    return season

while(True):
    month = input("Anna kuukausi: ")
    if(month.isnumeric()==False or int(month)<=0):
        break
    print(get_season(int(month)))