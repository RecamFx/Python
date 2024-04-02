import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instalar matplotlib y seaborn:
# py -m pip install matplotlib
# py -m pip install seaborn

df = pd.read_csv("Parte 3\\Problemas Graficos\\ingresos.csv")

# Dice que en x coloque fuentes, en y los ingresos. Donde las busca? en data=DF
sns.barplot(x="fuente",y="ingresos",data=df)

# Total de cuanto gana:
total_ingresos = df["ingresos"].sum()
print(total_ingresos) #? 4900


plt.show() # Nos muestra el grafico