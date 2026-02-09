"""
Módulo
"""

from typing import List, Union

import numpy as np
import pandas as pd


def upsert(
    df_existing: pd.DataFrame,
    df_new: pd.DataFrame,
    on: Union[str, List[str]],
    only_non_null: bool = True,
    include_new_columns: bool = False,
) -> pd.DataFrame:
    """
    Upsert `df_new` into `df_existing` using key column(s) `on`.

    - Atualiza apenas colunas que existem em ambos os dataframes (exceto as chaves).
    - `only_non_null=True` (padrão) faz com que valores NaN em df_new NÃO sobrescrevam valores em df_existing.
    - `include_new_columns=False` (padrão) para novas linhas adicionadas, mantém apenas colunas de df_existing;
      se True, adiciona também colunas novas vindas de df_new.

    Retorna um novo DataFrame resultado do upsert (não modifica os inputs).
    """
    if isinstance(on, str):
        on = [on]

    # Cópias para não modificar originais
    existing = df_existing.copy()
    new = df_new.copy()

    # Colunas chave não serão atualizadas
    keys = list(on)

    # Preparar índices
    existing_idx = existing.set_index(keys, drop=False)
    new_idx = new.set_index(keys, drop=False)

    # Determinar colunas comuns a atualizar (excluindo chaves)
    common_cols = [
        c for c in existing.columns if c in new.columns and c not in keys
    ]
    # print(common_cols)

    # Atualizar linhas existentes
    rows_to_update = new_idx.index.intersection(existing_idx.index)
    if len(rows_to_update) > 0 and len(common_cols) > 0:
        to_update = new_idx.loc[rows_to_update, common_cols]

        if only_non_null:
            # Para cada coluna, aplique apenas onde df_new não é nulo
            for col in common_cols:
                vals = to_update[col]
                non_null = vals[vals.notna()]
                if not non_null.empty:
                    existing_idx.loc[non_null.index, col] = non_null
        else:
            # sobrescreve (incluindo NaN)
            # existing_idx.update(to_update)

            # NOVO AJUSTE: Sobrescreve TUDO (incluindo NaN e NaT).
            # Usa atribuição direta via .loc em vez de .update().
            existing_idx.loc[rows_to_update, common_cols] = to_update.values
            # NOTA: Usar .values para evitar problemas de alinhamento de índice
            # e garantir que os nulos sejam passados.

    # Inserir novas linhas vindas de df_new
    new_rows_index = new_idx.index.difference(existing_idx.index)
    if len(new_rows_index) > 0:
        new_rows = new_idx.loc[new_rows_index]
        if not include_new_columns:
            # alinhar colunas às do existing
            cols = existing_idx.columns
            # reindex as colunas (mantém as chaves)
            new_rows = new_rows.reindex(columns=cols, fill_value=np.nan)
        # concat mantendo a ordem: existing primeiro, depois novas
        existing_idx = pd.concat([existing_idx, new_rows], axis=0, sort=False)

    # Reset index e retornar
    result = existing_idx.reset_index(drop=True)
    return result
