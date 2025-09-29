import pandas as pd
from dataset import create_dataset
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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


#BOX PLOTS AND OUTLIERS

cols = dataset.select_dtypes(include = 'number').columns
n_col = 3
n_rows = (len(cols) + n_col - 1) // n_col

fig, axes = plt.subplots(n_rows, n_col, figsize = (15, 5*n_rows))
axes = axes.flatten()


for i, col in enumerate(cols):

    Q1 = dataset[col].quantile(0.25)
    ME = dataset[col].median()
    Q3 = dataset[col].quantile(0.75)

    IQR = Q3 - Q1
    
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR

    sns.boxplot(y = dataset[col], ax = axes[i])
    axes[i].set_title(col)
    axes[i].set_xlabel(col, fontsize=9)
    axes[i].set_ylabel('')
    plt.subplots_adjust(hspace= 0.5, wspace=0.3)
    print(f'{col}: Q1 = {Q1}, ME = {ME}, Q3 = {Q3}, IQR = {IQR}, Lower Fence = {lower_fence}, Upper Fence = {upper_fence}')
    # Annotate outliers
    outliers = dataset['Geopolitical entity (reporting)'][(dataset[col] < lower_fence) | (dataset[col] > upper_fence)]
    for idx, outlier in enumerate(outliers):
        y_val = dataset[col].loc[dataset['Geopolitical entity (reporting)'] == outlier].values[0]
        axes[i].annotate(f'{outlier}',
                        xy=(0, y_val),
                         xytext=(0.05, y_val + idx * 2),
                        textcoords='data',
                        fontsize=8,
                        color='red',
                        arrowprops=dict(arrowstyle='->', color='red', lw=0.8)
                        )
    
for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

plt.savefig('plots/boxplots', dpi = 300)
plt.show()

    
#COVARIANCE AND COEFFICIENT OF CORRELATION

cols = dataset.select_dtypes(include='number')

cov_matrix = cols.cov()
print('Covariance matrix: ')
print(cov_matrix)

print('\n')

corr_matrix = cols.corr()
print('Correlation matrix: ')
print(corr_matrix)

plt.figure(figsize=(20, 15))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.xticks(rotation = 10, fontsize = 5)
plt.yticks(rotation = 10, fontsize = 5)

plt.title("Correlation Matrix Heatmap", fontsize=14)
plt.savefig('plots/correlation_matrix')
plt.show()

threshold = 0.5

high_pos_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_value = corr_matrix.iloc[i, j]
        if corr_value >= threshold:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            high_pos_corr_pairs.append((col1, col2, corr_value))

print("Highly positively correlated pairs (correlation >= {:.2f}):".format(threshold))
for col1, col2, corr_value in high_pos_corr_pairs:
    print(f"{col1} & {col2}: correlation = {corr_value:.2f}")

threshold = -0.5
high_neg_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        corr_value = corr_matrix.iloc[i, j]
        if corr_value <= threshold:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            high_neg_corr_pairs.append((col1, col2, corr_value))

print('\n')
print("Highly negatively correlated pairs (correlation >= {:.2f}):".format(threshold))
for col1, col2, corr_value in high_neg_corr_pairs:
    print(f"{col1} & {col2}: correlation = {corr_value:.2f}")