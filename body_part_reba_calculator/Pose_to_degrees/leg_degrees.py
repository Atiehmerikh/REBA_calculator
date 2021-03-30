import body_part_reba_calculator.Pose_to_degrees.body_part_numbering as bodyNum
import body_part_reba_calculator.Pose_to_degrees.Util as Util


class LegDegrees:
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
        right_knee_degree = Util.get_angle_between_degs(right_knee_hip_vector, right_ankle_knee_vector)
        left_knee_degree = Util.get_angle_between_degs(left_knee_hip_vector, left_ankle_knee_vector)

        return [right_knee_degree, left_knee_degree]
