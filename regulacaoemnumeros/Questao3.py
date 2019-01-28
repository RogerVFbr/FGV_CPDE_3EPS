import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

sns.set()
fig, axes = plt.subplots(nrows=2, ncols=3 , figsize=(10,10))
plt.subplots_adjust(hspace=0.5)
fig.suptitle('Questão 3 - Relação entre quantidade de responsáveis e:', weight='bold')



# ===============================================================================================================
#                                                  QUESTAO 3a
# ===============================================================================================================

agencias = list(df['AgenciaInt'].unique())
agencias = sorted(agencias)

d_3a={}

for x in agencias:
    main_index = roman.toRoman(int(x))
    d_3a[main_index] = []
    for index, row in df.iterrows():
        if row['AgenciaInt'] == x:
            d_3a[main_index].append(row['quant_responsaveis'])

result_3a = pd.DataFrame.from_dict(d_3a, orient='index')
large_left_ax = plt.subplot2grid((2,3), (0,0), colspan=2, rowspan=1)
result_3a.plot.bar(legend=False, ax=large_left_ax, title='a. Agência / Processo', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3b
# ===============================================================================================================

result_3b = df.groupby('Exercicio_Apurado')['quant_responsaveis'].sum()
result_3b.index.name = ''
result_3b = pd.Series(result_3b.index.values, index=result_3b) # Inverter indice com valores
result_3b = result_3b.apply(int) # Aplicar funcao conversora
result_3b = pd.Series(result_3b.index.values, index=result_3b) # Reinverter para manter numerais como indice
title = 'b. Ano (Total: {})'.format(result_3b.sum())
result_3b.plot.bar(legend=False, ax=axes[0,2], title=title, fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3c
# ===============================================================================================================

result_3c = df.groupby('Relator')['quant_responsaveis'].sum()
result_3c.index.name = ''
result_3c.plot.bar(legend=False, ax=axes[1,0], title='c. Relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3d
# ===============================================================================================================

result_3d = df.groupby('Unidade_Tecnica_Responsavel')['quant_responsaveis'].sum()
result_3d.index.name = ''
result_3d.plot.bar(legend=False, ax=axes[1,1], title='d. Unidade técnica', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3e
# ===============================================================================================================

result_3e = df.groupby('Unidade_Tecnica_Por_Agir')['quant_responsaveis'].sum()
result_3e.index.name = ''
result_3e.plot.bar(legend=False, ax=axes[1,2], title='e. Unidade técnica agir', fontsize=10)


plt.show()
