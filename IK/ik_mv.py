import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Arm Parameters
L1 = 4  # Length of the first link
L2 = 3  # Length of the second link

# Define start and end points for Cartesian Space trajectory
x_start, y_start = 4, 3
x_end, y_end = 6, 5
num_frames = 50  # Number of steps for the motion

# Linear interpolation for trajectory points
x_values = [x_start + t * (x_end - x_start) / num_frames for t in range(num_frames + 1)]
y_values = [y_start + t * (y_end - y_start) / num_frames for t in range(num_frames + 1)]

# Inverse Kinematics solver
def solve_inverse_kinematics(x, y, L1, L2):
    d = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = math.atan2(math.sqrt(1 - d**2), d)  # Elbow up solution
    theta1 = math.atan2(y, x) - math.atan2(L2 * math.sin(theta2), L1 + L2 * math.cos(theta2))
    return theta1, theta2

# Plotting
fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2 - 1, L1 + L2 + 1)
ax.set_ylim(-L1 - L2 - 1, L1 + L2 + 1)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

line, = ax.plot([], [], '-o', lw=2, markersize=8)

# Animation update function
def update(frame):
    x, y = x_values[frame], y_values[frame]
    theta1, theta2 = solve_inverse_kinematics(x, y, L1, L2)
    x1, y1 = L1 * math.cos(theta1), L1 * math.sin(theta1)
    x2, y2 = x1 + L2 * math.cos(theta1 + theta2), y1 + L2 * math.sin(theta1 + theta2)
    line.set_data([0, x1, x2], [0, y1, y2])
    return line,

ani = FuncAnimation(fig, update, frames=num_frames + 1, interval=100)
plt.title("2-Link Arm Straight-Line Motion in Cartesian Space")
plt.show()
