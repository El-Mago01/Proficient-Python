countries = [{"name": "Spain",
             "capital_city": "Madrid",
             "currency": "EUR"
            },
            {"name": "United States",
             "capital_city": "Washington",
             "currency": "USD"
            },
            {"name": "Canada",
             "capital_city": "Ottawa",
             "currency": "CAD"
            }
           ]


def write_country(country, capital_city):
    filename = country + ".txt"
    with open(filename, 'w') as fileobj:
        fileobj.write(capital_city)

def main():
    for country in countries:
        write_country(country['name'], country['capital_city'])


if __name__ == "__main__":
    main()
