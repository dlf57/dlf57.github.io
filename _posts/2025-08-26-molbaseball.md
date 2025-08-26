---
layout: single
title:  "What Molecule matches Shohei Ohtani's 2024 Season?!"
excerpt: "Comparing baseball player fingerprints and their corresponding molecule."
date:   2025-08-26
categories: projects
author_profile: true
classes: wide
header:
    teaser: /assets/images/mol-ohtani.png
---

My inspiration for making `diamondfp` was molecular fingerprinting used in cheminformatics for molecular similarity. Molecular similarity is a common practice, especially in medicinal chemistry and drug discovery, used for tasks such as similarity searching, clustering, and diversity analysis. I wanted to be able to employ these strategies when analyzing baseball statistics and use it as a quick way to cluster players based on performance. 

With initial fingerprint descriptors and some early analysis of careers and seasons complete, I wanted to do the fun tie back to chemistry! Can we take a fingerprint of a player’s season and compare it to a library of molecules and see what molecule matches that player?

## Creating Fingerprints
With the premise set, I decided to choose the most popular player of our time, Shohei Ohtani, and look at what has been one of his most productive seasons at the plate, the 2024 season. Obtaining the baseball data was relatively straightforward thanks to [Baseball Savant](https://baseballsavant.mlb.com/). 

Next was the task of getting a large set of molecules. What better place to start than [ChEMBL](https://www.ebi.ac.uk/chembl/). ChEMBL is a chemical database featuring a lot of drug like molecules. We will be specifically grabbing [chembl_35_chemreps.txt.gz](https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/) as it contains just shy of 2.5 million SMILES. SMILES stands for Simplified Molecular Input Line Entry System and are a way to represent a molecular structure in text notation (ex. Aspirin is represented as ‘O=C(C)Oc1ccccc1C(=O)O’). Using the SMILES strings from ChEMBL, we can build our molecules in [RDKit](https://www.rdkit.org/) and create our fingerprints. RDKit is a crucial Python library for cheminformatics/bioinformatics and I encourage those interested to checkout their blog and examples like [this showing how to make molecular fingerprints](https://greglandrum.github.io/rdkit-blog/posts/2023-01-18-fingerprint-generator-tutorial.html).

With our baseball fingerprint and molecular fingerprints made, we need some way to compare them. In cheminformatics, this is commonly done using what is called a Tanimoto similarity (known also as Jaccard score for those outside of cheminformatics) and measures how much the two sets overlap. 

## So What Molecule is Shohei Ohtani?!

The closest matching molecule to Shohei Ohtani's 2024 season was a preclinical drug, [CHEMBL5489980](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5489980). The paper is open access, so feel free to check it out and learn more about this small-molecule inhibitor! ([Paper Link](https://doi.org/10.1016/j.isci.2024.108907))

<div style="font-size:0;">
    <img src="/assets/images/mol-ohtani.png" width="500">
</div>

**3D Molecule made using [3Dmol.js](https://3dmol.csb.pitt.edu/)**

| ChEMBL ID | SCORE |
|-----------|-------|
| [CHEMBL5489980](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5489980) | 0.798 |
| [CHEMBL543342](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL543342)  | 0.795 |
| [CHEMBL3923723](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3923723) | 0.795 |
| [CHEMBL1192156](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1192156) | 0.795 |
| [CHEMBL3458430](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3458430) | 0.794 |
| [CHEMBL397829](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL397829)  | 0.793 |
| [CHEMBL1395909](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1395909) | 0.792 |
| [CHEMBL3477461](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3477461) | 0.792 |
| [CHEMBL2005900](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2005900) | 0.792 |
| [CHEMBL4754559](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4754559) | 0.792 |


This was a really fun experiment for me to do. While finding the molecule that matches Shohei Ohtani has no real meaning, it shows off fingerprints and similarity scoring in a fun way. It was also a great way to link two of my favorite things, chemistry and baseball, in a way that I had never really thought of prior to `diamondfp`. If you want to try this out for yourself or see the code, head over to [`diamondfp`'s GitHub](https://github.com/dlf57/diamondfp/blob/main/examples/molecule_match.ipynb)!
