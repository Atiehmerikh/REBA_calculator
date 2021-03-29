import numpy as np
import math
import body_part_reba_calculator.body_part_numbering as bodyNum
import body_part_reba_calculator.Util as util


class Trunk:
    def __init__(self, joints_position,joints_orientation):
        self.joints_position = joints_position
        self.joints_orientation = joints_orientation

    def trunk_plane(self):
        m_body_number = bodyNum.body_part_number()
        trunk_joint_numbers = m_body_number.trunk_whole_body()

        # finding a plane of upper body

        u = self.joints_position[trunk_joint_numbers[2]] - self.joints_position[trunk_joint_numbers[1]]
        v = self.joints_position[trunk_joint_numbers[2]] - self.joints_position[trunk_joint_numbers[0]]

        normal_plane = np.cross(u, v)
        return normal_plane

    def trunk_flex_calculator(self):
        normal_plane = self.trunk_plane()
        y_vector = np.array([0, 1, 0])

        trunk_flex =  util.get_angle_between_degs(y_vector,normal_plane) - 90
        return trunk_flex

    def trunk_side_calculator(self):
        m_body_number = bodyNum.body_part_number()
        trunk_joint_numbers = m_body_number.trunk_whole_body()

        normal_plane_xy = np.array([0, 0, 1])
        y_vector = np.array([0, 1, 0])
        spine_vector = self.joints_position[trunk_joint_numbers[2]] - self.joints_position[trunk_joint_numbers[3]]

        project_spine_on_xy_plane = spine_vector - np.dot(spine_vector, normal_plane_xy) * normal_plane_xy

        trunk_side_bending = math.degrees(math.acos(np.dot(project_spine_on_xy_plane, y_vector) / (
                math.sqrt(np.dot(project_spine_on_xy_plane, project_spine_on_xy_plane)) * math.sqrt(
            np.dot(y_vector, y_vector)))))

        return trunk_side_bending

    def trunk_twist_calculator(self):
        # In here the rotor needed to transfer orientation frame of core joint to neck joint is calculated
        # this considered as twist
        m_body_number = bodyNum.body_part_number()
        trunk_joint_numbers = m_body_number.trunk_whole_body()
        q1 = self.joints_orientation[trunk_joint_numbers[2]]# neck
        q2 = self.joints_orientation[trunk_joint_numbers[3]]# core
        # finding the rotor that express rotation between two orientational frame(between outer and inner joint)
        rotor = util.find_rotation_quaternion(q1, q2)
        trunk_twist = math.acos(rotor[0]) * 2 * (180 / np.pi)
        return trunk_twist

    def trunk_reba_score(self):

        trunk_flex_degree = self.trunk_flex_calculator()
        trunk_side_bending_degree = self.trunk_side_calculator()
        trunk_torsion_degree = self.trunk_twist_calculator()

        trunk_reba_score = 0
        trunk_flex_score = 0
        trunk_side_score = 0
        trunk_torsion_score = 0

        if trunk_flex_degree >= 0:
            # means flexion
            if 0 <= trunk_flex_degree < 5:
                trunk_reba_score += 1
                trunk_flex_score += 1
            elif 5 <= trunk_flex_degree < 20:
                trunk_reba_score += 2
                trunk_flex_score += 2
            elif 20 <= trunk_flex_degree < 60:
                trunk_reba_score += 3
                trunk_flex_score += 3
            elif 60 <= trunk_flex_degree:
                trunk_reba_score += 4
                trunk_flex_score += 4
        else:
            # means extension
            if 0 <= abs(trunk_flex_degree) < 5:
                trunk_reba_score += 1
                trunk_flex_score += 1
            elif 5 <= abs(trunk_flex_degree) < 20:
                trunk_reba_score += 2
                trunk_flex_score += 2
            elif 20 <= abs(trunk_flex_degree):
                trunk_reba_score += 3
                trunk_flex_score += 3

        if abs(trunk_side_bending_degree) >= 1:
            trunk_reba_score += 1
            trunk_side_score += 1
        if abs(trunk_torsion_degree) >= 1:
            trunk_reba_score += 1
            trunk_torsion_score += 1

        return [trunk_reba_score, trunk_flex_score, trunk_side_score, trunk_torsion_score]