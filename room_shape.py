# Import nml_bag and other modules

import nml_bag

import numpy as np

import matplotlib.pyplot as plt

# Read in bag files and create position array for the room outline and teleop path
bag = nml_bag.Reader("room_outline_bag")
second_bag = nml_bag.Reader("room_obstacles_record")
x = []
y = []

x_2 = []
y_2 = []

for record in bag.records:
    x.append((((record.get('pose').get('pose').get('position').get('x'))-2.575706720352173)*-1)+0.493)
    y.append((((record.get('pose').get('pose').get('position').get('y'))-(-5.211787700653076))*-1)+0.25)

for record in second_bag.records:
    x_2.append(((record.get('pose').get('pose').get('position').get('x')-2.575706720352173)*-1)+0.493)
    y_2.append(((record.get('pose').get('pose').get('position').get('y')-(-5.211787700653076))*-1)+0.25)

# Plot room outline and teleop path
plt.plot(x, y, label = "Room outline")
plt.plot(x_2,y_2, label = "teleop path around obstacles")

plt.xlabel("x")
plt.ylabel("y")

plt.title("Room outline from odometry data")
plt.legend(loc = "upper left")

#Create costmap overlay
data = np.random.rand(40, 30 )
data = np.zeros_like(data)
data[32,7:10 ] = 0.5
data[31,6:13 ] = 0.5
data[30, 5:16] = 0.5
data[29,5:19 ] = 0.5
data[28,4:22 ] = 0.5
data[27,3:22 ] = 0.5
data[26,3:20 ] = 0.5
data[25,2:20 ] = 0.5
data[24,1:19 ] = 0.5
data[23,0:20 ] = 0.5
data[22,0:24 ] = 0.5
data[21,2:25 ] = 0.5
data[20,3:26 ] = 0.5
data[19,9:27 ] = 0.5
data[18,10:26] = 0.5
data[17,9:20 ] = 0.5
data[16,9:19 ] = 0.5
data[15,7:19 ] = 0.5
data[14,7:19 ] = 0.5
data[13,7:18 ] = 0.5
data[12,7:17 ] = 0.5
data[11,6:16 ] = 0.5
data[10,5:15 ] = 0.5
data[9,4:15  ] = 0.5
data[8,3:14  ] = 0.5
data[7,2:13  ] = 0.5
data[6,1:11  ] = 0.5
data[5,4:11  ] = 0.5
data[4,8:10  ] = 0.5
data[3,8:10  ] = 0.5
data[2,8:9   ] = 0.5
# Create obstacles
data[14,14:16] = 1
data[15,13:17] = 1
data[16,14:16] = 1

data[18,13:14] = 1
data[19,12:15] = 1
data[20,13:14] = 1

data[24,9:11] = 1
data[25, 8:12] = 1
data[26,9:11] = 1

# Plot the data as a costmap

plt.imshow(data, cmap='viridis', origin = "upper right", alpha = 0.25, aspect = "auto", extent = [0,2,0,4])

plt.colorbar()



plt.show()
