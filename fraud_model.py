def check_for_anomalies(extracted_data):
    # You will implement logic later to detect issues like:
    # - Income mismatch
    # - Suspicious patterns
    return {
        "risk_score": 0.7,
        "flags": ["Possible income mismatch", "Missing KYC"]
    }
def check_for_anomalies(data):
    flags = []
    risk_score = 0

    # Basic checks
    declared_income = data.get("declared_income")
    credited_income = data.get("credited_income")
    avg_balance = data.get("average_balance", 0)
    pan_present = data.get("pan_found", False)

    # Income mismatch check
    if declared_income and credited_income:
        diff = abs(declared_income - credited_income)
        if diff > 0.2 * declared_income:
            flags.append("Income mismatch")
            risk_score += 0.3

    # Low average balance
    if avg_balance < 1000:
        flags.append("Low average balance")
        risk_score += 0.2

    # PAN not found
    if not pan_present:
        flags.append("Missing PAN card")
        risk_score += 0.2

    # Final score cap
    risk_score = min(risk_score, 1.0)

    return {
        "risk_score": round(risk_score, 2),
        "flags": flags
    }


