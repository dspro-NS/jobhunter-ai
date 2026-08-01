from scoring.relevance import is_relevant

titles = [
    "Senior Data Scientist",
    "Software Engineer",
    "AI Research Scientist",
    "Product Manager",
    "ML Engineer",
    "Sales Executive",
]

for title in titles:
    print(title, "->", is_relevant(title))