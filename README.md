# Balanceamento de Times

Este projeto consiste em uma API construída em Flask para balancear times com base em uma lista de jogadores com suas respectivas notas médias.

## Como usar

Para utilizar esta API, siga os seguintes passos:

1. Faça um POST para a rota `/balanceamento` com um JSON no formato:

```
{
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
```

2. A resposta será um JSON contendo os times balanceados:

```

[
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
```


