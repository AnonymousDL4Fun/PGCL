# PGCL
Prototype Governed Contrastive Learning for robust image classification in Histopathology

## PGCL Schematic
![PGCL Schematic](./Figures/Schematic_final.png)

Figure(a) shows the schematic of PGCL based training setup.

Figure(b) represents the output feature distribution separated by the trained linear classifier layer. Prediction confidence is computed via Softmax function.

Figure(c) shows the output vectors resulting from PGCL based training. The class vectors distribute in Laplacian distribution around their class prototypes. Prediction confidence is computed using Laplacian distribution mean and standard deviation.

## Visualization of Kather-19 In distribution (ID) and Out-of-distribution (OOD) classes
![Kather-19 samples](./Figures/PGCL_Kather_ID_OOD_sets.PNG)
