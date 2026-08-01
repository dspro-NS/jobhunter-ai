from database.crud import add_company

companies = [

    {
        "name":"Databricks",
        "url":"https://www.databricks.com/company/careers",
        "ats":"greenhouse",
        "country":"India"
    },

    {
        "name":"Stripe",
        "url":"https://stripe.com/jobs",
        "ats":"greenhouse",
        "country":"India"
    }

]

for company in companies:

    add_company(
        company["name"],
        company["url"],
        company["ats"],
        company["country"]
    )