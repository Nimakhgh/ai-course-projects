import numpy as np
import matplotlib.pyplot as plt

from pendulum import pendulum_derivatives
from integrators import integrate


def main():
    # --- Parameters ---
    g = 9.81       # gravity (m/s^2)
    L = 1.0        # pendulum length (m)
    c = 0.0        # damping (0 = undamped)
    theta0 = np.pi / 6   # initial angle: 30 degrees
    omega0 = 0.0         # initial angular velocity

    T = 10.0       # total simulation time (s)
    dt = 0.01      # time step (s)
    n_steps = int(T / dt) + 1

    t_array = np.linspace(0, T, n_steps)
    y0 = np.array([theta0, omega0])

    # --- Integrate ---
    f = lambda t, y: pendulum_derivatives(t, y, g=g, L=L, c=c)
    y_array = integrate(f, y0, t_array, method="rk4")

    theta = y_array[:, 0]
    omega = y_array[:, 1]

    # --- Energy check (for undamped pendulum) ---
    # E = 0.5 * m * L^2 * omega^2 + m * g * L * (1 - cos(theta))   (m = 1)
    energy = 0.5 * L**2 * omega**2 + g * L * (1 - np.cos(theta))

    # --- Plot ---
    fig, axes = plt.subplots(3, 1, figsize=(9, 8), sharex=True)

    axes[0].plot(t_array, theta, color="tab:blue")
    axes[0].set_ylabel("θ (rad)")
    axes[0].set_title("Pendulum simulation — RK4")

    axes[1].plot(t_array, omega, color="tab:orange")
    axes[1].set_ylabel("ω (rad/s)")

    axes[2].plot(t_array, energy, color="tab:green")
    axes[2].set_ylabel("Energy (J/kg)")
    axes[2].set_xlabel("Time (s)")
    axes[2].set_ylim(energy.mean() * 0.99, energy.mean() * 1.01)

    plt.tight_layout()
    plt.savefig("output/pendulum_result.png", dpi=120)
    plt.show()

    # --- Console summary ---
    print(f"Initial energy: {energy[0]:.6f}")
    print(f"Final energy:   {energy[-1]:.6f}")
    print(f"Energy drift:   {abs(energy[-1] - energy[0]):.2e}")
    print(f"Max |theta|:    {np.max(np.abs(theta)):.4f} rad")


if __name__ == "__main__":
    main()
