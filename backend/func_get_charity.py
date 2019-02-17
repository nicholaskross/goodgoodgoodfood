import requests

def get_charity_name_and_url(shoppingCart, pc):
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

    actual_items_info = []
    for item in shoppingCart:
        actual_items_info.append(pc.get_sku(item))

    weighting_tags = []
    if len(actual_items_info)>=10:
        weighting_tags.append("buyinginbulk")
    for food in shoppingCart:
        if !("eco" not in food.description):
            weighting_tags.append("eco")
    for food in shoppingCart:
        if !("kid" not in food.description):
            weighting_tags.append("haschildren")
    for food in shoppingCart:
        if !("health" not in food.description):
            weighting_tags.append("hasmedicalcondition")
    seafoodcount = 0
    for food in shoppingCart:
        if !("fish" not in food.name && "salmon" not in food.name && "tilapia" not in food.name && "shrimp" not in food.name && "filet" not in food.name && "cod" not in food.name && "lobster" not in food.name && "crab" not in food.name):
            seafoodcount+=1
    if seafoodcount>=2:
        weighting_tags.append("lotsofseafood")
    vegan=True
    if seafoodcount>0:
        vegan = False
    for food in shoppingCart:
        if !("beef" not in food.description && "chicken" not in food.description && "pork" not in food.description && "bacon" not in food.description && "egg" not in food.description && "dairy" not in food.description && "veal" not in food.description):
            vegan=False
    if vegan:
        weighting_tags.append("vegan")
    #ethnicfoodcount = 0
    #for food in shoppingCart:
        #if food.countryOfOrigin != null:
            #ethnicfoodcount+=1
    #if ethnicfoodcount>=2:
        #weighting_tags.append("ethnicfoods")

    correlates_table = {
        "vegan" : "Animal Rights, Welfare, and Services",
        "eco" : "Environmental Protection and Conservation",
        "haschildren" : "Children's and Family Services",
        "hasmedicalcondition" : "Medical Research",
        "buyinginbulk" : "Food Banks, Food Pantries, and Food Distribution",
        "lotsofseafood" : "Zoos and Aquariums",
        }
    #"ethnicfoods" : "Humanitarian Relief Supplies",

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
