from gnewsclient import gnewsclient
client=gnewsclient.NewsClient()
client.get_config()
def fetch_news(parameters):
    client.language=parameters.get('language')
    client.topic=parameters.get('topic')
    client.location=parameters.get('location')
    client.language=parameters.get('language')
    return client.get_news()[:5]
topics=[
    ['Top Stories','World','Nation'],
    ['Business','Technology','Entertainment'],
    ['Sports', 'Science','Health']
]