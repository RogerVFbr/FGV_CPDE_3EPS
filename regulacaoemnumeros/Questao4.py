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
fig.suptitle('Questão 4 - Relação entre decisão normativa e:', weight='bold')



# ===============================================================================================================
#                                                  QUESTAO 4a
# ===============================================================================================================

agencias = list(df['AgenciaInt'].unique())
agencias = sorted(agencias)

d_4a={}

for x in agencias:
    main_index = roman.toRoman(int(x))
    d_4a[main_index] = {'OK':0, 'N/D':0}
    for index, row in df.iterrows():
        if row['AgenciaInt'] == x:
            if row['decisao_normativa'] == 'N/D':
                d_4a[main_index]['N/D'] += 1
            else:
                d_4a[main_index]['OK'] += 1

result_3a = pd.DataFrame.from_dict(d_4a, orient='index')
ax_4a = result_3a.plot.bar(ax=axes[0,0], title='a. Agência', fontsize=10)

for x in ax_4a.patches:
    ax_4a.annotate(str(x.get_height()), (x.get_x()*1.005 + x.get_width()/2,
                                                          x.get_height()*1.005), fontsize=6, ha='center')


# ===============================================================================================================
#                                                  QUESTAO 4b
# ===============================================================================================================

anos = list(df['Exercicio_Apurado'].unique())
anos = sorted([int(x) for x in anos])

d_4b={}

for x in anos:
    d_4b[x] = {'OK':0, 'N/D':0}
    for index, row in df.iterrows():
        if row['Exercicio_Apurado'] == x:
            if row['decisao_normativa'] == 'N/D':
                d_4b[x]['N/D'] += 1
            else:
                d_4b[x]['OK'] += 1

result_4b = pd.DataFrame.from_dict(d_4b, orient='index')
ax_4b = result_4b.plot.bar(ax=axes[0, 1], title='b. Ano', fontsize=10)

for x in ax_4b.patches:
    ax_4b.annotate(str(x.get_height()), (x.get_x()*1.005 + x.get_width()/2,
                                                          x.get_height()*1.005), fontsize=6, ha='center')


# ===============================================================================================================
#                                                  QUESTAO 4c
# ===============================================================================================================

relatores = list(df['Relator'].unique())
relatores = sorted(relatores)

d_4c={}

for x in relatores:
    d_4c[x] = {'OK':0, 'N/D':0}
    for index, row in df.iterrows():
        if row['Relator'] == x:
            if row['decisao_normativa'] == 'N/D':
                d_4c[x]['N/D'] += 1
            else:
                d_4c[x]['OK'] += 1

result_4c = pd.DataFrame.from_dict(d_4c, orient='index')
large_left_ax = plt.subplot2grid((3,2), (1,0), colspan=2, rowspan=1)
ax_4c = result_4c.plot.bar(ax=large_left_ax, title='c. Relator', fontsize=10)


for x in ax_4c.patches:
    ax_4c.annotate(str(x.get_height()), (x.get_x()*1.005 + x.get_width()/2,
                                                          x.get_height()*1.005), fontsize=6, ha='center')


# ===============================================================================================================
#                                                  QUESTAO 4d
# ===============================================================================================================

unidades = list(df['Unidade_Tecnica_Responsavel'].unique())
unidades = sorted(unidades)

d_4d={}

for x in unidades:
    d_4d[x] = {'OK':0, 'N/D':0}
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Responsavel'] == x:
            if row['decisao_normativa'] == 'N/D':
                d_4d[x]['N/D'] += 1
            else:
                d_4d[x]['OK'] += 1

result_4d = pd.DataFrame.from_dict(d_4d, orient='index')
ax_4d = result_4d.plot.bar(ax=axes[2,0], title='d. Unidade técnica', fontsize=10)

for x in ax_4d.patches:
    ax_4d.annotate(str(x.get_height()), (x.get_x()*1.005 + x.get_width()/2,
                                                          x.get_height()*1.005), fontsize=6, ha='center')


# ===============================================================================================================
#                                                  QUESTAO 4e
# ===============================================================================================================

agir = list(df['Unidade_Tecnica_Por_Agir'].unique())
agir = sorted(agir)

d_4e={}

for x in agir:
    d_4e[x] = {'OK':0, 'N/D':0}
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Por_Agir'] == x:
            if row['decisao_normativa'] == 'N/D':
                d_4e[x]['N/D'] += 1
            else:
                d_4e[x]['OK'] += 1

result_4e = pd.DataFrame.from_dict(d_4e, orient='index')
ax_4e = result_4e.plot.bar(ax=axes[2,1], title='e. Unidade técnica agir', fontsize=10)

for x in ax_4e.patches:
    ax_4e.annotate(str(x.get_height()), (x.get_x()*1.005 + x.get_width()/2,
                                                          x.get_height()*1.005), fontsize=6, ha='center')


plt.show()
