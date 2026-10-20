import numpy as np

def pendulum_derivatives(t, state, g=9.81, L=1.0, c=0.0):
    theta, omega = state
    dtheta = omega
    domega = -(g / L) * np.sin(theta) - c * omega
    return np.array([dtheta, domega])