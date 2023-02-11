#Overall Method:
# retrieve the time data.
# get the success rate of getting four star and five star data for each hour in the day.
    #do this by separating data into four and five star data
    # find sucess rate (#success / #total) for each hour of the day.
    #Graph it
# check if there is any difference.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extracting data from our spreadsheets.
wish_total = pd.read_csv("wish_total.csv")
pulls = pd.read_csv("pulls.csv")

#separating into four star and five star data to control for rarity.
fourStarData = pulls.loc[(pulls["rarity"] == 4) & (pulls["pity"] <= 10)]
fiveStarData = pulls.loc[(pulls["rarity"] == 5) & (pulls["pity"] <= 90)]

HourlySucessRate = [] # List to store the success rate per hour.

# separating data by the hour of the day the pull occurred and calculating success rate based on time of roll.
for hour in range(0,24):
    fourStarData['time'] = pd.to_datetime(fourStarData['time'])
    hourlyData = fourStarData[fourStarData['time'].dt.hour == hour]
    
    totalTrials = hourlyData["pity"].sum()
    success = hourlyData.shape[0]
    HourlySucessRate.append(success / totalTrials)

#plotting our data
fig, (axs, ax2) = plt.subplots(2,1, tight_layout = True)
bins = np.arange(1,25)

axs.hist(x = bins, weights = HourlySucessRate)

axs.set_xlabel("Hour of Roll")
axs.set_ylabel("Success Proportion")

for i in range(0,24):
    ax2.plot(i + 1, HourlySucessRate[i], marker = "o")

plt.show()

#we find that there is no real correlation between when you roll and your success in rolling a rare or legendary.