#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct ChemicalElement {
    string name;
    double density;
    double radius;
    double mass;
    double eventrate;
    double metalratio;

    // Constructor
    ChemicalElement(string n, double ro, double r, double M, int Z)
        : name(n), density(ro), radius(r), mass(M), eventrate() , metalratio(ro * (r * r) / M){}
};

int main() {
   
    // g/cm^3; m ; g/mol ; Z ---> transforming into kg/m^3 ; m ; kg/mol ; Z
    vector<ChemicalElement> elements = {
        {"Hydrogen", 0.00008988, 53e-12, 1.008, 1},
        {"Helium", 0.0001786, 31e-12, 4.0026, 2},
        {"Lithium", 0.534, 152e-12, 6.94, 3},
        {"Beryllium", 1.85, 112e-12, 9.0122, 4},
        {"Boron", 2.34, 87e-12, 10.81, 5},
        {"Carbon", 2.267, 67e-12, 12.011, 6},
        {"Nitrogen", 0.0012506, 56e-12, 14.007, 7},
        {"Oxygen", 0.001429, 48e-12, 15.999, 8},
        {"Fluorine", 0.001696, 42e-12, 18.998, 9},
        {"Neon", 0.0008999, 38e-12, 20.180, 10},
        {"Sodium", 0.971, 190e-12, 22.990, 11},
        {"Magnesium", 1.738, 145e-12, 24.305, 12},
        {"Aluminum", 2.7, 118e-12, 26.982, 13},
        {"Silicon", 2.3296, 111e-12, 28.085, 14},
        {"Phosphorus", 1.82, 98e-12, 30.974, 15},
        {"Sulfur", 2.07, 88e-12, 32.06, 16},
        {"Chlorine", 0.003214, 79e-12, 35.45, 17},
        {"Argon", 0.0017837, 71e-12, 39.948, 18},
        {"Potassium", 0.862, 243e-12, 39.098, 19},
        {"Calcium", 1.54, 194e-12, 40.078, 20},
        {"Scandium", 2.989, 184e-12, 44.956, 21},
        {"Titanium", 4.54, 176e-12, 47.867, 22},
        {"Vanadium", 6.11, 171e-12, 50.942, 23},
        {"Chromium", 7.15, 166e-12, 51.996, 24},
        {"Manganese", 7.44, 161e-12, 54.938, 25},
        {"Iron", 7.874, 156e-12, 55.845, 26},
        {"Cobalt", 8.86, 152e-12, 58.933, 27},
        {"Nickel", 8.912, 149e-12, 58.693, 28},
        {"Copper", 8.96, 145e-12, 63.546, 29},
        {"Zinc", 7.14, 142e-12, 65.38, 30},
        {"Gallium", 5.91, 136e-12, 69.723, 31},
        {"Germanium", 5.323, 125e-12, 72.63, 32},
        {"Arsenic", 5.727, 114e-12, 74.922, 33},
        {"Selenium", 4.81, 103e-12, 78.971, 34},
        {"Bromine", 3.1028, 94e-12, 79.904, 35},
        {"Krypton", 0.003733, 88e-12, 83.798, 36},
        {"Rubidium", 1.532, 265e-12, 85.468, 37},
        {"Strontium", 2.64, 219e-12, 87.62, 38},
        {"Yttrium", 4.469, 212e-12, 88.906, 39},
        {"Zirconium", 6.506, 206e-12, 91.224, 40},
        {"Niobium", 8.57, 198e-12, 92.906, 41},
        {"Molybdenum", 10.22, 190e-12, 95.95, 42},
        {"Technetium", 11.5, 183e-12, 98, 43},
        {"Ruthenium", 12.37, 178e-12, 101.07, 44},
        {"Rhodium", 12.41, 173e-12, 102.91, 45},
        {"Palladium", 12.02, 169e-12, 106.42, 46},
        {"Silver", 10.49, 165e-12, 107.87, 47},
        {"Cadmium", 8.65, 161e-12, 112.41, 48},
        {"Indium", 7.31, 156e-12, 114.82, 49},
        {"Tin", 7.31, 145e-12, 118.71, 50},
        {"Antimony", 6.685, 133e-12, 121.76, 51},
        {"Tellurium", 6.24, 123e-12, 127.6, 52},
        {"Iodine", 4.93, 115e-12, 126.9, 53},
        {"Xenon", 0.005887, 108e-12, 131.29, 54},
        {"Cesium", 1.873, 298e-12, 132.91, 55},
        {"Barium", 3.594, 253e-12, 137.33, 56},
        {"Lanthanum", 6.145, 195e-12, 138.91, 57},
        {"Cerium", 6.77, 185e-12, 140.12, 58},
        {"Praseodymium", 6.77, 185e-12, 140.91, 59},
        {"Neodymium", 7.007, 175e-12, 144.24, 60},
        {"Promethium", 7.26, 169e-12, 145, 61},
        {"Samarium", 7.52, 162e-12, 150.36, 62},
        {"Europium", 5.244, 208e-12, 151.96, 63},
        {"Gadolinium", 7.895, 180e-12, 157.25, 64},
        {"Terbium", 8.23, 175e-12, 158.93, 65},
        {"Dysprosium", 8.55, 175e-12, 162.5, 66},
        {"Holmium", 8.795, 174e-12, 164.93, 67},
        {"Erbium", 9.066, 173e-12, 167.26, 68},
        {"Thulium", 9.321, 172e-12, 168.93, 69},
        {"Ytterbium", 6.965, 176e-12, 173.05, 70},
        {"Lutetium", 9.84, 174e-12, 174.97, 71},
        {"Hafnium", 13.31, 155e-12, 178.49, 72},
        {"Tantalum", 16.65, 146e-12, 180.95, 73},
        {"Tungsten", 19.25, 139e-12, 183.84, 74},
        {"Rhenium", 21.02, 137e-12, 186.21, 75},
        {"Osmium", 22.59, 135e-12, 190.23, 76},
        {"Iridium", 22.56, 136e-12, 192.22, 77},
        {"Platinum", 21.46, 139e-12, 195.08, 78},
        {"Gold", 19.32, 144e-12, 196.97, 79},
        {"Mercury", 13.5336, 149e-12, 200.59, 80},
        {"Thallium", 11.85, 148e-12, 204.38, 81},
        {"Lead", 11.342, 147e-12, 207.2, 82},
        {"Bismuth", 9.807, 146e-12, 208.98, 83},
        {"Polonium", 9.32, 144e-12, 209, 84},
        {"Astatine", 7, 143e-12, 210, 85},
        {"Radon", 0.00973, 120e-12, 222, 86},
        {"Francium", 1.87, 348e-12, 223, 87},
        {"Radium", 5.5, 283e-12, 226, 88},
        {"Actinium", 10.07, 215e-12, 227, 89},
        {"Thorium", 11.72, 206e-12, 232.04, 90},
        {"Protactinium", 15.37, 200e-12, 231.04, 91},
        {"Uranium", 19.1, 196e-12, 238.03, 92},
        {"Neptunium", 20.45, 190e-12, 237, 93},
        {"Plutonium", 19.86, 175e-12, 244, 94},
        {"Americium", 13.69, 173e-12, 243, 95},
        {"Curium", 13.51, 174e-12, 247, 96},
        {"Berkelium", 14.78, 170e-12, 247, 97},
        {"Californium", 15.1, 186e-12, 251, 98},
        {"Einsteinium", 8.84, 186e-12, 252, 99},
        {"Fermium", 19.1, 175e-12, 257, 100},

        
    };

    const double Nbeam=5*1e5;
    const double NA=6.022*1e23;
    const double l=0.03;

    for (auto& elem : elements) {
        elem.mass/=1000;
        elem.density*=1000;
    }
    
    for (auto& elem : elements) {
        double luminosity=Nbeam*NA*elem.density/elem.mass*l;
        double sigma=3.14*elem.radius*elem.radius;
        elem.eventrate =luminosity*sigma;
        elem.metalratio=elem.density*elem.radius*elem.radius/elem.mass;
    }

    for (const auto& elem : elements) {
         if( elem.name=="Iron" || elem.name == "Tungsten" || elem.name== "Barium" ||  elem.name=="Beryllium" )
        
         {cout << elem.name << ": " << elem.metalratio  << "\n";
             cout<<elem.eventrate<<" reactions/second \n";}
    }
    
    return 0;
}
