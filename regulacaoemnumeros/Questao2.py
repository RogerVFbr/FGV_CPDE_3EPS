import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

exclude = ['N/D', 'N/A']
df = df[~df['Data_Encerramento'].isin(exclude)]

df['Duracao'] = pd.to_numeric(df['Data_Encerramento']) -  pd.to_numeric(df['Data_Autuacao'])

g = df.groupby(['AgenciaInt']).mean()
s = g['Duracao']
s = pd.Series(s.index.values, index=s) # Inverter indice com valores
s = s.apply(roman.toRoman) # Aplicar funcao conversora
s = pd.Series(s.index.values, index=s) # Reinverter para manter numerais como indice
s = s.append(pd.Series([s.mean()], index=['Geral']))

sns.set()
s.plot(kind='bar', title='Questão 2 - Média de duração por agência e total', fontsize=10)
plt.show()
