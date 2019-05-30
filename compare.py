import pandas as pd
from operator import itemgetter

dfs = pd.read_csv('us-city-data.csv')
dfc = pd.read_csv('country-data.csv')

f = open('testfile.txt', 'w+')


#Sort by the metric you want to compare to
#Choices are:
# Captial City Pop
# Largest City Pop
# Population
# mi2_total
# km2_total
# mi2_land
# km2_land
# mi2_water
# km2_water
# % water
def sortBy(metric):
    s = []
    c = []
    dfct = dfc[~dfc[metric].isnull()]
    dfct.reset_index(inplace=True)

    for label, content in dfs.iterrows():
        s.append([dfs.iloc[label][metric], dfs.iloc[label]["State"]])
    s.sort(key=itemgetter(0), reverse=True)

    for label, content in dfct.iterrows():
        c.append([dfct.iloc[label][metric], dfct.iloc[label]["Country"]])
    c.sort(key=itemgetter(0), reverse=True)

    return s, c


def compare(metric):
    sortedState, sortedCountry = sortBy(metric)
    for i in range(len(sortedState)):
        if i != len(sortedState)-1:
            t = (sortedState[i][0] + sortedState[i+1][0]) / 2
        else:
            t = 0       
        f.write('\n'+'\n'+sortedState[i][1]+": "+str(sortedState[i][0]))
        while sortedCountry[0][0] > t:
            f.write('\n'+"   "+str(sortedCountry[0][1]) +
                  ": "+str(int(sortedCountry[0][0])))
            sortedCountry.remove(sortedCountry[0])
            if sortedCountry == []:
                break


compare('Capital City Pop')
f.close()
