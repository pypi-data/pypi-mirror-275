# Hybrid Kalman Filter (hybridkf)

[![PyPI version](https://badge.fury.io/py/hybridkf.svg)](https://badge.fury.io/py/hybridkf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Hybrid Kalman Filter (HKF) is an extension of the traditional Kalman filter that combines elements of both linear and nonlinear models to provide accurate state estimation in dynamic systems. It is particularly useful in scenarios where the underlying system dynamics exhibit both linear and nonlinear behavior with regards to physical systems that exhibit a continuous-time model and discrete-time measurements are recorded for state estimation.

## Overview

The `hybridkf` package provides a Python implementation of the Hybrid Kalman Filter algorithm. It offers a flexible and customizable framework for performing state estimation in dynamic systems with mixed linear and nonlinear dynamics. The package includes functionality for:

- State prediction and update based on linear and nonlinear motion models.
- Measurement update using noisy observations.
- Handling process noise and measurement noise to improve estimation accuracy.

## Installation

You can install the `hybridkf` package via pip:

```bash
pip install hybridkf
```

## Usage
Here is a simple example demonstrating how to use the hybridkf package for state estimation:

```python
Copy code
from hybridkf import HybridKalmanFilter
```

# Create a HybridKalmanFilter instance
```python
hkf = HybridKalmanFilter(dt=1, noise_std=3, noise_covariance_factor=0.1, n=4, max_x=1000, max_y=5000, motion_type='linear', linear_timesteps=False)
```
# Execute the Hybrid Kalman Filter algorithm for 20 time steps
```python
hkf.execute_hybrid_kf(time_steps=20)
```
For more detailed usage instructions and advanced customization options, please refer to the documentation.

## Documentation
The complete documentation for the hybridkf package can be found here:

### Class HybridKalmanFilter()

#### Constructor:
```python
HybridKalmanFilter(dt, noise_std, noise_covariance_factor, n, max_x, max_y, motion_type=None, verbose=False, state_transition_factor=1, process_noise_covariance_factor=0.01, u=0, P_init=np.matrix([[1, 0, 0, 0, 0, 0], 
                                                                                        [0, 1, 0, 0, 0, 0], 
                                                                                        [0, 0, 5, 0, 0, 0], 
                                                                                        [0, 0, 0, 5, 0, 0], 
                                                                                        [0, 0, 0, 0, 13, 0], 
                                                                                        [0, 0, 0, 0, 0, 13]]), 
B=0, linear_timesteps=True, timestep_var=0.1, linear_motion_x_factor=2, linear_motion_y_factor=5, 
nonlinear_motion_x_factor=6, nonlinear_motion_y_factor=6, seed=42)
```
#### Parameters
dt: Time step for state prediction.
noise_std: Noise standard deviation for observation Gaussian distributions.
noise_covariance_factor: Factor to scale the noise covariance matrix.
n: Number of observations/objects to generate.
max_x: Maximum x coordinate for state estimation.
max_y: Maximum y coordinate for state estimation.
motion_type: Type of motion model ('linear' or 'nonlinear').
verbose: Verbosity mode (True or False) - view all true, noisy, and estimated measurements for all observations at each time step.
state_transition_factor: Factor to scale the state transition matrix.
process_noise_covariance_factor: Factor to scale the process noise covariance matrix.
u: Control input.
P_init: Initial uncertainty weights matrix.
B: Input control matrix.
linear_timesteps: Flag indicating whether time steps are linear (True) or nonlinear (False).
timestep_var: Variance of time steps.
linear_motion_x_factor: Factor to scale linear motion in the x direction.
linear_motion_y_factor: Factor to scale linear motion in the y direction.
nonlinear_motion_x_factor: Factor to scale nonlinear motion in the x direction.
nonlinear_motion_y_factor: Factor to scale nonlinear motion in the y direction.
seed: Random seed for reproducibility.

#### Methods
generate_true_positions: Generates random true positions for objects.
generate_noisy_observations: Simulates noisy observations based on true positions.
predict: Predicts the state of an object based on the current state and input.
measurement_update: Updates the state estimate based on noisy observations.
execute_hybrid_kf: Executes the Hybrid Kalman Filter algorithm for the specified number of time steps.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## References
Wikipedia contributors. "Kalman filter." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 5 May. 2024. Link
Wikipedia contributors. "Hybrid Kalman filter." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Dec. 2023. Link