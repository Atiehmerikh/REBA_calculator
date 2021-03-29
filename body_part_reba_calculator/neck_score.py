import numpy as np
import math
import body_part_reba_calculator.body_part_numbering as bodyNum
import body_part_reba_calculator.Util as util


class Neck:
    # for calculating Neck flexion score first we find the plane that the trunk is in there, then angle of
    # neck relative to this plane is calculated.
    def __init__(self, joints,orientation):
        self.joints = joints
        self.orientation = orientation

    def trunk_plane(self):
        m_body_number = bodyNum.body_part_number()
        trunk_joint_numbers = m_body_number.trunk_upper_body()

        # finding a plane of upper body
        u = self.joints[trunk_joint_numbers[1]] - self.joints[trunk_joint_numbers[0]]
        v = self.joints[trunk_joint_numbers[3]] - self.joints[trunk_joint_numbers[0]]

        normal_plane = np.cross(u, v)
        return normal_plane

    def neck_flex_calculator(self):
        m_body_number = bodyNum.body_part_number()
        neck_joint_numbers = m_body_number.neck()
        normal_plane = self.trunk_plane()
        neck_vector = self.joints[neck_joint_numbers[1]] - self.joints[neck_joint_numbers[0]]

        neck_flex = 90 - util.get_angle_between_degs(neck_vector,normal_plane)

        return neck_flex

    def neck_side_calculator(self):
        m_body_number = bodyNum.body_part_number()
        neck_joint_numbers = m_body_number.neck()
        trunk_joint_numbers = m_body_number.trunk_upper_body()

        normal_plane = self.trunk_plane()
        neck_vector = self.joints[neck_joint_numbers[1]] - self.joints[neck_joint_numbers[0]]
        project_neck_on_trunk_plane = neck_vector - np.dot(neck_vector, normal_plane) * normal_plane

        spine_vector = self.joints[trunk_joint_numbers[2]] - self.joints[trunk_joint_numbers[0]]

        neck_side_bending = math.degrees(math.acos(np.dot(project_neck_on_trunk_plane, spine_vector) / (
                math.sqrt(np.dot(project_neck_on_trunk_plane, project_neck_on_trunk_plane)) * math.sqrt(
            np.dot(spine_vector, spine_vector)))))

        return neck_side_bending

    def neck_twist_calculator(self):
        m_body_number = bodyNum.body_part_number()
        neck_joint_numbers = m_body_number.neck()
        q1 = self.orientation[neck_joint_numbers[1]]
        q2 = self.orientation[neck_joint_numbers[0]]
        # finding the rotor that express rotation between two orientational frame(between outer and inner joint)
        rotor = util.find_rotation_quaternion(q1, q2)
        neck_twist = math.acos(rotor[0]) * 2 * (180 / np.pi)
        return neck_twist

    def neck_reba_score(self):
        neck_flex_degree = self.neck_flex_calculator()
        neck_side_bending_degree = self.neck_side_calculator()
        neck_twist_degree = self.neck_twist_calculator()

        neck_reba_score = 0
        neck_flex_score =0
        neck_side_score = 0
        neck_torsion_score =0

        if neck_flex_degree >= 0:
            if 0 <= neck_flex_degree < 20:
                neck_reba_score += 1
                neck_flex_score +=1
            if 20 <= neck_flex_degree:
                neck_reba_score += 2
                neck_flex_score +=2
        else:
            # neck is in extension
            neck_reba_score += 2
            neck_flex_score +=2

        if abs(neck_side_bending_degree) >= 1:
            neck_reba_score += 1
            neck_side_score +=1
        if abs(neck_twist_degree) >= 1:
            neck_reba_score += 1
            neck_torsion_score +=1

        return [neck_reba_score,neck_flex_score,neck_side_score,neck_torsion_score]
