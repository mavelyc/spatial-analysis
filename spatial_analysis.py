# import matplotlib.pyplot as plt

# plt.plot([1,2,3],[5,7,4])

# plt.show()

from shapely.geometry import Polygon

polygon = Polygon([(0,0),(1,1),(1,0)])
print (polygon.area)
print (polygon.length)