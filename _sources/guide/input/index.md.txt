# Inputs

Although a few preprocessors, such as PreVABS, have been developed to create VABS input files, it is still beneficial for advanced users, particularly those who want to embedded VABS in their own design environment, to understand the meaning of the input data.

Starting from VABS 4.0, the inputs for the VABS are separated into two files: homogenization input file and dehomogenization input file.
VABS homogenization run only requires the homogenization input file with a name of the user's choice.
The dehomogenization input file associated with the homogenization input file with extension `glb`.
In other words, if the homogenization input file name is `input_file_name`, the dehomogenization input file must be `input_file_name.glb`.
Empty lines or comment lines can be used in the input file for readability.
The comment line must start with `!`.

```{toctree}
main.md
global.md
ufc.md
```
