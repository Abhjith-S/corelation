import time
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns


"""............................"""

Month = "January"
TestArea = "PRE MONSOON(valankulam)"
saveToLoc = "C:/Users/hp/Desktop/Random/APPLICATION/HALL TICKETS/Test/"
CSV_FolderPath = 'data_cor.csv'
y_cord_Annotate = 120

""".........................."""

con = pd.read_csv(CSV_FolderPath)
HeadingList = []

"""Getting Months and area(may vary according to data)"""
for i in con.columns:
    HeadingList.append(i)
monthList = HeadingList[20:32]
AreaList = HeadingList[3:19]
"""Function to Draw Graph"""


def GetChart(month, area, path=None):
    slope, intercept, r_value, p_value, std_er = stats.linregress(con[month], con[area])
    R2Value = round(r_value ** 2, 3)
    print("slope = ", slope, "\nY Intercept = ", intercept, "\nR2 Value", R2Value, "Std Err =", std_er)
    # use the function regplot to make a scatterplot
    A = sns.regplot(x=con[area], y=con[month], line_kws={'color': 'red'}, scatter_kws={'color': 'green'})
    A.set_title(area, loc='left')
    A.set_title(f"R\u00b2 = {R2Value}\ny ={round(slope, 3)}x + {round(intercept, 3)}",loc='right')
    A.set_xlabel("AREA(sqkm)")
    A.set_ylabel("RAINFALL(mm)")
    time.sleep(5)
    B = A.get_figure()
    name = area + month
    if path:
        B.savefig(path + f"{name}.png")
    else:
        B.savefig(f"{name}.png")
    # to avoid plotting iver the same graph
    plt.clf()


"""Function Calling"""

for i in monthList:
    for j in AreaList:
        print("---------------")
        GetChart(i, j, saveToLoc)
        print("---------------")


def getProper():
    AllData = list()
    for a in monthList:
        for j in AreaList:
            slope, intercept, r_value, p_value, std_er = stats.linregress(con[a], con[j])
            rSq = round(r_value ** 2, 3)
            # dictdata = {a, j, slope, intercept, rSq, std_er}
            dictdata = {'month': a, "area": j, 'slope': slope, "intercept": intercept, "rSq": rSq, "stdEr":std_er}
            AllData.append(dictdata)
    AllDataNew = sorted(AllData, key=lambda d: d['stdEr'])
    print(AllDataNew)
    # for i in AllData:
        # print(i["stdEr"])


# getProper()