import requests

def cases_by_country(country):
    covid_url = "https://covid-api.mmediagroup.fr/v1/cases"
    params = {
        "country": country,
    }

    try:
            result = requests.get(covid_url, params = params)
            result.raise_for_status()
            covid_data = result.json()
            if 'All' in covid_data:
                try:
                    return covid_data['All']
                except(IndexError,TypeError):
                    return False 
    except(requests.RequestException, ValueError):
            print('Ошибка сети')
            return False
    return False

if __name__ == "__main__":
    country_data = cases_by_country("France")
    print(country_data)
