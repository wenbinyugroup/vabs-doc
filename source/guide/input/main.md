# Homogenization Input File

## Control parameters

The first line lists two newly introduced integer flags arranged as:
```
format_flag  nlayer
```

If the first flag is 1, the input is prepared in the new format, otherwise, it is prepared in the old format.
The second integer provides the number of layers in the section.
Note, here layer is defined as a unique combination of material type and layup orientation, it does not necessarily corresponds to the definition used in the manufacturing sense.
For example, even if a section is made of a single isotropic material, we consider it has one layer.
Hence, nlayer should be always given a value greater than 1 if `format flag=1` and it is not used when using the old format.

The second line has two flags arranged as
```
Timoshenko_flag  damping_flag  thermal_flag
```

The first flag, `Timoshenko_flag`, can be only 1 or 0.
If it is 1, VABS will construct both the classical model (also called the Euler-Bernoulli model) and the Timoshenko model.
If it is 0, it will only construct the classical model.
The second flag, `damping_flag`, can be equal to 0 or 1.
If it is equal to 0, VABS will not compute the damping matrix for the section.
If it is equal to 1, VABS will compute the damping matrix.
The third flag, `thermal_flag`, can be equal to 0 or 3.
If it is equal to zero, VABS will carry out a pure mechanical analysis.
If it is equal to 3, VABS will carry out a one-way coupled thermoelastic analysis.

:::{figure-md} fig-oblique
![](../../_static/oblique.jpeg)

Sketch of an oblique reference cross-section
:::

The third line has four flags arranged as

```
curve_flag oblique_flag trapeze_flag Vlasov_flag
```

These flags can be only 1 or 0.
Their uses are explained in the following:

1. To model initially curved and twisted beams, `curve_flag` is 1, and three real numbers for the twist ($k_1$) and curvatures ($k_2$ and $k_3$) should be provided in the very next line.
2. To model oblique cross-sections, `oblique_flag` is 1, and two real numbers are needed in the following line to specify the orientation of an oblique reference cross-section, see {numref}`fig-oblique` for a sketch of such a cross-section. The first number is cosine of the angle between normal of the oblique section ($y_1$) and beam axis $x_1$. The second number is cosine of the angle between $y_2$ of the oblique section and beam axis ($x_1$). The summation of the square of these two numbers should not be greater than 1.0 in double precision. The inputs including coordinates, material properties, etc. and the outputs including mass matrix, stiffness matrix, etc. are given in the oblique system, the $y_i$ coordinate system as shown in {numref}`fig-oblique` Note that this feature is only enabled for the classical beam model.
3. To obtain the trapeze effect, `trapeze_flag` is 1.
4. To obtain the Vlasov model, `Vlasov_flag` is 1. `Vlasov_flag` can be 1 only if `Timoshenko_flag` is 1. VABS will first construct the Timoshenko model, which determines the location of the shear center. If the shear center is not at the origin of the beam coordinate system, VABS will move the origin of beam coordinate system to the shear center and repeat the calculation to obtain the Vlasov model.



## Mesh

The next line lists three integers arranged as

```
nnode nelem nmate
```

where `nnode` is the total number of nodes, `nelem` the total number of elements, and `nmate` the total number of material types.

The next nnode lines are the coordinates for each node arranged as

```
node_no x2 x3
```

where `node_no` is an integer representing the unique number assigned to each node and `x2`, `x3` are two real numbers describing the location ($x_2$, $x_3$) of the node.
Although the arrangement of node no is not necessary to be consecutive, every node starting from 1 to nnode should be present.

The next `nelem` lines list 10 integers for the nodes for each element (also known as the connectivity relations).
They are arranged as:
```
elem_no node_1 node_2 node_3 node_4 node_5 node_6 node_7 node_8 node_9
```
where `elem_no` is the number of element and `node_i` (i = 1, 2, . . . , 9) are nodes of this element.
If a node is not present in the element, the value is 0.
If `node_4` is 0, the element is a triangular element; see {numref}`fig-tri_elem` and {numref}`fig-quad_elem` for the VABS numbering convention.
Although the arrangement of elem no is not necessary to be consecutive, every element starting from 1 to nelem should be present.


## Element property and orientation

