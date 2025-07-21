# serenity_core.py

import datetime
import random

# Map 1–5 mood scale to descriptive labels
mood_labels = {
    1: "Very Low",
    2: "Low",
    3: "Neutral",
    4: "High",
    5: "Very High"
}

# Coping strategies keyed by symptom and time of day
coping_strategies = {
    "anxiety": {
        "morning": [
            "5-minute guided breathing",
            "short mindfulness walk"
        ],
        "afternoon": [
            "grounding exercise (5-4-3-2-1)",
            "stretching break"
        ],
        "evening": [
            "progressive muscle relaxation",
            "guided imagery"
        ],
        "night": [
            "body scan meditation",
            "light journaling"
        ]
    },
    "depression": {
        "morning": [
            "gratitude journaling",
            "sunlight exposure (10 min)"
        ],
        "afternoon": [
            "uplifting music mini-break",
            "positive affirmation list"
        ],
        "evening": [
            "gentle yoga flow",
            "creative doodling"
        ],
        "night": [
            "reflective journaling",
            "guided sleep meditation"
        ]
    },
    "stress": {
        "morning": [
            "deep breathing sequence",
            "prioritize today’s tasks"
        ],
        "afternoon": [
            "short walk outside",
            "5-min desk stretch"
        ],
        "evening": [
            "aromatherapy with lavender",
            "light reading break"
        ],
        "night": [
            "body scan meditation",
            "prepare tomorrow’s plan"
        ]
    }
}

# Encouragement badges for peer Check-In Circles
encouragement_badges = [
    "🌟 You’ve got this!",
    "👏 Keep going!",
    "💪 Stay strong!",
    "👍 Proud of you!"
]

# Sample resource hub by state code
resource_hub = {
    "NY": [
        {"name": "NYU Counseling Center", "url": "https://counseling.nyu.edu"},
        {"name": "Crisis Text Line", "url": "https://www.crisistextline.org"}
    ],
    "GA": [
        {"name": "Emory University Counseling Center", "url": "https://counseling.emory.edu"},
        {"name": "Georgia Crisis & Access Line (GCAL)", "url": "https://gacal.ga.gov/"},
        {"name": "Mental Health America of Georgia", "url": "https://www.mhageorgia.org/"}
    ]
}


def get_time_bucket(hour: int) -> str:
    """
    Determine time of day bucket from hour.
    """
    if 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

def get_mood_label(score: int) -> str:
    """
    Convert a 1–5 mood score to a descriptive label.
    """
    return mood_labels.get(score, "Unknown")

def suggest_coping_strategies(symptoms: list, mood_score: int, when: datetime.datetime = None) -> dict:
    """
    Given a list of symptoms and a mood score, return tailored coping strategies,
    peer encouragement badges, and local resources.
    """
    if when is None:
        when = datetime.datetime.now()
    time_bucket = get_time_bucket(when.hour)
    mood_label = get_mood_label(mood_score)

    # Gather strategies for each symptom
    strategies = []
    for symptom in symptoms:
        symptom = symptom.lower()
        options = coping_strategies.get(symptom, {})
        strategies.extend(options.get(time_bucket, []))

    # Limit to 5 unique strategies
    unique_strats = list(dict.fromkeys(strategies))[:5]

    # Randomly pick 2 encouragement badges
    badges = random.sample(encouragement_badges, k=2)

    # Lookup resources by user's state code (placeholder; replace with real geo lookup)
    state_code = getattr(when, 'state_code', None) or "NY"
    resources = resource_hub.get(state_code, [])

    return {
        "time_of_day": time_bucket.title(),
        "mood_label": mood_label,
        "strategies": unique_strats,
        "encouragement_badges": badges,
        "resources": resources
    }

# Example usage
if __name__ == "__main__":
    now = datetime.datetime.now()
    rec = suggest_coping_strategies(
        symptoms=["Anxiety", "Stress"],
        mood_score=2,
        when=now
    )
    print(f"🕒 Time: {rec['time_of_day']}")
    print(f"😊 Mood: {rec['mood_label']}")
    print("🛠️ Strategies:")
    for s in rec["strategies"]:
        print(f"  - {s}")
    print("🏅 Encouragement:")
    for b in rec["encouragement_badges"]:
        print(f"  - {b}")
    print("📚 Resources:")
    for r in rec["resources"]:
        print(f"  - {r['name']}: {r['url']}")
