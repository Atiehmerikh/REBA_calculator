import numpy as np
import body_part_reba_calculator.Degree_to_REBA.neck_reba_score as RebaNeck
import body_part_reba_calculator.Degree_to_REBA.trunk_reba_score as RebaTrunk
import body_part_reba_calculator.Degree_to_REBA.leg_reba_score as RebaLeg
import body_part_reba_calculator.Degree_to_REBA.upperarm_reba_score as RebaUA
import body_part_reba_calculator.Degree_to_REBA.lowerarm_reba_score as RebaLA
import body_part_reba_calculator.Degree_to_REBA.wrist_reba_score as RebaWrist


class DegreeToREBA:

    def __init__(self, joints_degree):
        self.joints_degree = joints_degree

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
        neck_degrees = self.joints_degree[0]
        m_neck_REBA = RebaNeck.NeckREBA(neck_degrees)
        neck_scores = m_neck_REBA.neck_reba_score()

        # step2: locate trunck posture
        trunk_degrees = self.joints_degree[1]
        m_trunk_REBA = RebaTrunk.TrunkREBA(trunk_degrees)
        trunk_scores = m_trunk_REBA.trunk_reba_score()

        # step3: locate legs
        leg_degrees = self.joints_degree[2]
        m_leg_REBA = RebaLeg.LegREBA(leg_degrees)
        leg_scores = m_leg_REBA.leg_reba_score()
        # leg_scores =[1]

        # step 4: Look up score in table _A
        if neck_scores[0] - 1>2:
            neck_scores[0] = 3
        if trunk_scores[0] - 1>4:
            trunk_scores[0]  = 5
        if leg_scores[0] - 1>3:
            leg_scores[0] = 4
        posture_score_a = table_a[neck_scores[0] - 1][trunk_scores[0] - 1][leg_scores[0] - 1]

        # step 5: load score
        # load = input("what is the load(in lbs) ")
        load = 0
        if 11 <= int(load) < 22:
            posture_score_a = posture_score_a + 1
        if 22 <= int(load):
            posture_score_a = posture_score_a + 2

        # step 7: upper arm score
        UA_degrees = self.joints_degree[3]
        m_upper_arm_REBA = RebaUA.UAREBA(UA_degrees)
        UA_scores = m_upper_arm_REBA.upper_arm_reba_score()

        # step 8: lower arm score
        LA_degrees = self.joints_degree[4]
        m_lower_arm_REBA = RebaLA.LAREBA(LA_degrees)
        LA_scores = m_lower_arm_REBA.lower_arm_score()

        # step 9: wrist score
        wrist_degrees = self.joints_degree[5]
        m_wrist_REBA = RebaWrist.WristREBA(wrist_degrees)
        wrist_scores = m_wrist_REBA.wrist_reba_score()

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
                              neck_scores[2], neck_scores[3], trunk_scores[2], trunk_scores[3], UA_scores[2],
                              UA_scores[3], wrist_scores[2],
                              wrist_scores[3]]

        return reba_scores_vector
