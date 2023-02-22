import requests

DAD_JOKER = 'https://icanhazdadjoke.com/'
DAD_jokes_search_url = f'{DAD_JOKER}/search'
def main():

    joke = get_random_dad_joke()
    print(joke)

    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list)
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes 

    Args:
        search_term (_type_): _description_

    Returns:
        _type_: _description_
    """
    header_params = {
        'Accept': 'application/json' 
    }
    
    #setup the query string params
    query_string_params = {
        'term': search_term
    }

    print(f'Sending DAD jokes... "{search_term}" jokes..', end='')
    resp_msg = requests.get(DAD_jokes_search_url, headers=header_params, params=query_string_params)

    
    #check wheather the GET request was sucessfull
    if resp_msg.ok:
        print("Sucess")
        body_dict = resp_msg.json()
        jokes_portion = body_dict['results']
        Jokes_list = [j['joke'] for j in jokes_portion]
        return Jokes_list
    else:
        print("Failure")
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason : {resp_msg.text}')

    return

def get_random_dad_joke():
    """Gets a random dad jokes

    Returns:
        str: Dad jokes
    """
    #seting up the header parameter
    header_params = {
        'Accept': 'application/json' 

    }

    print('Sending get request...', end='')
    resp_msg = requests.post(DAD_JOKER, headers=header_params)

    
    #check wheather the GET request was sucessfull
    if resp_msg.ok:
        print("Sucess")
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    else:
        print("Failure")
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason : {resp_msg.text}')


    return

if __name__ == '__main__':
    main()