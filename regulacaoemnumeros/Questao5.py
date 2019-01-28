import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

sns.set()
grid = (2,4)
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(10,10))
plt.subplots_adjust(hspace=0.4)
fig.suptitle('Questão 5 - Relação entre quantidade de deliberações e:', weight='bold')


# ===============================================================================================================
#                                                  QUESTAO 5a
# ===============================================================================================================

result_5a = df.groupby('AgenciaInt')['deliberacoes_quantidade'].sum()
result_5a = pd.Series(result_5a.index.values, index=result_5a) # Inverter indice com valores
result_5a = result_5a.apply(roman.toRoman) # Aplicar funcao conversora
result_5a = pd.Series(result_5a.index.values, index=result_5a) # Reinverter para manter numerais como indice
ax_5a = plt.subplot2grid(grid, (0,0), colspan=2, rowspan=1)
result_5a.plot.bar(ax=ax_5a, title='a. Agência', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5b
# ===============================================================================================================

result_5b = df.groupby('Exercicio_Apurado')['deliberacoes_quantidade'].sum()
result_5b = pd.Series(result_5b.index.values, index=result_5b) # Inverter indice com valores
result_5b = result_5b.apply(int) # Aplicar funcao conversora
result_5b = pd.Series(result_5b.index.values, index=result_5b) # Reinverter para manter numerais como indice
title_5b = 'b. Ano (Total: {})'.format(result_5b.sum())
ax_5b = plt.subplot2grid(grid, (0,2), colspan=2, rowspan=1)
result_5b.plot.bar(ax=ax_5b, title=title_5b, fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5c
# ===============================================================================================================

result_5c = df.groupby('Relator')['deliberacoes_quantidade'].sum()
result_5c.index.name = ''
ax_5c = plt.subplot2grid(grid, (1,0), colspan=2, rowspan=1)
result_5c.plot.bar(ax=ax_5c, title='c. Relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5d
# ===============================================================================================================

result_5d = df.groupby('Unidade_Tecnica_Responsavel')['deliberacoes_quantidade'].sum()
result_5d.index.name = ''
ax_5d = plt.subplot2grid(grid, (1,2), colspan=1, rowspan=1)
result_5d.plot.bar(ax=ax_5d, title='d. Unidade técnica', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5e
# ===============================================================================================================

result_5e = df.groupby('Unidade_Tecnica_Por_Agir')['deliberacoes_quantidade'].sum()
result_5e.index.name = ''
ax_5e = plt.subplot2grid(grid, (1,3), colspan=1, rowspan=1)
result_5e.plot.bar(ax=ax_5e, title='e. Unidade técnica agir', fontsize=10)


plt.show()
