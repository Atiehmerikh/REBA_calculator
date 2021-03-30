import body_part_reba_calculator.Pose_to_degrees.neck_degrees as degNeck
import body_part_reba_calculator.Pose_to_degrees.trunk_degrees as degTrunk
import body_part_reba_calculator.Pose_to_degrees.leg_degrees as degLeg
import body_part_reba_calculator.Pose_to_degrees.upper_arm_degrees as degUA
import body_part_reba_calculator.Pose_to_degrees.lower_arm_degrees as degLA
import body_part_reba_calculator.Pose_to_degrees.wrist_degrees as degWrist


class PoseToDeg:

    def __init__(self, joints_position, joints_orientation):
        self.joints_position = joints_position
        self.joints_orientation = joints_orientation

    def degree_computation(self):
        # step1: locate neck position
        m_neck = degNeck.NeckDegree(self.joints_position, self.joints_orientation)
        neck_degrees = m_neck.neck_degrees()

        # step2: locate trunck posture
        m_trunk = degTrunk.TrunkDegree(self.joints_position, self.joints_orientation)
        trunk_degrees = m_trunk.trunk_degrees()

        # step3: locate legs
        m_leg = degLeg.LegDegrees(self.joints_position)
        leg_degrees = m_leg.leg_degree()

        # step 7: upper arm score
        m_upper_arm = degUA.UpperArmDegree(self.joints_position)
        UA_degrees = m_upper_arm.upper_arm_degrees()

        # step 8: lower arm score
        m_lower_arm = degLA.LADegrees(self.joints_position)
        LA_degrees = m_lower_arm.lower_arm_degree()

        # step 9: wrist score
        m_wrist = degWrist.WristDegrees(self.joints_position, self.joints_orientation)
        wrist_degrees = m_wrist.wrist_degrees()

        degrees = [neck_degrees, trunk_degrees, leg_degrees, UA_degrees, LA_degrees, wrist_degrees]

        return degrees
