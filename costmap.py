import matplotlib.pyplot as plt
import numpy as np

# Generate some random data

data = np.random.rand(10, 10)



# Plot the data as a costmap

plt.imshow(data, cmap='viridis', origin = "upper right", alpha = 0.5)

plt.colorbar()

plt.show()
