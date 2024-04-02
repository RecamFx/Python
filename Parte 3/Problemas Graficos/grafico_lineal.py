import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instalar matplotlib y seaborn:
# py -m pip install matplotlib
# py -m pip install seaborn

df = pd.read_csv("Parte 3\\Problemas Graficos\\registro.csv")

# Dice que en x coloque fecha, en y acciones. Donde las busca? en data=DF
sns.lineplot(x="fecha",y="acciones",data=df)

plt.plot("01-07",32,"o") # Creamos un punto en el momento mas alto de acciones

plt.show() # Nos muestra el grafico