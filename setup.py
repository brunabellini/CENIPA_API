from setuptools import setup

setup(
    name = 'CENIPA_API',
    version = '0.0.3',
    description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA',
    long_description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA para '
                        + 'retornar datasets individuais com informações sobre, acidentes, fatores contribuintes, aeronave e recomendações, '
                        + 'retornar insights das informações (colunas) do dataset',
    long_description_content_type='text/markdown',
    author = 'Alunos Ciência de Dados PUC-SP',
    packages = ['CENIPA_API'],
    license= 'MIT',
    keywords = ['API', 'acidentes', 'CENIPA', 'analise de dados'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    url = 'https://github.com/brunabellini/CENIPA_API'
)
