import os
from trello import TrelloClient
from services.redis import redis

TOKEN_KEY = "trello_token"


def get_auth_url(
    key: str,
    return_url: str,
    name="HubSpot",
    expiration="30days",
    scope="read",
    response_type="token",
):
    return "https://trello.com/1/authorize?key={}&name={}&expiration={}&response_type={}&scope={}&return_url={}".format(
        key, name, expiration, response_type, scope, return_url
    )


def save_token(token):
    redis.set(TOKEN_KEY, token)

    return token


def is_authorized():
    return redis.exists(TOKEN_KEY)


def get_token():
    return redis.get(TOKEN_KEY).decode()


def get_client():
    return TrelloClient(api_key=os.getenv("TRELLO_API_KEY"), token=get_token(),)


def search_cards(query=None):
    client = get_client()
    if query is not None and len(query) > 0:
        return client.search(query=query, partial_match=True, models=["cards"])
    else:
        return []


def create_webhook(callback_url, card_id, description=None):
    client = get_client()
    # standard webhook creation method is not correct
    # prepare data manually
    data = {
        'callbackURL': callback_url,
        'idModel': card_id,
        'description': description,
        'key': os.getenv("TRELLO_API_KEY"),
    }
    url = "https://trello.com/1/tokens/{}/webhooks/".format(get_token())

    return client.http_service.post(url, data=data, auth=client.oauth, proxies=client.proxies)
