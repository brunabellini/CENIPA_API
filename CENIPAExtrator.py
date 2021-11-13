'''
Bibliotecas utilizadas
'''
import pandas as pd


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
	def top_acidentes(df): #Principais acidentes # bru
		'''
		Essa função tem o objetivo de 
  		'''
		pass

	def top_aeronaves(df): #Aeronaves com mais acidentes # helo
		'''
		Essa função tem o objetivo de 
  		'''
		df['aeronave_registro_categoria']
		pass

	def tipo_aeronave(df): #Se é Regular, privada, agrícola etc. # helo
		'''
		Essa função tem o objetivo de 
  		'''
		df['aeronave_registro_segmento']
		pass

	def top_fatores_contribuintes(df): #O que mais influencia os acidentes 
		'''
		Essa função tem o objetivo de 
  		'''
		df['fator_nome', 'fator_aspecto','fator_condicionante','fator_area']
		pass

	def ocorrencia_tipo(df):
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_tipo','ocorrencia_tipo_categoria']
		pass

	def pequisa_estados(df): #Estados onde mais ocorreram acidentes # bibi
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_uf'] 
		pass

	def pesquisa_cidade(df): #Cidades em que mais ocorreram acidentes # bibi
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_cidade']
		pass

	def gravidade_acidente(df): # bru
		'''
		Essa função tem o objetivo de 
  		'''
		df['aeronave_nivel_dano','ocorrencia_classificacao', 'aeronave_fatalidades_total']
		pass

	def ocorrencia_MesHora(df):
		'''
		Essa função tem o objetivo de 
  		'''
		df['ocorrencia_dia','ocorrencia_hora']
		pass


# Utilize o espaço abaixo para rodar as funções que deseja utilizar, não se esqueça de chamar a classe desejada antes de usufruir da função dentro da mesma

teste = Insights()
print(teste.get_table())
