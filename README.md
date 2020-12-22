# Projeto_Coviduana

# Como usar o Coviduana
Para usar o Coviduana, o usuário precisa apenas rodar o site em seu navegador, sendo assim, a ferramenta estará pronta para uso. Não se preocupe se o server cair, tudo estará salvo.
É permitido cadastrar no máximo 100 produtos, sendo o código de cada produto do 0 ao 99, os cadastros de estoque e venda usa da mesma lógica.
Para evitar muitas páginas, no menu principal já possui uma lista de produtos e de vendas, ambas com campo de filtragem na qual a lista de produto recebe como filtro o código e a lista de venda recebe o filtro por data, é possível acessar uma lista de estoque com a mesma lógica das demais. Nessas 3 listas, ao cadastrar algo em suas respectivas categorias, há um campo para excluir/editar o produto ou o estoque e um campo para excluir a venda.

# Ferramentas
As ferramentas usadas nesse teste foi a linguagem de programação Python devido uma maior afinidade com a mesma, linguagem de programação JavaScript para requisições ajax e fazer os filtros das listas, a framework Flask para desenvolvimento web com python, e juntamente do Flask, a framework SQLAlchemy que trabalhou junto com o Flask para a criação do banco de dados do Coviduana.

# Dificuldades
Por parte do SQLAlchemy, não foi possível criar uma tabela de vendas sem primary key, busquei em toda internet e infelizmente não achei uma solução.
As requisições Ajax estão sendo feitas nos campos de cadastros, porém devido ao Flask e SQLAlchemy, foi necessário pedir essas requisições via uma função do Flask de manipulamento de página ("@app.route") para inserir os dados no banco de dados e executar o commit.
Não consegui encontrar nenhuma forma clara de rodar esse desenvolvimento no endpoint "www.arcossp.com.br/arcos_novo/ws.coviduana", apenas no meu localhost.