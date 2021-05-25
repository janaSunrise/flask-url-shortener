from importlib import import_module


def bring_databases_into_scope():
    from app.core import loader

    loaded_tables = []

    for table in loader.DATABASES:
        imported_table = import_module(table)
        loaded_tables.append(imported_table)

    return loaded_tables
