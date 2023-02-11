import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
#Motivating Question: Based on banner, does the soft pity system still apply?

#To do this, we utilize the wish_total.csv data

#We do this by considering each banner dataset separately.


wish_total = pd.read_csv("wish_total.csv") #data extraction.

banners = ["beginners", "standard", "character-event", "weapon-event"] #list of possible banner events.

#defining a function to retrieve the percentage chance of success given a certain banner.
def bannerStats(banner):
    bannerData = wish_total[wish_total["bannerType"] == banner]
    totals = bannerData["total"].sum()
    numberofLegendaries = bannerData["legendary"].sum()
    numberofRares = bannerData["rare"].sum()
    percentLegendaries = numberofLegendaries / totals
    percentRares = numberofRares / totals
    return percentLegendaries, percentRares


bannerData = [bannerStats(banner) for banner in banners]

#plotting our data.
fig, (ax1,ax2,ax3, ax4) = plt.subplots(4,1, tight_layout = True)
bins = np.arange(0,2)

ax1.hist(x = bins, weights = bannerData[0])
ax2.hist(x = bins, weights = bannerData[1])
ax3.hist(x = bins, weights = bannerData[2])
ax4.hist(x = bins, weights = bannerData[3])

plt.show()

#We find that banners do not have significantly different probability distributions for prize success.