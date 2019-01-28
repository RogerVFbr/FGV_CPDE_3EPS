import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros
df['Exercicio_Apurado'] = df['Exercicio_Apurado'].apply(lambda x: int(x))

sns.set()
fig, axes = plt.subplots(nrows=3, ncols=3 , figsize=(10,10))
plt.subplots_adjust(hspace=0.7)
fig.suptitle('Questão 1 - Relação entre quantidade de processos e:', weight='bold')


# ===============================================================================================================
#                                                  QUESTAO 1a
# ===============================================================================================================

s_1a = df['AgenciaInt'].value_counts().sort_index() # Criar Serie com total de processos
s_1a = pd.Series(s_1a.index.values, index=s_1a) # Inverter indice com valores
s_1a = s_1a.apply(roman.toRoman) # Aplicar funcao conversora
s_1a = pd.Series(s_1a.index.values, index=s_1a) # Reinverter para manter numerais como indice
s_1a.plot(kind='bar', ax=axes[0,0], title='a. Agência', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 1b
# ===============================================================================================================

s_1b = df['Exercicio_Apurado'].value_counts().sort_index() # Criar Serie com total de processos
s_1b.plot(kind='bar', ax=axes[0,1], title='b. Ano', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 1c
# ===============================================================================================================

agencias = list(s_1a.index)
anos = list(s_1b.index)
d = {}
for x in agencias:
    d[x] = [] # Uma chave para cada agencia contendo uma lista de totais de processo por ano
    for y in anos:
        df_1c = df[
            (df['Exercicio_Apurado'] == y) &
            (df['Agencia'] == x)]
        d[x].append(df_1c.shape[0]) #
d = pd.DataFrame(d)
d.index = anos
large_left_ax = plt.subplot2grid((3,3), (1,0), colspan=2, rowspan=2)
d.plot(ax=large_left_ax, title='c. Agência / Ano', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 1d
# ===============================================================================================================

s_1d = df['Relator'].value_counts().sort_index() # Criar Serie com total de processos
s_1d.plot(kind='bar', ax=axes[0,2], title='d. Relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 1e
# ===============================================================================================================

s_1e = df['Quantidade_Relatores'].value_counts().sort_index() # Criar Serie com total de processos
s_1e = pd.Series(s_1e.index.values, index=s_1e) # Inverter indice com valores
s_1e = s_1e.apply(int) # Aplicar funcao conversora
s_1e = pd.Series(s_1e.index.values, index=s_1e) # Reinverter para manter numerais como indice
s_1e.plot(kind='bar', ax=axes[1,2], title='e. Quantidade de relatores', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 1f
# ===============================================================================================================

s_1d = df['Unidade_Tecnica_Por_Agir'].value_counts().sort_index() # Criar Serie com total de processos
s_1d.plot(kind='bar', ax=axes[2,2], title='f. Unidade técnica', fontsize=10)

yint = []
locs, labels = plt.yticks()
for each in locs:
    yint.append(int(each))
plt.yticks(yint)

xint = [x for x in range(1997, 2016, 2)]
plt.xticks([value for idx, value in enumerate(anos) if idx%2 == 0])

plt.show()
