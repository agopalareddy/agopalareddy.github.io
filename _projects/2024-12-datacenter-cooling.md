---
date: 2024-11-30 #11 to show "Fall" and not "Winter"
title: "Datacenter Cooling Optimization using Deep Reinforcement Learning"
collection: projects
permalink: /projects/2024-12-datacenter-cooling
excerpt: "Implemented multiple deep reinforcement learning algorithms (DDQN, PPO, SAC) integrated with EnergyPlus simulations to optimize datacenter cooling systems for improved energy efficiency."
venue: "Washington University in St. Louis"
last_modified_at: 2025-02-22 20:04:59
---

Developed a comprehensive deep reinforcement learning solution for optimizing datacenter cooling systems using EnergyPlus simulations. The project was completed as part of Washington University in St. Louis's CSE 510A: Deep Reinforcement Learning course, focusing on implementing and comparing multiple DRL algorithms for energy efficiency optimization.

### Research Context

With the growing popularity of deep learning and big data, data centers have become essential to modern infrastructure, leading to increased energy consumption both for computing operations and cooling needs. While large-scale data centers have been extensively studied, small- to mid-sized data centers remain understudied despite occupying 42.5% and 19.5% of the market share respectively. Our project specifically addresses this gap by optimizing cooling efficiency in these smaller facilities.

As machines within a data center complete their tasks, they generate heat, creating a complex spatial cooling problem. Our approach leverages DRL to dynamically adapt to changing conditions such as machine workload and external temperature.

### Key Features

- Multiple DRL algorithm implementations:
  - Dueling Deep Q-Network (DDQN) - Our novel contribution to datacenter cooling
  - Proximal Policy Optimization (PPO) with Generalized Advantage Estimation
  - Soft Actor-Critic (SAC) with automatic entropy tuning
- Integration with EnergyPlus for accurate building energy simulation
- Custom environment for datacenter cooling optimization
- Performance metrics and energy efficiency tracking
- Configurable hyperparameters for training
- Baselines for comparison (Random, Rules-Based Controller, Rules-Based Incremental)

### Implementation Details

The project consists of three main DRL implementations, each serving different purposes:
- DDQN for discretized action spaces (our best performer with 35.8% improvement over baseline)
- PPO for stable training performance (achieved 10.9% improvement over baseline)
- SAC for continuous action spaces with exploration (showed limited improvement at 0.284%)

The system integrates with EnergyPlus for realistic building energy simulations, considering:
- Dynamic thermal conditions
- Energy consumption patterns
- Cooling system efficiency
- Environmental impact

### Experimental Setup

We used the `Sinergym` Python package to simulate a small datacenter through the `Eplus-datacenter-mixed-continuous-stochastic-v1` environment. The environment simulates:

- A 491.3 m² building divided into two asymmetrical zones (west and east)
- Each zone equipped with an HVAC system
- Hosted servers as primary heat sources
- Stochastic weather conditions with 1.5 standard deviations of normal amplification
- Training period from June 1st to August 31st

### Key Findings

Our experiments revealed:

- DDQN significantly outperformed other approaches, showing a 35.8% improvement over the Rules-Based Incremental Controller
- PPO achieved a 10.9% improvement over the baseline
- SAC showed limited improvement (0.284%) compared to the baseline
- Weather forecasting data generally reduced model performance across configurations
- Model-free approaches like DDQN offer promising results for small to mid-sized data centers with limited computational resources

### Technologies Used

- Python 3.12
- PyTorch 2.5.1
- EnergyPlus 24.2.0
- Gymnasium 1.0.0
- Sinergym 3.7.0
- NumPy
- Tensorboard 2.18.0
- Version Control (Git)

### Links

- [GitHub Repository](https://github.com/agopalareddy/CSE510A_Datacenter_Cooling)