# PCOS Data Exploration and Clinical Evaluation Tool
This project is a Python 3 desktop application developed to explore and analyze data related to Polycystic Ovary Syndrome (PCOS).
The application provides an interactive graphical interface (built with Tkinter) that allows users to:

- View statistical summaries (means, maximums, minimums) for various clinical parameters
- Explore graphs showing relationships between key variables
- Display frequency tables related to PCOS factors
- Perform a personalized clinical evaluation, generating a PDF report with results

The goal of this tool is to provide both exploratory data analysis and basic clinical insights using a real [PCOS dataset](https://www.kaggle.com/datasets/shreyasvedpathak/pcos-dataset/data) obtained from [Kaggle](https://www.kaggle.com/).

## Dataset
The application uses the open-source PCOS Dataset from Kaggle, originally published by Shreyas Vedpathak.
- Original dataset: 45 columns, 541 observations
- After preprocessing: 42 variables retained (removing ID columns and an empty column)
- PCOS patients: 177 diagnosed individuals

This dataset includes clinical, biochemical, and lifestyle parameters of women, providing a foundation for PCOS analysis and visualization.

## Features
1. **Parameter Analysis**
Displays tables showing mean, maximum, and minimum values for selected parameters (e.g., Age, Menstrual Cycle Length, Glucose, Hormones, Follicles).
Tables are generated using Plotly and rendered as images with Pillow.

2. **Graphical Visualization**
Exploratory data analysis through:
- Histograms, box plots, scatter plots, and regression plots
- Built with Seaborn and Matplotlib
- Allows visualization of relationships such as:
    - Age distribution among PCOS vs non-PCOS patients
    - Vitamin D levels
    - FSH/LH ratio
    - Follicle count correlations
    - Endometrium thickness, BMI vs glucose, and more

3. **Frequency Tables**
Displays relative and absolute frequencies for variables such as:
- PCOS occurrence
- BMI classification
- Pregnancy status
- Weight gain
- Hair growth
- Physical exercise

4. **Clinical Evaluation (PDF Report)**
Users can input their own clinical values (e.g., TSH, AMH, Vitamin D, Hemoglobin, and Cycle Length) into the GUI.
The system evaluates these values against reference ranges and generates a personalized PDF report using ReportLab, including an illustrative diagram of PCOS etiology.

## Instalation and requirements
The file environment.yml have all dependencies needed for this project:
```yaml
name: pac_pcos
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - python=3.12
  - pip
  - pandas
  - matplotlib
  - seaborn
  - reportlab
  - pillow
  - plotly
  - kaleido
  - tk
```
### Conda
1. Clone the repository:
```
    git clone https://github.com/anarmsilva10/PAC_PCOS.git
    cd PAC_PCOS
```
2. Create Conda environment:
```
    conda env create -f environment.yml
    conda activate pac_pcos
```
3. Run the application:
```
    python Programa.py
```

## Contribution:
To contribute to this project:
1. Fork the repository.
2. Create a new branch: `git checkout -b my-branch`.
3. Commit your changes: `git commit -m 'changes'`.
4. Push to your branch: `git push origin my-branch`.
5. Open a pull request.

## Developers:
Developed by Adriana Gomes & Ana Rita Silva, during master's degree in clinical bioinformatics, specifically in the Programming and Algorithms in Science course.

University: Universidade de Aveiro – MSc in Clinical Bioinformatics.

## Branches
update_version is a branch that features a new application architecture and a more efficient way of working with the application.

The streamlite branch was created with the goal of transforming the initial application into a more complete and user-friendly application.

## License
This project is licensed under the terms of the MIT License.
