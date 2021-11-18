from setuptools import setup

setup(
    name = 'CENIPA_API',
    version = '1.0.0',
    author = 'Abdul Malik de Barros \nAna Beatriz Oliveira de Macedo \nBruna Bellini Faria \nHeloisa Mariani Rodrigues',
    packages = ['CENIPA_API'],
    description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA',
    long_description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA para '
                        + 'retornar datasets individuais com informações sobre, acidentes, fatores contribuintes, aeronave e recomendações, '
                        + 'retornar insights das informações (colunas) do dataset',
    url = 'https://github.com/brunabellini/CENIPA_API',
    project_urls = {
        'Código fonte': 'https://github.com/yanorestes/aluratemp',
        'Download': 'https://github.com/yanorestes/aluratemp/archive/1.0.0.zip'
    }
)
