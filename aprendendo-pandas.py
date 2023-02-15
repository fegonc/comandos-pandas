import pandas as pd

# venda = {
#     "data": ['15/02/203', '16/02/2023'],
#     "produto": [500,300],
#     "qtde": [50,70]
# }

vendas_df = pd.read_excel("arquivos/Vendas.xlsx")

# print(vendas_df.head())
# print(vendas_df.shape)
# print(vendas_df.describe())

# produtos = vendas_df[['Produto', 'ID Loja']]
# print(produtos.head())


#OBTER LINHAS QUE CORRESPONDEM A UMA CONDIÇÃO
condicao_df = vendas_df['ID Loja'] == 'Norte Shopping'
# print(vendas_df.loc[condicao_df].head(10))


#OBTER BARIAS LINHAS E COLUNAS USANDO LOC
#vendas_df.loc[linhas,colunas]
vendas_norte_shopping = vendas_df.loc[condicao_df, ['ID Loja', 'Produto', 'Data']]
# print(vendas_norte_shopping)

#OBTER UMA LINHA EM ESPECIFICO, LEMBRANDO QUE NO LOC FUNCIONA LINHA E COLUNAS
# print(vendas_df.loc[1,'Produto'])

#CRIAR COLUNA A PARTIR DE UMA QUE JA EXISTE
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
# print(vendas_df.head())

#CRIAR UMA COLUNA PADRAO COM VALOR PADRÃO
vendas_df.loc[:, "Imposto"] = 0
# print(vendas_df)



vendas_dez_df = pd.read_excel("arquivos/Vendas - Dez.xlsx")
# print(vendas_dez_df)

#UNINDO DOIS DATAFRAMES(TABELAS)
# vendas_df = vendas_df.append(vendas_dez_df)
# print(vendas_df)

#DELETAR UMA COLUNA
# vendas_df = vendas_df.drop("Imposto", axis=1)

vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05
vendas_df = vendas_df.append(vendas_dez_df)


#DELETAR LINHAS E COLUNAS COMPLETEMENTE VAZIAS
# vendas_df = vendas_df.dropna(how='all', axis=1)

#DELETAR LINHAS QUE POSSUEM PELO MENOS 1 VALOR VAZIO
# vendas_df = vendas_df.dropna()

#PREENCHER VALORES VAZIOS
#PREENCHER COM A MÉDIA DA COLUNA
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
# print(vendas_df)


#PREENCHER COM O ULTIMO VALOR
vendas_df = vendas_df.ffill()


#VALUE COUNTS
transacoes_loja = vendas_df['ID Loja'].value_counts()
# print(transacoes_loja)

#GROUP BY
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').mean()
# print(faturamento_produto)

#MERGE (PROCURAR INFORMAÇÕES DE UMA TABELA EM OUTRA)
gerentes_df = pd.read_excel('arquivos/Gerentes.xlsx')
vendas_df = vendas_df.merge(gerentes_df)
print(vendas_df)