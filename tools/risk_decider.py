def decide_risk_level(analysis_result):
    if analysis_result == "small":
        return "Low Risk"
    elif analysis_result == "medium":
        return "Medium Risk"
    elif analysis_result == "large":
        return "High Risk"
    else:
        return "Unknown Risk"