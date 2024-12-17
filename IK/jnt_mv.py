import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Arm Parameters
L1 = 4  # Length of the first link
L2 = 10  # Length of the second link
theta1_start, theta1_end = math.radians(0), math.radians(80)  # Start and end angles for joint 1
theta2_start, theta2_end = math.radians(45), math.radians(-90)  # Start and end angles for joint 2
num_frames = 60  # Number of steps for the motion

# Function to calculate the position of each joint
def get_joint_positions(theta1, theta2, L1, L2):
    x1, y1 = L1 * math.cos(theta1), L1 * math.sin(theta1)
    x2, y2 = x1 + L2 * math.cos(theta1 + theta2), y1 + L2 * math.sin(theta1 + theta2)
    return (0, 0), (x1, y1), (x2, y2)

# Generate trajectory for the angles
theta1_values = [theta1_start + t * (theta1_end - theta1_start) / num_frames for t in range(num_frames + 1)]
theta2_values = [theta2_start + t * (theta2_end - theta2_start) / num_frames for t in range(num_frames + 1)]

print(theta1_values)
print(theta2_values)

# Plotting
fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2 - 1, L1 + L2 + 1)
ax.set_ylim(-L1 - L2 - 1, L1 + L2 + 1)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

line, = ax.plot([], [], '-o', lw=2, markersize=8)

# Animation update function
def update(frame):
    base, joint1, joint2 = get_joint_positions(theta1_values[frame], theta2_values[frame], L1, L2)
    line.set_data([base[0], joint1[0], joint2[0]], [base[1], joint1[1], joint2[1]])
    return line,

ani = FuncAnimation(fig, update, frames=num_frames + 1, interval=100)
plt.title("2-Link Arm Movement in Joint Space")
plt.show()
