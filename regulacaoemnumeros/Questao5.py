import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

sns.set()
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10,10))
plt.subplots_adjust(hspace=0.7)


# ===============================================================================================================
#                                                  QUESTAO 5a
# ===============================================================================================================

result_5a = df.groupby('AgenciaInt')['deliberacoes_quantidade'].sum()
result_5a = pd.Series(result_5a.index.values, index=result_5a) # Inverter indice com valores
result_5a = result_5a.apply(roman.toRoman) # Aplicar funcao conversora
result_5a = pd.Series(result_5a.index.values, index=result_5a) # Reinverter para manter numerais como indice
result_5a.plot.bar(ax=axes[0,0], title='5a. Deliberacoes por agencia', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5b
# ===============================================================================================================

result_5b = df.groupby('Exercicio_Apurado')['deliberacoes_quantidade'].sum()
result_5b = pd.Series(result_5b.index.values, index=result_5b) # Inverter indice com valores
result_5b = result_5b.apply(int) # Aplicar funcao conversora
result_5b = pd.Series(result_5b.index.values, index=result_5b) # Reinverter para manter numerais como indice
title_5b = '5b. Deliberacoes por ano (Total: {})'.format(result_5b.sum())
result_5b.plot.bar(ax=axes[0,1], title=title_5b, fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5c
# ===============================================================================================================

result_5c = df.groupby('Relator')['deliberacoes_quantidade'].sum()
result_5c.index.name = ''
large_left_ax = plt.subplot2grid((3,2), (1,0), colspan=2, rowspan=1)
result_5c.plot.bar(ax=large_left_ax, title='5c. Deliberacoes por relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5d
# ===============================================================================================================

result_5d = df.groupby('Unidade_Tecnica_Responsavel')['deliberacoes_quantidade'].sum()
result_5d.index.name = ''
result_5d.plot.bar(ax=axes[2,0], title='5d. Deliberacoes por UT responsavel', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5e
# ===============================================================================================================

result_5e = df.groupby('Unidade_Tecnica_Por_Agir')['deliberacoes_quantidade'].sum()
result_5e.index.name = ''
result_5e.plot.bar(ax=axes[2,1], title='5e. Deliberacoes por UT responsavel agir', fontsize=10)


plt.show()
