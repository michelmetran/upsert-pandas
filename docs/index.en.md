# _Upsert_ Pandas

[![Repo](https://img.shields.io/badge/GitHub-repo-blue?logo=github&logoColor=f5f5f5)](https://github.com/michelmetran/upsert-pandas)
[![PyPI - Version](https://img.shields.io/pypi/v/upsert-pandas?logo=pypi&label=PyPI&color=blue)](https://pypi.org/project/upsert-pandas/)<br>
[![Read the Docs](https://img.shields.io/readthedocs/upsert-pandas?logo=ReadTheDocs&label=Read%20The%20Docs)](https://upsert-pandas.readthedocs.io/)
[![Publish Python to PyPI](https://github.com/michelmetran/upsert-pandas/actions/workflows/publish-to-pypi-uv.yml/badge.svg)](https://github.com/michelmetran/upsert-pandas/actions/workflows/publish-to-pypi-uv.yml)

The Upsert function is a fundamental operation in databases and data management systems that combines the Update and Insert operations into a single atomic step. The name Upsert is, literally, a join of the two verbs.

<br>

---

## Purpose of the Upsert Function

The main purpose of the upsert is to ensure that data from a source is efficiently synchronized with a target table, without causing duplicate primary key errors.

It works by checking for the existence of a record based on a Business Key (or Primary Key):

- IF the record EXISTS in the target table (key match): Updates the existing record's columns with the new values from the source.

- IF the record does NOT EXIST in the target table (no key match): Inserts the new record into the target table.

<br>

---

## Common Use Cases

Upsert is widely used in Data Engineering, ETL/ELT and Data Warehousing:

- Data Synchronization: It is the basis for keeping dimension tables in Data Warehouses up to date, ensuring that new customers are inserted and that existing customer data (such as address or name) is corrected.
- Stream Processing: In real-time processing systems (such as Apache Kafka or Flink), Upsert is used to ensure that an entity's state is consistently updated, handling new events or modifications.
- Pandas/PySpark: In environments such as PySpark (with Delta Lake) or Pandas, Upsert logic is implemented to efficiently merge DataFrames.
