📚 API de Livros

API REST simples feita com Flask para gerenciar uma lista de livros, com as quatro operações do CRUD: consultar, criar, editar e excluir.

Os dados ficam em memória (uma lista Python), então são reiniciados toda vez que o servidor é reiniciado.

1. Objetivo

Praticar o desenvolvimento de um backend com API, testando as respostas HTTP com o Postman (ou similar).

2. URL base
http://localhost:7500
3. Tecnologias
Python 3.8+
Flask
4. Como rodar
bash
# 1. (opcional) criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 2. instalar o Flask
pip install flask

# 3. executar a API
python teste.py

O servidor sobe em http://localhost:7500 com o modo debug ativado.

5. Endpoints
Método	Rota	Descrição	Sucesso	Erro
GET	/livros	Lista todos os livros	200	—
GET	/livros/<id>	Busca um livro pelo id	200	404 (não encontrado)
POST	/livros	Cadastra um novo livro	201	—
PUT	/livros/<id>	Edita um livro existente	200	404 (não encontrado)
DELETE	/livros/<id>	Exclui um livro	200	404 (não encontrado)
6. Recurso disponibilizado: Livro
json
{
  "id": 1,
  "titulo": "A empregada",
  "autor": "Freida McFadden"
}
Campo	Tipo	Descrição
id	inteiro	Identificador único
titulo	texto	Título do livro
autor	texto	Autor(a) do livro
7. Exemplos de uso

Listar todos

bash
curl http://localhost:7500/livros

Buscar por id

bash
curl http://localhost:7500/livros/1

Criar um livro

bash
curl -X POST http://localhost:7500/livros \
  -H "Content-Type: application/json" \
  -d '{"id": 14, "titulo": "Novo Livro", "autor": "Autor Exemplo"}'

Editar um livro

bash
curl -X PUT http://localhost:7500/livros/1 \
  -H "Content-Type: application/json" \
  -d '{"titulo": "A Empregada"}'

Excluir um livro

bash
curl -X DELETE http://localhost:7500/livros/1

Resposta de erro (404)

json
{ "message": "livro não encontrado!" }
8. Testando no Postman
Crie uma requisição com o método desejado e a URL http://localhost:7500/livros.
Para POST e PUT, vá em Body → raw → JSON e envie o conteúdo do livro.
Confira o status e o corpo da resposta.
9. Estrutura do projeto
.
├── teste.py    # versão corrigida da API (use esta)
├── app.py      # versão inicial, com anotações de estudo
└── README.md
10. Observações
Os dados não são persistidos: ao reiniciar o servidor, a lista volta ao estado inicial.
O id não é gerado automaticamente; ele deve ser enviado no POST.
Não há validação dos campos enviados.
11. Possíveis melhorias
Gerar o id automaticamente
Validar os dados recebidos (campos obrigatórios e tipos)
Persistir em banco de dados (SQLite, por exemplo)
Adicionar busca por título ou autor
Escrever testes automatizados
