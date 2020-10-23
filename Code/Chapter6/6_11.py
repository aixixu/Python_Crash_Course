cities = {
    'London':{
        'country':'United Kingdom of Great Britain and Northern Ireland',
        'population':'8.9 million',
        'fact':'British capital',
    },
    'Paris':{
        'country':'France',
        'population':'2.2 million',
        'fact':'French capital',
    },
    'Berlin':{
        'country':'Germany',
        'population':'3.4 million',
        'fact':'German capital',
    },
}

for city, cityinfo in cities.items():
    print(f"{city}:")
    for cityinfo_key,cityinfo_value in cityinfo.items():
        print(f"\t{cityinfo_key}: {cityinfo_value}.")