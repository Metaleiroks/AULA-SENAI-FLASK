from flask import Flask, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Kevyn"},
    {"id": 2, "nome": "July"},
    {"id": 3, "nome": "Aline"},
]

#endpoint: buscar todos os alunos
@app.route('/buscaraluno/<int:id>', methods=['GET'])
def buscar_alunos(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return aluno

    return {"mensagem": "Aluno não encontrado"}
#endpoint: adicionar aluno
@app.route('/adicionaraluno', methods=['POST'])
def adicionar_aluno():
    
    id = request.args.get('id')
    nome = request.args.get('nome')
    novo = {"id": id, "nome": nome}
    novo["id"] = len(alunos) + 1
    alunos.append(novo)
    return alunos 

#endpoint: adicionar aluno por json
@app.route('/adicionaralunojson', methods=['POST'])
def adicionar_aluno_json():
    
    novo = request.get_json()
    novo[" id"] = len(alunos) + 1
    alunos.append(novo)
    return alunos



#endpoint: listar alunos
@app.route('/listaralunos', methods=['GET'])
def listar_alunos():
    return alunos 

#endpoint: deletar aluno
@app.route('/deletaraluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    for aluno in alunos:
        if aluno['id'] == id:
            alunos.remove(aluno)
            return {"mensagem": "Aluno deletado com sucesso"}
    return {"mensagem": "Aluno não encontrado"}



if __name__ == "__main__":
    app.run(debug=True)


    