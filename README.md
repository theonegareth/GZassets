# Gazebo Simulation Drone Assets — KRTI 2025

This repository contains the drone model and simulation assets developed by the BINUS ASO AeroBASE team for the **Kontes Robot Terbang Indonesia (KRTI) 2025**.

## 🛩️ Overview

The drone is modeled for integration with **Gazebo Sim** and **ROS 2 Jazzy**, supporting both visual and physics-based simulation for autonomous flight tasks. This repository includes:

- ✅ Full SDF/URDF drone model
- ✅ Meshes for frame, propellers, and camera mounts
- ✅ Gazebo Sim world with ground plane
- ❌ Sensor configurations (camera, IMU, LiDAR-ready) **NOT IMPLEMENTED**
- ❌ Coordinate transform trees (`tf`) **NOT IMPLEMENTED**
- ❌ ROS 2 launch files for testing in simulation

## 📁 Folder Structure

```plaintext
GZassets/
├── hexadrone
│   ├── config/
│   ├── models/
│   ├── scripts/
│   ├── worlds/
│   ├── CMakeList.txt
│   ├── package.xml
├── LICENSE              # License file (e.g., MIT)
└── README.md            # Main project documentation
```


## 🚀 Getting Started

### Requirements

- [Gazebo Sim](https://gazebosim.org/) (Harmonic or later)
- [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/index.html) (optional, for ROS integration)
- [colcon](https://docs.ros.org/en/rolling/Tutorials/Colcon-Tutorial.html) (optional)

### Running the Simulation

```bash
cd GZassets/hexadrone/worlds
gz sim -v4 -r hexadrone_runway.sdf
```

### ROS 2 Integration (Work in Progress)

The ROS 2 launch files are currently being developed. To build with ROS 2:

```bash
# Clone and build
cd ~/your_ros2_ws/src
git clone https://github.com/theonegareth/GZassets.git
cd ..
colcon build
source install/setup.bash

# Launch (coming soon)
ros2 launch hexadrone bringup.launch.py
ros2 launch hexadrone spawn_drone.launch.py world:=your_custom_world
```


## 📷 Sensors Status

| Sensor         | Status    | Topic         | Notes                          |
|----------------|-----------|---------------|--------------------------------|
| IMU            | ⚠️ Partial | `/imu`        | Sensor defined, ROS bridge WIP |
| Camera (Front) | ❌ Not Implemented | `/image_raw`  |                                |
| LiDAR          | ❌ Not Implemented | `/scan`       |                                |

---

## 🛠️ Development Team

- **Gareth** – [github.com/theonegareth](https://github.com/theonegareth)
- **Maul** - [https://github.com/Futprodev](https://github.com/Futprodev)

BINUS ASO School of Engineering  
**AeroBASE – Research & Development Division**  

📍 BINUS ASO School of Engineering

---

## 📄 [License](LICENSE)

**MIT License**  
Feel free to use or modify this project for educational or non-commercial KRTI-related work.

