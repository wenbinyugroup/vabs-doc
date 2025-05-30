# User-defined Failure Criterion

A simple UMAT is provided for users to program their own failure criterion by changing the fortran code `UserFC.f90`.
The sample code is for max stress failure criterion for anisotropic materials.
The failure criterion number and strength constants should be provided as described above.
Pointwise strains and stresses and strength constants are passed to the user subroutine, failure index, strength ratio, failure mode, and strength ratio for each stress component are computed inside this subroutine and passed back to VABS.
Users need to first modify `UserFC.f90` according to their own failure criterion, then compile it to be a shared library.
A sample make file (`MakeUser`) for using the fortran compiler ifort is included.
One only needs to execute `make -f MakeUser` to compile the user subroutine.
Then, one can use VABS with user-defined failure criterion.
The code is simple enough and there is enough comments inside the source codes for the user to adopt the sample code for other user-defined failure criterion.
