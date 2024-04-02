import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instalar matplotlib y seaborn:
# py -m pip install matplotlib
# py -m pip install seaborn

df = pd.read_csv("Parte 3\\Problemas Graficos\\dispersion.csv")

# Dice que en x coloque tiempo, en y el dinero. Donde las busca? en data=DF
sns.scatterplot(x="tiempo",y="dinero",data=df)

plt.show() # Nos muestra el grafico