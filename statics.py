# dictionary mapping the icons in the dataframe on emojis
emoji_dict={
    '01d':'☀️',
    '01n':'🌕',
    '02d':'🌤️',
    '02n':'☁️🌙',
    '03d':'☁️',
    '03n':'☁️🌙',
    '04d':'☁️',
    '04n':'☁️🌙',
    '09d':'🌧️',
    '09n':'🌧️🌙',
    '10d':'🌦️',
    '10n':'🌧️🌙',
    '11d':'⛈️',
    '11n':'⛈️',
    '13d':'❄️',
    '13n':'❄️',
    '50d':'🌫️',
    '50n':'🌫️'
}

# list of icons for the night
night_icons=['01n', '02n', '03n', '04n', '09n', '10n', '11n', '13n' '50n']

# function for rounding the temperature to ten degrees
def roundtempto10(x):
    return 10 * round(x/10)

# dictionary of tips based on the temperature
temp_dict={
    -10: 'Put on warm clothes and drink a warm cup of tea',
    0: 'Put on warm clothes',
    10: "It's the perfect temperature to do something outside!",
    20: "Wear light clothes and don't forget your sunnies!",
    30: "Wear light clothes, drink a lot of water and don't forget suncream",
    40: "It's way too hot - hitzefrei!"
}

# function for getting tips based on the wind speed
def wind_tips(row):
    if(5 <= row['wind.speed'] and row['wind.speed'] < 10):
        return 'Watch out - your hat may get blown off'
    if(10 <= row['wind.speed'] and row['wind.speed'] < 17):
        return 'Watch out for branches falling from the trees'
    if(17 <= row['wind.speed'] and row['wind.speed'] < 28):
        return 'Be careful when staying outside trees can fall over and things can fly around'
    if(28 <= row['wind.speed']):
        return "Stay inside - there's a heavy storm going on"
    else:
        return ""

# dictionary for getting rain tips based on the id 
rain_dict={
    500: "Take an umbrella or a rain jacket with you",
    501: "Take an umbrella or a rain jacket with you",
    502: "Take an umbrella or a rain jacket with you",
    503: "Take an umbrella or a rain jacket with you",
    504: "Take an umbrella or a rain jacket with you",
    511: "Take an umbrella or a rain jacket with you",
    520: "Take an umbrella or a rain jacket with you",
    521: "Take an umbrella or a rain jacket with you",
    522: "Take an umbrella or a rain jacket with you",
    531: "Take an umbrella or a rain jacket with you",
    200: "Better stay inside - there's a thunderstorm going on",
    201: "Better stay inside - there's a thunderstorm going on",
    202: "Better stay inside - there's a thunderstorm going on",
    210: "Better stay inside - there's a thunderstorm going on",
    211: "Better stay inside - there's a thunderstorm going on",
    212: "Better stay inside - there's a thunderstorm going on",
    221: "Better stay inside - there's a thunderstorm going on",
    230: "Better stay inside - there's a thunderstorm going on",
    231: "Better stay inside - there's a thunderstorm going on", 
    232: "Better stay inside - there's a thunderstorm going on"
}

# dictionary for getting snow tips based on the icon
snow_dict={
    '13d': "Put winter tires on your car and watch out to not slip outside!"
}

# function for getting all the defined tips into one string and checking if it's night time
def all_tips(row):
    tip = ""
    if row['night_tips'] == "":
        if row['temp_tips'] != '':
            tip = tip + row['temp_tips'] + '<br>'
        if row['rain_tips'] != '':
            tip = tip + row['rain_tips'] + '<br>'
        if row['wind_tips'] != '':
            tip = tip + row['wind_tips'] + '<br>'
        if row['snow_tips'] != '':
            tip = tip + row['snow_tips'] + '<br>'
    else:
        tip = row['night_tips']
    if tip == "":
        return "-"
    else:
        return tip