import math
import meep as mp
from meep import mpb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

num_bands = 10

k_points = [mp.Vector3(0.5),         # X
            mp.Vector3(),            # Gamma
            mp.Vector3(0, 0.5),      # Y
            mp.Vector3(0, 0.25),     # k
            mp.Vector3(0.5, 0.25),   # k'
            mp.Vector3(0.25),        # l
            mp.Vector3(0.25, 0.5)]   # l'

k_points = mp.interpolate(4, k_points)

###############################################################################################
########################################Star Geometry##########################################
# Read the data file into a DataFrame
df = pd.read_csv('/home/linuxmint/Documents/BandStructure/SMUs1.txt', header=None, names=['x', 'y'], delim_whitespace=True)

# Translate the x-coordinate by 1.581139
df['x'] = df['x'] + 1.581139

# Initialize geometry list
geometry = []

# Define the material for the cylinders
cylinder_material = mp.Medium(epsilon=12.9)

# Define the material for the background (corner cubes)
background_material = mp.Medium(epsilon=1.0)  # assuming air

# Cylinder radius
radius = 0.2

# Lattice boundary
boundary = 3.162278

# Loop through each row in the DataFrame to create cylinders
for index, row in df.iterrows():
    x, y = row['x'], row['y']
    
    # Full cylinder
    geometry.append(mp.Cylinder(material=cylinder_material,
                                center=mp.Vector3(x, y),
                                radius=radius,
                                height=0.2))


##########################End Geometry####################################################
##########################################################################################

# Resolution
resolution = 10  # pixels per distance unit

# Initialize the simulation

geometry_lattice = mp.Lattice(size = mp.Vector3(boundary, boundary),
                              basis1 = mp.Vector3(0, boundary),
                              basis2 = mp.Vector3(boundary, 0))

ms = mpb.ModeSolver(num_bands=num_bands,
                    k_points=k_points,
                    geometry=geometry,
                    geometry_lattice=geometry_lattice,
                    resolution=resolution)

#sim = mp.Simulation(cell_size=cell,
 #                   boundary_layers=[mp.PML(1.0)],
  #                  geometry=geometry,
   #                 resolution=resolution)


ms.run_tm()
tm_freqs = ms.all_freqs
tm_gaps = ms.gap_list
ms.run_te()
te_freqs = ms.all_freqs
te_gaps = ms.gap_list

# Initialize a plot
fig, ax = plt.subplots()

# Loop through each row in the DataFrame to create cylinders
for index, row in df.iterrows():
    x, y = row['x'], row['y']
    
    # Plot a full circle for each cylinder
    circle = patches.Circle((x, y), radius, edgecolor='blue', facecolor='blue')
    ax.add_patch(circle)

# Set aspect ratio and axis limits
ax.set_aspect('equal', 'box')
ax.set_xlim([0, boundary])
ax.set_ylim([0, boundary])

plt.show()


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = range(len(tm_freqs))
# Plot bands
# Scatter plot for multiple y values, see https://stackoverflow.com/a/34280815/2261298
for xz, tmz, tez in zip(x, tm_freqs, te_freqs):
    ax.scatter([xz]*len(tmz), tmz, color='blue')
    ax.scatter([xz]*len(tez), tez, color='red', facecolors='none')
ax.plot(tm_freqs, color='blue')
ax.plot(te_freqs, color='red')
ax.set_ylim([0, 0.9])
ax.set_xlim([x[0], x[-1]])

# Plot gaps
for gap in tm_gaps:
    if gap[0] > 1:
        ax.fill_between(x, gap[1], gap[2], color='blue', alpha=0.2)

for gap in te_gaps:
    if gap[0] > 1:
        ax.fill_between(x, gap[1], gap[2], color='red', alpha=0.2)


# Plot labels
ax.text(12, 0.04, 'TM bands', color='blue', size=15)
ax.text(13.05, 0.235, 'TE bands', color='red', size=15)

points_in_between = (len(tm_freqs) - 3) / 7
tick_locs = [i*points_in_between+i for i in range(7)]
tick_labs = ['X','Γ', 'Y', 'k', 'k`','l','l`']
ax.set_xticks(tick_locs)
ax.set_xticklabels(tick_labs, size=16)
ax.set_ylabel('frequency (c/a)', size=16)
ax.grid(True)

plt.show()


efields = []

def get_efields(ms, band):
    efields.append(ms.get_efield(band, bloch_phase=True))

ms.run_tm(mpb.output_at_kpoint(mp.Vector3(), mpb.fix_efield_phase,
          get_efields))

# Create an MPBData instance to transform the efields
md = mpb.MPBData(rectify=True, resolution=boundary, periods=3)

converted = []
for f in efields:
    # Get just the z component of the efields
    f = f[..., 0, 2]
    converted.append(md.convert(f))

# Get epsilon data from the ModeSolver object (replace ms with your actual ModeSolver object)
converted_eps = ms.get_epsilon()

# Limit the number of subplots to 9 (for a 3x3 grid)
n_plots = min(9, len(converted))

# Plotting
for i in range(1, n_plots + 1):  # start the loop from 1
    plt.subplot(330 + i)  # this will go from 331 to 339
    plt.contour(converted_eps.T, cmap='binary')
    plt.imshow(np.real(converted[i-1]).T, interpolation='spline36', cmap='RdBu', alpha=0.9)
    plt.axis('off')

plt.show()




