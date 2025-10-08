from flask import Flask, request

app = Flask(__name__)

#endpoint: buscar todos os alunos
#metodo: GET
@app.route('/buscaraluno', methods=['GET'])
def buscar_alunos():
    return f"Todos alunos listados"

#endpoint: adicionar aluno
#metodo: POST
@app.route('/adicionaraluno', methods=['POST'])
def adicionar_aluno():
    
    aluno_id = request.args.get('id')
    nome = request.args.get('nome')
    return f"Aluno adicionado: id:{aluno_id} - nome: {nome}"

#endpoint: listar alunos
#metodo: GET
@app.route('/listaralunos', methods=['GET'])
def listar_alunos():
    return "Listando alunos" 


   


if __name__ == "__main__":
    app.run(debug=True)


    