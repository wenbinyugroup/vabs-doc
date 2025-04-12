# Changelog



## What is New in VABS 4.1

The new capabilities of VABS 4.1 are:

- 1. Perform dehomogenization for multiple load cases in terms of forces and moments corresponding to the Euler-Bernoulli model and the Timoshenko model.
- 2. Output the modes and corresponding ratios for failure criteria with identifiable modes such as failure criterion 1, 2, 5.
- 3. Provide documentation for the user-define failure criterion capability.
- 4. Enable users to suppress the output of other stress/strain files except the average stresses/strains for each element in the ele file.
- 5. Remove damping input for no damping analysis.
- 6. Output the classical stiffness matrix and compliance matrix at the shear center.
- 7. Enable comment lines in the inputs for better readability.
- 8. Output the time and date the code is compiled and released.
- 9. Provide simple instructions when VABS, VABS -h, or VABS -help is issued in the command line.
- 10. Simplify the installation process without administrator privilege.

## What is New in VABS 4.0

The new capabilities of VABS 4.0 are:

- 1. Compute pointwise distributions of failure indexes and strength ratios over the cross-section under a given load.
- 2. Compute the safety margin (the minimum strength ratio among all elements) of the crosssection under a given load.
- 3. Output the nodal stress/strain values according to the original numbering of the finite element nodes.
- 4. Output the complete set of engineering properties commonly used in conventional beam analysis including extension stiffness (EA), torsional stiffness (GJ), principal bending stiffnesses (EI22, EI33), principal shear stiffness (GA22, GA33), tension center, shear center, principal inertial axes, principal bending axes, and principal shear axes.
- 5. Since VABS 4.0, we change the executable name to VABS.

## What is New in VABS 3.9

The main new feature of VABS 3.9 is prediction of sectional damping matrix based on the lamina damping coefficients. VABS 3.9 can also output the cross-sectional area. Another feature is that VABS 3.9 is now distributed as a single library.

## What is New in VABS 3.8

The main new feature of VABS 3.8 is a new license manager to allow more versatile license mechanisms including node locked licenses and floating licenses. The user does not have to put the license in the same folder as the input file as it was the case for previous versions. Instead, the user can use a node locked license file stored in the same folder as the VABS executable or obtain a floating license from a license server.

Since VABS 3.8, we provide free academic licenses for students and professors to use the full version of VABS for teaching and academic research.

Since VABS 3.8, we provide both Linux and Windows versions.

## What is New in VABS 3.7

The main new feature of VABS 3.7 is to carry out the recovery up to the second order which provides a better prediction for the 3D recovered fields in comparison to known exact solutions.

## What is New in VABS 3.6

The main new feature of VABS 3.6 is to use an improved method for optimizing the numbering of finite element mesh. For large problems, it is much faster than the method used in previous versions. The most recent version of fortran compiler is used for compiling the code resulting in much faster recovery.

## What is New in VABS 3.5

The main new feature of VABS 3.5 is for oblique cross-sectional analysis, the inputs are given in the oblique cross-sectional system while in previous versions, the inputs are given in the normal crosssectional coordinates. Also starting VABS 3.5, users can use long names of input file, including spaces in the path and file names.

## What is New in VABS 3.4

The main new feature is expanding <sup>√</sup><sup>g</sup> in the modeling for initially curved/twisted beams. For some cases such a change made significant differences for obtaining first and second correction of the stiffness matrix due to initial curvature and twist. Such a change is verified using an initially curved strip for which an elasticity solution is obtainable. The input file for this case is isorectTrif2.sg. A 64-bit version of VABS is also available since VABS 3.4.

## What is New in VABS 3.3

The main new feature is introducing a new input format, and keeping the previous input format as optional. In the new format, the user only needs to provide one real number for θ<sup>1</sup> as few users take advantage of the nine real numbers for θ1, which is useful for elements with highly curved edges. In the new format, we introduce layer definition so that a layer type instead of material type is provided for each element. Each layer is defined through a unique combination of material type and layerup angle θ3. It is more economical than assigning θ<sup>3</sup> for each element, as what we have done in the previous format, because the number of layers usually is much less than the number of elements. These two changes reduce approximately 3/4 of real numbers needed for VABS inputs, saving space and time. These changes will also simplify the development of VABS preprocessors as it is easier to compute just one number for θ<sup>1</sup> for each element.

