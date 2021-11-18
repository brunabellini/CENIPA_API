# CENIPA API

## Descrição
O CENIPA API é um framework que auxilia o entendimento sobre acidentes aéreos no Brasil com auxílio de sua base de dados pública. Facilitando, assim, o seu acesso e uso.

## Como usar

    (Inserir aqui o pip)
    
## Importar a biblioteca

    (Comando)

## Documentação

## Funções
### Legenda para variáveis: col= coluna que deseja utilizar, nome_UF= nome da sigla do estado que deseja utilizar

`get_table()` - Retornar e mostrar o Dataset dentro do terminal
`get_acidente()` - Retornar um dataset com as colunas relevantes para analise sobre os acidentes
`get_fator_contribuinte()` - Retornar um dataset com os fatores contribuintes para o acidente
`get_aeronave()` - Retornar um dataset para a analise das fatores das aeronaves
`get_recomendacao()` - Retornar um dataset para a analise das recomendações do casos 
`moda_coluna(col)` - Retornar o valor mais recorrente em uma coluna escolhida do dataset
`mediana_coluna(col)` - Retornar a mediana de uma coluna escolhida do dataset
`media_coluna(col)` - Retornar a média de uma coluna escolhida do dataset
`variancia_coluna(col)` - Retornar a variancia de uma coluna escolhida do dataset
`desvio_padrao_coluna(col)` - Retornar o desvio padrão de uma coluna escolhida do dataset
`gravidade_acidentes()` - Gerar o número de mortes totais e alguns gráficos com insights sobrer nível de dano, fatalidade e classificação da ocorrência
`tipos_mortes_aeronaves()` - Retornar os tipos de aeronaves e a porcentagem de ocorrencias fatais nas aeronaves listadas com ocorrências
`top_fatores_contribuintes()` - Retornar os top fatores contribuintes
`ocorrencia_tipo()` - Visualizar quais são as ocorrências mais frequentes
`ocorrencia_estados(nome_UF)` - Filtrar ocorrências pela sigla dos estados
`ocorrencia_cidade(nome_cidade)` - Filtrar ocorrências pelo nome de cidades
`informacoes_acidentes()` - Retornar informações sobre a gravidade e detalhes de fatalidade do acidente
`ocorrencia_MesHora()` - Apresentar os meses e horários que mais existem ocorrências
`ocorrencia_ano(ano)` - Apresentar as informações de acordo com o ano selecionado