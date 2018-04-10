# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# read in all our data
kickstarters_2017 = pd.read_csv("D:\\work\\python\\DataClean\\ks-projects-201801.csv")

# set seed for reproducibility
np.random.seed(0)

# START : Scaling - We change the Range of the Data without changing the shape of distribution
# This means that you're transforming your data so that it fits within a specific scale, like 0-100 or 0-1.
# http://scikit-learn.org/stable/modules/preprocessing.html 
# or https://stats.stackexchange.com/questions/41704/how-and-why-do-normalization-and-feature-scaling-work/254815#254815

# select the usd_goal_real column
usd_goal = kickstarters_2017.usd_goal_real
print(usd_goal.head())
# scale the goals from 0 to 1
scaled_data = minmax_scaling(usd_goal, columns = [0])
print(scaled_data)
# plot the original & scaled data together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(kickstarters_2017.usd_goal_real, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")
plt.show(block=False)
# END : Scaling

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=(range(6)))
s2 = pd.Series([10, 9, 8, 7, 6, 5], index=(range(6)))
df = pd.DataFrame(s1, columns=['s1'])
df['s2'] = s2
print(df)
print(minmax_scaling(df, columns=['s1', 's2']))


# START : Scaling just changes the range of your data. 
# Normalization is to change your observations so that they can be described as a normal distribution (Bell Curve).
# get the index of all positive pledges (Box-Cox only takes postive values)
index_of_positive_pledges = kickstarters_2017.pledged > 0

# get only positive pledges (using their indexes)
positive_pledges = kickstarters_2017.pledged.loc[index_of_positive_pledges]

# normalize the pledges (w/ Box-Cox)
normalized_pledges = stats.boxcox(positive_pledges)[0]

# plot both together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(positive_pledges, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_pledges, ax=ax[1])
ax[1].set_title("Normalized data")
plt.show()
