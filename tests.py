print("Loading 265 countries ...")
import matplotlib.pyplot as plt, csv, pylab, numpy, pandas as pd

year_list = ["1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]


"""not needed - different method used. dictreader (below)
with open('life-exp-data.csv', newline='') as csvfile:
    lifereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in lifereader:
        rows = []
        #print(', '.join(row))
        rows.append(', '.join(row))
        #print(row)
        #print(type(row))
        #print(len(row))

    print("Countries loaded.")"""
"""        print(row[len(row)-len(row)-1])
"""

user_country1 = input('Choose a country. Type a three-letter country code: ').upper()

with open('life-exp-data.csv', newline='') as csvdict:
    life_dict = csv.DictReader(csvdict, fieldnames=['Country Name','Country Code','Indicator Name','Indicator Code',"1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"])
    for row in life_dict:
        print(row['Country Name'], row['Country Code'])
        #print(row.keys())
        new_row = []
        if row['Country Code'] == user_country1:
            row_y = []
            for y in year_list:
                row_y.append(row[y])
            print(row_y)
            print(new_row)
            new_row_floats = [float(f) for f in new_row]
            print(new_row_floats)
            print("Row y")
            print(row_y)
            print(f"Length of row y: {len(row_y)}")
            row_y_floats = [float(g) for g in row_y]
    print("Countries loaded.")

user_country2 = input('Choose another country. Type a three-letter country code: ').upper()

with open('life-exp-data.csv', newline='') as csvdict:
    life_dict = csv.DictReader(csvdict, fieldnames=['Country Name','Country Code','Indicator Name','Indicator Code',"1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"])
    for row in life_dict:
        print(row['Country Name'], row['Country Code'])
        #print(row.keys())
        new_row2 = []
        if row['Country Code'] == user_country2:
            row_y2 = []
            for z in year_list:
                row_y2.append(row[z])
            print(row_y2)

            print(new_row2)
            new_row_floats2 = [float(f) for f in new_row2]
            print(new_row_floats2)
            print("Row y 2")
            print(row_y2)
            print(f"Length of row y 2: {len(row_y2)}")
            row_y_floats2 = [float(h) for h in row_y2]

x = year_list
y = row_y_floats

y2 = row_y_floats2



plt.plot(x, y, label=user_country1, color="red")
plt.plot(x, y2, label=user_country2, color="blue")
plt.xlabel('Year')
plt.ylabel('Average life expectancy')
plt.legend()
plt.title('Life expectancy over time')
plt.xticks([0, 10, 20, 30, 40, 50, 60], x[::10])

print(row_y_floats)
print(row_y_floats2)

# function to show the plot
plt.show()
"""
life_dict = csv.DictReader('life-exp-data.csv')
print(life_dict)
print(life_dict.items())"""

"""for b in rows:
            if b[1] == 'CHN':
                print("China!")
"""



print(row_y)

dict = []
"""get countries"""