def get_all_expenses():
    c.execute("SELECT amount, category FROM expenses")
    return c.fetchall()


def get_category_summary():
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    return c.fetchall()
