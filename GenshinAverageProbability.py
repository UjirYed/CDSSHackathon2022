import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wish_total = pd.read_csv("wish_total.csv")
pulls = pd.read_csv("pulls.csv")

fourStarData = pulls.loc[(pulls["rarity"] == 4) & (pulls["pity"] <= 10)]
fiveStarData = pulls.loc[(pulls["rarity"] == 5) & (pulls["pity"] <= 90)]



# finding the observed average probability (with soft pity)
# successful/total = sum(successful pulls at each pity) / sum (success at pity i x i)
sum1 = 0 # successful pulls at each pity
sum2 = 0 # success at pity i x i for each pity i
for pity in range(1,11):
    # number of four star wins with the assumed pity count
    num = fourStarData[fourStarData["pity"] == pity].shape[0]
    sum1 += num
    sum2 += num * pity

print("Observed avg prob for 4-star: " + str(sum1/sum2))


# finding the observed average probability (with soft pity)
# successful/total = sum(successful pulls at each pity) / sum (success at pity i x i)
sum1 = 0 # successful pulls at each pity
sum2 = 0 # success at pity i x i for each pity i
for pity in range(1,11):
    # number of four star wins with the assumed pity count
    num = fourStarData[fourStarData["pity"] == pity].shape[0]
    sum1 += num
    sum2 += num * pity

print("Observed avg prob for 4-star: " + str(sum1/ sum2) )


# finding the expected average probability (every prob is 0.051 except at 10 its 1)
# successful/total = sum(expected successful pulls at each pity) / sum (success at pity i x i)
sum1 = 0 # expected successful pulls = \sum(attempts at pity i)*0.051 + (attempts at pity 10)*1
sum2 = 0 # success at pity i x i for each pity i
for pity in range(1,10):
    # number of total four star attempts with the assumed pity count
    num = fourStarData[fourStarData["pity"] >= pity].shape[0]
    sum1 += num*0.051
# case where pity is 10
sum1 += fourStarData[fourStarData["pity"] == 10].shape[0]

for pity in range(1,11):
    sum2 += (fourStarData[fourStarData["pity"] == pity].shape[0])*pity

print("Expected avg prob for 4-star: " + str(sum1/ sum2) )




### Now for the five star case...

# finding the observed average probability (with soft pity)
# successful/total = sum(successful pulls at each pity) / sum (success at pity i x i)
sum1 = 0 # successful pulls at each pity
sum2 = 0 # success at pity i x i for each pity i
for pity in range(1,91):
    # number of four star wins with the assumed pity count
    num = fiveStarData[fiveStarData["pity"] == pity].shape[0]
    sum1 += num
    sum2 += num * pity

print("Observed avg prob for 5-star: " + str(sum1/ sum2) )


# finding the expected average probability (every prob is 0.006 except at 90 its 1)
# successful/total = sum(expected successful pulls at each pity) / sum (success at pity i x i)
sum1 = 0 # expected successful pulls = \sum(attempts at pity i)*0.006 + (attempts at pity 90)*1
sum2 = 0 # success at pity i x i for each pity i
for pity in range(1,90):
    # number of total four star attempts with the assumed pity count
    num = fiveStarData[fiveStarData["pity"] >= pity].shape[0]
    sum1 += num*0.006
# case where pity is 90
sum1 += fiveStarData[fiveStarData["pity"] == 90].shape[0]

for pity in range(1,91):
    sum2 += (fiveStarData[fiveStarData["pity"] == pity].shape[0])*pity

print("Expected avg prob for 5-star: " + str(sum1/ sum2) )

