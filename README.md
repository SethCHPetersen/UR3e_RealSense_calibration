# UR3e_Realsense_calibration
This repository is for calibrating a Universal Robots UR3e robotic arm with a Intel Realsense depth camera. 

This repo is edited from https://github.com/IFL-CAMP/easy_handeye, and more specifically https://github.com/portgasray/ur5_realsense_calibration.

This repo is intended to be a calibration between the UR3e industrial robot and any Intel Realsense D400 series camera. To set up the camera and robot for the calibration, first mount the camera on a tripod so that it can see the area of which the robot will be working in. Then print and mount the Aruco marker on a plate and attach it to the end of the arm of the robot. Solid works files for a calibration plate that can be laser cut from mdf are included in this package. After that the hardware side of things should be good to go.

First make a workspace and src folder for this repo to be cloned into
```
mkdir -p catkin_ws/src && cd catkin_ws/src
```
Then clone the repository into the workspace
```
git clone https://github.com/SethCHPetersen/UR3e_Realsense_calibration.git

```
Then build the library and source it.
```
cd ../
catkin_make
source devel/setup.bash
```

My version of this library should have everything necessary for the specific case of a UR3e but if you would like to use another UR robot, their github is https://github.com/UniversalRobots/Universal_Robots_ROS_Driver. 

Before starting the calibration, the calibration positions need to be acquired. This is done using a python script I wrote which can be run using the command below. This script will allow the user to move the robot to positions where the camera can see the aruco marker and store those positions so that the calibration process is repeatable. 
```
rosrun auto_calibrate getCalibrationPositions.py
```
This will generate a .txt file which you will have to get the file path to and remap the file path within CalibrateUsingPositionList.py. 
CalibrateUsingPositionList.py is used to go to those positions that you selected with getCalibrationPositions.py. 

OOnce you have those positions and CalibrateUsingPositionList.py file path changed, you are ready to start calibration.

Run these commands in this order, waiting for each to stabilize before starting the next.
```
roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.56.101
roslaunch ur3e_moveit_config ur3e_moveit_planning_execution.launch
roslaunch realsense2_camera rs_rgbd.launch
roslaunch easy_handeye ur3e_realsense_handeyecalibration.launch eye_on_hand:=false
```

Once those are run as in https://github.com/portgasray/ur5_realsense_calibration. 

