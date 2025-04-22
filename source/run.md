# Execution

VABS is a command line code.
When the user types `VABS`, `VABS -h`, or `VABS -help` in the command line, some simple instructions for providing correct arguments is provided.
VABS is executed using

```
VABS inputfile analysis nload
```

in the regular command prompt with `inputfile` required and `analysis` and `nload` optional.
The command line argument analysis lets VABS know which type of analyses to perform.


## Arguments

1. If `analysis` does not exist, VABS will carry out a homogenization analysis to compute the inertial and stiffness properties.
2. If `analysis` is equal to 1, VABS will carry out a dehomogenization analysis to recover 3D displacements, strains, stresses based on the nonlinear beam theory with minimum outputs.
3. If `analysis` is equal to 10, VABS will carry out a dehomogenization analysis to recover 3D displacements, strains, stresses based on the nonlinear beam theory with large outputs.
4. If `analysis` is equal to 2, VABS will carry out a dehomogenization analysis to recover 3D displacements, strains, stresses based on the linear beam theory with minimum outputs.
5. If `analysis` is equal to 20, VABS will carry out a dehomogenization analysis to recover 3D displacements, strains, stresses based on the linear beam theory with large outputs.
6. If `analysis` is equal to 3, VABS will carry out a dehomogenization analysis to evaluate the distribution of failure index and strength ratio over the cross-section, and the strength ratio of the entire cross-section.

If `analysis` is equal to 1, 2, 3, we can also provide another command line argument `nload` as the total number of loads for VABS to perform the corresponding dehomogenization analysis.
If this argument does not exist, it will perform the dehomogenization analysis for a single load case.
