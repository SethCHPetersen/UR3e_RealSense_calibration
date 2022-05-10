#this program is to be used in conjuction with the list created by getCalibrationPositions.py
#and also with the launch file ---- to complete the calibration while in these positions

from encodings import utf_8
import time
import rospy
from std_msgs.msg import String
import moveit_commander
import moveit_msgs.msg
import sys
import cv2
import cv_bridge
import geometry_msgs.msg

# class MoveGroupTutorial(object):
#     def __init__(self):
#         super(MoveGroupTutorial, self).__init__()
#         moveit_commander.roscpp_initialize(sys.argv)
#         rospy.init_node('test_move', anonymous=True)
#         robot = moveit_commander.RobotCommander()
#         scene = moveit_commander.PlanningSceneInterface()
#         group_name = "manipulator"
#         group = moveit_commander.MoveGroupCommander(group_name)
#         display_trajectory_publisher = rospy.Publisher(
#             '/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
#         planning_frame = group.get_planning_frame()
#         eef_link = group.get_end_effector_link()
#         group_names = robot.get_group_names()
#         self.box_name = ''
#         self.robot = robot
#         self.scene = scene
#         self.group = group
#         self.display_trajectory_publisher = display_trajectory_publisher
#         self.planning_frame = planning_frame
#         self.eef_link = eef_link
#         self.group_names = group_names

#     def go_to_pose_from_list(self, jointPositions):
#         group=self.group
#         current_pose=group.get_current_pose().pose
        

#         pose_goal=geometry_msgs.msg.Pose()
#         pose_goal.orientation.x= 0.5
#         pose_goal.orientation.y= 0.5
#         pose_goal.orientation.z= -0.5
#         pose_goal.orientation.w= 0.5
#         pose_goal.position.x= 0.0 #0
#         pose_goal.position.y= -0.5 #-0.5
#         pose_goal.position.z= 0.07 #0.44
#         group.set_pose_target(pose_goal)
#         plan=group.go(wait=True)
#         group.stop()
#         group.clear_pose_targets()
#         current_pose=group.get_current_pose().pose
#         print("New current pose: ", current_pose)
#         return all_close(pose_goal, current_pose, 0.01)

#     def talker():
#         runAgain = True
#         while(runAgain):
#             pub = rospy.Publisher(
#                 '/ur_hardware_interface/script_command', String, queue_size=1000000)
#             #rospy.init_node('talker', anonymous=True)
#             rate = rospy.Rate(125)  # 10hz
#             hello_str = "freedrive_mode()"
#             rospy.loginfo(hello_str)
#             pub.publish(hello_str)
#             rate.sleep()

#             val = raw_input("run again? Y or N : ")
#             val = val.lower()
#             if(val == "y"):
#                 print("running program again")
#                 runAgain = True
#             else:
#                 hello_str = "end_freedrive_mode()"
#                 pub.publish(hello_str)
#                 rate.sleep()
#                 runAgain = False
def main():
    try:
        #tutorial=MoveGroupTutorial()
        #f = open("/home/seth/python_code_for_calibration/posListForCalibration.txt", "r")
        # print(f.read())
        # posString = f.read()
        # posList = posString[1,-1].strip()
        print("posList")


    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__=='__main__':
    main()