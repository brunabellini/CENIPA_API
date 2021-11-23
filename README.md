<h2>CENIPA API</h2>
<p>O CENIPA API é um framework que auxilia o entendimento sobre acidentes aéreos no Brasil com auxílio de sua base de dados pública. Facilitando, assim, o seu acesso e uso.</p>

<h4><a href="#about">Autores</a> | <a href="#introduction">Introdução</a> | <a href="#instruction">Instruções de uso</a> | <a href="#reference">Referência</a> | <a href="#functions">Funções disponíveis</a> |</h4>


<h2 id="about">Autores</h2>

<br />

<p><b>Turma da graduação de Ciência de Dados e Inteligência Artificial na PUC-SP<b/></p>

<br />

<p>Abdul Malik de Barros</p> 	
<p>Ana Beatriz Oliveira de Macedo</p> 
<p>Bruna Bellini Faria</p> 
<p>Heloisa Mariani Rodrigues</p>  

<br />

<h2 id="introduction">Introdução </h2>


<p>
	<p>Diante da fatalidade que ocorreu no dia 5 de novembro, que ocasionou na morte da cantora Marília Mendonça e mais 4 pessoas, nosso grupo iniciou uma pesquisa sobre acidentes aéreos, identificamos uma base de dados de ocorrências aeronáuticas, que é gerenciada pelo Centro de Investigação e Prevenção de Acidentes Aeronáuticos (CENIPA).  Constam nesta base de dados as ocorrências aeronáuticas notificadas ao CENIPA nos últimos 10 anos e que ocorreram em solo brasileiro. O relatório conta com detalhes sobre os acidentes, fatalidades, características das aeronaves, causas e fatores contribuintes, local, data, horário do evento e recomendações. A partir disso, compilamos os dados sobre as ocorrências e trouxemos algumas análises sobre o que obtemos, com gráficos, estatísticas e Dataframes. Permitindo uma ampla visualização, a compreensão mais abrangente dos fatos ocorridos e a obtenção de conclusões. </p>
	
</p>

<br />

<h2 id="instruction">Instruções de uso</h2>

<strong>Bibliotecas necessárias</strong>

    pandas
    matplotlib
    re
    numpy

<br />

<strong>Instalando esta API</strong>

    pip install CENIPA_API

<h2>Resultados</h2>

Abaixo você encontra o link do repositório com todos os códigos e dados até então coletados para a evolução do projeto e análise de dados para o desenvolvimento da página de visualização.

<ul>
	<li>https://github.com/brunabellini/CENIPA_API</li>
</ul>
<br />
	
<h2 id="functions">Funções disponíveis</h2>

| Nome da função:                | O que ela executa:                                                                                                   |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------- |
|`get_table()`| Retornar e mostrar o Dataset dentro do terminal                                                                                         |
|`get_acidente()`| Retornar um dataset com as colunas relevantes para analise sobre os acidentes                                                        |
|`get_fator_contribuinte()`| Retornar um dataset com os fatores contribuintes para o acidente                                                           |
|`get_aeronave()`| Retornar um dataset para a analise das fatores das aeronaves                                                                         |
|`get_recomendacao()`| Retornar um dataset para a analise das recomendações do casos                                                                    |
|`moda_coluna(col)`| Retornar o valor mais recorrente em uma coluna escolhida do dataset                                                                |
|`mediana_coluna(col)`| Retornar a mediana de uma coluna escolhida do dataset                                                                           |
|`media_coluna(col)`| Retornar a média de uma coluna escolhida do dataset                                                                               |
|`variancia_coluna(col)`| Retornar a variancia de uma coluna escolhida do dataset                                                                       |
|`desvio_padrao_coluna(col)`| Retornar o desvio padrão de uma coluna escolhida do dataset                                                               |
|`gravidade_acidentes()`| Gerar o número de mortes totais e alguns gráficos com insights sobrer nível de dano, fatalidade e classificação da ocorrência |
|`tipos_mortes_aeronaves()`| Retornar os tipos de aeronaves e a porcentagem de ocorrencias fatais nas aeronaves listadas com ocorrências                |
|`top_fatores_contribuintes()`| Retornar os top fatores contribuintes                                                                                   |
|`ocorrencia_tipo()`| Visualizar quais são as ocorrências mais frequentes                                                                               |
|`ocorrencia_estados(nome_UF)`| Filtrar ocorrências pela sigla dos estados                                                                              |
|`ocorrencia_cidade(nome_cidade)`| Filtrar ocorrências pelo nome de cidades                                                                             |
|`informacoes_acidentes()`| Retornar informações sobre a gravidade e detalhes de fatalidade do acidente                                                 |
|`ocorrencia_MesHora()`| Apresentar os meses e horários que mais existem ocorrências                                                                    |
|`ocorrencia_ano(ano)`| Apresentar as informações de acordo com o ano selecionado                                                                       |

<p>Legenda para variáveis das funções:
	<ul>
		<li>col= coluna que deseja utilizar</li>
		<li>nome_UF= nome da sigla do estado que deseja utilizar</li>
	</ul>
</p>

<h2 id="reference">Referência</h2>

<ul>
	<li>https://dados.gov.br/dataset/ocorrencias-aeronauticas-da-aviacao-civil-brasileira</li>
</ul>

<br />
