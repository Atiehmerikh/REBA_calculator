# REBA calculation
## Description:
The Rapid Entire Body Assessment method is a rapid method to evaluate the risk of musculoskeletal disorders(MSD) caused by working in the industry.   
In this method, by using a step-wise procedure, the overall ergonomic status of humans is evaluated. In each step, the joints degree is calculated, and by utilizing some tables, the score is evaluated, and at the end, the final REBA score determines the worker's ergonomic status. 
The complete description and pictures can be seen in the provided link:

[https://ergo-plus.com/reba-assessment-tool-guide/](https://ergo-plus.com/reba-assessment-tool-guide/)


The REBA calculation is done in 6 steps.
1.   Neck
2.   Trunk
3.   Legs
4.   Upper arms
5.   Lower arms
6.   Wrists

In each above step, the degree associated with the mentioned body part is evaluated, and its REBA score is derived from the table.
## Code:
This library consists of two main module:
1.  [Pose\_to\_degree](https://github.com/Atiehmerikh/REBA_calculator/tree/master/body_part_reba_calculator/Pose_to_degrees "Pose_to_degrees")
2.  [Degree\_to\_REBA](https://github.com/Atiehmerikh/REBA_calculator/tree/master/body_part_reba_calculator/Degree_to_REBA "Degree_to_REBA")


The first module, by receiving the joints pose data(position, orientation), can evaluate the joints' degree to make it ready for REBA calculation. These joints pose data that can be fed by motion capture devices or datasets.   
For instance, \[1\] provided some pose datasets that can be fed to this module.   
After the joints, degrees are computed. Based on the tables, the REBA score is calculated for each body part and also the final REBA score. This final score is a measure for evaluating the ergonomic condition of the posture.

## References
\[1\] . Morana, Marco; Lo Re, Giuseppe; Gaglio, Salvatore (2017), “KARD - Kinect Activity Recognition Dataset”, Mendeley Data, V1, doi: 10.17632/k28dtm7tr6.1
