import math
import matplotlib.pyplot as plt

def forward_kinematics(L1, L2, theta1, theta2):
    # Convert angles to radians
    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)
    
    # Calculate joint 1 position
    x1 = L1 * math.cos(theta1)
    y1 = L1 * math.sin(theta1)
    
    # Calculate end-effector position
    x = x1 + L2 * math.cos(theta1 + theta2)
    y = y1 + L2 * math.sin(theta1 + theta2)
    
    return (0, 0), (x1, y1), (x, y)  # Base, Joint 1, End-effector positions

def plot_arm(base, joint1, end_effector):
    # Unpack positions
    x_values = [base[0], joint1[0], end_effector[0]]
    y_values = [base[1], joint1[1], end_effector[1]]
    
    # Plot the arm
    plt.figure()
    plt.plot(x_values, y_values, '-o', label="Robot Arm")
    plt.scatter(*base, color='red', label="Base")
    plt.scatter(*end_effector, color='blue', label="End Effector")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(0, color='gray', linestyle='--')
    plt.grid()
    plt.legend()
    plt.title("2D Robotic Arm Visualization")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Example usage
L1, L2 = 3, 3  # Link lengths
theta1, theta2 = 70, 90  # Joint angles in degrees

base, joint1, end_effector = forward_kinematics(L1, L2, theta1, theta2)
print("Base:", base)
print("Joint 1:", joint1)
print("End Effector:", end_effector)

plot_arm(base, joint1, end_effector)
