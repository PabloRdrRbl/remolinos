"""
Description: The following code creates the grid for a rectalgular wing using
             rectangular panels.
"""

import numpy as np

class Panel:

    def __init__(self, xa, xb, xc, xd, ya, yb, yc, yd):

        # Panel corners
        self.xa, self.ya = xa, ya
        self.xb, self.yb = xb, yb
        self.xc, self.yc = xc, yc
        self.xd, self.yd = xd, yd

        # Control point at 3/4 chord
        self.x_control = self.xa + 0.75 * (self.xb - self.xa)
        self.y_control = (self.ya + self.yd) / 2

        # Front of the horseshoe at 1/4 chord

        # Left point
        self.x1n = self.xa + 0.25 * (self.xb - self.xa)
        self.y1n = self.ya

        # Right point
        self.x2n = self.xa + 0.25 * (self.xb - self.xa)
        self.y2n = self.yd

        # Circulation
        self.gamma = 0.0


class Wing:

    def __init__(self, chord, span, m, n):

        self.chord = chord  # wing chord
        self.span = span  # wing span

        self.surface = chord * span


    def grid(self, m, n):

        self.m = m  # number of vertical panels
        self.n = n  # number of horizontal panels

        self.x = np.linspce(0, self.span/2, self.n+1)
        self.y = np.linspace(0, self.chord, self.m+1)

        # Coordinates of the nodes for the panels
        self.xx, self.yy = np.mesgrid(self.x, self.y)

        # Array of panels

        self.panels = np.empty(m*n, dtype=object)  # Each element of the array
                                                    # is an object Panel

        for j in range(n):
            for i in range(m):

                xcoor = [xx[i, j], xx[i+1, j], xx[i+1, j+1], xx[i, j+1]]
                ycoor = [yy[i, j], yy[i+1, j], yy[i+1, j+1], yy[i, j+1]]

                self.panels[i, j] = Panel(*xcoor, *ycoor)
