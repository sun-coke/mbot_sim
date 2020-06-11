#!/usr/bin/env python

import rospy,cv2,cv_bridge,numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class Follower:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()
    self.image_sub = rospy.Subscriber('camera/image_raw', Image, self.image_callback)
    self.cmd_vel_pub = rospy.Publisher('/mbot/cmd_vel', Twist, queue_size=1)
    self.err_pub = rospy.Publisher('err', Float64, queue_size=1)
    self.twist = Twist()

  def image_callback(self, msg):
      image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

      h, w, d = image.shape
      search_left = 1 * w / 4      
      search_right = 3 * w / 4
      dst=image[0:h , search_left:search_right]

      hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
      lower_yellow = numpy.array([10, 10, 10])
      upper_yellow = numpy.array([255, 255, 250])
      mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

      h, w, d = dst.shape
      search_top = 3 * h / 4
      search_bot = 3 * h / 4 + 20
      mask[0:search_top, 0:w] = 0
      mask[search_bot:h, 0:w] = 0

      M = cv2.moments(mask)
      if M['m00'] > 0:
          cx = int(M['m10'] / M['m00'])
          cy = int(M['m01'] / M['m00'])
          cv2.circle(dst, (cx, cy), 20, (0, 0, 255), -1)

          err = cx - w / 2
          self.twist.linear.x = 0.3
          self.twist.angular.z = -float(err) / 500
          self.cmd_vel_pub.publish(self.twist)

          msg = Float64()
          msg.data = err
          self.err_pub.publish(msg)

      cv2.namedWindow("window", 2)
      cv2.imshow("window", dst)
      cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()
