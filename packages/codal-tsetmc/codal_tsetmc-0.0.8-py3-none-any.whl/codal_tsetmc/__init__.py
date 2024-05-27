import os

from .config.engine import HOME_PATH, CDL_TSE_FOLDER, default_db_path, CONFIG_PATH
from .models.create import models
from .tools.database import read_table_by_conditions
from .models.stocks import Stocks
from .models.companies import Companies
from .download.codal.query import CodalQuery

from .config import engine as db
from .initializer import (
    init_db,
    init_table,
    fill_db,
    fill_companies_table,
    fill_categories_table,
    fill_interim_financial_statements_letters,
    fill_stocks_table,
    fill_stocks_prices_table,
    fill_stocks_capitals_table,
    fill_commodities_prices_table,
)


def db_is_empty():
    try:
        for table in models:
            db.session.execute(f"select * from {table.__tablename__} limit 1;")

        return False
    except Exception as e:
        print(e.__context__)
        return True
    finally:
        pass


if db_is_empty():
    init_db()
    init_table()
