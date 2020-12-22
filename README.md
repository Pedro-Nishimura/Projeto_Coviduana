# Projeto_Coviduana

# Como usar o Coviduana
Para usar o Coviduana, o usuário precisa apenas rodar o site em seu navegador, sendo assim, a ferramenta estará pronta para uso. Não se preocupe se o server cair, tudo estará salvo.
É permitido cadastrar no máximo 100 produtos, sendo o código de cada produto do 0 ao 99, os cadastros de estoque e venda usa da mesma lógica.
Para evitar muitas páginas, no menu principal já possui uma lista de produtos e de vendas, ambas com campo de filtragem na qual a lista de produto recebe como filtro o código e a lista de venda recebe o filtro por data, é possível acessar uma lista de estoque com a mesma lógica das demais. Nessas 3 listas, ao cadastrar algo em suas respectivas categorias, há um campo para excluir/editar o produto ou o estoque e um campo para excluir a venda.

# Executar o Coviduana como localhost
Primeiro passo, baixe a framework Flask no cmd com o comando "pip install flask" (windows).
Segundo passo, baixe o banco de dados da framework Flask com o comando no cmd "pip install flask-sqlalchemy" e baixe a migration do banco com o comando "pip install flask-migrate (windows).
Terceiro passo, baixe o ambiente virtual no cmd com o comando "pip install virtualenv" (windows).
Quarto passo, escreva no cmd "virtualenv venv", esse comando criará uma pasta venv e pedirá para instalar o flake8 (instale-o).
Quinto passo, rode o comando "python app.py". OBS: quando abrir o terminal, pode acontecer de aparecer a mensagem de que o windows não execute o script por questão de segurança, ignore, na linha debaixo escreva "python app.py" que o localhost estará disponível para rodar, caso queira derrubar o servidor, execute "ctrl c".

# Ferramentas
As ferramentas usadas nesse teste foi a linguagem de programação Python devido uma maior afinidade com a mesma, linguagem de programação JavaScript para requisições ajax e fazer os filtros das listas, a framework Flask para desenvolvimento web com python, e juntamente do Flask, a framework SQLAlchemy que trabalhou junto com o Flask para a criação do banco de dados do Coviduana.

# Dificuldades
Por parte do SQLAlchemy, não foi possível criar uma tabela de vendas sem primary key, mas solucionei com um código da venda como primary key para que um produto possa ser vendido inúmeras vezes.
As requisições Ajax estão sendo feitas nos campos de cadastros, porém devido ao Flask e SQLAlchemy, foi necessário pedir essas requisições via uma função do Flask de manipulamento de página ("@app.route") para inserir os dados no banco de dados e executar o commit.
Não consegui encontrar nenhuma forma clara de rodar esse desenvolvimento no endpoint "www.arcossp.com.br/arcos_novo/ws.coviduana", apenas no meu localhost.