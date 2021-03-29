import sys
import numpy as np
# sys.path.append('..')
import body_part_reba_calculator as reba_calculator

def test():
    joints_position = np.loadtxt("joints_position_drink.txt")
    joints_orientation = np.loadtxt("joints_orientation_drink.txt")

    m_reba = reba_calculator.RebaScoreCalculator(joints_position,joints_orientation)
    reba_score_array = m_reba.reba_computation()
    print(reba_score_array[0])
    # joints_degree_array = m_reba.degree_computation()



test()