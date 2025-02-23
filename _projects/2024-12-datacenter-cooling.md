---
date: 2024-11-30
title: "Datacenter Cooling Optimization using Deep Reinforcement Learning"
collection: projects
permalink: /projects/2024-12-datacenter-cooling
excerpt: "Implemented multiple deep reinforcement learning algorithms (DQN, PPO, SAC) integrated with EnergyPlus simulations to optimize datacenter cooling systems for improved energy efficiency."
venue: "Washington University in St. Louis"
last_modified_at: 2025-02-22 20:04:59
---

Developed a comprehensive deep reinforcement learning solution for optimizing datacenter cooling systems using EnergyPlus simulations. The project was completed as part of Washington University in St. Louis's CSE 510A: Deep Reinforcement Learning course, focusing on implementing and comparing multiple DRL algorithms for energy efficiency optimization.

### Key Features

- Multiple DRL algorithm implementations:
  - Deep Q-Network (DQN)
  - Proximal Policy Optimization (PPO)
  - Soft Actor-Critic (SAC)
- Integration with EnergyPlus for accurate building energy simulation
- Custom environment for datacenter cooling optimization
- Performance metrics and energy efficiency tracking
- Configurable hyperparameters for training

### Implementation Details

The project consists of three main DRL implementations, each serving different purposes:
- PPO for stable training performance
- DQN for discrete action spaces
- SAC for continuous action spaces with exploration

The system integrates with EnergyPlus for realistic building energy simulations, considering:
- Dynamic thermal conditions
- Energy consumption patterns
- Cooling system efficiency
- Environmental impact

### Technical Architecture

Core components include:
- Custom DRL implementations in Python
- EnergyPlus integration for simulation
- Gymnasium-based environment
- Comprehensive performance tracking
- Configurable training parameters

### Skills/Technologies

- Python 3.12
- PyTorch
- EnergyPlus
- Gymnasium
- NumPy
- Deep Reinforcement Learning
- Building Energy Simulation
- System Optimization
- Software Architecture
- Version Control (Git)

### Links

- [GitHub Repository](https://github.com/peyton-gozon/CSE510A-Datacenter-Cooling)