from flask import Flask, render_template, request, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    preco = db.Column(db.Float)

    def __init__(self, id, descricao, preco):
        self.id = id
        self.descricao = descricao
        self.preco = preco


class Estoque(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)

    def __init__(self, id, quantidade):
        self.id = id
        self.quantidade = quantidade


class Vendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10))
    codigo = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)
    cpf = db.Column(db.String(14))

    def __init__(self, data, id, codigo, quantidade, preco, cpf=None):
        self.data = data
        self.id = id
        self.codigo = codigo
        self.quantidade = quantidade
        self.preco = preco
        self.cpf = cpf


@app.route('/')
def index():
    vendas = Vendas.query.all()
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos, vendas=vendas)


@app.route('/adicionar_p', methods=['GET', 'POST'])
def add_p():
    if request.method == 'POST':
        produtos = Produto(request.form['id'], request.form['descricao'],
                           request.form['preco'])
        db.session.add(produtos)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastro_p.html')


@app.route('/adicionar_e', methods=['GET', 'POST'])
def add_e():
    if request.method == 'POST':
        estoque = Estoque(request.form['id'], request.form['quantidade'])
        db.session.add(estoque)
        db.session.commit()
        return redirect(url_for('filter_e'))
    return render_template('cadastro_e.html')


@app.route('/adicionar_v', methods=['GET', 'POST'])
def add_v():
    if request.method == 'POST':
        vendas = Vendas(request.form['data'], request.form['id'],
                        request.form['codigo'],
                        request.form['quantidade'],
                        request.form['preco'],
                        request.form['cpf'])
        db.session.add(vendas)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('cadastro_v.html')


@app.route('/editar_e/<int:id>', methods=['GET', 'POST'])
def edit_e(id):
    estoque = Estoque.query.get(id)
    if request.method == 'POST':
        estoque.quantidade = request.form['quantidade']
        db.session.commit()
        return redirect(url_for('filter_e'))
    return render_template('editar_e.html', estoque=estoque)


@app.route('/editar_p/<int:id>', methods=['GET', 'POST'])
def edit_p(id):
    produtos = Produto.query.get(id)
    if request.method == 'POST':
        produtos.descricao = request.form['descricao']
        produtos.preco = request.form['preco']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_p.html', produtos=produtos)


@app.route('/excluir_p/<int:id>')
def del_p(id):
    produtos = Produto.query.get(id)
    db.session.delete(produtos)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/excluir_e/<int:id>')
def del_e(id):
    estoque = Estoque.query.get(id)
    db.session.delete(estoque)
    db.session.commit()
    return redirect(url_for('filter_e'))


@app.route('/excluir_v/<int:id>')
def del_v(id):
    vendas = Vendas.query.get(id)
    db.session.delete(vendas)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/filtro_e')
def filter_e():
    estoque = Estoque.query.all()
    return render_template('filtro_e.html', estoque=estoque)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
