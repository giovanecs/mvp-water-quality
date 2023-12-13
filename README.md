# MVP-WATER-QUALITY

Este pequeno projeto faz parte da avalicao das disciplinas Disciplina: Qualidade de Software, Segurança e Sistemas Inteligentes da especialização online **Pós-Graduação em Engenharia de Software**, do Departamento de Informática da PUC-Rio.

O objetivo aqui é ilutsrar o conteúdo apresentado ao longo da disciplina.


A idea é a criação de modelo de machine learning que possa ser utilizado por uma api para determinar se uma amostra de água é ou não potável.

O primeiro passo realizado foi a construção do modelo a partir do notebook no google colab.
Após a analise e testes com algoritmos apresentados da disciplina um algoritmo foi escolhido para ser utilizadom como modelo.


---
## Como executar a API

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo a partir do diretório "api".

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## Como executar o front end

A partir do diretorio "front" basta abrir o arquivo index.html no seu navegador.
para que funcione corretamente é necessário que a API esta sendo executada.