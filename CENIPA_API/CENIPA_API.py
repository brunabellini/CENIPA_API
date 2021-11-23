'''
Bibliotecas utilizadas
'''
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

'''
Funções Complementares 
'''

def limpezaFinal(txt):
  chars = "=*|>!:,[]'\()" 
  for chars in chars:
    txt = txt.replace(chars, '')
  txt = txt.replace('"', ' ') 
  txt = txt.replace('n', ' ') 
  return txt



class CENIPA_API:
	'''
	Esta superclasse representa um extrator com finalidade de utilizar dados públicos para entender características e correlações aeronáuticas da aviação civil brasileira nos últimos 10 anos
	'''
	def __init__(self):
		'''
		Inicializador 
  		'''
		self.df = pd.read_csv('https://raw.githubusercontent.com/brunabellini/CENIPA_API/main/Data/df_final_aeronautico.csv', sep=';')
		
	def get_table(self):
		'''
		Essa função tem o objetivo de retornar e mostrar o Dataset dentro do terminal
  		'''
		return self.df

	def get_acidente(self):
		'''
		Essa função tem o objetivo de retornar um dataset com as colunas relevantes para analise sobre os acidentes
		'''
		cols=['aeronave_tipo_veiculo', 'aeronave_fabricante','aeronave_modelo','aeronave_motor_tipo','aeronave_assentos','aeronave_ano_fabricacao','aeronave_registro_segmento','aeronave_voo_origem','aeronave_voo_destino','aeronave_fase_operacao','codigo_ocorrencia','ocorrencia_cidade','ocorrencia_uf','ocorrencia_hora','fator_aspecto','fator_condicionante','ocorrencia_tipo']
		self.df_acidente = self.df[cols]
		return self.df_acidente       

	def get_fator_contribuinte(self):
		'''
        Essa função tem o objetivo de retornar um dataset com os fatores contribuintes para o acidente
        '''
		cols=['aeronave_ano_fabricacao','aeronave_fabricante','fator_nome','fator_aspecto','fator_condicionante','fator_area','ocorrencia_tipo','ocorrencia_tipo_categoria']
		self.df_contribuinte = self.df[cols]
		return self.df_contribuinte

	def get_aeronave(self):
		'''
        Essa função tem o objetivo de retornar um dataset para a analise das fatores das aeronaves
        '''
		cols=['aeronave_tipo_veiculo','aeronave_fabricante','aeronave_modelo','aeronave_tipo_icao','aeronave_motor_tipo','aeronave_ano_fabricacao','aeronave_pais_fabricante','aeronave_pais_registro','aeronave_registro_categoria','aeronave_registro_segmento','aeronave_voo_origem','aeronave_voo_destino','aeronave_fase_operacao','aeronave_tipo_operacao','aeronave_nivel_dano', 'aeronave_fatalidades_total']
		self.df_aero = self.df[cols]
		return self.df_aero

	def get_recomendacao(self):
		'''
		Essa função tem objetivo de retornar um dataset para a analise das recomendações do casos 
        '''
		cols = ['recomendacao_dia_encaminhamento', 'recomendacao_conteudo', 'recomendacao_status','recomendacao_destinatario_sigla','recomendacao_destinatario'] 
		self.df_recom = self.df[cols]
		return self.df_recom


