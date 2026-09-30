import requests
import json
YOUR_API_KEY = "AIzaSyDbx56JuMBerOHiojDP7xGkytgCOCHSqbc"
Channel_Handle = "dhruvrathee"

def getplaylist_id():
    try:
        url =f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_Handle}&key={YOUR_API_KEY}"

        response = requests.get(url)
        #print(response) '''

        data = response.json()
# print(json.dumps(data,indent=4))

        channel_items = data["items"][0]
        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_playlistID)
        return channel_playlistID
    except requests.exceptions.RequestException as e:
        raise e

if __name__== "__main__":
    getplaylist_id()

