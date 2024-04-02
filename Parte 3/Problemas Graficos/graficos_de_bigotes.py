import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instalar matplotlib y seaborn:
# py -m pip install matplotlib
# py -m pip install seaborn

df = pd.read_csv("Parte 3\\Problemas Graficos\\bigotes.csv")

# Dice que en x coloque tiempo, en y el dinero. Donde las busca? en data=DF
sns.boxenplot(x="categoria",y="valor",data=df)

plt.show() # Nos muestra el grafico