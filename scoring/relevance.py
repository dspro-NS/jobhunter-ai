DATA_KEYWORDS = [
    "data scientist",
    "machine learning",
    "ml engineer",
    "ai engineer",
    "research scientist",
    "analytics",
    "data analyst",
    "decision scientist",
    "quantitative",
    "computer vision",
    "nlp",
    "genai",
    "llm",
    "applied scientist"
]


def is_relevant(title):
    title = title.lower()

    return any(keyword in title for keyword in DATA_KEYWORDS)