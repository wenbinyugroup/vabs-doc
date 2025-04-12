# Homogenization Input File

The first line lists two newly introduced integer flags arranged as: "format flag nlayer". If the first flag is 1, the input is prepared in the new format, otherwise, it is prepared in the old format. The second integer provides the number of layers in the section. Note, here layer is defined as a unique combination of material type and layup orientation, it does not necessarily corresponds to the definition used in the manufacturing sense. For example, even if a section is made of a single isotropic material, we consider it has one layer. Hence, nlayer should be always given a value greater than 1 if format flag=1 and it is not used when using the old format.

The second line has two flags arranged as: "Timoshenko flag damping flag thermal flag". The first flag, Timoshenko flag, can be only 1 or 0. If it is 1, VABS will construct both the classical model (also called the Euler-Bernoulli model) and the Timoshenko model. If it is 0, it will only construct the classical model. The second flag, damping flag, can be equal to 0 or 1. If it is equal to 0, VABS will not compute the damping matrix for the section. If it is equal to 1, VABS will compute the damping matrix. The third flag, thermal flag, can be equal to 0 or 3. If it is equal to zero, VABS will carry out a pure mechanical analysis. If it is equal to 3, VABS will carry out a one-way coupled thermoelastic analysis.

![](_page_12_Figure_0.jpeg)

<span id="page-12-0"></span>Figure 6: Sketch of an oblique reference cross-section

The third line has four flags arranged as: "curve flag oblique flag trapeze flag Vlasov flag." These flags can be only 1 or 0. Their uses are explained in the following:

