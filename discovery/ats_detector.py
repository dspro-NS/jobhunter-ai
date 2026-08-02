import requests

ATS_PATTERNS = {
    "greenhouse": "greenhouse",
    "lever": "lever",
    "myworkdayjobs": "workday",
    "ashbyhq": "ashby",
    "smartrecruiters": "smartrecruiters",
    "icims": "icims",
    "taleo": "taleo",
    "successfactors": "successfactors",
}


def detect_ats(careers_url: str) -> str | None:
    """
    Detect which ATS powers a careers page.
    """

    try:
        response = requests.get(careers_url, timeout=10)
        response.raise_for_status()
        html = response.text.lower()

    except Exception:
        return None

    for pattern, ats in ATS_PATTERNS.items():
        if pattern in html:
            return ats

    return None