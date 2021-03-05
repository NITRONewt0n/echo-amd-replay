import keyboard, time, json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

while True:
    while True: 
        try:
            req = Request("http://127.0.0.1:6721/session")
            response = urlopen(req)
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
            time.sleep(1)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)        
            time.sleep(1)
        else: 
            res_body = response.read()
            data = json.loads(res_body.decode("utf-8"))
            # print(data)
            #### prevent null status for details field
            match_type = data["match_type"]
            if match_type == "Social_2.0":
                game_mode = "lobby"
            else: 
                game_mode = "match"

            if game_mode == "match":
                status = data["game_status"]
                if status == "score":
                    time.sleep(10)
                    keyboard.press_and_release('ctrl+shift+s')
                    time.sleep(30)
                break