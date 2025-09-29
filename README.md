# Health-Indicators-EDA

## Table of Contents

1. Description  
2. Features  
3. Data Design  
4. Tables  
5. Sources  
6. How to Run  

---

## 1. Description

This repository demonstrates an end-to-end data analysis solution for public health indicators in the EU. The scenario centers on a data analyst or data scientist tasked with integrating, cleaning, analyzing, and visualizing health, fitness, and nutrition data for policy and research purposes.

> **Note:**  
> This project is for educational and demonstration purposes only. The data and analyses are intended to showcase best practices in data engineering, analytics, and visualization.

---

## 2. Features

- Automated data download and merging from Eurostat APIs and Excel sources
- Analysis of life expectancy, healthcare spending, perceived health, vaccination confidence, death rates, smoking, and alcohol consumption
- Visualizations: bar charts, pie charts, histograms, boxplots (with outlier annotation), scatter plots, and correlation heatmaps
- Identification of highly correlated health indicators

---

## 3. Data Design

- Data acquisition: Automated download from APIs and reading from Excel.
- Data cleaning: Handling missing values, renaming columns, and merging datasets.
- Data transformation: Creating analytics-ready tables for visualization and reporting.

All data is merged into a single DataFrame with the following columns:
- Geopolitical entity (reporting)
- Life Expectancy
- Healthcare Spending (% GDP)
- Share of People with Good or Very Good Perceived Health
- Confidence in Vaccination (Percentage of Population)
- Crude Death Rates (Per 1000 Persons)
- Daily Smokers (% Population)
- Daily Alcohol Consumers (% Population)

---

## 4. Tables

| Column Name                                         | Description                                      |
|-----------------------------------------------------|--------------------------------------------------|
| Geopolitical entity (reporting)                     | Country/region name                              |
| Life Expectancy                                    | Life expectancy at birth (years)                 |
| Healthcare Spending (% GDP)                        | Health spending as % of GDP                      |
| Share of People with Good or Very Good Perceived Health | % of people reporting good/very good health |
| Confidence in Vaccination (Percentage of Population)| % confident in vaccination                       |
| Crude Death Rates (Per 1000 Persons)               | Deaths per 1000 persons                          |
| Daily Smokers (% Population)                       | % of daily smokers                               |
| Daily Alcohol Consumers (% Population)             | % of daily alcohol consumers                     |

---

## 5. Sources

- [Eurostat](https://ec.europa.eu/eurostat) (API)
- Custom Excel file for vaccination confidence and death rates

---

## 6. How to Run

1. Set up a `.env` file with the path to your Excel data:
    ```
    excel_path=path/to/your/data.xlsx
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the main analysis script:
    ```bash
    python analysis.py
    ```
4. Output plots will be saved in the `plots/` directory.

---

## License

This project is licensed under the MIT License.
