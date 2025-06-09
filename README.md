# Cell Maps for AI (CM4AI) Affinity Purification-Mass Spectrometry (AP-MS) Embedding Tutorial

## Overview
This tutorial will work with the AP-MS data that are available in the [CM4AI May 2024 Data Release](https://dataverse.lib.virginia.edu/dataset.xhtml?persistentId=doi:10.18130/V3/DXWOS5). This release contains AP-MS raw data in untreated, acquired on a Orbitrap Fusion™ Lumos™ Tribrid™ Mass Spectrometer (Thermo Scientific).
Raw data are processed using Maxquant v1.6.12.0 using default parameter with LFQ quantification and the “202209_uniprot_human_reviewed.fasta” file as reference.

With the Python notebooks and scripts in the src directory, you will be able to:
1. Download and extract the raw AP-MS data from Dataverse,
2. Run an exploratory data analysis (EDA) for the AP-MS data,
3. Generate embeddings for the AP-MS data using the [CM4AI cell maps pipeline](https://github.com/idekerlab/cellmaps_pipeline),
4. Create and visualize a protein-protein interaction (PPI) network using AP-MS data, and
5. Explore the patterns of the protein interactions with the PPI network graph.

## Background Information
For a quick background on CM4AI data and tools, the following short videos provide a quick introduction:

| **Introduction to CM4AI** | **Introduction to the Cell Map Pipeline** |
|:-------------------------:|:----------------------------------------:|
| [![Introduction to CM4AI](https://img.youtube.com/vi/wiGgof7gY3w/hqdefault.jpg)](https://www.youtube.com/watch?v=wiGgof7gY3w) | [![Cell Map Pipeline](https://img.youtube.com/vi/AK2eQbOys2I/hqdefault.jpg)](https://www.youtube.com/watch?v=AK2eQbOys2I) |

## Working with the Tutorial
1. Create a conda environment
```
conda env create -f environment.yml
```
2. Activate the environment
```
conda activate cm4ai-apms-tutorial
```
3. Review and run the tutorial scripts
   1. Download the CM4AI data release: [View Script](src/download.py)
   2. Explore the data set: [View Notebook](src/eda.ipynb)
   3. Generate embeddings with cellmaps_image_embedder: [View Script](src/generate_embeddings.py)
   4. Generate a protein similarity graph based on the embedding and visualize results: [View Notebook](src/generate_network.ipynb)

## Links and References
* CM4AI Website: https://cm4ai.org
* YouTube Channel: https://youtube.com/@cm4ai
* CM4AI Pre-Print: https://www.biorxiv.org/content/10.1101/2024.05.21.589311v1