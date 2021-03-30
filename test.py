import sys
import numpy as np
# sys.path.append('..')
import body_part_reba_calculator.Pose_to_degrees as transformer
import body_part_reba_calculator.Degree_to_REBA as REBA


def test():
    joints_position = np.loadtxt("joints_position_drink.txt")
    joints_orientation = np.loadtxt("joints_orientation_drink.txt")

    m_transformer = transformer.PoseToDeg(joints_position,joints_orientation)
    joints_degrees = m_transformer.degree_computation()

    m_reba = REBA.DegreeToREBA(joints_degrees)
    REBA_scores = m_reba.reba_computation()

    print(REBA_scores)
    # joints_degree_array = m_reba.degree_computation()


test()