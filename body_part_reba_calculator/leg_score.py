import numpy as np
import math
import body_part_reba_calculator.body_part_numbering as bodyNum
import body_part_reba_calculator.Util as util


class Leg:
    def __init__(self, joints_position):
        self.joints_position = joints_position

    def leg_degree(self):
        m_body_number = bodyNum.body_part_number()
        right_leg_joint_numbers = m_body_number.right_leg()
        left_leg_joint_numbers = m_body_number.left_leg()
        right_knee_hip_vector = self.joints_position[right_leg_joint_numbers[0]] - self.joints_position[right_leg_joint_numbers[1]]
        right_ankle_knee_vector = self.joints_position[right_leg_joint_numbers[1]] - self.joints_position[right_leg_joint_numbers[2]]

        left_knee_hip_vector = self.joints_position[left_leg_joint_numbers[0]] - self.joints_position[left_leg_joint_numbers[1]]
        left_ankle_knee_vector = self.joints_position[left_leg_joint_numbers[1]] - self.joints_position[left_leg_joint_numbers[2]]

        # knee degree
        right_knee_degree = util.get_angle_between_degs(right_knee_hip_vector,right_ankle_knee_vector)
        left_knee_degree = util.get_angle_between_degs(left_knee_hip_vector,left_ankle_knee_vector)

        return [right_knee_degree, left_knee_degree]

    def leg_reba_score(self):
        leg_degrees = self.leg_degree()
        leg_reba_score = 0
        right_leg_degree = leg_degrees[0]
        left_leg_degree = leg_degrees[1]
        if abs(right_leg_degree) >= abs(left_leg_degree):
            if right_leg_degree < 30:
                leg_reba_score = leg_reba_score + 1
            if 30 <= right_leg_degree < 60:
                leg_reba_score = leg_reba_score + 1
            if 60 <= right_leg_degree:
                leg_reba_score = leg_reba_score + 2

        else:
            if left_leg_degree < 30:
                leg_reba_score = leg_reba_score + 1
            if 30 <= left_leg_degree < 60:
                leg_reba_score = leg_reba_score + 1
            if 60 <= left_leg_degree:
                leg_reba_score = leg_reba_score + 2

        return [leg_reba_score]
