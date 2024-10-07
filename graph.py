# import matplotlib.pyplot as plt

# xmin = -10
# xmax = 10
# ymin = -10
# ymax = 10

# fig, ax = plt.subplots()
# plt.axis([xmin, xmax, ymin, ymax])  # window size
# plt.plot([xmin, xmax], [0, 0], 'b')  # blue x axis
# plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis

# for x in range(10):
#     y = 0.5*x + 1
#     plt.plot([x], [y], 'ro')

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# xmin = -10
# xmax = 10
# ymin = -10
# ymax = 10
# points = 2*(xmax-xmin)
# x = np.linspace(xmin, xmax, points)

# fig, ax = plt.subplots()
# plt.axis([xmin, xmax, ymin, ymax])  # window size
# plt.plot([xmin, xmax], [0, 0], 'b')  # blue x axis
# plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis

# ax.set_xlabel('x values')
# ax.set_ylabel('y values')
# ax.set_title('Some Graph')
# ax.grid(True)

# ax.set_xticks(np.arange(xmin, xmax, 2))
# ax.set_yticks(np.arange(ymin, ymax, 2))

# y = 2*x + 1
# plt.plot(x, y, label='y=2x+1')
# plt.plot([4], [6], 'ro', label='point')
# plt.plot(x, 3*x, label='steeper line')
# # plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x1 = 0
# y1 = 0
# x2 = 40
# y2 = 13

# # Develop the equation y = mx + b
# m = (y2 - y1) / (x2 - x1)
# b = y1 - m*x1
# print("y = ", m, "x + ", b)

# # For the graph
# xmin = 0
# xmax = 100
# ymin = 0
# ymax = 50

# # For the line on the graph
# y3 = m*xmin + b
# y4 = m*xmax + b

# # Basic setup for the graph
# fig, ax = plt.subplots()
# plt.axis([xmin, xmax, ymin, ymax])  # window size
# plt.plot([xmin, xmax], [0, 0], 'b')  # blue x axis
# plt.plot([0, 0], [ymin, ymax], 'b')  # blue y axis

# # Add details to the graph
# ax.set_xlabel("thousands")
# ax.set_ylabel("tons")
# ax.grid(True)
# # ax.set_xticks(np.arange(xmin, xmax, 2))
# # ax.set_yticks(np.arange(ymin, ymax, 1))


# # Plot the linear function as a red line
# plt.plot([xmin, xmax], [y3, y4], 'r')

# plt.show()


from datetime import datetime
from meteostat import Point, Daily
import matplotlib.pyplot as plt
import numpy as np


def C(x):
    return 10*x + 500


x_values = np.arange(0, 100, 1)

y_values = C(x_values)

plt.plot(x_values, y_values, label="C(x) = 10x + 500")

plt.xlabel('Number of Items Produced')
plt.ylabel('Cost in Dollars')
plt.title('Cost Function Plot')
plt.grid(True)
plt.legend()

plt.show()


def distance(t):
    return 54.07 * t


t_values = np.arange(0, 14, 0.1)

d_values = distance(t_values)

plt.plot(t_values, d_values, label="Distance Traveled")

plt.xlabel('Time in Hours')
plt.ylabel('Distance in Miles')
plt.title('Distance Traveled Over Time')
plt.grid(True)
plt.legend()

plt.show()


def trip_distance(gallons):
    return 30 * gallons


fuel_values = np.arange(0, 12, 1)

trip_distances = trip_distance(fuel_values)

plt.plot(fuel_values, trip_distances, label="Distance vs Fuel")

plt.xlabel('Fuel in Gallons')
plt.ylabel('Distance in Miles')
plt.title('Fuel Efficiency of a Car')

plt.grid(True)
plt.legend()

plt.show()


def fahrenheit_to_celsius(t):
    return (t - 32) * 5/9


celsius_values = np.arange(32, 213, 1)

celsius_convert = fahrenheit_to_celsius(celsius_values)

plt.plot(celsius_values, celsius_convert, label="Fahrenheit to Celsius")

plt.xlabel('Fahrenheit values')
plt.ylabel('Celsius values')
plt.title('Fahrenheit to Celsius Conversion')
plt.grid(True)
plt.legend()
plt.show()

x = np.linspace(-10, 10, 400)

y1 = 2 * x + 3
y2 = -x + 1

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label="y = 2x + 3", color="blue")
plt.plot(x, y2, label="y = -x + 1", color="red")
plt.title("Graph of the system of Equations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


location = Point(48.8566, 2.3522, 35)

start = datetime(2024, 2, 1)
end = datetime(2024, 2, 29)

data = Daily(location, start, end)
data = data.fetch()

plt.plot(data.index, data['tavg'], label='Avg Temp (°C)', color='blue')
plt.plot(data.index, data['tmax'], label='Max Temp (°C)', color='red')
plt.plot(data.index, data['prcp'], label='Precipitation (mm)', color='green')

plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()

plt.show()