If `format_flag = 1`, that is, if the new format is used, the next `nelem` lines list the layer type and the layer plane angle ($\theta_1$) for each element as:
```
elem_no  layer_type  theta_1
```
where `layer_type` is an integer representing which layer the element `elem_no` belongs to, and `theta_1` is a real number describing the layer plane angle ($\theta_1$) for the element.
Here, $\theta_1$ is assumed to be constant for each element, thus it can be calculated at any material point belonging to the element, such as the centroid, or computed as the average of $\theta_1$ of all the points within the element.
Although the arrangement of `elem_no` is not necessary to be consecutive, every element starting from 1 to `nelem` should be present.
For isotropic materials, `theta_1` will not enter the calculations.

If `format_flag` is not equal to 1, that is, if the old format is used, the next `nelem` lines list the material type and layup parameters for each element as
```
elem_no  material_type  theta_3  theta_1(9)
```
where `material_type` is an integer representing the type of the material for the element `elem_no`, `theta_3` is a real number representing the layup angle in degrees for this element, and `theta_1(9)` is an array storing nine real numbers for the layer plane angles at the nodes of this element.
For simplification, if the ply orientation can be considered as uniform for this element, `theta_1(1)` stores the layer plane angle and `theta_1(2)` = $540^{\circ}$, and all the rest can be zeros or other real numbers because they do not enter the calculation.
If the element has fewer than nine nodes, zeros are to be input for the corresponding missing nodes, as in the case for connectivity.
Although the arrangement of `elem_no` is not necessary to be consecutive, every element starting from 1 to `nelem` should be present.
For isotropic materials, neither `theta_3` nor `theta_1(9)` will enter the calculations.


## Materials and layers

If `format_flag` = 1, that is, if the new format is used, the next `nlayer` lines define the layers used in the section.
They are arranged as:
```
layer_id  mate_type  theta_3
```
where `layer_id` is an integer denoting the identification number for each layer, `mate_type` is an integer denoting the material type used in the layer, and `theta_3` is a real number denoting the layup orientation.
For example, if layer 1 is made of material 1 and having $−15^{\circ}$ layup, we will provide the information as `1 1 −15.0`.
If `damping_flag` is 1, a damping coefficient for each layer is also needed to input right after `theta_3`.
In others words, the input should be arranged as
```
layer_id  mate_type  theta_3  damping_layer
```
with `damping_layer` indicating the damping coefficient for the layer.

The next `nmate` blocks defines the material properties.
They are arranged as
```
mat_id  orth
const1  const2  ....
```
where `mat_id` is the number of material type, `orth` is the flag to indicate whether the material is isotropic (0), orthotropic (1) or general anisotropic (2).
The rest are material constants.

For isotropic materials, `orth` is 0, if `thermal_flag` is 0, there are 3 constants arranged as
```
E  nu
rho
```
where `E` is the Young's modulus, `nu` is the Poisson's ratio, and `rho` is the density of the material.
Poisson's ratio must be greater than -1.0 and less than 0.5 for isotropic materials, although VABS allows users to input values that are very close to those limits.

If `thermal_flag` is 3 and `orth` is 0, and there are 4 constants arranged as
```
E  nu
rho
alpha
```
where `alpha` is the coefficient of thermal expansion (CTE).

For orthotropic materials, `orth` is 1, if `thermal_flag` is 0, there are 10 constants arranged as
```
E1  E2  E3
G12  G13  G23
nu12  nu13  nu23
rho
```
including the Young's moduli (`E1`, `E2`, and `E3`), the shear moduli (`G12`, `G13`, and `G23`), the Poisson's ratios (`nu12`, `nu13`, and `nu23`), and the mass density (`rho`).
The convention of values is such that these values will be used to form the following the Hooke's law for composite materials:

