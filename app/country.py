import json


class Country():

    def getCapCity(self, countryName):
        # json file of all countries and their capital cities
        capitalCities = '/home/marcus/Glade/cities.json'

        # selecting entry field and content from user

        # loop through json file and append city to list if it matches user content
        readfile = open(capitalCities)
        data = json.load(readfile)
        for line in data["cities"]:
            if countryName.capitalize() == line["country"]:
                city = line["city"]
                return city

        readfile.close
