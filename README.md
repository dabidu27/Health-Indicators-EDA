# Health-Indicators-EDA

Exploratory Data Analysis (EDA) of key health indicators across European Union countries, using data from Eurostat and other sources.

---

## Table of Contents

1. Description
2. Business Requirements & Goals
3. Reports, Dashboards & KPIs
   - Dashboard Example Output
4. Data Design, Tables & Sources
   - 4.1 APIs and Data Sources
   - 4.2 Data Processing Pipeline
   - 4.3 Data Structure
5. Data Governance & Project Administration
6. Graphical User Interface (GUI)
   - GUI Example

---

## 1. Description

This repository demonstrates an end-to-end data analysis solution for public health indicators in the EU. The scenario centers on a data analyst or data scientist tasked with integrating, cleaning, analyzing, and visualizing health, fitness, and nutrition data for policy and research purposes.

The project shows how to:

- Integrate and process data from multiple sources (Eurostat APIs, Excel files).
- Build robust data pipelines for cleaning, validating, and transforming raw data into analytics-ready tables.
- Enforce good data governance and documentation practices.
- Provide interactive visualizations and key performance indicators (KPIs) for health metrics.
- Identify and visualize outliers and highly correlated indicators.

> **Note:**  
> This project is for educational and demonstration purposes only. The data and analyses are intended to showcase best practices in data engineering, analytics, and visualization.

---

## 2. Business Requirements & Goals

### Business Requirements

- Integrate and process health data (life expectancy, healthcare spending, perceived health, vaccination confidence, death rates, smoking, alcohol) from multiple sources.
- Ensure data quality and reproducibility.
- Support analytics and reporting with trusted, well-structured data.

### Core Business Goals

- Provide actionable insights on health indicators and their relationships.
- Demonstrate best practices in data analysis and visualization.
- Enable interactive dashboards and KPIs for key health metrics.

---

## 3. Reports, Dashboards & KPIs

> **Note:**  
> Before generating dashboards, you must first set up your environment and run the main analysis script.

### How to Run

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

### Dashboards and KPIs Included

- **Life Expectancy:** Bar chart by country
- **Daily Smokers vs. Alcohol Consumers:** Grouped bar chart
- **Smokers by Region:** Pie chart
- **Distribution Analysis:** Histograms and boxplots (with outlier annotation) for all numeric indicators
- **Key Relationships:** Scatter plots for selected indicator pairs
- **Correlation Analysis:** Correlation matrix heatmap and list of highly correlated pairs

#### Dashboard Example Output

- All plots are saved in the `plots/` directory for easy review and sharing.

---

## 4. Data Design, Tables & Sources

### 4.1 APIs and Data Sources

- **Eurostat API:** For life expectancy, healthcare spending, perceived health, smoking, and alcohol data.
- **Custom Excel File:** For vaccination confidence and death rates.

### 4.2 Data Processing Pipeline

- **Data Acquisition:** Automated download from APIs and reading from Excel.
- **Data Cleaning:** Handling missing values, renaming columns, and merging datasets.
- **Data Transformation:** Creating analytics-ready tables for visualization and reporting.

### 4.3 Data Structure

- All data is merged into a single DataFrame with the following columns:
	- Geopolitical entity (reporting)
	- Life Expectancy
	- Healthcare Spending (% GDP)
	- Share of People with Good or Very Good Perceived Health
	- Confidence in Vaccination (Percentage of Population)
	- Crude Death Rates (Per 1000 Persons)
	- Daily Smokers (% Population)
	- Daily Alcohol Consumers (% Population)

---

## 5. Data Governance & Project Administration

- **Data Quality:** Missing values are imputed with column means where appropriate.
- **Documentation:** All scripts are commented and the project structure is documented in this README.
- **Reproducibility:** All dependencies are listed in `requirements.txt`.

---

## 6. Graphical User Interface (GUI)

- The project uses Matplotlib and Seaborn for static visualizations.
- All output is graphical and saved as PNG files in the `plots/` directory.

#### GUI Example

- Example output plots include bar charts, pie charts, histograms, boxplots, scatter plots, and heatmaps.

---

## License

This project is licensed under the MIT License.