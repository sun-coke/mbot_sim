# mbot_sim仿真小车
## 目录
├── CMakeLists.txt
├── config
│   ├── cfg.rviz
│   └── rviz.rviz
├── course.material
├── follow2.png
├── follow.png
├── image
│   ├── frames.bmp
│   ├── frames.gv
│   └── gmapping.png
├── launch
│   ├── empty_world.launch
│   ├── gmapping.launch
│   ├── hector.launch
│   ├── mbot_follow.launch
│   ├── mbot_gazebo.launch
│   ├── mbot_rviz.launch
│   ├── mbots_gazebo.launch
│   └── tb3_maze.launch
├── package.xml
├── src
│   ├── follower_p.py
│   ├── mbot.py
│   ├── mbots.py
│   └── teleop_twist_keyboard.py
├── urdf
│   ├── urdf
│   │   └── hokuyo.dae
│   └── xacro
│       ├── mbot_base_gazebo.xacro
│       ├── mbot_base_rviz.xacro
│       ├── mbot_camera_gazebo.xacro
│       ├── mbot_camera_rviz.xacro
│       ├── mbot_gazebo.xacro
│       ├── mbot_imu_gazebo.xacro
│       ├── mbot_lidar_gazebo.xacro
│       ├── mbot_lidar_rviz.xacro
│       └── mbot_rviz.xacro
└── worlds
    ├── course.world
    ├── empty.world
    ├── maze1.world
    ├── maze2.world
    └── maze.world

## A、键盘控制
```
$ roslaunch mbot_sim mbot_gazebo.launch ##运行仿真环境（mbot+maze）
$ rosrun mbot_sim teleop_twist_keyboard.py
```

## B、运行建图
```
$ roslaunch mbot_sim mbot_gazebo.launch 
$ roslaunch mbot_sim gmapping.launch ## gmapping_slam
/$ roslaunch mbot_sim hector.launch ## hector_slam
$ rviz
```
add->RobotModel
Fixed Frame->base_link
add->By topic->/map&/scan

## C、运行循线
```
$ roslaunch mbot_sim mbot_follow.launch ## 运行仿真环境（follow）
$ rosrun mbot_sim follower_p.py
```
输出偏差值曲线：
rqt—>plot—>/err/data

## D、多机器人仿真与控制
```
$ roslaunch mbot_sim mbots_gazebo.launch ## 运行仿真环境（mbots）
$ rosrun mbot_sim mbot.py ##单机器人控制（topic：mbot2/cmd_vel）
$ rosrun mbot_sim mbots.py  ##多机器人控制（topic：mbot/cmd_vel）
```

## E、运行TB3迷宫仿真
```
$ roslaunch mbot_sim tb3_maze.launch




