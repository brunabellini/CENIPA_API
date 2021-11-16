'''
Bibliotecas utilizadas
'''
import pandas as pd
import plotly.graph_objects as go

class CENIPAExtrator:
	'''
	Esta superclasse representa um extrator com finalidade de utilizar dados públicos para entender características e correlações aeronáuticas da aviação civil brasileira nos últimos 10 anos
	'''
	def __init__(self):
		'''
		Inicializador 
  		'''
		path = './Data/df_final_aeronautico.csv'
		self.df = pd.read_csv(path, sep=';')
		
	def get_table(self):
		'''
		Essa função tem o objetivo de retornar e mostrar o Dataset dentro do terminal
  		'''
		return self.df

	def get_acidente(self): # abdul
		'''
		Essa função tem o objetivo de 
  		'''
		pass

	def get_fator_contribuinte(self):
		'''
		Essa função tem o objetivo de 
  		'''
		pass
	
	def get_aeronave(self):
		'''
		Essa função tem o objetivo de 
  		'''
		pass

	def get_recomendacao(self):
		'''
		Essa função tem o objetivo de 
  		'''
		df['recomendacao_dia_encaminhamento', 'recomendacao_conteudo', 'recomendacao_status','recomendacao_destinatario_sigla','recomendacao_destinatario']
		pass


class Insights(CENIPAExtrator):
	'''
	Essa classe representa uma variedade de insights retirados e pensados a partir do dataframe de acidentes aeronáuticos apresentado na classe CENIPAExtrator
	'''
	def top_acidentes(self): #Principais acidentes # bru
		'''
		Essa função tem o objetivo de a partir de certas caracteristicas retornar os acidentes mais graves e os mais leves entre os 10 anos
  		'''
		df_ta = self.df[['aeronave_nivel_dano', 'ocorrencia_classificacao', 'aeronave_fatalidades_total']]
		print('Contagem de acidentes em certo nível de dano:')
		print(df_ta['aeronave_nivel_dano'].value_counts())
		colors = ['orange', 'red', 'yellow', 'green']

		fig = go.Figure(data=[go.Pie(labels=['Dano substancial','Destruída','Dano leve','Nenhum dano'],
                             values=[5525, 5525, 1450, 1087])])
		fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=1)))
		fig.show()
		num_mortes = df_ta['aeronave_fatalidades_total'].sum()
		print(f'Houveram {num_mortes} mortes neste período de 10 anos de análise')

	def top_aeronaves(self): #Aeronaves com mais acidentes # helo
		'''
		Essa função tem o objetivo de 
  		'''
		df['aeronave_registro_categoria']
		pass

	def tipo_aeronave(self): #Se é Regular, privada, agrícola etc. # helo
		'''
		Essa função tem o objetivo de 
  		'''
		df['aeronave_registro_segmento']
		pass

	def top_fatores_contribuintes(self): #O que mais influencia os acidentes 
		'''
		Essa função tem o objetivo de 
  		'''
		df['fator_nome', 'fator_aspecto','fator_condicionante','fator_area']
		pass

	def ocorrencia_tipo(self):
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_tipo','ocorrencia_tipo_categoria']
		pass

	def pequisa_estados(self): #Estados onde mais ocorreram acidentes # bibi
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_uf'] 
		pass

	def pesquisa_cidade(self): #Cidades em que mais ocorreram acidentes # bibi
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_cidade']
		pass

	def gravidade_acidente(self): # FEITA
		'''
		Essa função tem o objetivo de retornar informações sobre a gravidade e detalhes da ocorrencia
  		'''
		return self.df[['aeronave_nivel_dano', 'ocorrencia_classificacao', 'aeronave_fatalidades_total']]

	def ocorrencia_MesHora(self):
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_dia','ocorrencia_hora']
		pass


# Utilize o espaço abaixo para rodar as funções que deseja utilizar, não se esqueça de chamar a classe desejada antes de usufruir da função dentro da mesma

teste = Insights()
# print(teste.gravidade_acidente())
print(teste.top_acidentes())

