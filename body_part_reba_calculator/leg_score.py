from pycg3d.cg3d_point import CG3dPoint
from pycg3d.cg3d_vector import CG3dVector
import math
from pycg3d import utils


def leg_score(joints,file):
    right_hip_index = 9
    left_hip_index = 12
    right_knee_index = 10
    left_knee_index = 13
    right_ankle_index = 11
    left_ankle_index = 14

    right_hip_point = CG3dPoint(joints[right_hip_index][0], joints[right_hip_index][1],
                                joints[right_hip_index][2])
    left_hip_point = CG3dPoint(joints[left_hip_index][0], joints[left_hip_index][1], joints[left_hip_index][2])

    right_knee_point = CG3dPoint(joints[right_knee_index][0], joints[right_knee_index][1],
                                 joints[right_knee_index][2])
    left_knee_point = CG3dPoint(joints[left_knee_index][0], joints[left_knee_index][1],
                                joints[left_knee_index][2])

    right_ankle_point = CG3dPoint(joints[right_ankle_index][0], joints[right_ankle_index][1],
                                  joints[right_ankle_index][2])
    left_ankle_point = CG3dPoint(joints[left_ankle_index][0], joints[left_ankle_index][1],
                                 joints[left_ankle_index][2])

    right_knee_hip_vector = CG3dVector(right_hip_point[0] - right_knee_point[0],
                                       right_hip_point[1] - right_knee_point[1],
                                       right_hip_point[2] - right_knee_point[2])
    right_ankle_knee_vector = CG3dVector(right_knee_point[0] - right_ankle_point[0],
                                         right_knee_point[1] - right_ankle_point[1],
                                         right_knee_point[2] - right_ankle_point[2])

    left_knee_hip_vector = CG3dVector(left_hip_point[0] - left_knee_point[0],
                                      left_hip_point[1] - left_knee_point[1],
                                      left_hip_point[2] - left_knee_point[2])
    left_ankle_knee_vector = CG3dVector(left_knee_point[0] - left_ankle_point[0],
                                        left_knee_point[1] - left_ankle_point[1],
                                        left_knee_point[2] - left_ankle_point[2])

    # knee degree
    right_knee_degree = math.degrees(math.acos((right_knee_hip_vector * right_ankle_knee_vector) / (
            utils.distance(right_hip_point, right_knee_point) * utils.distance(right_knee_point,
                                                                               right_ankle_point))))
    left_knee_degree = math.degrees(math.acos((left_knee_hip_vector * left_ankle_knee_vector) / (
            utils.distance(left_hip_point, left_knee_point) * utils.distance(left_knee_point, left_ankle_point))))

    leg_reba_score = 0
    # if right_alpha != left_knee_degree:
    #     leg_reba_score = leg_reba_score + 2
    if (joints[right_ankle_index][0] != joints[left_ankle_index][0] and joints[right_ankle_index][1] !=
          joints[left_ankle_index][1] and joints[right_ankle_index][2] != joints[left_ankle_index][2]):
        leg_reba_score = leg_reba_score + 2
        if abs(right_knee_degree)>= abs(left_knee_degree):
            file.write(str(right_knee_degree) + ',')
        else:
            file.write(str(left_knee_degree) + ',')
        return leg_reba_score
    if abs(right_knee_degree) >= abs(left_knee_degree):
        if right_knee_degree < 30:
            leg_reba_score = leg_reba_score + 1
        if 30 <= right_knee_degree < 60:
            leg_reba_score = leg_reba_score + 1
        if 60 <= right_knee_degree:
            leg_reba_score = leg_reba_score + 2

        file.write(str(right_knee_degree) + ',')
    else:
        if left_knee_degree < 30:
            leg_reba_score = leg_reba_score + 1
        if 30 <= left_knee_degree < 60:
            leg_reba_score = leg_reba_score + 1
        if 60 <= left_knee_degree:
            leg_reba_score = leg_reba_score + 2
        file.write(str(left_knee_degree) + ',')

    return leg_reba_score
