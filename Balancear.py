from flask import Flask, request
import copy
import json


app = Flask(__name__)


def balanceamento(PessoasOrdenadas, QuantidadePessoasTimes):
    QuantidadeTotal = len(PessoasOrdenadas)
    QuantidadeTimes = QuantidadeTotal // QuantidadePessoasTimes
    QuantidadeExcedentes = QuantidadeTotal % QuantidadePessoasTimes

    if (QuantidadeExcedentes):
        return f'Não é possivel fazer esse balanceamento pois temos {QuantidadeExcedentes} jogadores excedente. Adicione mais {QuantidadePessoasTimes - QuantidadeExcedentes} jogador(es) para fazer o balanceamento'
    
    Times = [[] for i in range(QuantidadeTimes)]

    for i in range(QuantidadePessoasTimes):
        for j in range(QuantidadeTimes):
            if PessoasOrdenadas:
                if(len(Times[j]) > 0):
                    Times[j].append(PessoasOrdenadas.pop(len(PessoasOrdenadas)-1))
                Times[j].append(PessoasOrdenadas.pop(0))
        

    while PessoasOrdenadas:
        TimeMenorMedia = min(Times, key=lambda x: sum(p['media'] for p in x))
        PessoaRestante = PessoasOrdenadas.pop(0)
        TimeComNovaPessoa = copy.deepcopy(TimeMenorMedia)
        TimeComNovaPessoa.append(PessoaRestante)

    return json.dumps(Times)


@app.route('/')
def index():
    return '<h1 style="text-align: center;">Bem vindo à API</h1>'

@app.route('/', methods=['POST'])
def PostBalanceamento():
    jogadores = request.json
    PessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    QuantidadePessoasTimes = jogadores['PessoasPorTime']
    return balanceamento(PessoasOrdenadas, QuantidadePessoasTimes)

app.run()