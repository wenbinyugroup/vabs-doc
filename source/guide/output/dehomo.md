# Dehomogenization Outputs

If `analysis` is equal to 1 or 2, VABS will carry out a dehomogenization analysis to predict 3D displacements/strains/stresses based on the nonlinear or linear beam theory.
The recovered 3D displacements are stored in `input_file_name.U`.
The values are listed for each node identified by its location as
```
x2  x3  u1  u2  u3
```
where `x2` and `x3` are the coordinates of the node, `ui` the recovered 3D displacements at this node, expressed in the beam coordinate system.

The recovered 3D strains for each Gauss point measured in the beam coordinate system are stored in `input_file_name.E`.
The values are listed for each Gauss point identified by its location as
```
x2  x3  epsilon11  2epsilon12  2epsilon13  epsilon22  2epsilon23  epsilon33
```
where `epsilonij` are the 3D strain components.
The recovered 3D strains measured in the material coordinate system are stored in `input_file_name.EM`.

The recovered 3D stresses for each Gauss point measured in the beam coordinate system are stored in `input_file_name.S`.
The values are listed for each Gauss point identified by its location as
```
x2  x3  sigma11  sigma12  sigma13  sigma22  sigma23  sigma33
```
where `sigmaij` are the 3D stress components.
The recovered 3D stresses measured in the material coordinate system are stored in `input_file_name.SM`.

The recovered 3D strains for each node measured in the beam coordinate systems are stored in `input_file_name.EN`.
The values are listed for each node identified by its node number and the location as
```
node_no  x2  x3  epsilon11  2epsilon12  2epsilon13  epsilon22  2epsilon23  epsilon33
```
where `node_no` denotes the node number originally given in the homogenization input file.
The node number is arranged consecutively from 1 to the total number of nodes.
Multiple strain values could exist for one node if the node is shared by multiple elements.
The recovered 3D strains for each node measured in the material coordinate system are stored in `input_file_name.EMN`.
The corresponding recovered 3D stresses for each node measured in the beam coordinate system and the material coordinate system are stored in `input_file_name.SN` and `input_file_name.SMN`, respectively.

The average of 3D strains and stresses among all the Gauss points within each element are stored in `input_file_name.ELE`, where the integer number indicating the element number, the following six real numbers are strains measured in the beam coordinate system, the next six real numbers are the stresses measured in the beam coordinate system, the next six real numbers are strains measured in the material coordinate system, the last six real numbers are the stresses measured in the material coordinate system.

If `analysis` is equal to 10 or 20, only `input_file_name.ELE` will be written and all other files will be suppressed for saving time and space.
The savings become significant particularly for many dehomogenization runs needed for automatic optimization.

If `analysis` is equal to 3, VABS will carry out a dehomogenization analysis to compute failure indexes and strength ratios for each element based on the recovered results of the linear beam theory.
The results are stored in `input_file_name.fi`, where the integer number indicating the element number, the following real number is the failure index for the element, and the next real number is the strength ratio for the element.
If a failure criterion with clearly identifiable failure modes is used, such as failure criterion 1 (max stress), 2 (max strain), 5 (Hashin), VABS will also output the corresponding failure mode for each element in the following column.
For criterion 1 or 2, the failure modes could be normal stress failure including 11 tensile (compressive), 22 tensile (or compressive), 33 tensile (or compressive), and shear failure including 23, 13, 12.
For criterion 5, the failure modes could be fiber (tensile or compressive) failure, or matrix (tensile or compressive) failure.
For criterion 1 or 2, six more columns are also used to indicate the strength ratios for corresponding stress/strain components (11, 22, 33, 23, 13, 12).
For criterion 5, two more column are also used to indicate the strength ratios for fiber and matrix failure.
The last line of this output file stores the minimum strength ratio among all the elements, and the smallest element number when this happens.
The minimum strength ratio is the safety margin of the cross-section under the given global responses.
