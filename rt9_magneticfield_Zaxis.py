#!/usr/bin/env python
# coding: UTF-8
import rospy
from sensor_msgs.msg import MagneticField

f = open('z軸.txt', 'w') # 書き込みモードで開く
def callback(message):
   #  print message.magnetic_field.x
   # print message.magnetic_field.y
    print message.magnetic_field.z
    
   # f.write(str( message.magnetic_field.x)) # 引数の文字列をファイルに書き込む
   # f.write('	')
   # f.write(str( message.magnetic_field.y))
   # f.write('	')
    f.write(str( message.magnetic_field.z))
    f.write('\r\n')

rospy.init_node('ziku')
sub = rospy.Subscriber('/imu/mag', MagneticField,callback)
rospy.spin()
f.close() # ファイルを閉じる