$$
\begin{Bmatrix}
\varepsilon_{11} \\
2\varepsilon_{12} \\
2\varepsilon_{13} \\
\varepsilon_{22} \\
2\varepsilon_{23} \\
\varepsilon_{33}
\end{Bmatrix} =
\begin{bmatrix}
\frac{1}{E_1} & 0 & 0 & -\frac{\nu_{12}}{E_1} & 0 & -\frac{\nu_{13}}{E_1} \\
0 & \frac{1}{G_{12}} & 0 & 0 & 0 & 0 \\
0 & 0 & \frac{1}{G_{13}} & 0 & 0 & 0 \\
-\frac{\nu_{12}}{E_1} & 0 & 0 & \frac{1}{E_2} & 0 & -\frac{\nu_{23}}{E_2} \\
0 & 0 & 0 & 0 & \frac{1}{G_{23}} & 0 \\
-\frac{\nu_{13}}{E_1} & 0 & 0 & -\frac{\nu_{23}}{E_2} & 0 & \frac{1}{E_3}
\end{bmatrix}
\begin{Bmatrix}
\sigma_{11} \\
\sigma_{12} \\
\sigma_{13} \\
\sigma_{22} \\
\sigma_{23} \\
\sigma_{33}
\end{Bmatrix}
$$

If `thermal_flag` is 3 and `orth` is 1, and there are 13 constants arranged as:
```
E1  E2  E3
G12  G13  G23
nu12  nu13  nu23
rho
alpha11  alpha22  alpha33
```
where `alpha11`, `alpha22`, `alpha33` are the CTEs along three directions.

For general anisotropic materials, `orth` is 2, if `thermal_flag` is 0, there are 22 constants arranged as:
```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
            c44 c45 c46
                c55 c56
                    c66
                    rho
```
These values are defined using the following Hooke's law:

$$
\begin{Bmatrix}
\sigma_{11} \\
\sigma_{12} \\
\sigma_{13} \\
\sigma_{22} \\
\sigma_{23} \\
\sigma_{33}
\end{Bmatrix} =
\begin{bmatrix}
c_{11} & c_{12} & c_{13} & c_{14} & c_{15} & c_{16} \\
c_{12} & c_{22} & c_{23} & c_{24} & c_{25} & c_{26} \\
c_{13} & c_{23} & c_{33} & c_{34} & c_{35} & c_{36} \\
c_{14} & c_{24} & c_{34} & c_{44} & c_{45} & c_{46} \\
c_{15} & c_{25} & c_{35} & c_{45} & c_{55} & c_{56} \\
c_{16} & c_{26} & c_{36} & c_{46} & c_{56} & c_{66}
\end{bmatrix}
\begin{Bmatrix}
\varepsilon_{11} \\
2\varepsilon_{12} \\
2\varepsilon_{13} \\
\varepsilon_{22} \\
2\varepsilon_{23} \\
\varepsilon_{33}
\end{Bmatrix}
$$

If `thermal_flag` is 3 and `orth` is 2, there are 28 constants arranged as:

```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
            c44 c45 c46
                c55 c56
                    c66
                    rho
alpha11  2alpha12  2alpha13  alpha22  2alpha23  alpha33
```
where `alphaij` , with i = 1, 2, 3 and j = 1, 2, 3, are the components of the second-order CTE tensor.
CTEs corresponding to the shear strains are multiplied by two because the engineering shear strains are twice of the corresponding tensorial shear strains.
The material constants are expressed in the material coordinate system (see {numref}`fig-local_coord_sys`).
If the material properties are given in a different coordinate system, or the arrangement of stresses and strains are different from what VABS uses, a proper transformation of the material properties is needed.

If `damping_flag` is 1, a damping coefficient is input on the very next line following the density input.
For example, if `orth`=0 and `thermal_flag`=3 (thermoelastic analysis with isotropic materials), the material constants are arranged as:
```
E nu
rho
gamma
alpha
```
where `gamma` is a scalar representing the material damping property.
It is noted that the damping coefficients for each layer and for each material are additive.
In other words, the total damping coefficient used to scale the stiffness-related matrices is `damping_layer`+`gamma`.

If `thermal_flag` is equal to 3, we also need to provide the following `nnode` lines for temperature for each node arranged as
```
node_no  T
```
where `node_no` is an integer representing the unique number assigned to each node and `T` is a real number describing the temperature of the node.
These temperature values can be calculated either from a 3D heat conduction analysis or using VABS Conduction, which is a generalization of the VABS approach for heat conduction analysis.
Although the arrangement of `node_no` is not necessary to be consecutive, every node starting from 1 to `nnode` should be present.

Now, we have prepared all the inputs necessary for performing the homogenization run to compute the inertial properties and structural properties of the cross-section.
That is, when `analysis` in Section [6] does not exist.
