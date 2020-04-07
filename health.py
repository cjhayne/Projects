import csv
import matplotlib.pyplot as plt

def worst_county(year, path):
    counties = info
    #list of counties information that correspond to the state provided in the parameter
    county_year_lst = []
    #iterates thorugh the list
    for county in counties:
        #checks to see if the key "Years" is equeal to the year provided within the parameter
        if county["Year"] == year:
            #if so, appends it to the county_year_lst
            county_year_lst.append(county)

    #the worst county starts out as the first item in the list
    worst_county = county_year_lst[0]
    #the minumum average is the male + female life expectancy for that county
    min_avg = (worst_county["Male life expectancy (years)"] + worst_county["Female life expectancy (years)"]) / 2
    average = 0
    #iterates through the counties in the county_year_lst
    for county in county_year_lst:
        #looks at the current county and finds the average life expectancy of males + females
        average = (county["Male life expectancy (years)"] + county["Female life expectancy (years)"]) / 2
        #if that county's average is lower than the current minimum averege "min_avg"
        if average < min_avg:
            #the new min_avg equals the average for that county
            min_avg = average
            #and the worst county changes to become the info from that current county
            worst_county = county
    result = worst_county["State"] + "  " + worst_county["County"]
    return result.split("  ")

def plotdata(state, county, filename):
    counties = info

    #a list of the county's information from each year
    county_each_year = []

    #iterates through every county
    for item in counties:
        #checks to see if the current county "item"'s county equals the county parameter and also if the current  county "item"'s state is equal to the state parameter
        if item["County"] == county and item["State"] == state:
            #if so, it appends that county's information "item" into the county_each_year list
            county_each_year.append(item)

    #sorts the counties by year
    county_each_year.sort(key = lambda x:x["Year"])
    #creates emply lists
    years = []
    #le means life expectancy
    male_county_le = []
    male_state_le = []
    male_nation_le = []

    female_county_le = []
    female_state_le = []
    female_nation_le = []

    for item in county_each_year:
        #appends each year to the year list and does similar to the following below with each corresponding list
        years.append(item["Year"])
        #cle means county life expectancy
        #sle means state life expectancy
        #nle means national life expectancy
        male_cle = item["Male life expectancy (years)"]
        male_sle = item["Male life expectancy (state, years)"]
        male_nle = item["Male life expectancy (national, years)"]
        male_county_le.append(male_cle)
        male_state_le.append(male_sle)
        male_nation_le.append(male_nle)

        female_cle = item["Female life expectancy (years)"]
        female_sle = item["Female life expectancy (state, years)"]
        female_nle = item["Female life expectancy (national, years)"]
        female_county_le.append(female_cle)
        female_state_le.append(female_sle)
        female_nation_le.append(female_nle)

    #plotting 
    #RESOURCE TO PLOT: https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
    #RESOURCE TO USE LINESTYLE: https://matplotlib.org/3.1.1/tutorials/intermediate/legend_guide.html
    fig = plt.figure()
    plt.plot(years,female_county_le, label="Female in County", linestyle=":")
    plt.plot(years, female_state_le, label="Female in State", linestyle="--")
    plt.plot(years, female_nation_le, label="Female in Nation", linestyle="-")
    plt.plot(years,male_county_le, label="Male in County", linestyle=":")
    plt.plot(years, male_state_le, label="Male in State", linestyle="--")
    plt.plot(years, male_nation_le, label="Male in Nation", linestyle="-")
    plt.xlabel("Years")
    plt.ylabel("Life Expectancy")
    plt.title("%s, %s: Life expectancy" % (county, state))
    plt.legend()
    plt.show()
    #RESOURCE: https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
    fig.savefig("Assignent50_graph.png")
    

if __name__ == "__main__":
    filename = "Assignment50/data.csv"

    data = open(filename,"r")
    info = list(csv.DictReader(data))

    #making data easier to use
    for county in info:
        #capitalizes each word of each county's name as well as each word in each state
        county["County"] = county["County"].title()
        county["State"] = county["State"].title()
        #turns string values that should be integers or floats into integers or floats
        county["Year"] = int(county["Year"])
        county["fips"] = int(county["fips"])
        county["Female life expectancy (state, years)"] = float(county["Female life expectancy (state, years)"])
        county["Female life expectancy (years)"] = float(county["Female life expectancy (years)"])
        county["Female life expectancy (national, years)"] = float(county["Female life expectancy (national, years)"])
        county["Male life expectancy (years)"] = float(county["Male life expectancy (years)"])
        county['Male life expectancy (national, years)'] = float(county["Male life expectancy (national, years)"])
        county["Male life expectancy (state, years)"] = float(county["Male life expectancy (state, years)"])
 
    state,county = worst_county(2005,filename)
    plotdata(state,county,filename)
