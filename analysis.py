import pandas as pd
from dataset import create_dataset
import matplotlib.pyplot as plt
import seaborn as sns

dataset = create_dataset()
#print(dataset)


#GRAPHICAL PROJECTION OF THE DATA

#barchart of life expectancy
g = sns.catplot(x = 'Geopolitical entity (reporting)', y = 'Life Expectancy', data = dataset, kind ='bar')
g.set_xticklabels(rotation = 90)
g.set_axis_labels('Country', 'Life expectancy (years)')
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

print(df_long)

g = sns.catplot(x = 'Geopolitical entity (reporting)', y = 'Value', hue = 'Indicator', data = df_long, kind = 'bar')
g.set_xticklabels(rotation = 90)
g.fig.suptitle('Daily Smokers (% Population) VS Daily Alcohol Consumers (% Population) in EU Countries')

plt.savefig('plots/smokers_vs_drinkers', dpi=300)
plt.show()

#piechart of daily smokers by region

