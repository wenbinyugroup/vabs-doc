# Homogenization Outputs

Sectional properties obtained by a VABS homogenization analysis are stored in `input_file_name.K`.
Some results are listed as individual numbers, and some are listed as matrices.
The definitions of these properties are briefly summarized here for the convenience of end users.
For more details, please refer to VABS related publications.

VABS first computes the inertial properties which is represented by a $6 \times 6$ mass matrix with respect to the beam coordinate system.
The elements of the mass matrix are arranged as

$$
\begin{bmatrix}
\mu & 0 & 0 & 0 & \mu x_{M3} & -\mu x_{M2} \\
0 & \mu & 0 & -\mu x_{M3} & 0 & 0 \\
0 & 0 & \mu & \mu x_{M2} & 0 & 0 \\
0 & -\mu x_{M3} & \mu x_{M2} & i_{22}+i_{33} & 0 & 0 \\
\mu x_{M3} & 0 & 0 & 0 & i_{22} & i_{23} \\
-\mu x_{M2} & 0 & 0 & 0 & i_{23} & i_{33}
\end{bmatrix}
$$

where $\mu$ is mass per unit length, $x_{M2}$ and $x_{M3}$ are the two coordinates of the mass center (also called the mass-weighted centroid), and $i_{22}$, $i_{23}$ and $i_{33}$ are the second mass moments of inertia.
The mass center and mass moments of inertia are measured with respect to the origin $O$ and coordinate axes $x_2$ and $x_3$.
VABS also outputs the mass center, the mass matrix measured with respect to the coordinate system with the mass center as the origin and coordinates parallel to the beam coordinate system.
Furthermore, VABS also outputs the inertial properties with respect to the principal inertial coordinate system (origin at the mass center, coordinates aligning with the principal inertial axes) including a mass per unit length, mass moments of inertia about the three axes, the orientation of the principal inertial axes, and mass-weighted radius of gyration (defined as the square root of the mass moment of inertia about $x_1$ divided by the mass per unit length).

VABS outputs the geometric center and the area of the cross-section.
Only the geometry occupied by a material enters the calculation.
In other words, if the cross-section is made of a single material, the geometric center is located at the same location as the mass center and the tension center.

VABS outputs the $4\times4$ stiffness matrix and compliance matrix for the classical beam model with respect to the beam coordinate system.
Based on the compliance matrix, VABS also outputs the tension center (also called the modulus-weighted centroid), extension stiffness (commonly denoted as $EA$), torsional stiffness (commonly denoted as $GJ$), principal bending stiffnesses (commonly denoted as $EI_{22}$, $EI_{33}$), and the orientation of the principal bending axes.
The principal bending stiffnesses are computed with respect to the tension center and the principal bending axes.

If `damping_flag` is equal to 1, VABS also outputs the $4\times4$ damping matrix for the cross-section.

If `thermal_flag` is equal to 3, VABS also output the thermal stress resultants and thermal strains due to temperature changes for the classical beam model.

If `curve_flag` is equal to 1, VABS also output the stiffness matrix, compliance matrix, tension center, tension center, extension stiffness, torsional stiffness, principal bending stiffnesses, and the orientation of the principal bending axes modified by the initial curvatures/twist of the beam.

If `Timoshenko_flag` is equal to 1, VABS outputs the $6\times6$ stiffness matrix and compliance matrix for the Timoshenko beam model with respect to the beam coordinate system.
Based on the compliance matrix, VABS also outputs the shear center (also called the twist center), principal shear stiffnesses, and the orientation of the principal shear axes.
The principal shear stiffnesses are computed with respect to the shear center and the principal shear axes.
If damping flag is equal to 1, VABS also outputs the $6\times6$ damping matrix for the cross-section.
VABS also outputs the classical stiffness matrix and classical compliance at the shear center as these are the inputs should be used for an Euler-Bernoulli beam model.

If `Vlasov_flag` is equal to 1, VABS outputs the $5\times5$ stiffness matrix and compliance matrix for the Vlasov beam model with respect to the beam coordinate system.
This model is important for capturing the "restrained warping" effect for thin-walled beams with open sections.
For such beams, it is meaningful to have a Vlasov model based on choosing the shear center as its reference.
Hence to obtain a Vlasov model, VABS finds the shear center first and then shifts the origin of the coordinate system to the shear center and calculate the $5\times5$ stiffness matrix and compliance matrix.
If `damping_flag` is equal to 1, VABS also outputs the $5\times5$ damping matrix for the cross-section.

If `trapeze_flag` is equal to 1, VABS output four $4\times4$ coefficient matrices associated with the four classical deformation modes (extension, twist, and two bending modes) for capturing the trapeze effect important for torsionally soft rotating beams.

Users are encouraged to refer to a recent paper[26](#page-25-2) provides detailed explanations for the inertial and structural properties computed by VABS.
How these outputs are related to traditional definitions of sectional properties and how to extract engineering beam properties from VABS outputs as inputs for conventional beam analysis codes.

