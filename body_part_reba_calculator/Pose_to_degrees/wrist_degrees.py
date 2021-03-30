import numpy as np
import math
import body_part_reba_calculator.Pose_to_degrees.body_part_numbering as bodyNum
import body_part_reba_calculator.Pose_to_degrees.Util as Util


class WristDegrees:
    def __init__(self, joints_position,joints_orientation):
        self.joints_position = joints_position
        self.joints_orientation = joints_orientation

    def wrist_flex(self):
        m_body = bodyNum.body_part_number()
        right_arm_joint_number = m_body.right_arm()
        left_arm_joint_number = m_body.left_arm()

        right_shoulder_elbow_vector = self.joints_position[right_arm_joint_number[1]] - self.joints_position[
            right_arm_joint_number[0]]
        left_shoulder_elbow_vector = self.joints_position[left_arm_joint_number[1]] - self.joints_position[
            left_arm_joint_number[0]]
        right_elbow_wrist_vector = self.joints_position[right_arm_joint_number[2]] - self.joints_position[
            right_arm_joint_number[1]]
        left_elbow_wrist_vector = self.joints_position[left_arm_joint_number[2]] - self.joints_position[
            left_arm_joint_number[1]]
        right_wrist_finger_vector = self.joints_position[right_arm_joint_number[3]] - self.joints_position[
            right_arm_joint_number[2]]
        left_wrist_finger_vector = self.joints_position[left_arm_joint_number[3]] - self.joints_position[
            left_arm_joint_number[2]]

        right_plane_normal_vec = np.cross(right_shoulder_elbow_vector, right_elbow_wrist_vector)
        left_plane_normal_vec = np.cross(left_shoulder_elbow_vector, left_elbow_wrist_vector)

        right_wrist_flex = Util.get_angle_between_degs(right_elbow_wrist_vector, right_wrist_finger_vector)
        left_wrist_flex = Util.get_angle_between_degs(left_elbow_wrist_vector, left_wrist_finger_vector)

        if right_plane_normal_vec[0] != 0 or right_plane_normal_vec[1] != 0 or right_plane_normal_vec[2] != 0:
            if np.dot(np.cross(right_wrist_finger_vector, right_elbow_wrist_vector), right_plane_normal_vec) > 0:
                # means extend of wrist
                right_wrist_flex *= -1

        if left_plane_normal_vec[0] != 0 or left_plane_normal_vec[1] != 0 or left_plane_normal_vec[2] == 0:
            if np.dot(np.cross(left_wrist_finger_vector, left_elbow_wrist_vector), left_plane_normal_vec) > 0:
                # means extend of wrist
                left_wrist_flex *= -1

        return [right_wrist_flex, left_wrist_flex]

    def wrist_side(self):
        m_body = bodyNum.body_part_number()
        right_arm_joint_number = m_body.right_arm()
        left_arm_joint_number = m_body.left_arm()

        right_shoulder_elbow_vector = self.joints_position[right_arm_joint_number[1]] - self.joints_position[
            right_arm_joint_number[0]]
        left_shoulder_elbow_vector = self.joints_position[left_arm_joint_number[1]] - self.joints_position[
            left_arm_joint_number[0]]
        right_elbow_wrist_vector = self.joints_position[right_arm_joint_number[2]] - self.joints_position[
            right_arm_joint_number[1]]
        left_elbow_wrist_vector = self.joints_position[left_arm_joint_number[2]] - self.joints_position[
            left_arm_joint_number[1]]
        right_wrist_finger_vector = self.joints_position[right_arm_joint_number[3]] - self.joints_position[
            right_arm_joint_number[2]]
        left_wrist_finger_vector = self.joints_position[left_arm_joint_number[3]] - self.joints_position[
            left_arm_joint_number[2]]

        right_plane_normal_vec = np.cross(right_shoulder_elbow_vector, right_elbow_wrist_vector)
        left_plane_normal_vec = np.cross(left_shoulder_elbow_vector, left_elbow_wrist_vector)

        if right_plane_normal_vec[0] != 0 or right_plane_normal_vec[1] != 0 or right_plane_normal_vec[2] != 0:
            right_side_bent_degree = 90 - Util.get_angle_between_degs(right_plane_normal_vec, right_wrist_finger_vector)
        else:
            right_side_bent_degree = 0
        if left_plane_normal_vec[0] != 0 or left_plane_normal_vec[1] != 0 or left_plane_normal_vec[2] == 0:
            left_side_bent_degree = 90 - Util.get_angle_between_degs(left_plane_normal_vec, left_wrist_finger_vector)
        else:
            left_side_bent_degree = 0

        return [right_side_bent_degree, left_side_bent_degree]

    def wrist_torsion(self):
        m_body_number = bodyNum.body_part_number()
        right_wrist_joint_numbers = m_body_number.right_arm()
        q1 = self.joints_orientation[right_wrist_joint_numbers[3]]
        q2 = self.joints_orientation[right_wrist_joint_numbers[2]]
        # finding the rotor that express rotation between two orientational frame(between outer and inner joint)
        rotor = Util.find_rotation_quaternion(q1, q2)
        if (rotor[0]>1):
            rotor[0]=1
        elif rotor[0]<-1:
            rotor[0]=-1
        right_wrist_twist = math.acos(rotor[0]) * 2 * (180 / np.pi)

        m_body_number = bodyNum.body_part_number()
        left_wrist_joint_numbers = m_body_number.left_arm()
        q1 = self.joints_orientation[left_wrist_joint_numbers[3]]
        q2 = self.joints_orientation[left_wrist_joint_numbers[2]]
        # finding the rotor that express rotation between two orientational frame(between outer and inner joint)
        rotor = Util.find_rotation_quaternion(q1, q2)
        left_wrist_twist = math.acos(rotor[0]) * 2 * (180 / np.pi)

        return [right_wrist_twist, left_wrist_twist]

    def wrist_degrees(self):
        flex = self.wrist_flex()
        right_flex = flex[0]
        left_flex = flex[1]

        side = self.wrist_side()
        right_side = side[0]
        left_side = side[1]

        twist = self.wrist_torsion()
        right_twist = side[0]
        left_twist = side[1]

        return [right_flex,left_flex,right_side,left_side,right_twist,left_twist]


