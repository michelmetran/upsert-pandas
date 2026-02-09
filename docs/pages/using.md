# Como Usar?

Inicialmente importamos as bibliotecas.

```python
import pandas as pd

import upsert_pandas as upd
```

<br>

Inicialmente criamos uma tabela aleatória.

```python
# Criando uma lista de dicionários (cada dict é uma linha)
lista_pessoas = [
    {"Nome": "Ana Silva", "Idade": 28, "Endereço": "Rua das Flores, 123"},
    {"Nome": "Bruno Costa", "Idade": 34, "Endereço": "Av. Paulista, 1500"},
    {"Nome": "Carla Souza", "Idade": 22, "Endereço": "Rua Chile, 45"},
    {"Nome": "Diego Lima", "Idade": 45, "Endereço": "Praça da Sé, 10"},
    {"Nome": "Elena Rocha", "Idade": 30, "Endereço": "Al. dos Anjos, 99"},
]

# O pandas entende automaticamente que as chaves são as colunas
df = pd.DataFrame(lista_pessoas)

# Results
df.info()
df.head()
```

<br>

Tem uma segunda tabela, contendo novo registro/endereço para "Diogo Lima".

```python
lista_pessoas = [
    {
        "Nome": "Diego Lima",
        "Idade": 45,
        "Endereço": "Rua Almirante Barroso, 451",
    },
]
df_new = pd.DataFrame(lista_pessoas)

# Results
df_new.info()
df_new.head()
```

<br>

Fazemos o _upsert_ e o registro para "Diogo Lima" foi alterado.

```python
# Upsert
df = upd.upsert(
    df_existing=df,
    df_new=df_new,
    on='Nome',
    only_non_null=False,
)

# Results
df.info()
df.head()
```
