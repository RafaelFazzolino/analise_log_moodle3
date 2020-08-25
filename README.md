# Instalação

Instalar o Mozilla geckodriver: https://github.com/mozilla/geckodriver/releases

Basta instalar utilizando o pip3. Na pasta raiz deste projeto, execute:

```
$ pip install . 
```

Antes de executar, precisamos incluir um arquivo chamado "alunos.csv" na pasta raiz do projeto.]
Este arquivo deverá possuir a primeira coluna com os nomes dos alunos matriculados. Sugiro copiar toda a lista do SIGAA 
e colocar tudo numa planilha. Garanta que o nome dos alunos se encontra na primeira coluna. 

Este arquivo de alunos deve ser um arquivo CSV separado por vírgulas.


# Execução

Para executar o bot basta:

```
$  chamadaunb -d https://aprender3.unb.br/course/view.php?id=3153 -n 3
```

No exemplo acima, altere a URL para a URL da sua disciplina, e o número 3 representa a quantidade de páginas de log que serão analisadas.
Vale ressaltar que quando o número de páginas escolhido é muito grande, foram observados alguns bugs na paginação do próprio moodle. Então sugiro a todos executar periodicamente, evitando a necessidade de uma execução com muitas páginas.
Até 10 páginas pareceu se comportar muito bem..
