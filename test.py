import sys
import numpy as np
# sys.path.append('..')
import body_part_reba_calculator.Pose_to_degrees as transformer
import body_part_reba_calculator.Degree_to_REBA as REBA
import csv
import xlrd
import xlsxwriter
import matplotlib.pyplot as plt



def test():

    rebas = []

    for i in range(1, 547):

        address = "./Files/position-reordered/joints-position-" + str(i) + ".txt"
        address_rot = "./Files/rotation-reordered/joints-rotation-" + str(i) + ".txt"
        #
        joints_position = np.full((19, 3), 0)
        joints_orientation = np.full((19, 4), 0)

        with open(address) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                joints_position[line, :] = ([float(row[0]), float(row[1]), float(row[2])])
                line = line + 1

        with open(address_rot) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                joints_orientation[line, :] = ([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
                line = line + 1

        # joints_position = np.loadtxt("joints_position_drink.txt")
        # joints_orientation = np.loadtxt("joints_orientation_drink.txt")

        m_transformer = transformer.PoseToDeg(joints_position, joints_orientation)
        joints_degrees = m_transformer.degree_computation()

        m_reba = REBA.DegreeToREBA(joints_degrees)
        REBA_scores = m_reba.reba_computation()

        print(REBA_scores[0])
        rebas.append(REBA_scores[0])

    plt.plot(rebas)
    plt.show()

    # joints_degree_array = m_reba.degree_computation()

    # joints_position = np.loadtxt("joints_position_drink.txt")
    # joints_orientation = np.loadtxt("joints_orientation_drink.txt")
    #
    # m_transformer = transformer.PoseToDeg(joints_position,joints_orientation)
    # joints_degrees = m_transformer.degree_computation()
    # print(joints_degrees)

    # wb = xlrd.open_workbook('dREBA_optimized_joints.xlsx')
    # workbook = xlsxwriter.Workbook('REBA_dREBA_optimized.xlsx')
    # worksheet = workbook.add_worksheet()
    #
    # sheet = wb.sheet_by_index(0)
    # for k in range(sheet.nrows):
    #     joints_degrees = []
    #     neck =[]
    #     trunk=[]
    #     leg=[]
    #     ua=[]
    #     la=[]
    #     wrist=[]
    #
    #     for i in range(0,3):
    #         neck.append(sheet.cell_value(k,i))
    #     joints_degrees.append(neck)
    #
    #     for i in range(3,6):
    #         trunk.append(sheet.cell_value(k,i))
    #     joints_degrees.append(trunk)
    #
    #     for i in range(6,8):
    #         leg.append(sheet.cell_value(k,i))
    #
    #     joints_degrees.append(leg)
    #
    #     for i in range(8,14):
    #         ua.append(sheet.cell_value(k,i))
    #     joints_degrees.append(ua)
    #     for i in range(14,16):
    #         la.append(sheet.cell_value(k,i))
    #
    #     joints_degrees.append(la)
    #
    #     for i in range(16,22):
    #         wrist.append(sheet.cell_value(k,i))
    #     joints_degrees.append(wrist)
    #
    #     m_reba = REBA.DegreeToREBA(joints_degrees)
    #     REBA_scores = m_reba.reba_computation()
    #     worksheet.write(k,0,REBA_scores[0])
    # joints_degree_array = m_reba.degree_computation()

    # workbook.close()

def test_xsens():

    rebas = []

    for i in range(1, 1150):

        address = "./Files/position-xsens-reordered/joints-position-" + str(i) + ".txt"
        address_rot = "./Files/rotation-xsens-reordered/joints-rotation-" + str(i) + ".txt"
        #
        joints_position = np.full((19, 3), 0)
        joints_orientation = np.full((19, 4), 0)

        with open(address) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                joints_position[line, :] = ([float(row[0]), float(row[1]), float(row[2])])
                line = line + 1

        with open(address_rot) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader:
                joints_orientation[line, :] = ([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
                line = line + 1

        # joints_position = np.loadtxt("joints_position_drink.txt")
        # joints_orientation = np.loadtxt("joints_orientation_drink.txt")

        m_transformer = transformer.PoseToDeg(joints_position, joints_orientation)
        joints_degrees = m_transformer.degree_computation()

        m_reba = REBA.DegreeToREBA(joints_degrees)
        REBA_scores = m_reba.reba_computation()

        print(REBA_scores[0])
        rebas.append(REBA_scores[0])

    plt.plot(rebas)
    plt.show()

    # joints_degree_array = m_reba.degree_computation()

    # joints_position = np.loadtxt("joints_position_drink.txt")
    # joints_orientation = np.loadtxt("joints_orientation_drink.txt")
    #
    # m_transformer = transformer.PoseToDeg(joints_position,joints_orientation)
    # joints_degrees = m_transformer.degree_computation()
    # print(joints_degrees)

    # wb = xlrd.open_workbook('dREBA_optimized_joints.xlsx')
    # workbook = xlsxwriter.Workbook('REBA_dREBA_optimized.xlsx')
    # worksheet = workbook.add_worksheet()
    #
    # sheet = wb.sheet_by_index(0)
    # for k in range(sheet.nrows):
    #     joints_degrees = []
    #     neck =[]
    #     trunk=[]
    #     leg=[]
    #     ua=[]
    #     la=[]
    #     wrist=[]
    #
    #     for i in range(0,3):
    #         neck.append(sheet.cell_value(k,i))
    #     joints_degrees.append(neck)
    #
    #     for i in range(3,6):
    #         trunk.append(sheet.cell_value(k,i))
    #     joints_degrees.append(trunk)
    #
    #     for i in range(6,8):
    #         leg.append(sheet.cell_value(k,i))
    #
    #     joints_degrees.append(leg)
    #
    #     for i in range(8,14):
    #         ua.append(sheet.cell_value(k,i))
    #     joints_degrees.append(ua)
    #     for i in range(14,16):
    #         la.append(sheet.cell_value(k,i))
    #
    #     joints_degrees.append(la)
    #
    #     for i in range(16,22):
    #         wrist.append(sheet.cell_value(k,i))
    #     joints_degrees.append(wrist)
    #
    #     m_reba = REBA.DegreeToREBA(joints_degrees)
    #     REBA_scores = m_reba.reba_computation()
    #     worksheet.write(k,0,REBA_scores[0])
    # joints_degree_array = m_reba.degree_computation()

    # workbook.close()
test_xsens()
test()
