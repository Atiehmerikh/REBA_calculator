# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d, Axes3D
# from pycg3d.cg3d_point import CG3dPoint
# from pycg3d import utils
# import numpy as np
#
#
# class Draw:
#     def __init__(self, joints):
#         self.joints = joints
#         self.head_index = 0
#         self.neck_index = 1
#         self.right_shoulder_index = 2
#         self.right_elbow_index = 3
#         self.right_hand_index = 4
#         self.left_shoulder_index = 5
#         self.left_elbow_index = 6
#         self.left_hand_index = 7
#         self.base = 8
#         self.right_hip = 9
#         self.right_knee = 10
#         self.right_foot = 11
#         self.left_hip = 12
#         self.left_knee = 13
#         self.left_foot = 14
#
#         self.rightArmIndex = [self.right_shoulder_index, self.right_elbow_index, self.right_hand_index]
#         self.leftArmIndex = [self.left_shoulder_index, self.left_elbow_index, self.left_hand_index]
#         self.upperChain = [self.base, self.right_shoulder_index, self.left_shoulder_index, self.base]
#         self.lowerChain = [self.base, self.right_hip, self.left_hip, self.base]
#         self.rightLeg = [self.right_foot, self.right_knee, self.right_hip]
#         self.leftLeg = [self.left_foot, self.left_knee, self.left_hip]
#         self.neckHead = [self.neck_index,self.head_index,self.head_index]
#
#     def set_axes_radius(self,   ax, origin, radius):
#         ax.set_xlim3d([origin[0] - radius, origin[0] + radius])
#         ax.set_ylim3d([origin[1] - radius, origin[1] + radius])
#         ax.set_zlim3d([origin[2] - radius, origin[2] + radius])
#
#     def set_axes_equal(self, ax):
#         limits = np.array([
#             ax.get_xlim3d(),
#             ax.get_ylim3d(),
#             ax.get_zlim3d(),
#         ])
#
#         origin = np.mean(limits, axis=1)
#         radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
#         self.set_axes_radius(ax, origin, radius)
#
#     def fill_array(self, body_part_index, joints):
#         w, h = 3, len(body_part_index)
#         coordinate = [[0 for x in range(w)] for y in range(h)]
#         # coordinate =[][len(body_part_index)]
#         x = []
#         y = []
#         z = []
#         for i in range(len(body_part_index)):
#             x.append(joints[body_part_index[i]][0])
#             y.append(joints[body_part_index[i]][1])
#             z.append(joints[body_part_index[i]][2])
#         coordinate[0][:] = x
#         coordinate[1][:] = y
#         coordinate[2][:] = z
#         return coordinate
#
#     def draw_final(self):
#         # The Second Pose
#         coordinate = self.fill_array(self.rightArmIndex, self.joints)
#         x_primeRArm = coordinate[0]
#         y_primeRArm = coordinate[1]
#         z_primeRArm = coordinate[2]
#
#         coordinate = self.fill_array(self.leftArmIndex, self.joints)
#         x_primeLArm = coordinate[0]
#         y_primeLArm = coordinate[1]
#         z_primeLArm = coordinate[2]
#
#         coordinate = self.fill_array(self.upperChain, self.joints)
#         x_primeU = coordinate[0]
#         y_primeU = coordinate[1]
#         z_primeU = coordinate[2]
#
#         coordinate = self.fill_array(self.lowerChain, self.joints)
#         x_primeL = coordinate[0]
#         y_primeL = coordinate[1]
#         z_primeL = coordinate[2]
#
#         coordinate = self.fill_array(self.rightLeg, self.joints)
#         x_primeRLeg = coordinate[0]
#         y_primeRLeg = coordinate[1]
#         z_primeRLeg = coordinate[2]
#
#         coordinate = self.fill_array(self.leftLeg, self.joints)
#         x_primeLLeg = coordinate[0]
#         y_primeLLeg = coordinate[1]
#         z_primeLLeg = coordinate[2]
#
#         coordinate = self.fill_array(self.neckHead, self.joints)
#         x_primeNeckHead = coordinate[0]
#         y_primeNeckHead = coordinate[1]
#         z_primeNeckHead = coordinate[2]
#
#         fig = plt.figure()
#         ax = fig.gca(projection='3d')
#
#         ax.plot3D(x_primeRArm, y_primeRArm,z_primeRArm, color='green')
#         ax.plot3D(x_primeLArm, y_primeLArm, z_primeLArm, color='green')
#         ax.plot3D(x_primeU, y_primeU, z_primeU, color='green')
#         ax.plot3D(x_primeL, y_primeL, z_primeL, color='green')
#         ax.plot3D(x_primeRLeg, y_primeRLeg, z_primeRLeg, color='green')
#         ax.plot3D(x_primeLLeg, y_primeLLeg, z_primeLLeg, color='green')
#         ax.plot3D(x_primeNeckHead, y_primeNeckHead, z_primeNeckHead, color='green')
#         # ax.plot3D(x_primeHead, y_primeHead, z_primeHead, color='green')
#
#         # FrightUpperArmLength = distance_calculation(joints[0], joints[9])
#         # LrightUpperArmLength = distance_calculation(first_pos[0], first_pos[9])
#         #
#         # # ax.scatter3D(joints[head[1]][0], joints[head[1]][1], joints[head[1]][2],edgecolors='green')
#         # ax.scatter3D(self.target[0], self.target[1], self.target[2])
#         #
#         self.set_axes_equal(ax)
#         plt.show()
#
#     def distance_calculation(i, j):
#         i_point = CG3dPoint(i[0], i[1], i[2])
#         j_point = CG3dPoint(j[0], j[1], j[2])
#
#         return utils.distance(i_point, j_point)
