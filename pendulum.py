import numpy as np

def pendulum_derivatives(t, state, g=9.81, L=1.0, c=0.0):
    """
    Pendulum equation of motion in state-space form.

    Parameters
    ----------
    t : float
        Current time (not used for autonomous systems).
    state : array-like, shape (2,)
        [theta, omega] — angle (rad) and angular velocity (rad/s).
    g : float
        Gravitational acceleration (m/s^2).
    L : float
        Pendulum length (m).
    c : float
        Damping coefficient (1/s). Set to 0 for undamped.

    Returns
    -------
    dstate : np.ndarray, shape (2,)
        [dtheta/dt, domega/dt]
    """
    
    theta, omega = state
    dtheta = omega
    domega = -(g / L) * np.sin(theta) - c * omega
    return np.array([dtheta, domega])

