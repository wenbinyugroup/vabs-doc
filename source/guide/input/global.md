# Dehomogenization Input File

If `analysis` in Section [6](#page-10-1) is equal to 1,2, 3, users should provide additional information in the dehomogenization input file for VABS to perform a dehomogenization analysis.
A corresponding homogenization analysis must be run before carrying out the dehomogenization analysis.

If `analysis` is equal to 3, VABS will perform failure analysis of the cross-section.
Strength properties for each material must be provided in the dehomogenization input file.
Strength properties for each material include a failure criterion and corresponding strength constants.
Two lines will be inserted and the inputs needed for failure analyses should be arranged as:
```
failure_criterion  num_of_constants
const1  const2  const3  ...
```
`failure_criterion` is an integer identifier for the failure criterion.
`num_of_constants` indicates the number of strength constants needed for the corresponding failure criterion.
`const1  const2  const3  ...` are the corresponding strength constants.
It is noted that this block of data should be corresponding to the material block in the homogenization input file.
In other words, for each material with mat id, we need to provide such information.

`failure_criterion` can be equal to 1, 2, 3, 4, 5, and another number greater than 10.
For isotropic material, 1 is max principal stress criterion, 2 is max principal strain criterion, 3 is max shear stress criterion (also commonly called Tresca criterion), 4 max shear strain criterion, and 5 is Mises criterion.
For anisotropic materials, 1 is max stress criterion for anisotropic materials, 2 is max strain criterion for anisotropic materials, 3 is Tsai-Hill criterion, 4 is Tsai-Wu criterion and 5 is Hashin criterion.
11 and larger indicates a user-defined failure criterion.
It is assumed that the number of strength constants will not be greater than 9 for a material.
If the material is isotropic, the failure criterion and corresponding strength constants are defined as follows:
- If `failure_criterion` is 1, the max principal stress criterion is used and two strength constants are needed: one for tensile strength ($X$) and one for compressive strength ($X^′$ ), arranged as $X$, $X^′$ .
- If `failure_criterion` is 2, the max principal strain criterion is used and two strength constants in terms of strains are needed: one for tensile strength ($X_\varepsilon$) and one for compressive strength ($X^′_{\varepsilon}$), arranged as $X_\varepsilon$, $X^′_\varepsilon$.
- If `failure_criterion` is 3, the max shear stress criterion (aka Tresca criterion) is used and one shear strength constant ($S$) is needed.
- If `failure_criterion` is 4, the max shear strain criterion is used and one shear strength constant in terms of strains ($S_\varepsilon$) is needed.
- If `failure_criterion` is 5, the Mises criterion is used and one strength constant ($X$) is needed.

If the material is not isotropic (transversely isotropic, orthotropic, or general anisotropic), the failure criteria and corresponding strength constants are defined as follows:
- If `failure_criterion` is 1, the max stress criterion is used and nine strength constants are needed: tensile strengths ($X$, $Y$, $Z$) in three directions, compressive strengths ($X^′$ , $Y^′$ , $Z^′$ ) in three directions, and shear strengths ($R$, $T$, $S$) in three principal planes, arranged as $X$, $Y$, $Z$, $X^′$, $Y^′$, $Z^′$, $R$, $T$, $S$.
- If `failure_criterion` is 2, the max strain criterion is used and nine strength constants in terms of strains are needed: tensile strengths ($X_\varepsilon$, $Y_\varepsilon$, $Z_\varepsilon$) in three directions, compressive strengths ($X^′ _\varepsilon$, $Y^′_\varepsilon$, $Z^′_\varepsilon$) in three directions, and shear strengths ($R_\varepsilon$, $T_\varepsilon$, $S_\varepsilon$) in three principal planes, arranged as $X_\varepsilon$, $Y_\varepsilon$, $Z_\varepsilon$, $X^′_\varepsilon$, $Y^′_\varepsilon$, $Z^′_\varepsilon$, $R\varepsilon$, $T\varepsilon$, $S\varepsilon$.
- If `failure_criterion` is 3, the Tsai-Hill criterion is used and six strength constants are needed: normal strengths in three directions and shear strengths in three principal planes, arranged as $X$, $Y$, $Z$, $R$, $T$, $S$.
- If `failure_criterion` is 4, the Tsai-Wu criterion is used and nine strength constants are needed: tensile strengths (X, Y, Z), compressive strengths ($X^′$, $Y^′$, $Z^′$) in three directions, and shear strengths ($R$, $T$, $S$) in three principal planes, arranged as $X$, $Y$, $Z$, $X^′$, $Y^′$, $Z^′$, $R$, $T$, $S$.
- If `failure_criterion` is 5, the Hashin criterion is used and six strength constants are needed: tensile strengths ($X$, $Y$), compressive strengths ($X^′$, $Y^′$) in two directions, and shear strengths ($R$, $S$) in two principal planes, arranged as $X$, $Y$, $X^′$, $Y^′$, $R$, $S$.

It is noted that for failure analyses, general anisotropic materials are also approximated using orthotropic materials due to limited number of strength constants.
In VABS, both the tensile strengths and compressive strengths are expressed using positive numbers.
In other words, in the uniaxial compressive test along $y_1$ direction, $\sigma_{11}=−X^′$ when material fails.

The above block of data for strength properties for each material only needed if `analysis`=3.
If `analysis`=1 or 2, the strength properties are not needed and should not be provided in the dehomogenization input file.
Only the global beam responses as explained below should be stored in the dehomogenization input file.

The rest of inputs in the dehomogenization input file contains the global beam responses obtained from the 1D global beam analysis.
To carry out a dehomogenization analysis based on the classical model, VABS requires the following data:
```
u1  u2  u3
C11  C12  C13
C21  C22  C23
C31  C32  C33
F1  M1  M2  M3
```
where `u1`, `u2`, and `u3` are the 1D beam displacements along $x_1$, $x_2$, $x_3$, respectively.
The matrix `Cij`, with i = 1, 2, 3 and j = 1, 2, 3, is the direction cosine matrix defined as

$$
\mathbf{B}_{i} = C_{i1}\mathbf{b}_{1} + C_{i2}\mathbf{b}_{2} + C_{i3}\mathbf{b}_{3} \text{    with } i = 1, 2, 3
$$

where $B_1$, $B_2$, and $B_3$ are the base vectors of the deformed beam and $b_1$, $b_2$, and $b_3$ are the base vectors of the undeformed beam.
Details of this definition can be found in Ref. [\[7\]](#page-24-2).
`ui` and `Cij` are needed only for recovering 3D displacements.
If the user is not interested in 3D displacements, these values can be arbitrary real numbers.
`F1` is the axial force, `M1` is the torque, `M2` is the bending moment around $x_2$, and `M3` is the bending moment around $x_3$.
The sectional stress resultants are needed for computing 3D stresses/strains/failure indexes/strength ratios within the cross-section.
For example, if the user wants to compute these quantities under 1 unit tensile axial force along with 1 unit bending moment around $x_2$, the inputs can be arranged as:
```
0  0  0
1  0  0
0  1  0
0  0  1
1  0  1  0
```

To perform dehomogenization for multiple load cases, the user needs to insert corresponding lines of `F1`, `M1`, `M2`, `M3` after the end of this block.
For example, to perform dehomogenization for two more load cases with `F1` = 2, `M1` = 2, `M2` = `M3` = 0 and `F1` = 2, `M1` = 3, `M2` = 4, `M3` = 5, we must provide the following inputs:
```
0  0  0
1  0  0
0  1  0
0  0  1
1  0  1  0
2  2  0  0
2  3  4  5
```

To carry out a dehomogenization analysis based on the Timoshenko model, VABS requires the following data:
```txt
u1  u2  u3
C11  C12  C13
C21  C22  C23
C31  C32  C33
F1  M1  M2  M3
F2  F3
f1  f2  f3  m1  m2  m3
f1'  f2'  f3'  m1'  m2'  m3'
f1''  f2''  f3''  m1''  m2''  m3''
f1'''  f2'''  f3'''  m1'''  m2'''  m3'''
```
where the additional data `F2` and `F3` are transverse shear forces along $x_2$ and $x_3$, respectively.
`f1`, `f2`, `f3` are distributed forces (including both applied forces and inertial forces) per unit span along $x_1$, $x_2$, $x_3$ respectively.
`m1`, `m2`, `m3` are distributed moments (including both applied and inertial moments) per unit span along $x_1$, $x_2$, $x_3$ respectively.
The prime denotes derivative with respect to beam axis, that is $()^{'}=\partial/\partial x_1$, $()^{''} = \partial^2/\partial x_1^2$, and $()^{'''} = \partial^3/\partial x_1^3$.
If `nload` > 1, at the end of the above data block, we need to append two lines (one line for $F_1$, $M_1$, $M_2$, $M_3$ and one line for $F_2$, $F_3$) for each load case.

To carry out a dehomogenization analysis based on the Vlasov model, VABS requires the following data:
```
u1  u2  u3
C11  C12  C13
C21  C22  C23
C31  C32  C33
gamma11  kappa1  kappa2  kappa3  kappa1'  kappa1''  kappa'''
```
where `gamma11` is the beam axial strain, `kappa1` is the twist , `kappa2` and `kappa3` are the curvatures around $x_2$ and $x_3$ respectively.

It is noted that the global behavior needed for dehomogenization analyses should not violate the small strain assumption.
Otherwise, you might get some unexpected results.
For example, if your transverse shear stiffness is 2.5 N, then inputting a shear force resultant of 1 N is too large as the shear strain will be about 0.4, which cannot be considered as small, the basic assumption of the VABS theory.

Both input files, `input_file_name` and `input_file_name.glb`, should be ended with a blank line to avoid any possible incompatibility of different computer operating systems.
The input file can be given any name as long as the total number of the characters of the name including extension is not more than 256.
For the convenience of the user to identify mistakes in the input file, all the inputs are echoed in the file named `input_file_name.ech`.
Error messages are also written at the end of `input_file_name.ech` and on the output screen.
