
def finance_agent(text):
    return f"Expense processed: {text}"

def inventory_agent(text):
    return f"Inventory updated: {text}"

def insight_agent(text):
    return "Basic insights generated"

def ai_insight_agent(expenses):
    if not expenses:
        return ["No data yet"]

    insights = []

    total = sum([e[0] for e in expenses])

    if total > 1000:
        insights.append("⚠️ High spending detected")

    # category analysis
    category_map = {}
    for amt, cat in expenses:
        category_map[cat] = category_map.get(cat, 0) + amt

    top_category = max(category_map, key=category_map.get)

    insights.append(f"💡 Highest spending in: {top_category}")

    if len(expenses) > 5:
        insights.append("📊 Frequent transactions detected")

    return insights
