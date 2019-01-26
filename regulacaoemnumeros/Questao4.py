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
result_3a.plot.bar(ax=axes[0,0], title='4a. Decisoes normativas por agencia', fontsize=10)


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
result_4b.plot.bar(ax=axes[0, 1], title='4b. Decisoes normativas por ano', fontsize=10)


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
result_4c.plot.bar(ax=large_left_ax, title='4c. Decisoes normativas por relator', fontsize=10)



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
result_4d.plot.bar(ax=axes[2,0], title='4d. Decisoes normativas por unidade tecnica', fontsize=10)


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
result_4e.plot.bar(ax=axes[2,1], title='4e. Decisoes normativas por unidade tecnica agir', fontsize=10)


plt.show()
