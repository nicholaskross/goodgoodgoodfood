import requests

def get_charity_name_and_url(shoppingCart):
    causes_table = {
        #Animals
        "Animal Rights, Welfare, and Services" : 2,
        "Wildlife Conservation" : 1,
        "Zoos and Aquariums": 32,

        #Arts, Culture, Humanities
        "Libraries, Historical Societies and Landmark Preservation" : 6,
        "Museums" : 3,
        "Performing Arts" : 4,
        "Public Broadcasting and Media" : 5,

        #Community Development
        "United Ways" : 42,
        "Jewish Federations" : 43,
        "Community Foundations" : 22,
        "Housing and Neighborhood Development" : 27,

        #Education
        "Early Childhood Programs and Services" : 36,
        "Youth Education Programs and Services" : 40,
        "Adult Education Programs and Services" : 39,
        "Special Education" : 38,
        "Education Policy and Reform" : 41,
        "Scholarship and Financial Support" : 37,

        #Environment
        "Environmental Protection and Conservation" : 11,
        "Botanical Gardens, Parks, and Nature Centers" : 10,

        #Health
        "Diseases, Disorders, and Disciplines" : 13,
        "Patient and Family Support" : 34,
        "Treatment and Prevention Services" : 12,
        "Medical Research" : 14,

        #Human and Civil Rights
        "Advocacy and Education" : 21,

        #Human Services
        "Children's and Family Services" : 17,
        "Youth Development, Shelter, and Crisis Services" : 16,
        "Food Banks, Food Pantries, and Food Distribution" : 18,
        "Multipurpose Human Service Organizations" : 15,
        "Homeless Services" : 28,
        "Social Services" : 29,

        #International
        "Development and Relief Services" : 20,
        "International Peace, Security, and Affairs" : 19,
        "Humanitarian Relief Supplies" : 30,

        #Research and Public Policy
        "Non-Medical Science & Technology Research" : 35,
        "Social and Public Policy Research" : 24,

        #Religion
        "Religious Activities" : 26,
        "Religious Media and Broadcasting" :25}

    weighting_tags = ["buyinginbulk", "eco"]

    #INSERT SHOPPING CART TESTS

    correlates_table = {
        "vegan" : "Animal Rights, Welfare, and Services",
        "eco" : "Environmental Protection and Conservation",
        "haschildren" : "Children's and Family Services",
        "hasmedicalcondition" : "Medical Research",
        "ethnicfoods" : "Humanitarian Relief Supplies",
        "buyinginbulk" : "Food Banks, Food Pantries, and Food Distribution",
        "lotsofseafood" : "Zoos and Aquariums",
        }

    potential_causes = []
    final_cause = ""

    for tag in weighting_tags:
        potential_causes.append(correlates_table[tag])

    final_cause = max(set(potential_causes), key=potential_causes.count)

    final_cause_id = causes_table[final_cause]

    charityParams = {"app_id":"adcbebfd", "app_key":"68bbeba05b4dd80d57ca19d79965e545", "pageSize":1, "sort":"RATING", "causeID" : str(final_cause_id)}

    charityData = requests.get("https://api.data.charitynavigator.org/v2/Organizations/", params=charityParams)

    the_url = charityData.json()[0]["websiteURL"]

    the_name = charityData.json()[0]["charityName"]
    return the_name, the_url

print(get_charity_name_and_url(0))
