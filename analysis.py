import pandas as pd
from dataset import create_dataset
import matplotlib.pyplot as plt
import seaborn as sns

dataset = create_dataset()
#print(dataset)


#GRAPHICAL PROJECTION OF THE DATA

#barchart of life expectancy
g = sns.catplot(x = 'Geopolitical entity (reporting)', y = 'Life Expectancy', data = dataset, kind ='bar', height = 8, aspect=1.5)
g.set_xticklabels(rotation = 90)
g.set_axis_labels('Country', 'Life expectancy (years)')

g.fig.subplots_adjust(bottom=0.30, top=0.92)
g.fig.suptitle('Life expectancy by country (2023)')

plt.savefig('plots/life_expectancy.png', dpi = 300)
#plt.show()

#barchart of daily smoking and daily alcohol drinking

df_long = dataset.melt(
    id_vars="Geopolitical entity (reporting)",
    value_vars=["Daily Smokers (% Population)", "Daily Alcohol Consumers (% Population)"],
    var_name="Indicator",
    value_name="Value"
)

#print(df_long)

g = sns.catplot(x = 'Geopolitical entity (reporting)', y = 'Value', hue = 'Indicator', data = df_long, kind = 'bar')
g.set_xticklabels(rotation = 90)

g.fig.subplots_adjust(bottom=0.30, top=0.92)
g.fig.suptitle('Daily Smokers (% Population) VS Daily Alcohol Consumers (% Population) in EU Countries')

plt.savefig('plots/smokers_vs_drinkers', dpi=300)
plt.show()

#piechart of daily smokers by region

#split by regions
# Eastern & Central Europe
eastern_central_eu = [
    "Bulgaria",
    "Czechia",
    "Hungary",
    "Poland",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Croatia",
    "Estonia",
    "Latvia",
    "Lithuania"
]

# Northern Europe
northern_eu = [
    "Denmark",
    "Finland",
    "Sweden",
    "Ireland"
]

# Southern Europe
southern_eu = [
    "Cyprus",
    "Greece",
    "Italy",
    "Malta",
    "Portugal",
    "Spain"
]

# Western Europe
western_eu = [
    "Austria",
    "Belgium",
    "France",
    "Germany",
    "Luxembourg",
    "Netherlands"
]

#print(dataset)

#compute daily smokers by region
smokers_ec_europe = dataset[dataset['Geopolitical entity (reporting)'].isin(eastern_central_eu)]['Daily Smokers (% Population)'].sum()
smokers_n_europe = dataset[dataset['Geopolitical entity (reporting)'].isin(northern_eu)]['Daily Smokers (% Population)'].sum()
smokers_s_europe = dataset[dataset['Geopolitical entity (reporting)'].isin(southern_eu)]['Daily Smokers (% Population)'].sum()
smokers_w_europe = dataset[dataset['Geopolitical entity (reporting)'].isin(western_eu)]['Daily Smokers (% Population)'].sum()

#print(smokers_ec_europe, smokers_n_europe, smokers_s_europe, smokers_w_europe)

pie_chart_values = [smokers_ec_europe, smokers_w_europe, smokers_n_europe, smokers_s_europe]

#create pie chart

sns.set_style('whitegrid')

values = pie_chart_values
labels = ['Eastern and Central Europe', 'Western Europe', 'Northern Europe', 'Southern Europe']

plt.figure(figsize=(10, 10))
plt.pie(values, labels = labels, startangle=90, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title('Daily Smokers (% Population) Split by EU Regions')

plt.savefig('plots/daily_smokers_pie_chart', dpi = 300)
plt.show()

#DISTRIBUTION OF DATA

cols = dataset.select_dtypes(include='number').columns
n_col = 3
n_rows = (len(cols) + n_col - 1) // n_col

fig, axes = plt.subplots(n_rows, n_col, figsize = (15, 5*n_rows))
axes = axes.flatten()

for i, col in enumerate(cols):

    sns.histplot(data = dataset, x = col, kde = True, bins = 5, ax = axes[i])
    axes[i].set_title(f'Distribtion of {col}', fontsize = 10, wrap = True)

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.savefig('plots/histograms', dpi = 300)
plt.show()

#DESCRIPTIVE STATISTICS

for col in dataset.select_dtypes(include = 'number').columns:

    print(col)
    print(dataset[col].describe())
    print('\n')


#SCATTER PLOTS

fig, axes = plt.subplots(1, 2, figsize = (15, 15))

col1 = 'Daily Smokers (% Population)'
col2 = 'Share of People with Good or Very Good Perceived Health'
sns.regplot(data = dataset, x = col1, y = col2, ci = None, line_kws={'color': 'red', 'linestyle': '--'}, ax = axes[0])
axes[0].set_title(f'The Relationship between {col1} and {col2}', fontsize=8, wrap = True)

col1 = 'Share of People with Good or Very Good Perceived Health'
col2 = 'Healthcare Spending (% GDP)'
sns.regplot(data = dataset, x = col1, y = col2, ci = None, line_kws={'color': 'red', 'linestyle': '--'}, ax = axes[1])
axes[1].set_title((f'The Relationship between {col1} and {col2}'), fontsize=8, wrap = True)

plt.savefig('plots/scatter_plots', dpi = 300)
plt.show()

