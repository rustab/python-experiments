import matplotlib.pyplot as plt
import numpy as np
import time

mind = [65,60,75,80,80,80,60,90,95,95,90,90,90,90,95]
effort = [80,90,90,90,75,60,70,65,70,80,75,80,65,75,85]
timex = [32,52,90,93,75,30,70,65,65,80,55,80,65,75,85]

print(np.__version__)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(time)

ax.scatter(3,2,3,'o')
ax.set_xlabel("Mind")
ax.set_ylabel("Effort")
ax.set_zlabel("Time")


plt.show()