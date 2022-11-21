import matplotlib.pyplot as plt

x1 = [2, 4, 6]
y1 = [3, 5, 7]

plt.plot(x1, y1, label = 'Line1')

x2 = [3, 5, 7]
y2 = [2, 4, 6]

plt.plot(x2, y2, label = 'Line2')


plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph- Two Lines')

plt.legend()

plt.show()

