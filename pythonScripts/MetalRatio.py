import matplotlib.pyplot as plt

# Define the chemical elements data
elements = [
    {"name": "Hydrogen", "density": 0.00008988, "radius": 53e-12, "mass": 1.008, "Z": 1},
    {"name": "Helium", "density": 0.0001786, "radius": 31e-12, "mass": 4.0026, "Z": 2},
    {"name": "Lithium", "density": 0.534, "radius": 152e-12, "mass": 6.94, "Z": 3},
    {"name": "Beryllium", "density": 1.85, "radius": 112e-12, "mass": 9.0122, "Z": 4},
    {"name": "Boron", "density": 2.34, "radius": 87e-12, "mass": 10.81, "Z": 5},
    {"name": "Carbon", "density": 2.267, "radius": 67e-12, "mass": 12.011, "Z": 6},
    {"name": "Nitrogen", "density": 0.0012506, "radius": 56e-12, "mass": 14.007, "Z": 7},
    {"name": "Oxygen", "density": 0.001429, "radius": 48e-12, "mass": 15.999, "Z": 8},
    {"name": "Fluorine", "density": 0.001696, "radius": 42e-12, "mass": 18.998, "Z": 9},
    {"name": "Neon", "density": 0.0008999, "radius": 38e-12, "mass": 20.180, "Z": 10},
    {"name": "Sodium", "density": 0.971, "radius": 190e-12, "mass": 22.990, "Z": 11},
    {"name": "Magnesium", "density": 1.738, "radius": 145e-12, "mass": 24.305, "Z": 12},
    {"name": "Aluminum", "density": 2.7, "radius": 118e-12, "mass": 26.982, "Z": 13},
    {"name": "Silicon", "density": 2.3296, "radius": 111e-12, "mass": 28.085, "Z": 14},
    {"name": "Phosphorus", "density": 1.82, "radius": 98e-12, "mass": 30.974, "Z": 15},
    {"name": "Sulfur", "density": 2.07, "radius": 88e-12, "mass": 32.06, "Z": 16},
    {"name": "Chlorine", "density": 0.003214, "radius": 79e-12, "mass": 35.45, "Z": 17},
    {"name": "Argon", "density": 0.0017837, "radius": 71e-12, "mass": 39.948, "Z": 18},
    {"name": "Potassium", "density": 0.862, "radius": 243e-12, "mass": 39.098, "Z": 19},
    {"name": "Calcium", "density": 1.54, "radius": 194e-12, "mass": 40.078, "Z": 20},
    {"name": "Scandium", "density": 2.989, "radius": 184e-12, "mass": 44.956, "Z": 21},
    {"name": "Titanium", "density": 4.54, "radius": 176e-12, "mass": 47.867, "Z": 22},
    {"name": "Vanadium", "density": 6.11, "radius": 171e-12, "mass": 50.942, "Z": 23},
    {"name": "Chromium", "density": 7.15, "radius": 166e-12, "mass": 51.996, "Z": 24},
    {"name": "Manganese", "density": 7.44, "radius": 161e-12, "mass": 54.938, "Z": 25},
    {"name": "Iron", "density": 7.874, "radius": 156e-12, "mass": 55.845, "Z": 26},
    {"name": "Cobalt", "density": 8.86, "radius": 152e-12, "mass": 58.933, "Z": 27},
    {"name": "Nickel", "density": 8.912, "radius": 149e-12, "mass": 58.693, "Z": 28},
    {"name": "Copper", "density": 8.96, "radius": 145e-12, "mass": 63.546, "Z": 29},
    {"name": "Zinc", "density": 7.14, "radius": 142e-12, "mass": 65.38, "Z": 30},
    {"name": "Gallium", "density": 5.91, "radius": 136e-12, "mass": 69.723, "Z": 31},
    {"name": "Germanium", "density": 5.323, "radius": 125e-12, "mass": 72.63, "Z": 32},
    {"name": "Arsenic", "density": 5.727, "radius": 114e-12, "mass": 74.922, "Z": 33},
    {"name": "Selenium", "density": 4.81, "radius": 103e-12, "mass": 78.971, "Z": 34},
    {"name": "Bromine", "density": 3.1028, "radius": 94e-12, "mass": 79.904, "Z": 35},
    {"name": "Krypton", "density": 0.003733, "radius": 88e-12, "mass": 83.798, "Z": 36},
    {"name": "Rubidium", "density": 1.532, "radius": 265e-12, "mass": 85.468, "Z": 37},
    {"name": "Strontium", "density": 2.64, "radius": 219e-12, "mass": 87.62, "Z": 38},
    {"name": "Yttrium", "density": 4.469, "radius": 212e-12, "mass": 88.906, "Z": 39},
    {"name": "Zirconium", "density": 6.506, "radius": 206e-12, "mass": 91.224, "Z": 40},
    {"name": "Niobium", "density": 8.57, "radius": 198e-12, "mass": 92.906, "Z": 41},
    {"name": "Molybdenum", "density": 10.22, "radius": 190e-12, "mass": 95.95, "Z": 42},
    {"name": "Technetium", "density": 11.5, "radius": 183e-12, "mass": 98, "Z": 43},
    {"name": "Ruthenium", "density": 12.37, "radius": 178e-12, "mass": 101.07, "Z": 44},
    {"name": "Rhodium", "density": 12.41, "radius": 173e-12, "mass": 102.91, "Z": 45},
    {"name": "Palladium", "density": 12.02, "radius": 169e-12, "mass": 106.42, "Z": 46},
    {"name": "Silver", "density": 10.49, "radius": 165e-12, "mass": 107.87, "Z": 47},
    {"name": "Cadmium", "density": 8.65, "radius": 161e-12, "mass": 112.41, "Z": 48},
    {"name": "Indium", "density": 7.31, "radius": 156e-12, "mass": 114.82, "Z": 49},
    {"name": "Tin", "density": 7.31, "radius": 145e-12, "mass": 118.71, "Z": 50},
    {"name": "Antimony", "density": 6.685, "radius": 133e-12, "mass": 121.76, "Z": 51},
    {"name": "Tellurium", "density": 6.24, "radius": 123e-12, "mass": 127.6, "Z": 52},
    {"name": "Iodine", "density": 4.93, "radius": 115e-12, "mass": 126.9, "Z": 53},
    {"name": "Xenon", "density": 0.005887, "radius": 108e-12, "mass": 131.29, "Z": 54},
    {"name": "Cesium", "density": 1.873, "radius": 298e-12, "mass": 132.91, "Z": 55},
    {"name": "Barium", "density": 3.594, "radius": 253e-12, "mass": 137.33, "Z": 56},
    {"name": "Lanthanum", "density": 6.145, "radius": 195e-12, "mass": 138.91, "Z": 57},
    {"name": "Cerium", "density": 6.77, "radius": 185e-12, "mass": 140.12, "Z": 58},
    {"name": "Praseodymium", "density": 6.77, "radius": 185e-12, "mass": 140.91, "Z": 59},
    {"name": "Neodymium", "density": 7.007, "radius": 175e-12, "mass": 144.24, "Z": 60},
    {"name": "Promethium", "density": 7.26, "radius": 169e-12, "mass": 145, "Z": 61},
    {"name": "Samarium", "density": 7.52, "radius": 162e-12, "mass": 150.36, "Z": 62},
    {"name": "Europium", "density": 5.244, "radius": 208e-12, "mass": 151.96, "Z": 63},
    {"name": "Gadolinium", "density": 7.895, "radius": 180e-12, "mass": 157.25, "Z": 64},
    {"name": "Terbium", "density": 8.23, "radius": 175e-12, "mass": 158.93, "Z": 65},
    {"name": "Dysprosium", "density": 8.55, "radius": 175e-12, "mass": 162.5, "Z": 66},
    {"name": "Holmium", "density": 8.795, "radius": 174e-12, "mass": 164.93, "Z": 67},
    {"name": "Erbium", "density": 9.066, "radius": 173e-12, "mass": 167.26, "Z": 68},
    {"name": "Thulium", "density": 9.321, "radius": 172e-12, "mass": 168.93, "Z": 69},
    {"name": "Ytterbium", "density": 6.965, "radius": 176e-12, "mass": 173.05, "Z": 70},
    {"name": "Lutetium", "density": 9.84, "radius": 174e-12, "mass": 174.97, "Z": 71},
    {"name": "Hafnium", "density": 13.31, "radius": 155e-12, "mass": 178.49, "Z": 72},
    {"name": "Tantalum", "density": 16.65, "radius": 146e-12, "mass": 180.95, "Z": 73},
    {"name": "Tungsten", "density": 19.25, "radius": 139e-12, "mass": 183.84, "Z": 74},
    {"name": "Rhenium", "density": 21.02, "radius": 137e-12, "mass": 186.21, "Z": 75},
    {"name": "Osmium", "density": 22.59, "radius": 135e-12, "mass": 190.23, "Z": 76},
    {"name": "Iridium", "density": 22.56, "radius": 136e-12, "mass": 192.22, "Z": 77},
    {"name": "Platinum", "density": 21.46, "radius": 139e-12, "mass": 195.08, "Z": 78},
    {"name": "Gold", "density": 19.32, "radius": 144e-12, "mass": 196.97, "Z": 79},
    {"name": "Mercury", "density": 13.5336, "radius": 149e-12, "mass": 200.59, "Z": 80},
    {"name": "Thallium", "density": 11.85, "radius": 148e-12, "mass": 204.38, "Z": 81},
    {"name": "Lead", "density": 11.342, "radius": 147e-12, "mass": 207.2, "Z": 82},
    {"name": "Bismuth", "density": 9.807, "radius": 146e-12, "mass": 208.98, "Z": 83},
    {"name": "Polonium", "density": 9.32, "radius": 144e-12, "mass": 209, "Z": 84},
    {"name": "Astatine", "density": 7, "radius": 143e-12, "mass": 210, "Z": 85},
    {"name": "Radon", "density": 0.00973, "radius": 120e-12, "mass": 222, "Z": 86},
    {"name": "Francium", "density": 1.87, "radius": 348e-12, "mass": 223, "Z": 87},
    {"name": "Radium", "density": 5.5, "radius": 283e-12, "mass": 226, "Z": 88},
    {"name": "Actinium", "density": 10.07, "radius": 215e-12, "mass": 227, "Z": 89},
    {"name": "Thorium", "density": 11.72, "radius": 206e-12, "mass": 232.04, "Z": 90},
    {"name": "Protactinium", "density": 15.37, "radius": 200e-12, "mass": 231.04, "Z": 91},
    {"name": "Uranium", "density": 19.1, "radius": 196e-12, "mass": 238.03, "Z": 92},
    {"name": "Neptunium", "density": 20.45, "radius": 190e-12, "mass": 237, "Z": 93},
    {"name": "Plutonium", "density": 19.86, "radius": 175e-12, "mass": 244, "Z": 94},
    {"name": "Americium", "density": 13.69, "radius": 173e-12, "mass": 243, "Z": 95},
    {"name": "Curium", "density": 13.51, "radius": 174e-12, "mass": 247, "Z": 96},
    {"name": "Berkelium", "density": 14.78, "radius": 170e-12, "mass": 247, "Z": 97},
    {"name": "Californium", "density": 15.1, "radius": 186e-12, "mass": 251, "Z": 98},
    {"name": "Einsteinium", "density": 8.84, "radius": 186e-12, "mass": 252, "Z": 99},
    {"name": "Fermium", "density": 19.1, "radius": 175e-12, "mass": 257, "Z": 100}
    # Continue adding other elements here...
]

# Calculate the expression and store the results
for elem in elements:
    elem["result"] = elem["density"] * 1e6 * (elem["radius"] ** 2) / elem["mass"]

# Extract Z and result values for plotting
Z_values = [elem["Z"] for elem in elements]
result_values = [elem["result"] for elem in elements]

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(Z_values, result_values, marker='o', linestyle='-', color='b')
plt.title('THE PLOT FOR THE METAL RATIO OVER Z')
plt.xlabel('Z')
plt.ylabel('METAL RATIO (mol/m)')
plt.grid(True)
plt.show()