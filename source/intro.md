# Introduction

VABS (Variational Asymptotic Beam Sectional Analysis) is a code implementing the beam theories[hodges1992simplified] based on the concept of simplifying the original nonlinear three-dimensional (3D) analysis of slender structures into a two-dimensional (2D) cross-sectional analysis and a one-dimensional (1D) nonlinear beam analysis using the variational asymptotic method.[25](#page-25-1)

VABS takes a finite element mesh of the cross-section including all the details of geometry and material as inputs to perform a homogenization analysis to compute sectional properties including inertial properties and structural properties. These properties are needed for the 1D beam analysis to predict the global behavior of slender structures. VABS can also perform a dehomogenization analysis to compute the distributions of 3D displacements/strains/stresses, and failure indexes and strength ratios over the cross-section based on the global behavior of the 1D beam analysis.

Since most of the theoretical details are presented in pertinent papers and collected in the book by Prof. Hodges,[7](#page-24-2) this manual will only serve to help readers get started using VABS to solve their own composite beam problems. This manual addresses the history of the code, its features, functionalities, conventions, inputs, outputs, maintenance, and tech support.


## Features

Along with the features of previous versions, the most recent version of VABS has the following features:

- 1. It is a highly modularized code written in the modern Fortran language. All the problemdependent arrays are allocated dynamically during run time, and the user can use all the memory up to the limit of the machine. All the outstanding abilities of array handling in the modern Fortran language have been exploited.
- 2. It adopts highly efficient techniques to reduce the requirement of RAM and increase the computing efficiency. Now cross-sections as complex as real composite helicopter rotor blades with hundreds of layers can be easily handled on a laptop computer.
- 3. It has a general element library that includes all the typical 2D elements such as 3, 4, 5, 6-node triangular elements and 4, 5, 6, 7, 8, 9-node quadrilateral elements. Users are free to choose the type of elements, and different types of elements can be mixed within one mesh.
- 4. It can deal with arbitrary layups. Users can provide one parameter for the layup orientation and one parameter for the ply orientation to uniquely specify the material system in the global coordinate system. Nine parameters can be used for the ply orientation if a ply is highly curved and the ply angle is not uniform within an element.
- 5. It detects singularities and properly removes them to render the solution as a true representation of the theory. Older versions before VABS II dealt with them approximately by asking the users to input four constraints on three distinct, user-specified nodes. The arbitrariness of

the older approach can affect the refined models, and sometimes may even render the linear system unsolvable.

- 6. It applies the four constraints on the warping functions in such a way that the 3D elasticity solution can be reproduced for isotropic beams, correcting a mistake related with these constraints in previous versions.
- 7. It does not require the beam reference line to be the locus of cross-sectional area centroids. VABS can calculate the centroid for any arbitrary cross-section, and users can choose their own reference line for the convenience of the 1D global beam analysis.
- 8. It can deal with isotropic materials, orthotropic materials, and general anisotropic materials, while the previous versions treat all materials as orthotropic.
- 9. It can be quickly and conveniently integrated with other environments such as computeraided design environments, multidisciplinary optimization environments, or commercial finite element packages.
- 10. VABS can be executed as a standalone executable in command line or called by other codes as a library.

## Functionalities

VABS is a general-purpose, cross-sectional analysis tool for computing inertial, stiffness, and strength properties of general cross-sections. Specifically, it has the following functionalities:

- 1. Compute the 6×6 mass matrix, written in terms of the mass per unit length, and the first and second mass moments of inertia about the three axes. Based on the information provided by the mass matrix, VABS calculates the mass center, the principal inertial axes, the principal mass moments of inertia, and the mass-weighted radius of gyration.
- 2. Compute the geometrical center of the cross-section and the area of the cross-section.
- 3. Compute the 4×4 stiffness matrix and compliance matrix for the classical model (also called the Euler-Bernoulli model) for prismatic or initially curved/twisted composite beams with normal or oblique cross-sections. Based on the classical model, VABS can calculate the location of tension center, the extension stiffness (EA), the torsional stiffness (GJ), the principal bending stiffnesses (EI<sup>22</sup> and EI33), and the principal bending axes.
- 4. Compute the 6×6 stiffness matrix and compliance matrix for the Timoshenko model for prismatic or initially curved/twisted composite beams with normal cross-sections. Based on the Timoshenko model, VABS can calculate the location of the shear center, the principal shear stiffnesses (GA<sup>22</sup> and GA33), and the principal shear axes.
- 5. Compute the 5×5 stiffness matrix and compliance matrix for the Vlasov model for prismatic or initially curved/twisted composite beams with normal cross-sections, which is important for thin-walled beams with open sections.

![](_page_7_Figure_0.jpeg)

<span id="page-7-0"></span>Figure 1: VABS beam coordinate system

- 6. Compute the trapeze effects, a nonlinear effect important for beams under large centrifugal forces. The composite beam could be either prismatic or initially twisted and curved.
- 7. Compute 3D pointwise displacement, strain, and stress fields using the global behavior of a 1D global beam analysis using the classical model, the Timoshenko model, or the Vlasov model. Multiple recovery runs can be performed for different inputs of global beam responses without repeating the homogenization analysis. The recovered stress/strain fields are evaluated both at the nodal positions and Gauss points. They are expressed in both the material coordinate system and the beam coordinate system.
- 8. Compute sectional damping matrix for composite beams. The computation is based on the simple concept of scaling stiffness related matrices with the lamina damping coefficient specified for each material.
- 9. Compute hygrothermal effects of composite beams due to temperature and moisture changes. As a companion capability, VABS Conduction is developed to carry out a dimensional reduction for the 3D conduction problem, which can be requested separately.
- 10. Compute the failure index and strength ratio distribution over the cross-section, and the strength ration for the entire cross-section.


## History

The research project that gave birth to VABS was initiated by Prof. Dewey Hodges when he was first introduced to the variational asymptotic method by Prof. Berdickevsky at Georgia Tech in 1989 and has been ongoing ever since till the time of writing. The program name VABS first appeared in [\[1\]](#page-24-0).

The original version of VABS was based on a research code written by Prof. Cesnik. The fall semester of 1998, when Prof. Yu began his graduate study at Georgia Tech, marked the beginning

<sup>\*</sup>VABS is copyrighted by Utah State University, Georgia Technology Research Cooperation, and Purdue Research Foundation. All rights reserved. VABS is commercialized by AnalySwift, LLC. To request VABS, please visit www.analyswift.com.

of the transition of VABS from a research code to a production design and analysis tool for practicing engineers. The code was rewritten from scratch using the modern Fortran language, with all unnecessary restrictions eliminated, and the computing and memory efficiency greatly enhanced. At the same time, Prof. Cesnik was continuing his work on VABS for piezoelectric materials at MIT and later at University of Michigan. Profs. Hodges and Yu continue their work on VABS for multiphysics modeling at Georgia Tech, Utah State University, and Purdue University. For this reason, there are two variants of VABS: the Georiga Tech/Utah State/Purdue VABS, released and maintained by Prof. Yu, and UM/VABS, released and maintained by Prof. Cesnik. From henceforth in this manual the term VABS will refer only to the Georgia Tech/Utah State/Purdue VABS, and what follows is only applicable to this code.

Many researchers and engineers all over the world are actively using VABS. VABS is becoming a standard tool for design and analysis of composite slender structures such as helicopter rotor blades, wind turbine blades, high aspect ratio wings, UAM/eVTOL/UAV blades, propellers, landing gear, composite tubes, etc.

