# Balanceamento de Times

Este projeto consiste em uma API construída em Flask para balancear times com base em uma lista de jogadores com suas respectivas notas médias.

## Como usar para balancear sem levar em conta o sexo

Para utilizar esta API, siga os seguintes passos:

1. Faça um POST para a rota `/` com um JSON no formato:

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
## Como usar o balanceamento lavando em conta o sexo:
1. Faça um POST para a rota `/misto` com o JSON no formato:

```
{
    "Pessoas": [
        {
            "nome": "Fulano",
            "media": 7.5,
            "sexo": "M"
        },
        {
            "nome": "Ciclano",
            "media": 8.0,
            "sexo": "M"
        },
        {
            "nome": "Beltrano",
            "media": 6.5,
            "sexo": "F"
        },
        {
            "nome": "Outro",
            "media": 9.0,
            "sexo": "F"
        }
    ],
    "PessoasPorTime": 2
}
```
2. A resposta será um JSON com os times balanceados levando em conta o sexo:

```
[
  [
      {
        "nome": "Ciclano",
        "media": 8,
        "sexo": "M"
      },
      {
        "nome": "Beltrano",
        "media": 6.5,
        "sexo": "F"
      }
  ],
  [
      {
        "nome": "Fulano",
        "media": 7.5,
        "sexo": "M"
      },
      {
        "nome": "Outro",
        "media": 9,
        "sexo": "F"
      }
  ]
]
```
