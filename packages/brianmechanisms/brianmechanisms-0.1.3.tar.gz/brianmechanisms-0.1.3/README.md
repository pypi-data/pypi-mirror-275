# Brian Mechanisms Designer

# Brian Mechanisms

Brian Mechanisms is a Python module designed for engineers and developers to easily design and simulate various mechanical mechanisms and robots. It provides a collection of tools and algorithms for kinematic analysis, motion planning, and visualization of mechanical systems.

## Features

- Kinematic analysis for various types of mechanisms, including linkages, gears, and robotic arms.
- Motion planning algorithms for path generation and trajectory optimization.
- Visualization tools to create interactive plots and animations of mechanical systems.
- Integration with popular libraries such as NumPy and Matplotlib for scientific computing and visualization.

## Installation

You can install Brian Mechanisms using pip:

```bash
pip install brianmechanisms
```

## Usage 
### Locii
For plotting &/or animating output paths of rigid link mechanisms.

#### Examples

##### 1. Tusi Couple
```python
from brianmechanisms import Locii
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

link1 = {
    "points": {
         "O": 0, "A":1
    },
    "speed": 1,
    "equation": "np.cos(x), np.sin(x)",
    "origin":"{0,0}"
}

link2 = {
    "points": {
        "A":0, "B":1
    },
    "len_factor": 1,
    "speed_factor": 1,
    "speed_source": "link1.speed",
    "equation": "np.cos(speed_factor * speed_source * x), np.sin(speed_factor * speed_source * x)",
    "origin":"link1.A",
    "theta0": 1,
    "output": "B"
}
linksTemplate = {
    "link1": link1.copy(),
    "link2": link2.copy()
}

fig, axs = plt.subplots(1, 1)
locii = Locii(linksTemplate, {})
fig, ax = locii.plotOutPutPaths(title={"title": "Tusi Couple", "sub": "Subtitle Example"}, plotConfig={"ax":axs, "fig":fig, "legend":False, "axes":False, "mechanism_theta":45, "ani":True})
# 

ani3 = FuncAnimation(fig, locii.update, frames=np.arange(0, 360, 10), fargs=(ax, {"title": "Example Plot", "sub": "Subtitle Example"}, {"ax":ax, "fig":fig, "legend":False, "axes":False, "mechanism_theta":45, "ani":True}), interval=100)

plt.show()

```

Variables:

mechanism_theta - If present, mechanism will be plotted at the position given by theta


### Locii

```python
from brianmechanisms import Locii
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

link1 = {
    "points": {
         "O": 0, "A":1
    },
    "speed": 1,
    "equation": "np.cos(x), np.sin(x)",
    "origin":"{0,0}"
}

link2 = {
    "points": {
        "A":0, "B":1
    },
    "len_factor": 1,
    "speed_factor": 2,
    "speed_source": "link1.speed",
    "equation": "np.cos(speed_factor * speed_source * x), np.sin(speed_factor * speed_source * x)",
    "origin":"link1.A",
    "theta0": 1,
    "output": "B"
}

linksTemplate = {
    "link1": link1.copy(),
    "link2": link2.copy()
}

```