# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1. write your update damages function here:

# Function to update damages
def damages_update(damage_list):
    damages_mod = []
    for damage in damage_list:
        if damage[-1:] == 'M':
            mod = float(damage[:-1])*1000000
            damages_mod.append(mod)
        elif damage[-1:] == 'B':
            mod = float(damage[:-1])*1000000000
            damages_mod.append(mod)
        else:
            damages_mod.append(damage)
    return damages_mod 

# Testing the function
damages_new = damages_update(damages)
# print(damages_new)


# 2. write your construct hurricane dictionary function here:

# Function to create a dictionary of hurricanes
def hurricanes_dictionary(Name, Month, Year, Max_Sustained_Wind, Areas_Affected, Damage, Death):
    hurricane_dic = {}
    for i in range(0, len(names)):
        hurricane = {}
        # First we update the list of hurricane's data
        hurricane.update({'name': Name[i], 'month': Month[i], 'year': Year[i],
                      'max_sustained_winds': Max_Sustained_Wind[i],
                      'areas_affected': Areas_Affected[i],'Damage': Damage[i],
                      'Deaths': Death[i]})
        # The we update the hurricane of hurricane's dictionary
        hurricane_dic.update({names[i]: hurricane})
    return hurricane_dic

hurricanes = hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_new, deaths)

# print(hurricanes)


# 3. write your construct hurricane by year dictionary function here:

# Function to create a dictionary of hurricanes ordered by year
def hurricanes_per_year(dictionary):
    hurricane_dic = {}
    for item in dictionary.items():
        # We get the year as a key
        key = item[1]['year']
        # If the key (year) exists in the dictionary, we  
        # add the existing hurricane dictionary in the list
        if key in hurricane_dic.keys():
            hurricane_dic[key].append(item[1])
        # If the key (year) doesn't exist in the dictionary,
        # we create a new list with the hurricane dictionary
        else:
            hurricane_dic.update({key: [item[1]]})
    return hurricane_dic

hurricanes_year = hurricanes_per_year(hurricanes)

# print(hurricanes_year[1932])


# 4. write your count affected areas function here:

# Function to create a dictionary of areas affected by a
# hurricane and the number of hurricanes
def hurricanes_areas_afected(dictionary):
    hurricanes_areas = {}
    for hurricane in dictionary.values():
        # We get the list of areas affected
        for area in hurricane['areas_affected']:
            # If the area exists, we add 1 to the value of the key
            if area in hurricanes_areas.keys():
                hurricanes_areas[area] = hurricanes_areas.get(area) + 1
            # If the area doesn't exists, we create the key with value 1
            else:
                hurricanes_areas.update({area: 1})
    return hurricanes_areas

areas_affected = hurricanes_areas_afected(hurricanes)

# print(areas_affected)


# 5. write your find most affected area function here:
def area_most_affected(dictionary):
    area_most = 'earth'
    total_hurricanes = 0
    for item in dictionary.items():
      if item[1] > total_hurricanes:
        area_most_affected = item[0]
        total_hurricanes = item[1]
    return (area_most_affected, total_hurricanes)

(area, tot_hurricanes) = area_most_affected(areas_affected)

# print(area + ': ' + str(tot_hurricanes) + ' hurricanes')


# 6. write your greatest number of deaths function here:
def hurricanes_deaths(dictionary):
    area_most = 'earth'
    total_deaths = 0
    for hurricane in dictionary.values():
        if hurricane['Deaths'] > total_deaths:
            total_deaths = hurricane['Deaths']
            area_most = hurricane['name']
    return (area_most, total_deaths)

(area, num_deaths) = hurricanes_deaths(hurricanes)

# print(area + ': ' + str(num_deaths) + ' deaths')


# 7. write your catgeorize by mortality function here:

# First I create a function for the mortality scale
def death_scale(deaths):
    if deaths == 0:
        return 0
    elif deaths > 0 and deaths <= 100:
        return 1
    elif deaths > 100 and deaths <= 500:
        return 2
    elif deaths > 500 and deaths <= 1000:
        return 3
    elif deaths > 1000 and deaths <= 10000:
        return 4
    elif deaths > 10000:
        return 5
  
# Then I create the function that classifies the hurricanes
# according to the mortality
def hurricanes_mortality_code(dictionary):
    hurricane_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for item in dictionary.values():
        code = death_scale(item['Deaths'])
        if code in hurricane_mortality.keys():
            hurricane_mortality[code].append(item['name'])
        else:
            print('Hurricane '+ item['name'] + ' has a not valid value')
    return hurricane_mortality
  
hurricanes_by_mortality = hurricanes_mortality_code(hurricanes)

# print(hurricanes_by_mortality)


# 8. write your greatest damage function here:
def hurricanes_damage(dictionary):
    area_most = 'earth'
    total_damage = 0
    for hurricane in dictionary.values():
        # If damage is not recorded, we ignore the data
        if hurricane['Damage'] == 'Damages not recorded':
            continue
        elif hurricane['Damage'] > total_damage:
            area_most = hurricane['name']
            total_damage = hurricane['Damage']
    return (area_most, total_damage)

(area, damages) = hurricanes_deaths(hurricanes)

# print(area + ': ' + str(damages) + '$')

# 9. write your catgeorize by damage function here:

# First I create a function for the damage scale
def damage_scale(damage):
    if damage == 0:
        return 0
    elif damage > 0 and damage <= 100000000:
        return 1
    elif damage > 100000000 and damage <= 1000000000:
        return 2
    elif damage > 1000000000 and damage <= 10000000000:
        return 3
    elif damage > 10000000000 and damage <= 50000000000:
        return 4
    elif damage > 50000000000:
        return 5

# Then I create the function that classifies the hurricanes
# according to the damage
def hurricanes_damage_code(dictionary):
    hurricane_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for item in dictionary.values():
        if item['Damage'] == 'Damages not recorded':
            continue
        else:
            code = damage_scale(item['Damage'])
            if code in hurricane_damage.keys():
                hurricane_damage[code].append(item['name'])
            else:
                continue
    return hurricane_damage

hurricanes_by_damage = hurricanes_damage_code(hurricanes)

# print(hurricanes_by_damage)
