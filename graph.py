#graph example using matplotlib#
'''
draw line plot (y=ax)
save it as png file
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend('agg')

y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = np.arange(10)
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, y, label='$y = numbers')
plt.title('Legend inside')
ax.legend()
# plt.show()

fig.savefig('plot.png')
