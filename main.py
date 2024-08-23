# simple bar and scatter plot
import numpy as np
from matplotlib import pyplot as plt
x = np.arange(7) # assume there are 5 students
y = (20,35,42,38,30,25,2) # their test scores
plt.bar(x,y) # Bar plot
# need to close the figure using show() or close(), if not closed any follow
#up plot commands will use same figure.
plt.show() # Try commenting this an run
plt.scatter(x,y) # scatter plot
plt.show()#Bar graph