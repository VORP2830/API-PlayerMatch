from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def balanceamento(pessoasOrdenadas, quantidadePessoasTimes):
    quantidadeTotal = len(pessoasOrdenadas)
    quantidadeTimes = quantidadeTotal // quantidadePessoasTimes
    quantidadeExcedentes = quantidadeTotal % quantidadePessoasTimes

    if (quantidadeExcedentes):
        return f'Não é possivel fazer esse balanceamento pois temos {quantidadeExcedentes} jogadores excedente. Adicione mais {quantidadePessoasTimes - quantidadeExcedentes} jogador(es) para fazer o balanceamento'
    
    times = [[] for i in range(quantidadeTimes)]

    for i in range(quantidadePessoasTimes):
        for j in range(quantidadeTimes):
            if pessoasOrdenadas:
                if(len(times[j]) > 0):
                    times[j].append(pessoasOrdenadas.pop(len(pessoasOrdenadas)-1))
                else:
                    times[j].append(pessoasOrdenadas.pop(0))

    return json.dumps(times)

import json

def balanceamentoMisto(pessoasOrdenadas, quantidadePessoasTimes):
    quantidadeTotal = len(pessoasOrdenadas)
    quantidadeTimes = quantidadeTotal // quantidadePessoasTimes
    quantidadeExcedentes = quantidadeTotal % quantidadePessoasTimes

    if (quantidadeExcedentes):
        return f'Não é possivel fazer esse balanceamento pois temos {quantidadeExcedentes} jogadores excedente. Adicione mais {quantidadePessoasTimes - quantidadeExcedentes} jogador(es) para fazer o balanceamento'
    
    times = [[] for i in range(quantidadeTimes)]

    for i in range(quantidadePessoasTimes):
        for j in range(quantidadeTimes):
            if pessoasOrdenadas and len(times[j]) < quantidadePessoasTimes:
                if(len(times[j]) == 0):
                    times[j].append(pessoasOrdenadas.pop(0))
                else:
                    homens = sorted(filter(lambda p: p['sexo'] == 'M', pessoasOrdenadas), key=lambda p: p['media'])
                    mulheres = sorted(filter(lambda p: p['sexo'] == 'F', pessoasOrdenadas), key=lambda p: p['media'])
                    for pessoa in times[j]:
                        if pessoa['sexo'] == "M":
                            if mulheres:
                                times[j].append(mulheres.pop(len(mulheres)-1))
                        elif pessoa['sexo'] == "F":
                            if homens:
                                times[j].append(homens.pop(len(homens)-1))
                        
                        if len(times[j]) == quantidadePessoasTimes:
                            break

    return json.dumps(times)



@app.route('/')
def index():
    return '<h1 style="text-align: center;">Bem vindo à API</h1>'

@app.route('/', methods=['POST'])
def postBalanceamento():
    jogadores = request.json
    pessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    quantidadePessoasTimes = jogadores['PessoasPorTime']
    return balanceamento(pessoasOrdenadas, quantidadePessoasTimes)

@app.route('/misto', methods=['POST'])
def postBalanceamentoMisto():
    jogadores = request.json
    pessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    quantidadePessoasTimes = jogadores['PessoasPorTime']
    return balanceamentoMisto(pessoasOrdenadas, quantidadePessoasTimes)

if __name__ == "__main__":
    app.run(host='0.0.0.0')