# Upsert Pandas

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/upsert-pandas)
[![PyPI - Version](https://img.shields.io/pypi/v/mni?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/mni/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/pyMNI?logo=ReadTheDocs&label=Read%20The%20Docs)](https://pyMNI.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/pyMNI/actions/workflows/publish-to-pypipoetry.yml/badge.svg)](https://github.com/michelmetran/pyMNI/actions/workflows/publish-to-pypipoetry.yml)

A função _Upsert_ é uma operação fundamental em bancos de dados e sistemas de gerenciamento de dados que combina as operações de _Update_ (Atualizar) e _Insert_ (Inserir) em uma única etapa atômica. O nome _Upsert_ é, literalmente, uma junção dos dois verbos.

<br>

---

## Objetivo da Função _Upsert_

O principal objetivo do _upsert_ é garantir que os dados de uma fonte de origem sejam sincronizados de forma eficiente com uma tabela de destino, sem gerar erros de duplicidade nas chaves primárias.

Ela funciona verificando a existência de um registro com base em uma Chave de Negócio (ou Chave Primária):

- SE o registro EXISTE na tabela de destino (_match_ na chave): Atualiza (Update) as colunas do registro existente com os novos valores da fonte de origem.

- SE o registro NÃO EXISTE na tabela de destino (não há _match_ na chave): Insere (_Insert_) o novo registro na tabela de destino.

<br>

---

## Cenários de Uso Comuns

O _Upsert_ é amplamente utilizado em Engenharia de Dados, ETL/ELT e _Data Warehousing_:

- Sincronização de Dados: É a base para manter tabelas de dimensão em _Data Warehouses_ atualizadas, garantindo que novos clientes sejam inseridos e que os dados de clientes existentes (como endereço ou nome) sejam corrigidos.
- Processamento de _Streams_: Em sistemas de processamento em tempo real (como _Apache Kafka_ ou _Flink_), o _Upsert_ é usado para garantir que o estado de uma entidade seja consistentemente atualizado, tratando eventos novos ou modificações.
- Pandas/PySpark: Em ambientes como _PySpark_ (com Delta Lake) ou Pandas, a lógica _Upsert_ é implementada para fundir (merge) DataFrames de forma eficiente.
