## Discovery of allosteric binding site in G-protein coupled receptors

### Aim: 
To find allosteric binding sites for the CysTLR2 receptor
### Steps:
0. CysTLR2 structure preparing
1. Run molecular dynamics (MD) for CysTLR2 
2. Apply a binding site search method to find hidden binding sites
3. Perform post-processing and statistical analysis of the results

### Methods
For MD a protein structure needs to be prepared. To begin with, we simulated the amino acid sequence [1] of a protein by the crystal structure [2] using the Modeller [3]. 
In "modelling" folder you can find model-single.py, which was used for: loops modelling, missed residuals simulating, auxiliary proteins removing and refinement.
Since GPCRs are membrane receptors, for MD it is necessary to place the receptor structure in the bilipid layer. For this, we used the CHARMM-GUI [4]. The bilipid layer was designed using the parameters described in the article [5]. 

Support files for the CHARMM-GUI, as well as the results of its work, can be found in the "gromacs" folder. Also in this folder you can find "run" script for running MD in GROMACS [6].

For binding sites searching we used fpocket [7]. 

For post-processing we used mdpocket (it's command in fpocket). For statistical analysis of the results we used "description_analysis.r" script. You can find mdpocket results and "description_analysis.r" script in "pockets"-folder.

### System requirements
python 3.8+, R 3.5+, GROMACS 5.1, fpocket 3.1

### Results

fpocket results are all of pockets of protein:
![fpocket result](all_pockets.png)

description_analysis.r allows you to analyze the time series of changes in the volume of the pocket
![description_analysis.r](stat_analysis.png)

### Bibliography
1. https://www.uniprot.org/uniprot/Q9NS75
2. https://www.rcsb.org/structure/6RZ8
3. B. Webb, A. Sali. Comparative Protein Structure Modeling Using Modeller. Current Protocols in Bioinformatics 54, John Wiley & Sons, Inc., 5.6.1-5.6.37, 2016.
4. Jo, Sunhwan, et al. "CHARMM‐GUI: a web‐based graphical user interface for CHARMM." Journal of computational chemistry 29.11 (2008): 1859-1865.
5. Gusach, Anastasiia, et al. "Structural basis of ligand selectivity and disease mutations in cysteinyl leukotriene receptors." Nature Communications 10.1 (2019): 1-9.
6. Van Der Spoel, David, et al. "GROMACS: fast, flexible, and free." Journal of computational chemistry 26.16 (2005): 1701-1718.
7. Vincent Le Guilloux, Peter Schmidtke and Pierre Tuffery, "Fpocket: An open source platform for ligand pocket detection", BMC Bioinformatics, 2009, 10:168

