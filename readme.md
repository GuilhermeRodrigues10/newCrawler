<h1 align="center">NewCrawler - Um exemplo prático da utilização do framework Scrapy</h1>
<p align="center">O objetivo deste repositório é apresentar um exemplo prático do 
                  framework Scrapy, buscando as principais notícias de um portal de tecnologia.</p>

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Scrapy requires Python 3.6+](https://docs.scrapy.org/en/latest/index.html). 

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### Rodando o projeto

```bash
# Clone este repositório
$ git clone <https://github.com/GuilhermeRodrigues10/newCrawler.git>

# Para instalar o Scrapy
$ pip install Scrapy

# Acesse a pasta do projeto no terminal/cmd
$ cd newCrawler

# Rode o script
$ scrapy runspider newCrawler/spiders/Tecmundo.py 

# O resultado estará no arquivo news.jl