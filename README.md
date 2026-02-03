# Gender Bias Analysis: ISTAT vs. Paisà Corpus

**Introduction to Programming** project (a.y. 2024-2025) by **Chiara Mancuso**.

## Research Objective
This project investigates the relationship between the Italian occupational reality and its linguistic representation, focusing on gender disparities. The goal is to verify whether written language reflects the actual distribution of employment or if it exhibits **sociolinguistic biases** that skew the perception of professional roles.

---

## Methodology
The analysis is divided into three main phases:

1.  **ISTAT Analysis:** A study of the real-world occupational distribution across 7 key sectors (Healthcare, Research, Education, Publishing, Mining, Legal/Accounting, and Real Estate) between 2012 and 2017.
2.  **Linguistic Analysis (Paisà Corpus):** Extraction and quantification of professional roles using **Regular Expressions (Regex)** and custom heuristics to identify grammatical gender.
3.  **Comparative Analysis:** A direct comparison between real-world gender gap data and linguistic frequency to highlight discrepancies between social reality and language.

---

## Repository Structure
The project is organized into a modular structure to ensure readability and reproducibility:

* **`Progetto.ipynb`**: Main Jupyter Notebook containing the full analysis and data visualizations.
* **`Moduli/`**: Directory containing custom Python scripts:
    * `euristiche.py`: Heuristics for gender identification.
    * `mie_funzioni.py`: Helper functions for data processing.
    * `classe.py`: Object-oriented approach for data management.
* **`output_progetto/`**: Directory for exported results, including charts and cleaned datasets.
* **`data/`**: Placeholder directories for input datasets.

---

## Data Management & Large Files
Due to high file sizes (>100MB), the raw linguistic data is not directly included in the repository:

* **Raw Dataset (Paisà Corpus):** Must be downloaded from [this Google Drive link](https://drive.google.com/file/d/1e77ZmvziskUIFKFIXA_2ft9kDdIVUG1f/view?usp=sharing) and placed in `data/paisa/`.
* **Cleaned Data:** The file `paisa_pulito.csv` and processed DataFrames are generated automatically by the code during the normalization phase.

---

## Setup & Execution
To reproduce the full analysis:
1.  **ISTAT Dataset:** Ensure the raw statistics are located in `data/istat/`.
2.  **Paisà Corpus:** Download the raw file from the Google Drive link and place it in `data/paisa/`.
3.  **Execution:** Run the `Progetto.ipynb` notebook. The normalization stage will automatically create the necessary files in `output_progetto/df_puliti/`.

---

## Key Findings
The analysis reveals that the **Paisà Corpus significantly overestimates male presence** compared to official ISTAT data, especially in female-majority sectors. This phenomenon reflects the persistence of cultural and linguistic biases that privilege masculine forms in written discourse, reinforcing traditional gender stereotypes regardless of the actual labor market distribution.

---

## Technologies Used
* **Language:** Python 3.x
* **Libraries:** Pandas, Matplotlib, Seaborn, Regex (`re`)
* **Tools:** Jupyter Notebook

---

## Documentation & Downloads
* **Full Report:** For an in-depth analysis of the methodology and results, please refer to the [Full Project Report (IT)](./Relazione_Chiara_Mancuso.pdf).
* **Full Package:** To download the complete project folder (including large datasets >100MB and pre-configured folder structures), use the link below:

>  [**Download the full project package from OneDrive**](https://liveunibo-my.sharepoint.com/:u:/g/personal/chiara_mancuso5_studio_unibo_it/EY601zz6Rh9As1x2hhGOyjkBP1mPfg2IObVUNZZElVxjLQ?e=7i1Frx)

---
📫 **Contact:** [chiaramncs@gmail.com](mailto:chiaramncs@gmail.com)
