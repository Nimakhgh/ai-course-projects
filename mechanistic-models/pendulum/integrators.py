import numpy as np
def rk4_step(f, t, y, dt):
    """
    One step of the classical 4th-order Runge-Kutta method.

    Parameters
    ----------
    f : callable
        Derivative function f(t, y) -> dy/dt.
    t : float
        Current time.
    y : np.ndarray
        Current state.
    dt : float
        Time step.

    Returns
    -------
    y_new : np.ndarray
        State after one step.
    """
    k1 = f(t, y)
    k2 = f(t + dt / 2, y + dt / 2 * k1)
    k3 = f(t + dt / 2, y + dt / 2 * k2)
    k4 = f(t + dt, y + dt * k3)
    return y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def integrate(f, y0, t_array, method="rk4"):
    """
    Integrate an ODE over a time grid.

    Parameters
    ----------
    f : callable
        Derivative function f(t, y) -> dy/dt.
    y0 : np.ndarray
        Initial state.
    t_array : np.ndarray
        Time points (must be equally spaced).
    method : str
        "euler" or "rk4".

    Returns
    -------
    y_array : np.ndarray, shape (len(t_array), len(y0))
        State at each time point.
    """
    n = len(t_array)
    y_array = np.zeros((n, len(y0)))
    y_array[0] = y0
    dt = t_array[1] - t_array[0]

    step = rk4_step if method == "rk4" else euler_step

    for i in range(n - 1):
        y_array[i + 1] = step(f, t_array[i], y_array[i], dt)

    return y_array