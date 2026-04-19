
# AUV Recruitment Tasks - ROS 2 & Computer Vision

---

This repository contains the completed tasks for the AUV Software Subsystem, demonstrating proficiency in ROS 2, Python, and OpenCV pipelines

---

## Tasks Overview
* **Task 1 (Comm-Link):** A ROS 2 Pub/Sub system for two-way chat.
* **Task 2 (Signal Pipeline):** A multi-node data processing pipeline using ROS 2 topics.
* **Task 3 (Dead Reckoning):** A custom message simulation for submarine state tracking.
* **Task 4 (Visual Lock):** A vision-based State Machine using OpenCV filters.

---

## Prerequisites
* ROS 2 (Humble) installed on Ubuntu.
* Python 3 with `opencv-python`, `numpy`, and `rclpy` installed.
* `colcon` build tools.

---

## Build Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/rsrohiit1609-sys/AUV_ws.git
   cd AUV_ws
   ```

2. **Build the workspace:**
   ```bash
   cd auv_ws/src
   colcon build --packages-select <your_package_name>
   ```

3. **Source the workspace:**
   ```bash
   source install/setup.bash
   ```

---

## Running the Nodes
### Task 1: The Comm-Link
Open two terminals and run the following in each:
* Terminal 1: `ros2 run task1 task1 Invictus`
* Terminal 2: `ros2 run task1 task1 Hawcker` 

### Task 2: Signal Processing
Run the nodes in separate terminals:
1. `ros2 run task2 publisher_node`
2. `ros2 run task2 processor_node`
3. `ros2 run task2 output_node`

### Task 3: Dead Reckoning System
1. `ros2 run task3 commander_node`
2. `ros2 run task3 navigator_node`

### Task 4: Visual Lock
* Ensure a camera or video source is accessible:
  ```bash
  ros2 run task4 visuallock
  ```
  
---

## Proof of Work
* **[Link to GitHub Repository](https://github.com/rsrohiit1609-sys/AUV_ws.git)**
