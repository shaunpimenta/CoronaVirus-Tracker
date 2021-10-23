import requests
def  perform_requests(countryname):
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name": countryname
                   }

    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "f17c39953bmsh0007a4eeb456190p17a165jsne07150166036"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return response.json()
