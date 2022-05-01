import math
import numpy as np
import csv
import os


def find_euler(rot_mat):
    if rot_mat[0][2] == 1 or rot_mat[0][2] == -1:
        E3 = 0
        dlta = math.atan2(rot_mat[0][1], rot_mat[0][2])
        if rot_mat[0][2] == -1:
            E2 = math.pi / 2
            E1 = E3 + dlta
        else:
            E2 = -math.pi / 2
            E1 = -E3 + dlta
    else:
        E2 = - math.asin(rot_mat[0][2])
        E1 = math.atan2(rot_mat[1][2] / math.cos(E2), rot_mat[2][2] / math.cos(E2))
        E3 = math.atan2(rot_mat[0][1] / math.cos(E2), rot_mat[0][0] / math.cos(E2))

    return [E1, E2, E3]


def euler_to_quaternion(roll, pitch, yaw):
    qx = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
    qy = np.cos(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2)
    qz = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2)
    qw = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)

    return [qx, qy, qz, qw]


body_part_names_xsens = ["Head", "Hips", "LeftShoulder", "LeftToe", "LeftElbow", "LeftWrist", "LeftKnee", "LeftHip",
                         "Neck",
                         "RightShoulder"
    , "RightToe", "RightElbow", "RightWrist", "RightKnee", "RightHip", "Chest2", "Chest3"]

body_part_numbers = [2, 18, 3, 13, 4, 5, 12, 11, 17, 7, 16, 8, 9, 15, 14, 0, 1]

for i in range(1, 1150):
    file1 = open("./Files/positions-xsens/joints-position-" + str(i) + ".csv", "w")
    file1_rot = open("./Files/rotations-xsens/joints-rotation-" + str(i) + ".csv", "w")

    writer = csv.writer(file1)
    writer2 = csv.writer(file1_rot)

    for j in range(0, len(body_part_names_xsens)):
        address = os.path.join(
            "./MotionBox_XSens_Transposed/" + body_part_names_xsens[
                j] + "/Translation Matrix/TranslationMatrixFrame" + str(
                i) + ".csv")
        address_rot = os.path.join(
            "./MotionBox_XSens_Transposed/" + body_part_names_xsens[j] + "/Rotation Matrix/RotationMatrixFrame" + str(
                i) + ".csv")

        row_toadd = []
        row_toadd_rot = []
        matrix_rot = []

        with open(address) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                row_toadd.append([float(row[0]), float(row[1]), float(row[2])])
        writer.writerow(row_toadd)

        with open(address_rot) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row_rot in csv_reader:
                matrix_rot.append([float(row_rot[0]), float(row_rot[1]), float(row_rot[2])])
        euler_angle = find_euler(matrix_rot)
        quaternions = euler_to_quaternion(euler_angle[0], euler_angle[1], euler_angle[2])
        writer2.writerow(quaternions)

    file1.close()
    file1_rot.close()

for i in range(1, 1150):
    file1 = open("./Files/position-xsens-reordered/joints-position-" + str(i) + ".txt", "w")
    file1_rot = open("./Files/rotation-xsens-reordered/joints-rotation-" + str(i) + ".txt", "w")

    writer = csv.writer(file1)
    writer2 = csv.writer(file1_rot)
    address_position = os.path.join("./Files/positions-xsens/joints-position-" + str(i) + ".csv")
    address_rotation = os.path.join("./Files/rotations-xsens/joints-rotation-" + str(i) + ".csv")
    row_posi = np.zeros((len(body_part_names_xsens) + 2, 3))
    row_roti = np.zeros((len(body_part_names_xsens) + 2, 4))

    with open(address_position) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            split_string1 = row[0].split('[')
            split_string2 = split_string1[1].split(']')
            split_string3 = split_string2[0].split(',')
            row_posi[body_part_numbers[line_count]] = [float(split_string3[0]),float(split_string3[1]),float(split_string3[2])]
            line_count += 1

    with open(address_rotation) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            row_roti[body_part_numbers[line_count]] = row
            line_count += 1

    for k in range(0, len(row_posi)):
        writer.writerow(row_posi[k])
        writer2.writerow(row_roti[k])
    file1.close()
    file1_rot.close()
