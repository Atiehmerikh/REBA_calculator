import numpy as np
import body_part_reba_calculator.neck_score as rebaNeck
import body_part_reba_calculator.trunck_score as rebaTrunk
import body_part_reba_calculator.leg_score as rebaLeg
import body_part_reba_calculator.upper_arm_score as rebaUA
import body_part_reba_calculator.lower_arm_score as rebaLA
import body_part_reba_calculator.wrist_score as rebaWrist


class RebaScoreCalculator:

    def __init__(self, joints_position,joints_orientation) :
        #,joints_orientation):
        self.joints_position = joints_position
        self.joints_orientation = joints_orientation

    def reba_table_a(self):
        return np.array([
            [[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [3, 5, 6, 7], [4, 6, 7, 8]],
            [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
            [[3, 3, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 9]]
        ])

    def reba_table_b(self):
        return np.array([
            [[1, 2, 2], [1, 2, 3]],
            [[1, 2, 3], [2, 3, 4]],
            [[3, 4, 5], [4, 5, 5]],
            [[4, 5, 5], [5, 6, 7]],
            [[6, 7, 8], [7, 8, 8]],
            [[7, 8, 8], [8, 9, 9]],
        ])

    def reba_table_c(self):
        return np.array([
            [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7],
            [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8],
            [2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8],
            [3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9],
            [4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9],
            [6, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 10],
            [7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 11],
            [8, 8, 8, 9, 10, 10, 10, 10, 10, 11, 11, 11],
            [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12],
            [10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12],
            [11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12],
            [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        ])

    def reba_computation(self):
        # Table A ( Neck X Trunk X Legs)
        table_a = self.reba_table_a()
        # Table B ( UpperArm X LowerArm X Wrist)
        table_b = self.reba_table_b()
        # Table C ( ScoreA X ScoreB)
        table_c = self.reba_table_c()

        # step1: locate neck position
        m_neck = rebaNeck.Neck(self.joints_position,self.joints_orientation)
        neck_scores = m_neck.neck_reba_score()

        # step2: locate trunck posture
        m_trunk = rebaTrunk.Trunk(self.joints_position, self.joints_orientation)
        trunk_scores = m_trunk.trunk_reba_score()

        # step3: locate legs
        m_leg = rebaLeg.Leg(self.joints_position)
        leg_scores = m_leg.leg_reba_score()
        # leg_scores =[1]

        # step 4: Look up score in table _A
        posture_score_a = table_a[neck_scores[0] - 1][trunk_scores[0] - 1][leg_scores[0] - 1]

        # step 5: load score
        # load = input("what is the load(in lbs) ")
        load = 0
        if 11 <= int(load) < 22:
            posture_score_a = posture_score_a + 1
        if 22 <= int(load):
            posture_score_a = posture_score_a + 2

        # step 7: upper arm score
        m_upper_arm = rebaUA.UpperArm(self.joints_position)
        UA_scores = m_upper_arm.upper_arm_reba_score()

        # step 8: lower arm score
        m_lower_arm = rebaLA.lower_arm(self.joints_position)
        LA_scores = m_lower_arm.lower_arm_score()

        # step 9: wrist score
        m_wrist = rebaWrist.Wrist(self.joints_position,self.joints_orientation)
        wrist_scores = m_wrist.wrist_reba_score()

        # step 10: Look up score in table _B
        posture_score_b = table_b[UA_scores[0] - 1][LA_scores - 1][wrist_scores[0] - 1]

        # step 11: coupling score
        coupling = 0
        # coupling = input("what is the coupling condition?(good(0) or fair(1) or poor(2) or unacceptable(3)? ")

        posture_score_b = posture_score_b + int(coupling)

        # step 12: look up score in table C
        posture_score_c = table_c[posture_score_a - 1][posture_score_b - 1]

        # step 13: Activity score
        # activity = 'static'
        # # activity = input("what is activity level?(static or repeated(small action more than 4 min) or rapid or none?")
        # if activity == 'static' or activity == 'repeated' or activity == 'rapid':
        #     posture_score_c = posture_score_c + 1

        reba_scores_vector = [posture_score_c, neck_scores[1], trunk_scores[1], leg_scores[0], UA_scores[1],
                              LA_scores, wrist_scores[1],
                              neck_scores[2], neck_scores[3],trunk_scores[2], trunk_scores[3], UA_scores[2], UA_scores[3], wrist_scores[2],
                                  wrist_scores[3]]

        return reba_scores_vector

    def degree_computation(self):
        # step1: Neck degree
        m_neck = rebaNeck.Neck(self.joints_position)#)
        neck_flex_degree = m_neck.neck_flex_calculator()
        neck_side_degree = m_neck.neck_side_calculator()
        # neck_torsion_degree = m_neck.neck_twist_calculator()
        neck_torsion_degree=0

        # step2: Trunk degree
        m_trunk = rebaTrunk.Trunk(self.joints_position)#,self.joints_orientation)
        trunk_flex_degree = m_trunk.trunk_flex_calculator()
        trunk_side_degree = m_trunk.trunk_side_calculator()
        # trunk_torsion_degree = m_trunk.trunk_twist_calculator()
        trunk_torsion_degree =0

        # step3: legs degree
        m_leg = rebaLeg.Leg(self.joints_position)
        leg_degrees = m_leg.leg_degree()
        right_leg_degree = leg_degrees[0]
        left_leg_degree = leg_degrees[1]

        # step4: Upper arm degree
        m_upper_arm = rebaUA.UpperArm(self.joints_position)
        UA_flex_degree = m_upper_arm.upper_arm_flex()
        right_UA_flex_degree = UA_flex_degree[0]
        left_UA_flex_degree = UA_flex_degree[1]
        UA_side_bending_degree = m_upper_arm.upper_arm_side_bending()
        right_UA_side_degree = UA_side_bending_degree[0]
        left_UA_side_degree = UA_side_bending_degree[1]
        UA_shoulder_rise_degree = m_upper_arm.shoulder_rise()
        right_UA_shoulder_rise_degree = UA_shoulder_rise_degree[0]
        left_UA_shoulder_rise_degree = UA_shoulder_rise_degree[1]

        # step 5: lower arm degree
        m_lower_arm = rebaLA.lower_arm(self.joints_position)
        LA_degrees = m_lower_arm.lower_arm_degree()
        right_LA_degree = LA_degrees[0]
        left_LA_degree = LA_degrees[1]

        # step 6: wrist degree
        m_wrist = rebaWrist.Wrist(self.joints_position)#,self.joints_orientation)
        wrist_flex_degrees = m_wrist.wrist_flex()
        right_wrist_flex_degree = wrist_flex_degrees[0]
        left_wrist_flex_degree = wrist_flex_degrees[1]
        wrist_side_degrees = m_wrist.wrist_side()
        right_wrist_side_degree = wrist_side_degrees[0]
        left_wrist_side_degree = wrist_side_degrees[1]
        wrist_torsion_degrees = m_wrist.wrist_side()
        right_wrist_torsion_degree = wrist_torsion_degrees[0]
        left_wrist_torsion_degree = wrist_torsion_degrees[1]

        degrees_vector = [neck_flex_degree, trunk_flex_degree, right_leg_degree, left_leg_degree, right_UA_flex_degree,
                          left_UA_flex_degree,
                          right_LA_degree, left_LA_degree, right_wrist_flex_degree, left_wrist_flex_degree,
                          neck_side_degree, neck_torsion_degree,
                          trunk_side_degree, trunk_torsion_degree,
                          right_UA_side_degree, left_UA_side_degree, right_UA_shoulder_rise_degree,
                          left_UA_shoulder_rise_degree,
                          right_wrist_side_degree, left_wrist_side_degree, right_wrist_torsion_degree,
                          left_wrist_torsion_degree
                          ]

        return degrees_vector

