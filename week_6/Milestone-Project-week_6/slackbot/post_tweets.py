import requests
from sqlalchemy import create_engine

webhook_url = "https://hooks.slack.com/services/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"

pg = create_engine('postgresql://postgres:1234@postgresdb:5432/tweets', echo=True)

tweets_request = pg.execute('''
    SELECT * 
    FROM tweets
;
''')


for i in tweets_request:
    i._asdict()
    print(i)
    data = {'text': i["text"]}

requests.post(url=webhook_url, json = data)
