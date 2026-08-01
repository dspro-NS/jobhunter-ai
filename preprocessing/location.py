INDIA_KEYWORDS = [
    "india",
    "bangalore",
    "bengaluru",
    "hyderabad",
    "pune",
    "mumbai",
    "gurgaon",
    "gurugram",
    "noida",
    "delhi",
    "chennai",
    "kolkata",
    "ahmedabad",
    "coimbatore",
    "kochi",
    "remote - india",
    "india remote",
    "remote, india",
]


def is_india_job(location):
    if not location:
        return False

    location = location.lower()

    return any(keyword in location for keyword in INDIA_KEYWORDS)