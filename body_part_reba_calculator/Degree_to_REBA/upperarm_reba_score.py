class UAREBA:
    # For calculating REBA score based on degrees
    def __init__(self, UA_degrees):
        self.UA_degrees = UA_degrees

    def upper_arm_reba_score(self):
        upper_arm_reba_score = 0
        upper_arm_flex_score = 0
        upper_arm_side_score = 0
        upper_arm_shoulder_rise = 0


        right_flexion = self.UA_degrees[0]
        left_flexion = self.UA_degrees[1]

        right_side = self.UA_degrees[2]
        left_side = self.UA_degrees[3]

        right_shoulder_rise = self.UA_degrees[4]
        left_shoulder_rise = self.UA_degrees[5]

        if right_flexion >= left_flexion:
            if -20 <= right_flexion < 20:
                upper_arm_reba_score += 1
                upper_arm_flex_score += 1
            if 20 <= right_flexion < 45:
                upper_arm_reba_score += 2
                upper_arm_flex_score += 2
            if right_flexion < -20:
                upper_arm_reba_score += 2
                upper_arm_flex_score += 2
            if 45 <= right_flexion < 90:
                upper_arm_reba_score += 3
                upper_arm_flex_score += 3
            if 90 <= right_flexion:
                upper_arm_reba_score += 4
                upper_arm_flex_score += 4
        if right_flexion < left_flexion:
            if -20 <= left_flexion < 20:
                upper_arm_reba_score += 1
                upper_arm_flex_score += 1
            if left_flexion < -20:
                upper_arm_reba_score += 2
                upper_arm_flex_score += 2
            if 20 <= left_flexion < 45:
                upper_arm_reba_score += 2
                upper_arm_flex_score += 2
            if 45 <= left_flexion < 90:
                upper_arm_reba_score += 3
                upper_arm_flex_score += 3
            if 90 <= left_flexion:
                upper_arm_reba_score += 4
                upper_arm_flex_score += 4

            # for side bending
            if abs(right_side) > 2 or abs(left_side) > 2:
                upper_arm_reba_score += 1
                upper_arm_side_score += 1

            # for shoulder rise

            if right_shoulder_rise > 90 or left_shoulder_rise > 90:
                upper_arm_reba_score += 1
                upper_arm_shoulder_rise += 1
        return [upper_arm_reba_score, upper_arm_flex_score, upper_arm_side_score, upper_arm_shoulder_rise]