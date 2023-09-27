import matplotlib.pyplot as plt
import numpy as np
import math

#data sets as arrays
x1 = [1, 4, 9, 16, 25, 36, 49, 64]
x2 = [1, 4, 9, 16, 25, 36, 49, 64]
x3 = [1, 4, 9, 16, 25, 36, 49, 64]

y1 = [1, 16, 30, 42,55, 68, 77,88]
y2 = [1,6,12,18,28, 40, 52, 65]
y3 = [1, 4, 9, 16, 25,36,49, 64]

#add figure from canvas coordinates (0.1, 0,1) to (0.9,0.9)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8]) #(x, y, len, wid)

plt.scatter(x1, y1, c='r')
plt.plot(x2, y2, 'go')
# plt.scatter(x3, y3, 'o')

ax.legend(labels = ('tv', 'watch', 'phone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()
