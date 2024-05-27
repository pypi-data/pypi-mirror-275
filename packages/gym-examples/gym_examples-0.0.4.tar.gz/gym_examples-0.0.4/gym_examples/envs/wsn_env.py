import gym
import numpy as np
from gym.spaces import Discrete, Box

import gym
import numpy as np
from gym.spaces import Discrete, Box

class WSNRoutingEnv(gym.Env):
  """
  Wireless Sensor Network Routing Environment

  This class defines a Gym environment for simulating routing decisions 
  in a Wireless Sensor Network (WSN) with a base station.

  Attributes:
      n_sensors: Number of sensor nodes in the network.
      coverage_radius: Transmission radius of each sensor node.
      max_hops: Maximum number of hops allowed for data transmission.
  """

  def __init__(self, n_sensors=10, coverage_radius=0.5, max_hops=5):
    self.n_sensors = n_sensors
    self.n_agents = n_sensors
    self.coverage_radius = coverage_radius
    self.max_hops = max_hops

    # Observation space: [remaining_energy (n_sensors,), distance_to_base (n_sensors,)]
    self.observation_space = Box(low=np.zeros(2*self.n_sensors), high=np.ones(2*self.n_sensors))

    # Action space: Choose next hop for each sensor (n_sensors,)
    # Each action can be:
    #   - range(n_sensors): Index of the next hop sensor for data forwarding
    #   - n_sensors: Special action indicating reaching base station
    self.action_space = Discrete(n_sensors + 1)

    # Reset the environment for a new episode
    self.reset()

  def reset(self):
    # Generate random sensor positions within the coverage radius
    self.sensor_positions = np.random.rand(self.n_sensors, 2) * self.coverage_radius

    # Calculate initial distance to base station for each sensor
    self.distance_to_base = np.linalg.norm(self.sensor_positions - np.array([0.5, 0.5]), axis=1)

    # Initialize remaining energy (can be replaced with a decay model)
    self.remaining_energy = np.ones(self.n_sensors)

    # Current sensor at which data resides (initially random)
    self.current_sensor = np.random.randint(self.n_sensors)

    return self._get_observation()

  def step(self, action):
    # Check for invalid actions
    if action not in range(self.action_space.n):
      raise ValueError("Invalid action!")

    # Update remaining energy (can be replaced with a more complex model)
    self.remaining_energy -= 0.1  # Example energy consumption per hop

    # Handle reaching base station
    if action == self.n_sensors:
      reward = 1.0  # Maximum reward for reaching base station
      done = True
    else:
      # Update current sensor and distance to base for next hop
      self.current_sensor = action
      self.distance_to_base[self.current_sensor] = np.linalg.norm(self.sensor_positions[self.current_sensor] - np.array([0.5, 0.5]))

      # Reward based on distance reduction and energy spent
      reward = (self.distance_to_base[self.current_sensor] - np.max(self.distance_to_base)) / self.coverage_radius - 0.1
      done = (self.distance_to_base[self.current_sensor] <= self.coverage_radius) or (np.min(self.remaining_energy) <= 0) or (self.step_count >= self.max_hops)
      self.step_count += 1

    # Check for terminal state (reached base station, out of energy, or max hops exceeded)
    if done:
      # Penalty for not reaching base station within max hops
      if self.distance_to_base[self.current_sensor] > self.coverage_radius:
        reward -= 0.5

    return self._get_observation(), reward, done, {}

  def _get_observation(self):
    # Combine remaining energy and distance to base station for all sensors
    return np.concatenate((self.remaining_energy, self.distance_to_base))
