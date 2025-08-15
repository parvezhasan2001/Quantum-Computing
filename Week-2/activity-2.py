import cmath
import matplotlib.pyplot as plt
import numpy as np

# ===== Function: Plot Complex Numbers =====
def plot_complex_numbers(nums, labels, title):
    plt.figure()
    for num, label in zip(nums, labels):
        plt.quiver(0, 0, num.real, num.imag, angles='xy', scale_units='xy', scale=1, label=label)
    plt.axhline(0, color='gray', linewidth=1)
    plt.axvline(0, color='gray', linewidth=1)
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title(title)
    plt.legend()
    plt.show()

# ===== Function: Convert Polar → Cartesian =====
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

# ===== Function: Convert Cartesian → Polar =====
def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

# ===== Main Script =====
if __name__ == "__main__":
    print("Complex Number Operations and Visualizations")
# Step 1: Take two complex numbers
a1 = complex(input("Enter first complex number (e.g. 3+4j): "))
b2 = complex(input("Enter second complex number (e.g. 1+2j): "))

# Step 2: Perform operations
add_res = a1 + b2
sub_res = a1 - b2
mul_res = a1 * b2
div_res = a1 / b2

# Step 3: Display results
print("\n=== Complex Number Operations ===")
print(f"Addition: {add_res}")
print(f"Subtraction: {sub_res}")
print(f"Multiplication: {mul_res}")
print(f"Division: {div_res}")

# Step 4: Visualize each operation
plot_complex_numbers([a1, b2, add_res], ['a1', 'b2', 'a1+b2'], "Addition of Complex Numbers")
plot_complex_numbers([a1, -b2, sub_res], ['a1', '-b2', 'a1-b2'], "Subtraction of Complex Numbers")
plot_complex_numbers([a1, b2, mul_res], ['a1', 'b2', 'a1*b2'], "Multiplication of Complex Numbers")
plot_complex_numbers([a1, b2, div_res], ['a1', 'b2', 'a1/b2'], "Division of Complex Numbers")

# Step 5: Polar ↔ Cartesian Conversion
print("\n=== Polar & Cartesian Conversion ===")
r, theta = cartesian_to_polar(a1.real, a1.imag)
print(f"a1 in Polar form: r = {r:.2f}, θ = {np.degrees(theta):.2f}°")

x, y = polar_to_cartesian(r, theta)
print(f"Polar back to Cartesian: x = {x:.2f}, y = {y:.2f}")

# Visualize Polar → Cartesian
plt.figure()
plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='red', label='Polar → Cartesian')
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)
plt.grid(True)
plt.axis('equal')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Polar to Cartesian Conversion')
plt.legend()
plt.show()
