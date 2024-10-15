import requests


# function for getting a joke
def get_chuck_norris_joke() -> str:
    try:
        answer = requests.get("http://api.chucknorris.io/jokes/random")
        if answer.status_code == 200:
            json_answer = answer.json()
            return json_answer["value"]
    except requests.RequestException as e:
        if __debug__:
            print(e)
    raise Exception("Request Failed")


# checking all the errors in main is probably better
def get_chuck_norris_joke_better_error_handling() -> str:
    answer = requests.get("http://api.chucknorris.io/jokes/random")
    answer.raise_for_status()  # better way to check for requests errors
    json_answer = answer.json()
    return json_answer["value"]


def main() -> None:
    # we have try catch loop in main to catch all errors
    try:
        print(get_chuck_norris_joke_better_error_handling())
    except Exception as e:
        if __debug__:
            print(e)
        else:
            print("Request Failed")


if __name__ == "__main__":
    main()
    input("Press Enter")

# extra joke
# I have a joke about UDP, but I don't you would get it.
