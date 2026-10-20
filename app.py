#desenvolver um backend com api - 
#postmann - teste http -> verificar respostas API
# 1. OBJETIVO
# 2. URLBASE
# 3. ENDPOINTS
# 4. RECURSOS DISPONIBILIZADOS


#VAMOS CRIAR UMA API:
"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

#app -> a aplicação flask
#__name__ identific que  o modulo da aplicação

livros = [
    {
        "id": 2,
        "titulo": "A empregada",
        "autor": "Frieda Mcfadeen"
    },
    {
        "id": 2,
        "titulo": "Verity",
        "autor": "Colenn Houver"
    },
    {
        "id": 3,
        "titulo": "A razão do amor",
        "autor": "Ali Hazzennold"
    },
    {
        "id": 4,
        "titulo": "O Segredo da Empregada",
        "autor": "Freida McFadden"
    },
    {
        "id": 5,
        "titulo": "É Assim que Acaba",
        "autor": "Colleen Hoover"
    },
    {
        "id": 6,
        "titulo": "A Hipótese do Amor",
        "autor": "Ali Hazelwood"
    },
    {
        "id": 7,
        "titulo": "Amor, Teoricamente",
        "autor": "Ali Hazelwood"
    },
    {
        "id": 8,
        "titulo": "A Garota no Trem",
        "autor": "Paula Hawkins"
    },
    {
        "id": 9,
        "titulo": "O Paciente Silencioso",
        "autor": "Alex Michaelides"
    },
    {
        "id": 10,
        "titulo": "Em Águas Sombrias",
        "autor": "Paula Hawkins"
    },
    {
        "id": 11,
        "titulo": "Teto Para Dois",
        "autor": "Beth O'Leary"
    },
    {
        "id": 12,
        "titulo": "Leitura de Verão",
        "autor": "Emily Henry"
    },
    {
        "id": 13,
        "titulo": "Manual de Assassinato para Boas Garotas",
        "autor": "Holly Jackson"
    }
];

#consultar livros - criar uma função
#def obter_livros():
#return jsonify(livros)


#criar as rotas /livros
#a rota foi especificada, somente o método GET sera aceitp
@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)

#criar as rotas /livros id
@app.route("/livros/<int:id>", methods = ["GET"])
#<int:> -> indica inteiro
def obter_livros_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify ({'message': 'livro não encontrado!'}), 404
    
#put -> primeiro, os dados enviados pelo cliente
#serão obtidos
#@
@app.route("/livros/<int:id>", methods = ["PUT"])
def editar_livro_por_id(id):
#permmite acessar os dados json enviados no corpo
#da requisição
   
    livro_alterado = request.get_json()
    
    for indice, livro in enumerate (livros):
        print(indice)
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livro[indice])


#criação de um novo livro
@app.route("/livros", methods = ['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json
    livros.append(novo_livro)
    return jsonify(livros)

#delete-excluir um livro
@app.route("/livros/<int:id>", methods = ['DELETE'])
def excluir_livro(id):
    #como é necessário excluir um elemento da lista
    #pelo seu índice, será utilizado novamente o
    #enumerate()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)



#INICILIZAÇÃO DO SERVIDOR LOCAL
app.run(
    host= 'localhost',
    port= 7500,
    debug = True
)
