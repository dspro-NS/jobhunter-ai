from discovery.ats_detector import detect_ats


def discover_companies():
    companies = [
    {
        "name": "Stripe",
        "careers_url": "https://stripe.com/jobs",
        "board": "stripe",
        "ats": "greenhouse",   # temporary
    }
    ]

    return companies


if __name__ == "__main__":
    companies = discover_companies()

    print(f"Found {len(companies)} companies")

    for company in companies:
        company["ats"] = detect_ats(company["careers_url"])
        print(company["ats"])
        