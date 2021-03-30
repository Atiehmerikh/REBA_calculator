

class NeckREBA:
    # For calculating REBA score based on degrees
    def __init__(self, neck_degrees):
        self.neck_degrees = neck_degrees

    def neck_reba_score(self):
        neck_flex_degree = self.neck_degrees[0]
        neck_side_bending_degree = self.neck_degrees[1]
        neck_twist_degree = self.neck_degrees[2]

        neck_reba_score = 0
        neck_flex_score = 0
        neck_side_score = 0
        neck_torsion_score = 0

        if neck_flex_degree >= 0:
            if 0 <= neck_flex_degree < 20:
                neck_reba_score += 1
                neck_flex_score += 1
            if 20 <= neck_flex_degree:
                neck_reba_score += 2
                neck_flex_score += 2
        else:
            # neck is in extension
            neck_reba_score += 2
            neck_flex_score += 2

        if abs(neck_side_bending_degree) >= 1:
            neck_reba_score += 1
            neck_side_score += 1
        if abs(neck_twist_degree) >= 1:
            neck_reba_score += 1
            neck_torsion_score += 1

        return [neck_reba_score, neck_flex_score, neck_side_score, neck_torsion_score]