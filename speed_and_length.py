from rel_rock import relativistic_rock
import numpy as np
import matplotlib.pyplot as plt

speeds = np.arange(1e5,2e8,1e4,dtype=int)
rel_mass = np.array([relativistic_rock(speed=s, length=1,time_interval=1).relativistic_mass() for s in speeds])
rel_length =  np.array([relativistic_rock(speed=s, length=1,time_interval=1).relativistic_length() for s in speeds])

fig, ax1 = plt.subplots()
plt.scatter(x=speeds,y=rel_mass)
plt.scatter(x=speeds,y=rel_length)
plt.xlabel("speed in m/s")
ax1.set_ylabel("relativistic mass (kg)",color="blue"),
ax2 = ax1.twinx()
ax2.set_ylabel("relativistic length (m)",color="red")
plt.figlegend()
plt.show()


rock1 = relativistic_rock(speed=1e8, length=1,time_interval=1)