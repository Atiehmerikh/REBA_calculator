class WristREBA:
    # For calculating REBA score based on degrees
    def __init__(self, Wrist_degrees):
        self.Wrist_degrees = Wrist_degrees

    def wrist_reba_score(self):
        wrist_reba_score = 0
        wrist_flex_score = 0
        wrist_side_bend_score = 0
        wrist_torsion_score = 0

        right_flex = self.Wrist_degrees[0]
        left_flex = self.Wrist_degrees[1]

        right_side = self.Wrist_degrees[2]
        left_side = self.Wrist_degrees[3]

        right_twist = self.Wrist_degrees[4]
        left_twist = self.Wrist_degrees[5]

        if right_flex > left_flex:
            if -15 <= right_flex < 15:
                wrist_reba_score += 1
                wrist_flex_score += 1
            if 15 <= right_flex or right_flex < -15:
                wrist_reba_score += 2
                wrist_flex_score += 2
        else:
            if -15 <= left_flex < 15:
                wrist_reba_score += 1
                wrist_flex_score += 1
            if 15 <= left_flex or left_flex < -15:
                wrist_reba_score += 2
                wrist_flex_score += 2

        if right_side != 0 or left_side != 0:
            wrist_reba_score += 1
            wrist_side_bend_score += 1

        if right_twist != 0 or left_twist !=0 :
            wrist_torsion_score +=1
            wrist_reba_score += 1

        return [wrist_reba_score, wrist_flex_score, wrist_side_bend_score, wrist_torsion_score]