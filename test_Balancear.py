import json
import pytest
from Balancear import balanceamento, app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_balanceamento():
    jogadores = {
    "Pessoas": [
        {
            "nome": "Fulano",
            "media": 7.5
        },
        {
            "nome": "Ciclano",
            "media": 8.0
        },
        {
            "nome": "Beltrano",
            "media": 6.5
        },
        {
            "nome": "Outro",
            "media": 9.0
        }
    ],
    "PessoasPorTime": 2
}
    pessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    quantidadePessoasTimes = jogadores['PessoasPorTime']
    times = balanceamento(pessoasOrdenadas, quantidadePessoasTimes)
    assert isinstance(json.loads(times), list)

def test_post_balanceamento(client):
    jogadores = {
        "Pessoas": [
            {
                "nome": "Fulano",
                "media": 7.5
            },
            {
                "nome": "Ciclano",
                "media": 8.0
            },
            {
                "nome": "Beltrano",
                "media": 6.5
            },
            {
                "nome": "Outro",
                "media": 9.0
            }
        ],
        "PessoasPorTime": 2
    }

    expected_output = [
        [
            {
                "nome": "Outro",
                "media": 9.0
            },
            {
                "nome": "Beltrano",
                "media": 6.5
            }
        ],
        [
            {
                "nome": "Ciclano",
                "media": 8.0
            },
            {
                "nome": "Fulano",
                "media": 7.5
            }
        ]
    ]

    response = client.post('/', json=jogadores)
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)
    assert json.loads(response.data) == expected_output

def test_balanceamento_errado():
    jogadores = {
    "Pessoas": [
        {
            "nome": "Fulano",
            "media": 7.5
        },
        {
            "nome": "Ciclano",
            "media": 8.0
        },
        {
            "nome": "Beltrano",
            "media": 6.5
        }
    ],
    "PessoasPorTime": 2
}
    pessoasOrdenadas = sorted(jogadores['Pessoas'], key=lambda x: x["media"], reverse=True)
    quantidadePessoasTimes = jogadores['PessoasPorTime']
    times = balanceamento(pessoasOrdenadas, quantidadePessoasTimes)
    assert u'Não é possivel fazer esse balanceamento pois temos 1 jogadores excedente. Adicione mais 1 jogador(es) para fazer o balanceamento' in times