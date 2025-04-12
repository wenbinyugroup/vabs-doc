# Dehomogenization Input File

If analysis in Section [6](#page-10-1) is equal to 1,2, 3, users should provide additional information in the dehomogenization input file for VABS to perform a dehomogenization analysis. A corresponding homogenization analysis must be run before carrying out the dehomogenization analysis.

If analysis is equal to 3, VABS will perform failure analysis of the cross-section. Strength properties for each material must be provided in the dehomogenization input file. Strength properties for each material include a failure criterion and corresponding strength constants. Two lines will be inserted and the inputs needed for failure analyses should be arranged as:

f ailure criterion num of constants

const<sup>1</sup> const<sup>2</sup> const<sup>3</sup> . . .

f ailure criterion is an integer identifier for the failure criterion. num of constants indicates the number of strength constants needed for the corresponding failure criterion. const<sup>1</sup> const<sup>2</sup> const<sup>3</sup> . . . are the corresponding strength constants. It is noted that this block of data should be corresponding to the material block in the homogenization input file. In other words, for each material with mat id, we need to provide such information.

f ailure criterion can be equal to 1, 2, 3, 4, 5, and another number greater than 10. For isotropic material, 1 is max principal stress criterion, 2 is max principal strain criterion, 3 is max shear stress criterion (also commonly called Tresca criterion), 4 max shear strain criterion, and 5 is Mises criterion. For anisotropic materials, 1 is max stress criterion for anisotropic materials, 2 is max strain criterion for anisotropic materials, 3 is Tsai-Hill criterion, 4 is Tsai-Wu criterion and 5 is Hashin criterion. 11 and larger indicates a user-defined failure criterion. It is assumed that the number of strength constants will not be greater than 9 for a material. If the material is isotropic, the failure criterion and corresponding strength constants are defined as follows:

- If f ailure criterion is 1, the max principal stress criterion is used and two strength constants are needed: one for tensile strength (X) and one for compressive strength (X′ ), arranged as X, X′ .
- If f ailure criterion is 2, the max principal strain criterion is used and two strength constants in terms of strains are needed: one for tensile strength (Xε) and one for compressive strength

(X′ ε ), arranged as Xε, X′ ε .

- If f ailure criterion is 3, the max shear stress criterion (aka Tresca criterion) is used and one shear strength constant (S) is needed.
- If f ailure criterion is 4, the max shear strain criterion is used and one shear strength constant in terms of strains (Sε) is needed.
- If f ailure criterion is 5, the Mises criterion is used and one strength constant (X) is needed.

If the material is not isotropic (transversely isotropic, orthotropic, or general anisotropic), the failure criteria and corresponding strength constants are defined as follows:

- If f ailure criterion is 1, the max stress criterion is used and nine strength constants are needed: tensile strengths (X, Y, Z) in three directions, compressive strengths (X′ , Y ′ , Z′ ) in three directions, and shear strengths (R, T, S) in three principal planes, arranged as X, Y, Z, X′ , Y ′ , Z′ , R, T, S.
- If f ailure criterion is 2, the max strain criterion is used and nine strength constants in terms of strains are needed: tensile strengths (Xε, Yε, Zε) in three directions, compressive strengths (X′ ε , Y ′ ε , Z′ ε ) in three directions, and shear strengths (Rε, Tε, Sε) in three principal planes, arranged as Xε, Yε, Zε, X′ ε , Y ′ ε , Z′ ε , Rε, Tε, Sε.
- If f ailure criterion is 3, the Tsai-Hill criterion is used and six strength constants are needed: normal strengths in three directions and shear strengths in three principal planes, arranged as X, Y, Z, R, T, S.
- If f ailure criterion is 4, the Tsai-Wu criterion is used and nine strength constants are needed: tensile strengths (X, Y, Z), compressive strengths (X′ , Y ′ , Z′ ) in three directions, and shear strengths (R, T, S) in three principal planes, arranged as X, Y, Z, X′ , Y ′ , Z′ , R, T, S.
- If f ailure criterion is 5, the Hashin criterion is used and six strength constants are needed: tensile strengths (X, Y ), compressive strengths (X′ , Y ′ ) in two directions, and shear strengths (R, S) in two principal planes, arranged as X, Y, X′ , Y ′ , R, S.

It is noted that for failure analyses, general anisotropic materials are also approximated using orthotropic materials due to limited number of strength constants. In VABS, both the tensile strengths and compressive strengths are expressed using positive numbers. In other words, in the uniaxial compressive test along y<sup>1</sup> direction, σ<sup>11</sup> = −X′ when material fails.

The above block of data for strength properties for each material only needed if analysis=3. If analysis=1 or 2, the strength properties are not needed and should not be provided in the dehomogenization input file. Only the global beam responses as explained below should be stored in the dehomogenization input file.

The rest of inputs in the dehomogenization input file contains the global beam responses obtained from the 1D global beam analysis. To carry out a dehomogenization analysis based on the classical model, VABS requires the following data:

$$\begin{array}{ccccc} u\_1 & u\_2 & u\_3 \\ C\_{11} & C\_{12} & C\_{13} \\ C\_{21} & C\_{22} & C\_{23} \\ C\_{31} & C\_{32} & C\_{33} \\ F\_1 & M\_1 & M\_2 & M\_3 \\ \end{array}$$

where u1, u2, and u<sup>3</sup> are the 1D beam displacements along x1, x2, x3, respectively. The matrix Cij , with i = 1, 2, 3 and j = 1, 2, 3, is the direction cosine matrix defined as

$$\mathbf{B}\_{i} = C\_{i1}\mathbf{b}\_{1} + C\_{i2}\mathbf{b}\_{2} + C\_{i3}\mathbf{b}\_{3} \text{ with } i = 1, 2, 3.$$

where B1, B2, and B<sup>3</sup> are the base vectors of the deformed beam and b1, b2, and b<sup>3</sup> are the base vectors of the undeformed beam. Details of this definition can be found in Ref. [\[7\]](#page-24-2). u<sup>i</sup> and Cij are needed only for recovering 3D displacements. If the user is not interested in 3D displacements, these values can be arbitrary real numbers. F<sup>1</sup> is the axial force, M<sup>1</sup> is the torque, M<sup>2</sup> is the bending moment around x2, and M<sup>3</sup> is the bending moment around x3. The sectional stress resultants are needed for computing 3D stresses/strains/failure indexes/strength ratios within the cross-section. For example, if the user wants to compute these quantities under 1 unit tensile axial force along with 1 unit bending moment around x2, the inputs can be arranged as:

$$
\begin{array}{cccc}
0 & 0 & 0 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 1 & 0
\end{array}
$$

To perform dehomogenization for multiple load cases, the user needs to insert corresponding lines of F1, M1, M2, M<sup>3</sup> after the end of this block. For example, to perform dehomogenization for two more load cases with F<sup>1</sup> = 2, M<sup>1</sup> = 2, M<sup>2</sup> = M<sup>3</sup> = 0 and F<sup>1</sup> = 2, M<sup>1</sup> = 3, M<sup>3</sup> = 4, M<sup>5</sup> = 5, we must provide the following inputs.

To carry out a dehomogenization analysis based on the Timoshenko model, VABS requires the

following data:

$$\begin{array}{ccccc} u\_1 & u\_2 & u\_3 \\ C\_{11} & C\_{12} & C\_{13} \\ C\_{21} & C\_{22} & C\_{23} \\ C\_{31} & C\_{32} & C\_{33} \\ F\_1 & M\_1 & M\_2 & M\_3 \\ F\_2 & F\_3 & \\ f\_1 & f\_2 & f\_3 & m\_1 & m\_2 & m\_3 \\ f\_1' & f\_2' & f\_3' & m\_1' & m\_2' & m\_3' \\ f\_1'' & f\_2'' & f\_3'' & m\_1'' & m\_2'' & m\_3'' \\ f\_1''' & f\_2''' & f\_3''' & m\_1''' & m\_2''' & m\_3''' \\ \end{array}$$

where the additional data F<sup>2</sup> and F<sup>3</sup> are transverse shear forces along x<sup>2</sup> and x3, respectively. f1, f2, f<sup>3</sup> are distributed forces (including both applied forces and inertial forces) per unit span along x1, x2, x<sup>3</sup> respectively. m1, m2, m<sup>3</sup> are distributed moments (including both applied and inertial moments) per unit span along x1, x2, x<sup>3</sup> respectively. The prime denotes derivative with respect to beam axis, that is ()′ = ∂ ∂x<sup>1</sup> , ()′′ = ∂ 2 x 2 1 , and ()′′′ = ∂ 3 x 3 1 . If nload > 1, at the end of the above data block, we need to append two lines (one line for F1, M1, M2, M<sup>3</sup> and one line for F2, F3) for each load case.

To carry out a dehomogenization analysis based on the Vlasov model, VABS requires the following data:

$$\begin{array}{ccccc} u\_1 & u\_2 & u\_3 \\ C\_{11} & C\_{12} & C\_{13} \\ C\_{21} & C\_{22} & C\_{23} \\ C\_{31} & C\_{32} & C\_{33} \\ \bar{\gamma}\_{11} & \bar{\kappa}\_1 & \bar{\kappa}\_2 & \bar{\kappa}\_3 & \bar{\kappa}\_1' & \bar{\kappa}\_1'' & \bar{\kappa}\_1''' \end{array}$$

where ¯γ<sup>11</sup> is the beam axial strain, ¯κ<sup>1</sup> is the twist , ¯κ<sup>2</sup> and ¯κ<sup>3</sup> are the curvatures around x<sup>2</sup> and x<sup>3</sup> respectively.

It is noted that the global behavior needed for dehomogenization analyses should not violate the small strain assumption. Otherwise, you might get some unexpected results. For example, if your transverse shear stiffness is 2.5 N, then inputting a shear force resultant of 1 N is too large as the shear strain will be about 0.4, which cannot be considered as small, the basic assumption of the VABS theory.

Both input files, input file name and input file name.glb, should be ended with a blank line to avoid any possible incompatibility of different computer operating systems. The input file can be given any name as long as the total number of the characters of the name including extension is not more than 256. For the convenience of the user to identify mistakes in the input file, all the inputs are echoed in the file named input file name.ech. Error messages are also written at the end of input file name.ech and on the output screen.
