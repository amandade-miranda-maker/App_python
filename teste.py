from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "A empregada", "autor": "Freida McFadden"},   # id corrigido (estava 2)
    {"id": 2, "titulo": "Verity", "autor": "Colleen Hoover"},
    {"id": 3, "titulo": "A razão do amor", "autor": "Ali Hazelwood"},
    {"id": 4, "titulo": "O Segredo da Empregada", "autor": "Freida McFadden"},
    {"id": 5, "titulo": "É Assim que Acaba", "autor": "Colleen Hoover"},
    {"id": 6, "titulo": "A Hipótese do Amor", "autor": "Ali Hazelwood"},
    {"id": 7, "titulo": "Amor, Teoricamente", "autor": "Ali Hazelwood"},
    {"id": 8, "titulo": "A Garota no Trem", "autor": "Paula Hawkins"},
    {"id": 9, "titulo": "O Paciente Silencioso", "autor": "Alex Michaelides"},
    {"id": 10, "titulo": "Em Águas Sombrias", "autor": "Paula Hawkins"},
    {"id": 11, "titulo": "Teto Para Dois", "autor": "Beth O'Leary"},
    {"id": 12, "titulo": "Leitura de Verão", "autor": "Emily Henry"},
    {"id": 13, "titulo": "Manual de Assassinato para Boas Garotas", "autor": "Holly Jackson"},
]


# CONSULTAR (todos)
@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)


# CONSULTAR (por id)
@app.route("/livros/<int:id>", methods=["GET"])
def obter_livros_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"message": "livro não encontrado!"}), 404


# EDITAR
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()

    for indice, livro in enumerate(livros):
        print(f"Índice: {indice} | ID: {livro.get('id')}")   # <- aparece no terminal

        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])          # livros[indice], com "s"

    return jsonify({"message": "livro não encontrado!"}), 404


# CRIAR
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros), 201


# EXCLUIR
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[indice]
            return jsonify({"message": "livro excluído!"})
    return jsonify({"message": "livro não encontrado!"}), 404


# INICIALIZAÇÃO DO SERVIDOR (sempre no final)
if __name__ == "__main__":
    app.run(host="localhost", port=7500, debug=True)