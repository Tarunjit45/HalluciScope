def classify_root_cause(claim, verdict, reason):
    if verdict != "false":
        return None
    
    r = reason.lower()
    c = claim.lower()

    if "year" in r or "date" in r:
        return "temporal_assumption"
    elif "not found" in r or "not mentioned" in r:
        return "fabricated_detail"
    elif "contradicts" in r:
        return "context_misinterpretation"
    else:
        return "overgeneralization"