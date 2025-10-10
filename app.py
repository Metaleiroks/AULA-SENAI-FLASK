from flask import Flask, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Kevyn","idade": 17, "end": "Rua Lunares, 155"},
    {"id": 2, "nome": "July","idade": 15, "end": "Rua Buenos Aires, 205"},
    {"id": 3, "nome": "Aline","idade": 42, "end": "Rua Satélite, 103"},
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
    idade = request.args.get('idade')
    endereco = request.args.get('end')
    novo = {"id": id, "nome": nome, "idade": idade, "end": endereco}
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
            return "Aluno deletado com sucesso", alunos
    return {"Aviso": "Aluno não encontrado"}


#endpoint: alterar aluno
@app.route('/alteraraluno', methods=['PUT'])
def alterar_aluno():
    alterado = request.get_json()
    for i, aluno in enumerate(alunos):
            if aluno['id'] == alterado ["id"]:
                alunos.pop(i)
                alunos.append(alterado)
                return alunos
    return {"Aviso": "Aluno não encontrado"}


if __name__ == "__main__":
    app.run(debug=True)


    