def get_season(month):
    if(month>12):
        return "Invalid Month"
    seasons = ("talvi", "kevät", "kesä", "syksy")
    season_num = (month//3)-4
    season = seasons[season_num]
    return season

while(True):
    kuukausi = int(input("Anna kuukausi: "))
    if(kuukausi<=0):
        break
    print(get_season(kuukausi))