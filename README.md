# mbot_sim仿真小车

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
```

## C、运行循线
```
$ roslaunch mbot_sim mbot_follow.launch ## 运行仿真环境（follow）
$ rosrun mbot_sim follower_p.py
```
输出偏差值曲线：
rqt——>plot——>/err/data

## D、多机器人仿真与控制
```
$ roslaunch mbot_sim mbots_gazebo.launch ## 运行仿真环境（mbots）
$ rosrun mbot_sim mbot.py ##单机器人控制（topic：mbot2/cmd_vel）
$ rosrun mbot_sim mbots.py  ##多机器人控制（topic：mbot/cmd_vel）
```

## E、运行TB3迷宫仿真
```
$ roslaunch mbot_sim tb3_maze.launch




