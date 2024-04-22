import sqlite3


def fetch_all(db_name, table_name):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

    return rows


def receipts_expenses(balance, store_id_from, store_id_to, nomenclature_id, amount):
    # Прибавляем приход
    if store_id_to:
        balance.setdefault(store_id_to, {}).setdefault(nomenclature_id, 0)
        balance[store_id_to][nomenclature_id] += amount

    # Вычитаем расход
    if store_id_from:
        balance.setdefault(store_id_from, {}).setdefault(nomenclature_id, 0)
        balance[store_id_from][nomenclature_id] -= amount


# Забираем данные о перемещениях из БД
re_list = fetch_all('db.db', 'store_movement')

# Складываем весь приход и вычитаем весь расход
balance = {}
for i in re_list:
    receipts_expenses(balance, i[0], i[1], i[2], i[3])

print(balance)
