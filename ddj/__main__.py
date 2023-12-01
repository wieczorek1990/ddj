import scrapetube


channel_id = 'UC-IeV5MVrzrWh3YtQJlWHAQ'
videos = scrapetube.get_channel(channel_id)

for video in videos:
    print(video['videoId'])
