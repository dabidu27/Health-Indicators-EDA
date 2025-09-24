import pandas as pd
import requests
from pyjstat import pyjstat
import json

def create_dataset():
    eu_countries = [
        "Austria",
        "Belgium",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czechia",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Ireland",
        "Italy",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Netherlands",
        "Poland",
        "Portugal",
        "Romania",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden"
    ]
    base_url = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data'

    #LIFE EXPECTANCY

    life_expectancy_dataset = 'demo_mlexpec'

    params = {'time': '2023', 'sex': 'M'}

    resp = requests.get(f"{base_url}/{life_expectancy_dataset}", params=params)
    data = resp.json()

    ds = pyjstat.from_json_stat(data)
    life_expectancy = pd.DataFrame(ds[0]) 

    life_expectancy= life_expectancy.loc[life_expectancy['Age class'] == 'Less than 1 year']
    life_expectancy = life_expectancy.loc[life_expectancy['Geopolitical entity (reporting)'].isin(eu_countries), ['Geopolitical entity (reporting)', 'value']]
    life_expectancy = life_expectancy.sort_values('Geopolitical entity (reporting)').reset_index(drop = True)
    #print(life_expectancy)

    #HEALTH SPENDING

    health_spending_dataset = 'tps00207'

    params = {'unit': 'PC_GDP', 'time': '2023'}
    resp = requests.get(f"{base_url}/{health_spending_dataset}", params=params)
    data = resp.json()

    ds = pyjstat.from_json_stat(data)
    health_spending = pd.DataFrame(ds[0])

    health_spending = health_spending.loc[health_spending['Geopolitical entity (reporting)'].isin(eu_countries), ['Geopolitical entity (reporting)', 'value']]
    health_spending = health_spending.sort_values('Geopolitical entity (reporting)').reset_index(drop = True)
    #print(health_spending)

    #PERCEIVED HEALTH STATUS

    health_status_dataset = 'sdg_03_20'

    params = {'time': '2023', 'sex': 'T'}
    resp = requests.get(f'{base_url}/{health_status_dataset}', params=params)
    data = resp.json()

    ds = pyjstat.from_json_stat(data)
    health_status = pd.DataFrame(ds[0])

    health_status = health_status.loc[health_status['Geopolitical entity (reporting)'].isin(eu_countries), ['Geopolitical entity (reporting)', 'value']]
    health_status = health_status.sort_values('Geopolitical entity (reporting)').reset_index(drop=True)
    #print(health_status)


    #CONFIDENCE IN VACCINATION

    df = pd.read_excel(r"C:\Users\David\Desktop\utile\facultate\semestrul 1\statistica\1037_Adamita_David-Stefan_Cipariu_Mihnea_Adrian_David_Robert_Luca\1037_Adamita_David-Stefan_Cipariu_Mihnea_Adrian_David_Robert_Luca.xlsx", sheet_name='Data')
    vaccination_confidence = df[['country', 'confidence in vaccination (percentage of population)']]
    vaccination_confidence = vaccination_confidence.rename(columns={'country': 'Geopolitical entity (reporting)', 'confidence in vaccination (percentage of population)': 'Confidence in Vaccination (Percentage of Population)'})
    #print(vaccination_confidence)


    #DEATH RATES

    df = pd.read_excel(r"C:\Users\David\Desktop\utile\facultate\semestrul 1\statistica\1037_Adamita_David-Stefan_Cipariu_Mihnea_Adrian_David_Robert_Luca\1037_Adamita_David-Stefan_Cipariu_Mihnea_Adrian_David_Robert_Luca.xlsx", sheet_name='Data')
    death_rates = df[['country', 'crude death rates(per 1000 persons)']]
    death_rates = death_rates.rename(columns={'country': 'Geopolitical entity (reporting)', 'crude death rates(per 1000 persons)': 'Crude Death Rates (Per 1000 Persons)'})
    #print(death_rates)

    #DAILY SMOKING

    smoking_dataset = 'hlth_ehis_sk1e'

    params = {'isced11': 'TOTAL', 'age': 'TOTAL', 'sex': 'T', 'smoking': 'SM_DAY', 'time': '2019', 'unit': 'PC'}
    resp = requests.get(f'{base_url}/{smoking_dataset}', params=params)
    data = resp.json()

    ds = pyjstat.from_json_stat(data)
    smoking = pd.DataFrame(ds[0])

    smoking = smoking.loc[smoking['Geopolitical entity (reporting)'].isin(eu_countries), ['Geopolitical entity (reporting)', 'value']]
    smoking = smoking.sort_values('Geopolitical entity (reporting)').reset_index(drop = True)

    #print(smoking)


    #DAILY DRINKING

    drinking_dataset = 'hlth_ehis_al1e'

    params = {'age': 'TOTAL', 'frequenc': 'DAY', 'isced11': 'TOTAL', 'sex': 'T', 'time': '2019'}
    resp = requests.get(f'{base_url}/{drinking_dataset}', params=params)
    data = resp.json()

    ds = pyjstat.from_json_stat(data)
    drinking = pd.DataFrame(ds[0])

    drinking = drinking.loc[drinking['Geopolitical entity (reporting)'].isin(eu_countries), ['Geopolitical entity (reporting)', 'value']]
    drinking = drinking.sort_values('Geopolitical entity (reporting)').reset_index(drop = True)

    #print(drinking)

    #RENAMING COLUMNS

    life_expectancy = life_expectancy.rename(columns={"value": "Life Expectancy"})
    health_spending = health_spending.rename(columns={"value": "Healthcare Spending (% GDP)"})
    death_rates = death_rates.rename(columns={"value": "Crude Death Rates/1000 Persons"})
    health_status = health_status.rename(columns={'value': 'Share of People with Good or Very Good Perceived Health'})
    vaccination_confidence = vaccination_confidence.rename(columns = {'value': 'Confidence in Vaccination (% Population)'})
    smoking = smoking.rename(columns={'value': 'Daily Smokers (% Population)'})
    drinking = drinking.rename(columns={'value': 'Daily Alcohol Consumers (% Population)'})

    #MERGING

    data = life_expectancy.merge(health_spending, on = 'Geopolitical entity (reporting)')

    datasets = [health_status, vaccination_confidence, death_rates, smoking, drinking]
    for dataset in datasets:

        data = data.merge(dataset, on = 'Geopolitical entity (reporting)')

    #print(data)

    #CLEANING DATASET

    #print(data.isna().sum())


    #print(data.loc[data['Healthcare Spending (% GDP)'].isna(), 
    #              ['Geopolitical entity (reporting)', 'Healthcare Spending (% GDP)']])
    mean_healthcare_spening = data['Healthcare Spending (% GDP)'].mean()
    data['Healthcare Spending (% GDP)'] = data['Healthcare Spending (% GDP)'].fillna(mean_healthcare_spening)

    mean_drinking = data['Daily Alcohol Consumers (% Population)'].mean()
    data['Daily Alcohol Consumers (% Population)'] = data['Daily Alcohol Consumers (% Population)'].fillna(mean_drinking)

    #print(data.isna().sum()) 

    return data