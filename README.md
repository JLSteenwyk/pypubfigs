<p align="center">
    <img src="https://github.com/JLSteenwyk/pypubfigs/pypubfigs_logo.png" alt="Logo" width="400">
</p>

<p align="center">
    <a href="https://github.com/jlsteenwyk/pypubfigs/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/jlsteenwyk/pypubfigs">
    </a>
    <a href="https://bsky.app/profile/jlsteenwyk.bsky.social">
        <img src="https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff">
    </a>
    <br />
    <a href="https://lbesson.mit-license.org/">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
    <a href="https://journals.asm.org/doi/10.1128/MRA.00871-21">
        <img src="https://zenodo.org/badge/DOI/10.1128/MRA.00871-21.svg">
    </a>
</p>

**`pypubfigs`** provides publication-quality themes and colorblind-friendly palettes for **seaborn** and **matplotlib**. This Python package helps scientists and researchers quickly create visually appealing, accessible, and professional figures for publications and presentations.

If you found `pypubfigs` helpful, please cite the original publication from its R equivalent:  
*ggpubfigs: Colorblind-Friendly Color Palettes and ggplot2 Graphic System Extensions for Publication-Quality Scientific Figures.*  
DOI: [10.1128/MRA.00871-21](https://jlsteenwyk.com/publication_pdfs/2021_Steenwyk_and_Rokas_Microbiology_Resource_Announcements.pdf)

<br />
<br />

## Guide
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Color Palettes](#color-palettes)
- [Table of Hex Codes](#table-of-hex-codes)
- [Themes](#themes)
- [FAQ](#faq)
- [Acknowledgements](#acknowledgements)

<br />
<br />

## Installation

```bash
pip install pypubfigs
```

<br />
<br />

## Quick Start

### With seaborn:
```python
import seaborn as sns
import matplotlib.pyplot as plt
from pypubfigs.themes import theme_big_simple
from pypubfigs.palettes import friendly_pal

# Set theme
move_legend = theme_big_simple()
sns.set_palette(friendly_pal('ito_seven'))

# Example plot
tips = sns.load_dataset('tips')
ax = sns.barplot(x='day', y='total_bill', hue='sex', data=tips)
move_legend(ax)
plt.show()
```

<br />

### With matplotlib:
```python
import matplotlib.pyplot as plt
from pypubfigs.themes import theme_big_grid
from pypubfigs.palettes import friendly_pal

# Set theme
move_legend = theme_big_grid()
palette = friendly_pal('bright_seven')

# Plot example data
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [30, 23, 15, 5]

plt.bar(x, y1, color=palette[0], label='Group 1')
plt.bar(x, y2, bottom=y1, color=palette[1], label='Group 2')

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Stacked Bar Plot')

ax = plt.gca()
move_legend(ax)
plt.show()
```

<br />
<br />

## Color Palettes

All color palettes in pypubfigs are colorblind-friendly, ensuring your figures are accessible to a broader audience.

### Discrete palette example:
```python
palette = friendly_pal("contrast_three")
```

### Continuous palette example:
```python
palette_continuous = friendly_pal("contrast_three", n=50, type="continuous")
```

## Table of Hex Codes
| Palettes       | Colors used                                                                     |
| -------------- | ------------------------------------------------------------------------------- |
| bright_seven   | #4477AA, #228833, #AA3377, #BBBBBB, #66CCEE, #CCBB44, #EE6677                   |
| contrast_three | #004488, #BB5566, #DDAA33                                                       |
| vibrant_seven  | #0077BB, #EE7733, #33BBEE, #CC3311, #009988, #EE3377, #BBBBBB                   |
| muted_nine     | #332288, #117733, #CC6677, #88CCEE, #999933, #882255, #44AA99, #DDCC77, #AA4499 |
| nickel_five    | #648FFF, #FE6100, #785EF0, #FFB000, #DC267F                                     |
| ito_seven      | #0072B2, #D55E00, #009E73, #CC79A7, #56B4E9, #E69F00, #F0E442                   |
| ibm_five       | #648FFF, #785EF0, #DC267F, #FE6100, #FFB000                                     |
| wong_eight     | #E69F00, #56B4E9, #009E73, #F0E442, #0072B2, #D55E00, #CC79A7, #000000          |
| tol_eight      | #332288, #117733, #44AA99, #88CCEE, #DDCC77, #CC6677, #AA4499, #882255          |
| zesty_four     | #F5793A, #A95AA1, #85C0F9, #0F2080                                              |
| retro_four     | #601A4A, #EE442F, #63ACBE, #F9F4EC                                              |

<br />
<br />

## Themes

### Themes work directly with both seaborn and matplotlib.

Publication-ready themes:
- theme_simple()
- theme_big_simple()
- theme_grid()
- theme_big_grid()
- theme_grey()

Presentation-ready themes:
- theme_black()
- theme_blue()
- theme_red()

<br />

### With seaborn:
```python
import seaborn as sns
import matplotlib.pyplot as plt
from pypubfigs import friendly_pal, theme_black

# Load sample dataset
tips = sns.load_dataset("tips")

# Apply theme
move_legend = theme_black()

# Set palette
sns.set_palette(friendly_pal("bright_seven"))

# Create a seaborn plot
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
move_legend(ax)

plt.title("Seaborn test with theme_black()")
plt.show()
```

### With matplotlib
```python
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
```

<br />
<br />

## FAQ
**Can I submit color palettes or themes to be incorporated into pypubfigs?**<br />
Yes! Submissions are encouraged, please feel free to contact me via  [twitter](https://twitter.com/jlsteenwyk) or from my [contact information](https://jlsteenwyk.com/contact.html). 

<br />
