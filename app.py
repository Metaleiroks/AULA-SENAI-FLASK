from flask import Flask, request

app = Flask(__name__)

#endpoint: buscar todos os alunos
#metodo: GET
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_alunos(id):
    return f"aluno de codigo: {id}"

#endpoint: adicionar aluno
#metodo: POST
@app.route('/adicionaraluno', methods=['POST'])
def adicionar_aluno():
    
    id = request.args.get('id')
    nome = request.args.get('nome')
    return f"Aluno Cadastrado: id:{id} - nome: {nome}"

#endpoint: listar alunos
#metodo: GET
@app.route('/listaralunos', methods=['GET'])
def listar_alunos():
    return "Todos alunos Listados" 


if __name__ == "__main__":
    app.run(debug=True)


    