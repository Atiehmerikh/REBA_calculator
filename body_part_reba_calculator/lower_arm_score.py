import math
import numpy as np
import body_part_reba_calculator.body_part_numbering as bodyNum
import body_part_reba_calculator.Util as util


class lower_arm:
    def __init__(self, joints_position):
        self.joints_position = joints_position

    def lower_arm_degree(self):
        m_body_number = bodyNum.body_part_number()
        right_arm_joint_numbers = m_body_number.right_arm()
        left_arm_joint_numbers = m_body_number.left_arm()

        right_shoulder_elbow_vector = self.joints_position[right_arm_joint_numbers[1]] - self.joints_position[right_arm_joint_numbers[0]]
        left_shoulder_elbow_vector = self.joints_position[left_arm_joint_numbers[1]] - self.joints_position[left_arm_joint_numbers[0]]

        right_elbow_wrist_vector = self.joints_position[right_arm_joint_numbers[2]] - self.joints_position[right_arm_joint_numbers[1]]
        left_elbow_wrist_vector = self.joints_position[left_arm_joint_numbers[2]] - self.joints_position[left_arm_joint_numbers[1]]

        # right and left arm degree in saggital plane
        right_degree = util.get_angle_between_degs(right_shoulder_elbow_vector,right_elbow_wrist_vector)
        left_degree =util.get_angle_between_degs(left_shoulder_elbow_vector,left_elbow_wrist_vector)

        return [right_degree,left_degree]

    def lower_arm_score(self):
        degree = self.lower_arm_degree()
        right_degree = degree[0]
        left_degree = degree[1]
        lower_arm_reba_score = 0
        if right_degree >= left_degree:
            if 0 <= right_degree < 60:
                lower_arm_reba_score = lower_arm_reba_score + 2
            if 60 <= right_degree < 100:
                lower_arm_reba_score = lower_arm_reba_score + 1
            if 100 <= right_degree:
                lower_arm_reba_score = lower_arm_reba_score + 1
        if right_degree < left_degree:
            if 0 <= left_degree < 60:
                lower_arm_reba_score = lower_arm_reba_score + 2
            if 60 <= left_degree < 100:
                lower_arm_reba_score = lower_arm_reba_score + 1
            if 100 <= left_degree:
                lower_arm_reba_score = lower_arm_reba_score + 1

        return lower_arm_reba_score

