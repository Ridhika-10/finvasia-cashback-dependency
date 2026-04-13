def micro_invest(data):
    # Replace cashback with investment
    cashback = data.get("cashback", 0)
    return cashback * 1.2   # invest + bonus growth idea

def growth_score(data):
    savings = data.get("savings", 0)
    spending = data.get("spending", 1)

    score = (savings / (savings + spending)) * 100
    return round(score, 2)

def saving_trigger(data):
    spending = data.get("spending", 0)

    if spending > 5000:
        return "⚠️ High spending! Save at least ₹500 today."
    return "✅ You're doing well!"

def milestones(score):
    if score > 70:
        return "🏆 Wealth Master"
    elif score > 40:
        return "🥈 Smart Saver"
    else:
        return "🥉 Beginner"