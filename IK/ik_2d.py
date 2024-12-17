import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def inverse_kinematics(x, y, L1, L2):
    distance_squared = x**2 + y**2
    if distance_squared > (L1 + L2)**2:
        return None, "Target is out of reach"
    
    cos_theta2 = (distance_squared - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = math.acos(cos_theta2)
    k1 = L1 + L2 * math.cos(theta2)
    k2 = L2 * math.sin(theta2)
    theta1 = math.atan2(y, x) - math.atan2(k2, k1)
    
    return (theta1, theta2), None

def plot_arm(ax, theta1, theta2, L1, L2):
    x1, y1 = L1 * math.cos(theta1), L1 * math.sin(theta1)
    x2, y2 = x1 + L2 * math.cos(theta1 + theta2), y1 + L2 * math.sin(theta1 + theta2)
    ax.clear()
    ax.plot([0, x1, x2], [0, y1, y2], '-o', linewidth=2, markersize=8)
    ax.scatter([x2], [y2], color='red')
    ax.set_xlim(-L1 - L2 - 1, L1 + L2 + 1)
    ax.set_ylim(-L1 - L2 - 1, L1 + L2 + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    ax.set_title("2-Link Arm Animation")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

# Parameters
L1 = 4
L2 = 3
target_x, target_y = 4, 4

angles, error = inverse_kinematics(target_x, target_y, L1, L2)
if error:
    print(error)
else:
    theta1, theta2 = angles
    num_frames = 50
    theta1_values = [theta1 * t / num_frames for t in range(num_frames + 1)]
    theta2_values = [theta2 * t / num_frames for t in range(num_frames + 1)]
    
    fig, ax = plt.subplots()
    def update(frame):
        plot_arm(ax, theta1_values[frame], theta2_values[frame], L1, L2)
    
    ani = FuncAnimation(fig, update, frames=num_frames + 1, interval=100)
    plt.show()
