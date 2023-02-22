import requests

Developer_KEY = 'Y5DfshF3j_GCndPe1stATo5iIVI1Wzl-'
Pastein_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("This is title", "This \nis \nbody", '1H', True)
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration = '10M', listed = False):
    """Posts a new public paste to Pastbin

    Args:
        title (str): _description_
        body_text (str): _description_
        expiration (str, optional): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y) Defaults to '10M'.
        listed (bool, optional): Wheather paste is publicly listed (True) or not (False). Defaults to True.

    Returns:
        str: URL of the new paste, if sucessfull. None if unsucessfull.
    """
    # setup the parameters for the request messsage
    paste_params ={
        'api_dev_key': Developer_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : expiration,
        'api_paste_private' : 0 if listed else 1
    }
    print('Posting new paste to PasteBin...', end='')
    resp_msg = requests.post(Pastein_API_URL, data=paste_params)

    if resp_msg.ok:
        print("Sucess")
        return resp_msg.text
    else:
        print("Failure")
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason : {resp_msg.text}')
    
if __name__ == '__main__':
    main()