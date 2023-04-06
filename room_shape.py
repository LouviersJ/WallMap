# Import nml_bag and other modules
import nml_bag
import numpy as np
import matplotlib.pyplot as plt
# run `python3 -c "from room_shape import Costmap; m = Costmap(100,100);"`
class Costmap:
	def __init__(self, dim):
		# Read in bag files
		bag = nml_bag.Reader("new_room_outline_bag")
		second_bag = nml_bag.Reader("new_room_obstacles_record")
		x = []
		y = []
		x_2 = []
		y_2 = []

		# Create position array for the room outline and teleop path
		for record in bag.records:
		    x.append((record.get('pose').get('pose').get('position').get('x'))+4.7)
		    y.append((record.get('pose').get('pose').get('position').get('y')))
		for record in second_bag.records:
		    x_2.append((record.get('pose').get('pose').get('position').get('x'))+4.7)
		    y_2.append(record.get('pose').get('pose').get('position').get('y'))
		
		# Cutting off ends of teleop path to make fill method clean
		x_2 = x_2[700:]
		y_2 = y_2[700:]
		
		x_2 = x_2[:1300]
		y_2 = y_2[:1300]
		
		
		# Converting inputed dimension
		x_dim = int(11/dim)
		y_dim = int(4/dim)

		#Create costmap overlay
		data = np.random.rand(x_dim,y_dim)
		data = np.zeros_like(data)
		squares_x = []
		squares_y = []
		path_x = []
		path_y = []
		
		# Create costmap squares and path squares
		for x_point, y_point in zip(x,y):
			data[round((y_point*(y_dim/4))),round((x_point*(x_dim/11)))]=0.5
			squares_x.append((round(x_point*(x_dim/11)))/(x_dim/11))
			squares_y.append((round(y_point*(y_dim/4)))/(y_dim/4))

		for x_point, y_point in zip(x_2,y_2):
			data[round((y_point*(y_dim/4))),round((x_point*(x_dim/11)))]=0.5
			path_x.append((round(x_point*(x_dim/11)))/(x_dim/11))
			path_y.append((round(y_point*(y_dim/4)))/(y_dim/4))
		
		# Filling in costmap
		plt.fill(squares_x,squares_y, alpha=0.25)
		plt.fill(path_x, path_y, alpha = 0.8)
		
		plt.imshow(data, cmap='viridis', origin = "upper right", aspect="auto", alpha = 0.25, extent = [0,4,0,11])
		plt.colorbar()

		# Plot room outline and teleop path
		#plt.plot(x, y, label = "Room outline")
		
		#plt.plot(x_2,y_2, label = "teleop path around obstacles")

		plt.xlabel("x")
		plt.ylabel("y")

		plt.title("Room costmap")
		plt.legend(loc = "upper left")
		plt.show()
