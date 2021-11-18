from setuptools import setup

setup(
    name = 'CENIPA_API',
    version = '1.0.0',
    author = 'Abdul Malik de Barros \nAna Beatriz Oliveira de Macedo \nBruna Bellini Faria \nHeloisa Mariani Rodrigues',
    packages = ['CENIPA_API'],
    license= 'MIT',
    keywords = 'API acidentes CENIPA',
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
    description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA',
    long_description = 'Coleta e análise dos últimos 10 anos de ocorrencias registradas pelo CENIPA para '
                        + 'retornar datasets individuais com informações sobre, acidentes, fatores contribuintes, aeronave e recomendações, '
                        + 'retornar insights das informações (colunas) do dataset',
    url = 'https://github.com/brunabellini/CENIPA_API',
    project_urls = {
        'Código fonte': 'https://github.com/brunabellini/CENIPA_API',
        'Download': 'https://github.com/brunabellini/CENIPA_API/archive/1.0.0.zip'
    }
)
