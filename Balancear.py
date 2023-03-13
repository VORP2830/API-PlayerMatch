from flask import Flask, request
import copy
import json
import os

app = Flask(__name__)

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

def balanceamento_misto(pessoasOrdenadas, quantidadePessoasTimes):
    quantidadeTotal = len(pessoasOrdenadas)
    quantidadeTimes = quantidadeTotal // quantidadePessoasTimes
    quantidadeExcedentes = quantidadeTotal % quantidadePessoasTimes

    if (quantidadeExcedentes):
        return f'Não é possível fazer esse balanceamento pois temos {quantidadeExcedentes} jogadores excedentes. Adicione mais {quantidadePessoasTimes - quantidadeExcedentes} jogador(es) para fazer o balanceamento'

    homens = sorted([p for p in pessoasOrdenadas if p['sexo'] == 'M'], key=lambda p: p['media'], reverse=True)
    mulheres = sorted([p for p in pessoasOrdenadas if p['sexo'] == 'F'], key=lambda p: p['media'])

    if len(homens) != len(mulheres):
        return 'Não é possível balancear os times com a mesma quantidade de homens e mulheres, o numero de homens e mulheres devem ser iguais para isso'

    duplas = [(homens[i], mulheres[i]) for i in range(len(homens))]

    times = [[] for i in range(quantidadeTimes)]
    for i, dupla in enumerate(duplas):
        j = i % quantidadeTimes
        times[j].append(dupla)

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
    return balanceamento_misto(pessoasOrdenadas, quantidadePessoasTimes)

if __name__ == "__main__":
    app.run(host='0.0.0.0')