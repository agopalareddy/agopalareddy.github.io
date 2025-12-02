---
date: 2025-08-01
title: "VLM Security: Red Team Attacks and Defenses for Vision Language Models"
collection: projects
permalink: /projects/2025-08-vlm-security
excerpt: "Explored adversarial attacks and defenses for Vision Language Models (VLMs), implementing red team attack strategies and defense mechanisms using OpenAI and Anthropic APIs."
venue: "Washington University in St. Louis"
last_modified_at: 2025-12-02 00:00:00
---

This project investigates the security vulnerabilities of Vision Language Models (VLMs) through adversarial attack generation and defense mechanism development. Completed as part of Washington University in St. Louis's CSE 5519: Computer Vision course.

### Project Overview

Vision Language Models like GPT-4V and Claude have become increasingly powerful, but they also present new security challenges. This project explores how adversarial images can be crafted to manipulate VLM outputs, and develops defense strategies to detect and mitigate such attacks.

### Research Focus

The project addresses two key areas:

1. **Red Team Attacks**: Generating adversarial images that can cause VLMs to produce unintended or harmful outputs
2. **Defense Mechanisms**: Developing detection and mitigation strategies to protect VLMs from adversarial inputs

### Key Components

- **Attack Pipeline**: Systematic approach to generating adversarial images that exploit VLM vulnerabilities
- **Defense Scripts**: Automated detection mechanisms for identifying potentially malicious image inputs
- **Multi-Provider Support**: Implementation supporting both OpenAI (GPT-4V) and Anthropic (Claude) APIs
- **Configurable Testing**: Flexible temperature settings for attack and defense scenarios
- **Mock Mode**: Testing infrastructure that doesn't require real API calls

### Technical Implementation

- Temperature-tuned generation for creative attacks (0.9) vs. precise defenses (0.3)
- Modular architecture supporting multiple VLM providers
- Comprehensive results logging and analysis
- Reproducible experimental framework

### Technologies Used

- Python
- OpenAI API (GPT-4V)
- Anthropic API (Claude)
- PIL/Pillow for image processing
- dotenv for configuration management

### GitHub Repository

[View the project on GitHub](https://github.com/agopalareddy/CSE5519-Project)