class Insights(CENIPA_API): 
	'''
	Essa classe representa uma variedade de insights retirados e pensados a partir do dataframe de acidentes aeronáuticos apresentado na classe CENIPA_API
	'''
	def moda_coluna(self, col): 
		'''
		Essa função tem o objetivo de retornar o valor mais recorrente em uma coluna escolhida do dataset
		'''
		try:
			result = self.df[col].value_counts()
		except KeyError:
			raise ColunaInexistente('Essa coluna não existe')

		restr = str(result)
		res = re.search(r'\w[^\n]+',restr)
		reestr = str(res) 
		a = re.findall(r"\='[^\'']+",reestr)
		astr = str(a)
		self.resultado = limpezaFinal(astr)        
		return self.resultado

	def mediana_coluna(self, col):
		'''
		Essa função tem o objetivo de retornar a mediana de uma coluna escolhida do dataset
		'''
		result = self.df[col].median()
		restr = str(result)
		res = re.search(r'\w[^\n]+',restr)
		reestr = str(res)
		a = re.findall(r"\='[^\'']+",reestr)
		astr = str(a)
		self.resultado = limpezaFinal(astr)
		return self.resultado

	def media_coluna(self,col):
		'''
		Essa função tem o objetivo de retornar a média de uma coluna escolhida do dataset
		'''
		try:
			self.result = self.df[col].mean()
		except ValueError:
		    raise ColunaNaoCalculavel('Essa coluna não é de um tipo calculável.')
		return self.result
        
	def variancia_coluna(self,col):
		'''
		Essa função tem o objetivo de retornar a variancia de uma coluna escolhida do dataset
		'''
		try:
			self.result = np.var(self.df[col])
		except ValueError:
			raise ColunaNaoCalculavel('Essa coluna não é de um tipo calculável.')
		return self.result
 
	def desvio_padrao_coluna(self,col):
		'''
		Essa função tem o objetivo de retornar o desvio padrão de uma coluna escolhida do dataset
		'''
		try:
			self.result = self.df[col].std()
		except ValueError:
			raise ColunaNaoCalculavel('Essa coluna não é de um tipo calculável.')
		return self.result
 
	def gravidade_acidentes(self): 
		'''
		Essa função tem o objetivo de gerar o número de mortes totais e alguns gráficos com insights sobrer nível de dano, fatalidade e classificação da ocorrência
  		'''
		df_ta = self.df[['aeronave_nivel_dano', 'ocorrencia_classificacao', 'aeronave_fatalidades_total']]
		num_mortes = df_ta['aeronave_fatalidades_total'].sum()
		print(f'Houveram \033[91m{num_mortes}\033[0m mortes neste período de 10 anos de análise de ocorrências')
  
		fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(aspect='equal'))
		labels = ['Dano substancial','Destruída','Dano leve','Nenhum dano']
		sizes = [df_ta['aeronave_nivel_dano'].value_counts()[0], df_ta['aeronave_nivel_dano'].value_counts()[1], df_ta['aeronave_nivel_dano'].value_counts()[2], df_ta['aeronave_nivel_dano'].value_counts()[3]]
		colors = ['darkorange','gold','tomato','lightgreen']
		wedges, texts, pct = ax.pie(sizes, startangle=90, colors=colors, pctdistance=1.1, autopct=lambda p : '{:.2f}%\n({:.0f})'.format(p,p * sum(sizes)/100))
		plt.setp(pct, size=18)
		plt.rcParams['font.size'] = 13
		plt.legend(labels, title= 'Legenda de nível:')
		ax.set_title('Porcentagem por nível de dano')
		plt.show()	
  
		fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(aspect='equal'))
		labels = ['Dano substancial','Dano leve','Destruída','Nenhum dano']
		sizes = [df_ta.loc[df_ta['aeronave_nivel_dano'] == 'SUBSTANCIAL', 'aeronave_fatalidades_total'].sum(), df_ta.loc[df_ta['aeronave_nivel_dano'] == 'LEVE', 'aeronave_fatalidades_total'].sum(), df_ta.loc[df_ta['aeronave_nivel_dano'] == 'DESTRUÍDA', 'aeronave_fatalidades_total'].sum(), df_ta.loc[df_ta['aeronave_nivel_dano'] == 'NENHUM', 'aeronave_fatalidades_total'].sum()] 
		colors = ['deepskyblue','darkblue','lightblue','dodgerblue']
		explode = (0, 0, 0.1, 0) 
		wedges, texts, pct = ax.pie(sizes, explode=explode, startangle=90, colors=colors, pctdistance=1.1, autopct=lambda p : '{:.2f}%\n({:.0f})'.format(p,p * sum(sizes)/100))
		plt.setp(pct, size=18)
		plt.rcParams['font.size'] = 13
		plt.legend(labels, title= 'Legenda de nível:')
		ax.set_title('Porcentagem por quantidade de fatalidade em cada nível de dano')
		plt.show()
  
		fig, ax = plt.subplots(figsize=(10,10), subplot_kw=dict(aspect='equal'))
		labels = ['Acidente','Incidente','Incidente grave']
		sizes = [df_ta['ocorrencia_classificacao'].value_counts()[0], df_ta['ocorrencia_classificacao'].value_counts()[1], df_ta['ocorrencia_classificacao'].value_counts()[2]]
		colors = ['darkorange','lightgreen','gold']
		wedges, texts, pct = ax.pie(sizes, startangle=90, colors=colors, pctdistance=1.1, autopct=lambda p : '{:.2f}%\n({:.0f})'.format(p,p * sum(sizes)/100))
		plt.setp(pct, size=18)
		plt.rcParams['font.size'] = 13
		plt.legend(labels, title= 'Legenda de nível:')
		ax.set_title('Porcentagem por classificação da ocorrência')
		plt.show()	 
		
	def tipos_mortes_aeronaves(self): 
		'''
		Essa função tem o objetivo de retornar os tipos de aeronaves e a porcentagem de ocorrencias fatais nas aeronaves listadas com ocorrências
  		'''
		print(self.df['aeronave_registro_categoria'].value_counts())
		df_tpa = self.df[['aeronave_registro_categoria', 'aeronave_fatalidades_total']]
		ma = (df_tpa.loc[df_tpa['aeronave_registro_categoria'] == 'AVIÃO', 'aeronave_fatalidades_total'].sum()*100) / df_tpa['aeronave_registro_categoria'].value_counts()[0]
		mh = (df_tpa.loc[df_tpa['aeronave_registro_categoria'] == 'HELICÓPTERO', 'aeronave_fatalidades_total'].sum()*100) / df_tpa['aeronave_registro_categoria'].value_counts()[1]
		mp =  (df_tpa.loc[df_tpa['aeronave_registro_categoria'] == 'PLANADOR', 'aeronave_fatalidades_total'].sum()*100) / df_tpa['aeronave_registro_categoria'].value_counts()[2]
		mu = (df_tpa.loc[df_tpa['aeronave_registro_categoria'] == 'ULTRALEVE', 'aeronave_fatalidades_total'].sum()*100) / df_tpa['aeronave_registro_categoria'].value_counts()[3]
		maf = (df_tpa.loc[df_tpa['aeronave_registro_categoria'] == 'ANFÍBIO', 'aeronave_fatalidades_total'].sum()*100) / df_tpa['aeronave_registro_categoria'].value_counts()[4]
		return f'\033[1mEntre os tipos de aeronaves, encontram-se a porcentagem de ocorrências fatais:\033[0m \n   Avião {ma:.2f}%\n   Helicóptero {mh:.2f}%\n   Planador {mp:.2f}%\n   Ultraleve {mu:.2f}%\n   Anfíbio {maf:.2f}%'
    
	def top_fatores_contribuintes(self):
		'''
		Essa função tem o objetivo de retornar os top fatores contribuintes
  		'''
		n1= self.df['fator_nome'].value_counts().index.tolist()[0]
		n2= self.df['fator_nome'].value_counts().index.tolist()[1]
		n3= self.df['fator_nome'].value_counts().index.tolist()[2]
		a1= self.df['fator_aspecto'].value_counts().index.tolist()[0]
		a2= self.df['fator_aspecto'].value_counts().index.tolist()[1]
		a3= self.df['fator_aspecto'].value_counts().index.tolist()[2]
		c1= self.df['fator_condicionante'].value_counts().index.tolist()[0]
		c2= self.df['fator_condicionante'].value_counts().index.tolist()[1]
		c3= self.df['fator_condicionante'].value_counts().index.tolist()[2]
		ar1= self.df['fator_area'].value_counts().index.tolist()[0]
		ar2= self.df['fator_area'].value_counts().index.tolist()[1]
		return f'Top fatores contribuintes: \nNome do fator: {n1}, {n2}, {n3}\nAspecto: {a1}, {a2}, {a3}\nCondicionante: {c1}, {c2}, {c3}\nArea: {ar1} e {ar2}'

	def ocorrencia_tipo(self):
		'''
		Essa função tem o objetivo de visualizar quais são as ocorrências mais frequentes 
  		'''
		return self.df['ocorrencia_tipo'].value_counts()

	def ocorrencia_estados(self, nome_UF): 
		'''
		Essa função tem o objetivo de filtrar ocorrências pela sigla dos estados
  		'''
		estado = self.df.loc[(self.df['ocorrencia_uf']==nome_UF.upper())]
		if len(estado)==0:
			raise ExceçãoEstadoInexistente('Não há ocorrências para esse estado')
		return estado
		
	def ocorrencia_cidade(self, nome_cidade): 
		'''
		Essa função tem o objetivo de filtrar ocorrências pelo nome de cidades
		'''
		cidade = self.df.loc[(self.df['ocorrencia_cidade']==nome_cidade.upper())]
		if len(cidade)==0:
			raise ExceçãoCidadeInexistente('Não há ocorrências para essa cidade')
		return cidade

	def informacoes_acidentes(self): 
		'''
		Essa função tem o objetivo de retornar informações sobre a gravidade e detalhes de fatalidade do acidente
  		'''
		return self.df[['aeronave_nivel_dano', 'ocorrencia_classificacao', 'aeronave_fatalidades_total']]

	def ocorrencia_MesHora(self): 
		'''
		Essa função tem o objetivo de apresentar os meses e horários que mais existem ocorrências
  		'''
		df_mh = self.df[['ocorrencia_dia','ocorrencia_hora']]
		novo_df = df_mh['ocorrencia_dia'].str.split("/", n=2, expand= True).astype(int)
		df_mh['mes_ocorrencia']= novo_df[1]
		df_mh['ano_ocorrencia']= novo_df[2]
		df_mh.drop('ocorrencia_dia', axis=1, inplace= True)
		m = df_mh['mes_ocorrencia'].value_counts().index.tolist()[0]
		a = df_mh['ano_ocorrencia'].value_counts().index.tolist()[0]
		h = df_mh['ocorrencia_hora'].value_counts().index.tolist()[0] 
		return f'Top mês, dia e hora das ocorrências: \nMês: {m}\nAno: {a}\nHora: {h}'

	def ocorrencia_ano(self, ano): 
		'''
		Essa função tem o objetivo de apresentar as informações de acordo com o ano selecionado
  		'''
		col_ano = self.df['ocorrencia_dia'].str.split("/", n=2, expand= True).astype(int)
		self.df['ano_ocorrencia']= col_ano[2]
		pesq_ano = self.df.loc[(self.df['ano_ocorrencia']==ano)]
		if len(pesq_ano)==0:
			raise ExceçãoAnoInexistente('Não há ocorrências para esse ano')
		return pesq_ano

class ColunaInexistente(Exception):
    pass

class ColunaNaoCalculavel(Exception):
    pass

class ExceçãoEstadoInexistente(Exception):
    pass

class ExceçãoCidadeInexistente(Exception):
    pass

class ExceçãoAnoInexistente(Exception):
    pass