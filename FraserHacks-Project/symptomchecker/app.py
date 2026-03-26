from database import SYMPTOMS, CONDITIONS, RED_FLAG_RULES

TRIAGE_PRIORITY = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "emergency": 4
}

def score_conditions(selected_symptoms):
    results = []

    for condition in CONDITIONS:
        score = 0
        matched = []

        for symptom, weight in condition["symptoms"].items():
            if symptom in selected_symptoms:
                score += weight
                matched.append(symptom)

        if score > 0:
            results.append({
                "name": condition["name"],
                "description": condition["description"],
                "triage": condition["triage"],
                "advice": condition["advice"],
                "score": score,
                "matched_symptoms": matched
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def check_red_flags(selected_symptoms):
    matched_rules = []

    for rule in RED_FLAG_RULES:
        if all(symptom in selected_symptoms for symptom in rule["trigger_symptoms"]):
            matched_rules.append(rule)

    if not matched_rules:
        return None

    matched_rules.sort(key=lambda r: TRIAGE_PRIORITY[r["triage"]], reverse=True)
    return matched_rules[0]

def get_final_triage(condition_results, red_flag):
    highest = "low"

    for result in condition_results:
        if TRIAGE_PRIORITY[result["triage"]] > TRIAGE_PRIORITY[highest]:
            highest = result["triage"]

    if red_flag and TRIAGE_PRIORITY[red_flag["triage"]] > TRIAGE_PRIORITY[highest]:
        highest = red_flag["triage"]

    return highest