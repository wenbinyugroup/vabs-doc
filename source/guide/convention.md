# Conventions


To understand the inputs and interpret outputs of the program correctly, we need to explain some conventions used by VABS.

First, VABS uses a right hand system, the beam coordinate system, denoted as x1, x<sup>2</sup> and x3, where x<sup>1</sup> is along the beam axis and x<sup>2</sup> and x<sup>3</sup> are the local Cartesian coordinates of the cross section, see Figure [1](#page-6-0) for a beam with an arbitrary cross section. Usually, for rotor blades, x<sup>1</sup> is along the direction of the span and points to the tip, x<sup>2</sup> is along the direction of the leading-edge to the trailing edge and points to the direction of the leading edge, and x<sup>3</sup> can be determined by the right hand rule. Usually the origin of x<sup>1</sup> is located at the root of the blade, yet the user is free to choose the origin of x<sup>2</sup> and x<sup>3</sup> at an arbitrary point of the cross section, such as the mass center, centroid, or shear center. Detailed information is needed to define the cross-sectional geometric domain spanned by x<sup>2</sup> and x<sup>3</sup> and the materials that occupy that domain. Also, certain characteristics along the span direction, such as initial curvature/twist or taper, are needed for cross-sectional analyses when they are not equal to zero. The obliqueness should be specified when the angle between x<sup>1</sup> and the x2-x<sup>3</sup> plane is not equal to 90◦ , that is, when reference cross section is not normal to the reference line, such as the case of a swept wing. It is noted that the beam coordinate system is the same as the undeformed beam coordinate system b defined in Ref. [\[10\]](#page-21-4).

Second, VABS numbers the nodes of each element in the counterclockwise direction, as shown in Figure [2](#page-7-0) for triangular elements and Figure [3](#page-7-1) for quadrilateral elements. Nodes 1, 2, and 3 of the triangular elements and nodes 1, 2, 3, and 4 of the quadrilateral elements are at the corners. Nodes 5, 6, 7 of the triangular elements and nodes 5, 6, 7, 8, 9 for quadrilateral elements are optional nodes.

The recovered 3D displacements are values at each node expressed in the VABS beam coordinate system (Figure [1\)](#page-6-0). However, stresses and strains are most accurately evaluated at Gaussian

![](_page_7_Figure_0.jpeg)

<span id="page-7-0"></span>Figure 2: VABS triangular element node numbering and corresponding integration schemes

![](_page_7_Figure_2.jpeg)

<span id="page-7-1"></span>Figure 3: VABS quadrilateral element node numbering and corresponding integration schemes

integration points. Gaussian integration schemes for different orders of the two types of elements are also shown in Figures [2](#page-7-0) and [3.](#page-7-1) The red interior points correspond to the integration scheme for linear elements and the green interior points correspond to the integration scheme for quadratic elements. VABS can also recover 3D stresses and strains at each node as suggested by our industry users. The recovered stresses, and strains are expressed in both the beam coordinate system and the material coordinate system, which is essential for applying failure criteria.

VABS allows users to use various kinds of units. However, it is necessary to be absolutely consistent in the choice of units to avoid errors. Particularly, users must never use the pound as a unit of mass to avoid confusion. When pounds are used for force and feet for length, the unit of mass must be the slug = lb-sec2/ft; if inches are used for length along with pounds for force, then the unit of mass must be lb-sec2/in.

Finally, to understand the VABS input convention for composite layups, we need to find relationships among three coordinate systems: the beam coordinate system (x1, x2, x3) used by the user to define the geometry, the material system (e1, e2, e3) used by the user to define the material properties, and an intermediate one to define the ply plane (y1, y2, y3). As shown in Figure [4,](#page-8-0) the

![](_page_8_Figure_0.jpeg)

<span id="page-8-0"></span>Figure 4: VABS layup convention

ply coordinate system (y1, y2, y3) is formed by rotating the global coordinate system (x1, x2, x3) in the right-hand sense about x<sup>1</sup> by the amount 0 ≤ θ<sup>1</sup> ≤ 360◦ . Then, the ply coordinate system (y1, y2, y3) is rotated about y<sup>3</sup> in the right-hand sense by the amount −90◦ ≤ θ<sup>3</sup> ≤ 90◦ to form the material system (e1, e2, e3), the range of θ<sup>3</sup> being same as is commonly defined in the field of the composite materials. Here we use the box-beam section depicted in Figure [5](#page-9-0) to illustrate VABS layup conventions. Here, x<sup>1</sup> is pointing toward the reader, x<sup>2</sup> is pointing to the right side of the reader, and x<sup>3</sup> is pointing upward vertically. For the upper wall: θ<sup>1</sup> = 0◦ ; the left wall: θ<sup>1</sup> = 90◦ ; the lower wall: θ<sup>1</sup> = 180◦ ; the right wall: θ<sup>1</sup> = 270◦ . For all the walls θ<sup>3</sup> = θ for the box-beam in Figure [5](#page-9-0) because all the fibers are rotating positively about y3/e<sup>3</sup> by the angle θ. The users can specify their own stacking sequences. The stacking sequences expressed from the innermost layer to the outermost layer for each wall are often used.