- 1. To model initially curved and twisted beams, curve flag is 1, and three real numbers for the twist (k1) and curvatures (k<sup>2</sup> and k3) should be provided in the very next line.
- 2. To model oblique cross-sections, oblique flag is 1, and two real numbers are needed in the following line to specify the orientation of an oblique reference cross-section, see Figure [6](#page-12-0) for a sketch of such a cross-section. The first number is cosine of the angle between normal of the oblique section (y1) and beam axis x1. The second number is cosine of the angle between y<sup>2</sup> of the oblique section and beam axis (x1). The summation of the square of these two numbers should not be greater than 1.0 in double precision. The inputs including coordinates, material properties, etc. and the outputs including mass matrix, stiffness matrix, etc. are given in the oblique system, the y<sup>i</sup> coordinate system as shown in Figure [6.](#page-12-0) Note that this feature is only enabled for the classical beam model.
- 3. To obtain the trapeze effect, trapeze flag is 1.
- 4. To obtain the Vlasov model, Vlasov flag is 1. Vlasov flag can be 1 only if Timoshenko flag is 1. VABS will first construct the Timoshenko model, which determines the location of the shear center. If the shear center is not at the origin of the beam coordinate system, VABS will move the origin of beam coordinate system to the shear center and repeat the calculation to obtain the Vlasov model.

The next line lists three integers arranged as: "nnode nelem nmate," where nnode is the total number of nodes, nelem the total number of elements, and nmate the total number of material types.

The next nnode lines are the coordinates for each node arranged as: "node no x<sup>2</sup> x3," where node no is an integer representing the unique number assigned to each node and x2, x<sup>3</sup> are two real numbers describing the location (x2, x3) of the node. Although the arrangement of node no is not necessary to be consecutive, every node starting from 1 to nnode should be present.

The next nelem lines list 10 integers for the nodes for each element (also known as the connectivity relations). They are arranged as: "elem no node 1 node 2 node 3 node 4 node 5 node 6 node 7 node 8 node 9," where elem no is the number of element and node i (i = 1, 2, . . . , 9) are nodes of this element. If a node is not present in the element, the value is 0. If node 4 is 0, the element is a triangular element; see Figures [2](#page-8-0) and [3](#page-8-1) for the VABS numbering convention. Although the arrangement of elem no is not necessary to be consecutive, every element starting from 1 to nelem should be present.

If format flag = 1, that is, if the new format is used, the next nelem lines list the layer type and the layer plane angle (θ1) for each element as: elem no layer type θ1, where layer type is an integer representing which layer the element elem no belongs to, and θ<sup>1</sup> is a real number describing the layer plane angle for the element. Here, θ<sup>1</sup> is assumed to be constant for each element, thus it can be calculated at any material point belonging to the element, such as the centroid, or computed as the average of θ<sup>1</sup> of all the points within the element. Although the arrangement of elem no is not necessary to be consecutive, every element starting from 1 to nelem should be present. For isotropic materials, θ<sup>1</sup> will not enter the calculations.

If format flag is not equal to 1, that is, if the old format is used, the next nelem lines list the material type and layup parameters for each element as: elem no material type θ<sup>3</sup> θ1(9), where material type is an integer representing the type of the material for the element elem no, θ<sup>3</sup> is a real number representing the layup angle in degrees for this element, and θ1(9) is an array storing nine real numbers for the layer plane angles at the nodes of this element. For simplification, if the ply orientation can be considered as uniform for this element, θ1(1) stores the layer plane angle and θ1(2) = 540◦ , and all the rest can be zeros or other real numbers because they do not enter the calculation. If the element has fewer than nine nodes, zeros are to be input for the corresponding missing nodes, as in the case for connectivity. Although the arrangement of elem no is not necessary to be consecutive, every element starting from 1 to nelem should be present. For isotropic materials, neither θ<sup>3</sup> nor θ1(9) will enter the calculations.

If format flag = 1, that is, if the new format is used, the next nlayer lines define the layers used in the section. They are arranged as: layer id mate type θ3, where layer id is an integer denoting the identification number for each layer, mate type is an integer denoting the material type used in the layer, and θ<sup>3</sup> is a real number denoting the layup orientation. For example, if layer 1 is made of material 1 and having −15◦ layup, we will provide the information as 1 1 − 15.0. If damping flag is 1, a damping coefficient for each layer is also needed to input right after θ3. In others words, the input should be arranged as layer id mate type θ<sup>3</sup> damping layer, with damping layer indicating the damping coefficient for the layer.

The next nmate blocks defines the material properties. They are arranged as: mat id orth

const1 const2 ....

where mat id is the number of material type, orth is the flag to indicate whether the material is isotropic (0), orthotropic (1) or general anisotropic (2). The rest are material constants.

For isotropic materials, orth is 0, if thermal flag is 0, there are 3 constants arranged as: E ν

ρ

where E is the Young's modulus, ν is the Poisson's ratio, and ρ is the density of the material. Poisson's ratio must be greater than -1.0 and less than 0.5 for isotropic materials, although VABS allows users to input values that are very close to those limits.

If thermal flag is 3 and orth is 0, and there are 4 constants arranged as: E ν ρ α

where α is the coefficient of thermal expansion (CTE).

For orthotropic materials, orth is 1, if thermal flag is 0, there are 10 constants arranged as: E<sup>1</sup> E<sup>2</sup> E<sup>3</sup> G<sup>12</sup> G<sup>13</sup> G<sup>23</sup> ν<sup>12</sup> ν<sup>13</sup> ν<sup>23</sup> ρ

including the Young's moduli (E1, E2, and E3), the shear moduli (G12, G13, and G23), the Poisson's ratios (ν12, ν13, and ν23), and the mass density (ρ). The convention of values is such that these values will be used to form the following the Hooke's law for composite materials:

$$\begin{Bmatrix} \varepsilon\_{11} \\ 2\varepsilon\_{12} \\ 2\varepsilon\_{13} \\ \varepsilon\_{22} \\ 2\varepsilon\_{23} \\ \varepsilon\_{33} \end{Bmatrix} = \begin{bmatrix} \frac{1}{E\_1} & 0 & 0 & -\frac{\nu\_{12}}{E\_1} & 0 & -\frac{\nu\_{13}}{E\_1} \\ 0 & \frac{1}{G\_{12}} & 0 & 0 & 0 & 0 \\ 0 & 0 & \frac{1}{G\_{13}} & 0 & 0 & 0 \\ -\frac{\nu\_{12}}{E\_1} & 0 & 0 & \frac{1}{E\_2} & 0 & -\frac{\nu\_{23}}{E\_2} \\ 0 & 0 & 0 & 0 & \frac{1}{G\_{23}} & 0 \\ -\frac{\nu\_{13}}{E\_1} & 0 & 0 & -\frac{\nu\_{23}}{E\_2} & 0 & \frac{1}{E\_3} \end{bmatrix} \begin{Bmatrix} \sigma\_{11} \\ \sigma\_{12} \\ \sigma\_{13} \\ \sigma\_{22} \\ \sigma\_{23} \\ \sigma\_{33} \end{Bmatrix}$$

If thermal flag is 3 and orth is 1, and there are 13 constants arranged as:

E<sup>1</sup> E<sup>2</sup> E<sup>3</sup> G<sup>12</sup> G<sup>13</sup> G<sup>23</sup> ν<sup>12</sup> ν<sup>13</sup> ν<sup>23</sup> ρ α<sup>11</sup> α<sup>22</sup> α<sup>33</sup>

where α11, α22, α<sup>33</sup> are the CTEs along three directions.

For general anisotropic materials, orth is 2, if thermal flag is 0, there are 22 constants arranged as:

```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
             c44 c45 c46
                  c55 c56
                      c66
                       ρ
```
These values are defined using the following Hooke's law:

| <br>σ11          |                          | c11<br>      | c12 | c13 | c14 | c15 | c16<br>      | <br>ε11           |           |
|-------------------|---------------------------|---------------|-----|-----|-----|-----|---------------|--------------------|------------|
| <br>σ12        | <br><br><br><br>= | c12           | c22 | c23 | c24 | c25 | c26<br>      | <br>2ε12        |         |
| <br>σ13<br>   |                           | <br>c13<br> | c23 | c33 | c34 | c35 | <br>c36<br> | <br>2ε13<br>   | <br>   |
| σ22               |                           | <br>c14<br> | c24 | c34 | c44 | c45 | <br>c46<br> | ε22                |            |
| <br>σ23<br> | <br>                | <br>c15<br> | c25 | c35 | c45 | c55 | <br>c56<br> | <br>2ε23<br> | <br> |
| σ33<br>          |                          | c16           | c26 | c36 | c46 | c56 | c66           | ε33<br>           |           |

If thermal flag is 3 and orth is 2, there are 28 constants arranged as:

```
c11 c12 c13 c14 c15 c16
    c22 c23 c24 c25 c26
        c33 c34 c35 c36
             c44 c45 c46
                  c55 c56
                      c66
                       ρ
```
α<sup>11</sup> 2α<sup>12</sup> 2α<sup>13</sup> α<sup>22</sup> 2α<sup>23</sup> α<sup>33</sup>

where αij , with i = 1, 2, 3 and j = 1, 2, 3, are the components of the second-order CTE tensor. CTEs corresponding to the shear strains are multiplied by two because the engineering shear strains are twice of the corresponding tensorial shear strains. The material constants are expressed in the material coordinate system (see Figure [4\)](#page-9-0). If the material properties are given in a different coordinate system, or the arrangement of stresses and strains are different from what VABS uses, a proper transformation of the material properties is needed.

If damping flag is 1, a damping coefficient is input on the very next line following the density input. For example, if orth=0 and thermal flag=3 (thermoelastic analysis with isotropic materials), the material constants are arranged as:

E ν ρ γ α

where γ is a scalar representing the material damping property. It is noted that the damping coefficients for each layer and for each material are additive. In other words, the total damping coefficient used to scale the stiffness-related matrices is damping layer + γ.

If thermal flag is equal to 3, we also need to provide the following nnode lines for temperature for each node arranged as: "node no T," where node no is an integer representing the unique number assigned to each node and T is a real number describing the temperature of the node. These temperature values can be calculated either from a 3D heat conduction analysis or using VABS Conduction, which is a generalization of the VABS approach for heat conduction analysis. Although the arrangement of node no is not necessary to be consecutive, every node starting from 1 to nnode should be present.

Now, we have prepared all the inputs necessary for performing the homogenization run to compute the inertial properties and structural properties of the cross-section. That is, when analysis in Section [6](#page-10-1) does not exist.
