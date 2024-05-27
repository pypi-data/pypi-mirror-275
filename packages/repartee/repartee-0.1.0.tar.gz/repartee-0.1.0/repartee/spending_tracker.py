spending_data = []

def track_usage(model, tokens_used):
    token_price = 0.02  # This is an example, you would fetch the real price
    cost = tokens_used * token_price
    spending_data.append({
        'model': model,
        'tokens': tokens_used,
        'cost': cost
    })
