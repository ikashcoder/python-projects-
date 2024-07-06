
travel_city =[
    {
        "city":"Pune",
        "visit":10,
        "spots":["kotharud","Pimpari","Nigadi"]
    },
    {
        "city":"Mumbai",
        "visit":3,
        "spots":"Marien"
    }
    
]


def Add_Traval_city(city,visit,spots):
    new_city={}
    
    new_city["city"]=city
    new_city["visit"]=visit
    new_city["spots"]=spots
    
    travel_city.append(new_city)
    

Add_Traval_city("Nagpur",4,"slam city")

print(travel_city)    