## VABS III and What is New

VABS was originally designed to run as a standalone code and its error handling, memory allocation/deallocation, and I/O were handled with this use in mind. However, in recent years, more and more users began to explore the possibility of using VABS in a design environment. This motivates the major upgrade of VABS to VABS III through restructuring the code.

Since the first release of VABS III, a few users have asked the difference between VABS III and previous versions, in particular VABS 2.1.1 which was the last release and the code accompanying Prof. Hodges' book.[7](#page-24-2) Overall, VABS III is a much improved code in both accuracy and efficiency. The main difference can be described according to the following two aspects.

- As far as functionalities concerned, VABS III
    - 1. Uses the correct constraints so that it can reproduce the 3D elasticity theory for isotropic prismatic beams. This change affects the warping functions, and affects all stiffness models except the classical one. Such a correction enables VABS to reproduce the 3D elasticity theory for isotropic prismatic beams and thus enables VABS to provide a better modeling for prismatic or initially curved/twisted composite beams (VABS 3.0).
    - 2. Recovers 3D stress/strain fields at each node in addition to Gauss points. The recovered 3D stress/strain fields are expressed in both the beam coordinate system and the material coordinate system. VABS 2.1.1 only recovers 3D stress/strain fields at Gauss points expressed in the beam coordinate system. For visualization, nodal values are convenient. To apply failure criteria of composite materials, stresses/strains expressed in the material coordinate system are needed (VABS 3.0).
    - 3. Handles isotropic, orthotropic, and anisotropic material differently. Previous versions treat all materials as orthotropic only and must take a total of 9 elastic constants. VABS III allows general anisotropic material with as many as 21 elastic constants and isotropic materials with as few as 2 elastic constants (VABS 3.0).
    - 4. Can model hygrothermal effects of composite beams due to temperature and moisture changes. As a companion capability, VABS Conduction is developed to carry out a dimensional reduction for the 3D conduction problem. VABS Conduction can be requested separately (VABS 3.1).
    - 5. Updates the transformation procedure into the Timoshenko model from the asymptotic energy. A new perturbation method is developed to capture the effects due to initial curvatures/twist during the transformation. The prediction for Timoshenko stiffness is generally improved, even for some prismatic beams (VABS 3.2).
    - 6. Outputs the average of 3D stresses/strains within each element for convenience of postprocessing (VABS 3.2.2).
    - 7. Provides an option for recovering the 3D displacement/strain/stress fields based on the linear beam theory (VABS 3.2.4).
- As far as the quality of the code is concerned, VABS III
    - 1. Is restructured to change the error handling and error message handling, memory allocation and de-allocation, and I/O handling to facilitate its integration with other software environments (VABS 3.0).
    - 2. Interprets and echoes all the input data for quicker identification of mistakes in the input file (VABS 3.0).
    - 3. Is much faster than VABS 2.1.1 by modifying the mesh optimization algorithm and adopting a new approach to calculate the elemental finite element matrices (VABS 3.0).
    - 4. Uses dynamic link libraries (DLLs) to encapsulate the analysis capability so that VABS has true plug-n-play capability which is convenient for integration into other environments. Now VABS can be used both as a standalone application and two callable libraries. The two callable libraries and the corresponding manual for developers can be requested separately (VABS 3.0).

5. Has more thorough and informative error handling (VABS 3.0).

Quite a few bugs in VABS 2.1.1 have been corrected in VABS III and its later versions. One bug is associated with the modified linear solver. Because of this bug, for some very rare cases, VABS 2.1.1 provides some annoying couplings which are not supposed to be there. VABS 3.0 has no such anomaly. At least one bug related with the Trapeze effect inherited from the original VABS before 1998 has been corrected in VABS 3.0. A bug related with recovery is also corrected in VABS 3.2.3.

Starting from VABS 3.0, an evaluation version of VABS is free for anybody who asks. It allows the user to evaluate the code for one month before obtaining a permanent license.

## 3.11 VABS II

VABS II was released in June 2004, with the major enhancement to remove the need of asking the user to choose arbitrary point constraints and let the code determine the singularity and apply the corresponding constraints. Other improvements of VABS II include calculation of principal inertial axes, the mass matrix, and neutral axes, and a significant reduction of the computing time for large size problems.


