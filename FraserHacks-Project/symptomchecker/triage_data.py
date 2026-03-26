SYMPTOMS = [
    "fever",
    "cough",
    "sore_throat",
    "runny_nose",
    "fatigue",
    "headache",
    "nausea",
    "vomiting",
    "diarrhea",
    "abdominal_pain",
    "chest_pain",
    "shortness_of_breath",
    "dizziness",
    "rash",
    "body_aches",
    "chills",
    "loss_of_taste_smell",
    "sneezing",
    "ear_pain",
    "blurred_vision"
]

CONDITIONS = [
    {
        "name": "Common Cold",
        "description": "A mild viral upper respiratory illness.",
        "triage": "low",
        "advice": "Rest, drink fluids, and monitor symptoms.",
        "symptoms": {
            "cough": 2,
            "sore_throat": 2,
            "runny_nose": 3,
            "fatigue": 1,
            "sneezing": 2
        }
    },
    {
        "name": "Influenza (Flu)",
        "description": "A viral illness that often causes fever, chills, and body aches.",
        "triage": "medium",
        "advice": "Rest, hydrate, and consider seeing a doctor if symptoms worsen.",
        "symptoms": {
            "fever": 3,
            "cough": 2,
            "fatigue": 2,
            "headache": 2,
            "body_aches": 3,
            "chills": 2,
            "sore_throat": 1
        }
    },
    {
        "name": "COVID-like Viral Illness",
        "description": "A viral respiratory illness pattern.",
        "triage": "medium",
        "advice": "Rest, hydrate, and monitor breathing. Seek care if symptoms worsen.",
        "symptoms": {
            "fever": 2,
            "cough": 2,
            "fatigue": 2,
            "shortness_of_breath": 3,
            "loss_of_taste_smell": 3,
            "headache": 1,
            "sore_throat": 1
        }
    },
    {
        "name": "Migraine",
        "description": "A headache disorder that may include nausea, dizziness, or vision changes.",
        "triage": "medium",
        "advice": "Rest in a dark quiet room and seek care if severe or unusual.",
        "symptoms": {
            "headache": 3,
            "nausea": 2,
            "vomiting": 1,
            "dizziness": 1,
            "blurred_vision": 2
        }
    },
    {
        "name": "Gastroenteritis",
        "description": "An illness causing vomiting, diarrhea, and stomach upset.",
        "triage": "medium",
        "advice": "Hydrate well and seek care if unable to keep fluids down.",
        "symptoms": {
            "nausea": 2,
            "vomiting": 3,
            "diarrhea": 3,
            "abdominal_pain": 2,
            "fever": 1,
            "fatigue": 1
        }
    },
    {
        "name": "Food Poisoning Pattern",
        "description": "Digestive symptoms possibly linked to contaminated food.",
        "triage": "medium",
        "advice": "Hydrate and monitor. Seek care for worsening symptoms or dehydration.",
        "symptoms": {
            "nausea": 2,
            "vomiting": 3,
            "diarrhea": 3,
            "abdominal_pain": 3,
            "fever": 1
        }
    },
    {
        "name": "Allergic Reaction Pattern",
        "description": "A symptom pattern involving rash and upper airway irritation.",
        "triage": "medium",
        "advice": "Seek medical attention if symptoms worsen or breathing becomes difficult.",
        "symptoms": {
            "rash": 3,
            "sneezing": 2,
            "runny_nose": 1,
            "shortness_of_breath": 3
        }
    },
    {
        "name": "Strep-like Throat Infection",
        "description": "A throat-focused infection pattern with fever and sore throat.",
        "triage": "medium",
        "advice": "Consider medical evaluation, especially if throat pain and fever are significant.",
        "symptoms": {
            "fever": 2,
            "sore_throat": 3,
            "headache": 1,
            "fatigue": 1
        }
    },
    {
        "name": "Ear Infection Pattern",
        "description": "An ENT-related symptom pattern often involving ear pain.",
        "triage": "medium",
        "advice": "Seek medical care if pain is severe, persistent, or paired with fever.",
        "symptoms": {
            "ear_pain": 3,
            "fever": 1,
            "headache": 1,
            "sore_throat": 1
        }
    },
    {
        "name": "Possible Pneumonia Pattern",
        "description": "A more serious respiratory symptom pattern.",
        "triage": "high",
        "advice": "Prompt medical evaluation is recommended.",
        "symptoms": {
            "fever": 2,
            "cough": 3,
            "shortness_of_breath": 3,
            "chills": 2,
            "fatigue": 2,
            "chest_pain": 2
        }
    },
    {
        "name": "Possible Cardiac Emergency Pattern",
        "description": "A high-risk symptom pattern involving chest discomfort and breathing difficulty.",
        "triage": "emergency",
        "advice": "Seek emergency medical attention immediately.",
        "symptoms": {
            "chest_pain": 3,
            "shortness_of_breath": 3,
            "dizziness": 2,
            "fatigue": 1
        }
    }
]

RED_FLAG_RULES = [
    {
        "name": "Chest pain emergency",
        "trigger_symptoms": ["chest_pain", "shortness_of_breath"],
        "triage": "emergency",
        "message": "Chest pain with shortness of breath may require emergency care."
    },
    {
        "name": "Breathing difficulty",
        "trigger_symptoms": ["shortness_of_breath"],
        "triage": "high",
        "message": "Shortness of breath is a high-priority symptom."
    },
    {
        "name": "Dehydration risk",
        "trigger_symptoms": ["vomiting", "diarrhea", "dizziness"],
        "triage": "high",
        "message": "Vomiting and diarrhea with dizziness may indicate dehydration."
    },
    {
        "name": "Fever with rash",
        "trigger_symptoms": ["fever", "rash"],
        "triage": "high",
        "message": "Fever with rash should be assessed promptly."
    },
    {
        "name": "Flu-like syndrome",
        "trigger_symptoms": ["fever", "cough", "fatigue", "body_aches"],
        "triage": "medium",
        "message": "This group of symptoms may need medical review if worsening."
    }
]