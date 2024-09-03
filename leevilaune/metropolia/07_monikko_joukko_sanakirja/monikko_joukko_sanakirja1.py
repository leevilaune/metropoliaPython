def get_season(month):
    if(month>12):
        return "Invalid Month"
    seasons = ("talvi", "kevät", "kesä", "syksy")
    #negative indexing to account for winter months
    #[-4,0]= talvi
    #[-3]  = kevät
    #[-2]. = kesä
    #[-1]  = syksy
    season_num = (month//3)-4
    print(season_num)
    season = seasons[season_num]
    return season

while(True):
    month = input("Anna kuukausi: ")
    if(month.isnumeric()==False or int(month)<=0):
        break
    print(get_season(int(month)))