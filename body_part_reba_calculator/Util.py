import math
import numpy as np
import reba_score_calculation.Matrixes as Mat


def get_angle_between_degs(v1, v2):
    len_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
    len_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2)

    result = math.acos(round(np.dot(v1, v2) / (len_v1 * len_v2), 3)) * 180 / math.pi
    return result


def get_distance_between(p1, p2):
    result = [x + y for x, y in zip(p2, np.dot(p1, -1))]
    return math.sqrt(result[0] ** 2 + result[1] ** 2 + result[2] ** 2)


def normalization(vector):
    l = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    if l == 0:
        l += 0.01
    normal_vector = [vector[0] / l, vector[1] / l, vector[2] / l]
    return normal_vector


def find_rotation_quaternion(outer_quaternion, inner_quaternion):
    conjucate = [outer_quaternion[0], -outer_quaternion[1], -outer_quaternion[2], -outer_quaternion[3]]
    length = math.sqrt(outer_quaternion[0] ** 2 + outer_quaternion[1] ** 2 +
                       outer_quaternion[2] ** 2 + outer_quaternion[3] ** 2)
    inverse = np.dot(conjucate, (1 / length))
    rotation = Mat.multiply_two_quaternion(inner_quaternion, inverse)
    return rotation
