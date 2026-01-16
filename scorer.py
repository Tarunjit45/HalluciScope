def calculate_score(claims):
    if not claims:
        return 0.0
    
    # We use .get() to look for 'conf'. If the LLM misses it, we default to 0.7
    false_weight = sum(c.get('conf', 0.7) for c in claims if c.get('verdict') == 'false')
    total_weight = sum(c.get('conf', 0.7) for c in claims)
    
    if total_weight == 0:
        return 0.0
        
    return round(false_weight / total_weight, 2)