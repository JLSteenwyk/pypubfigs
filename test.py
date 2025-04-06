import matplotlib.pyplot as plt
import numpy as np
from pypubfigs import friendly_pal, theme_black

# Apply theme
move_legend = theme_black()
palette = friendly_pal("bright_seven")

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot
plt.plot(x, y1, label='sin(x)', color=palette[0])
plt.plot(x, y2, label='cos(x)', color=palette[1])

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Matplotlib test with theme_black()")

# Apply custom legend positioning
ax = plt.gca()
move_legend(ax)

plt.show()
