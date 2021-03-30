class LegREBA:
    # For calculating REBA score based on degrees
    def __init__(self, leg_degrees):
        self.leg_degrees = leg_degrees

    def leg_reba_score(self):
        leg_degrees = self.leg_degrees
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