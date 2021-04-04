def countryandcity(cityname,countryname,population=0):
    if population:
        result = f"{cityname.title()}, {countryname.title()} {population}"
    else:
        result = f"{cityname.title()}, {countryname.title()}"
    return result