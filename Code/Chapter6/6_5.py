river_country ={
    'nile':'egypt',
    'changjiang':'china',
    'rhine':'germany',
}

for river, country in river_country.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in river_country.keys():
    print(f"The {river.title()}.")
    
for country in river_country.values():
    print(f"The {country.title()}.")