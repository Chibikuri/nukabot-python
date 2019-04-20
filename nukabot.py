from linebot import LineBotApi
from linebot.models import TextSendMessage
import json


Access_Token = json.load(open('./tk.json', 'r'))


line_bot_api = LineBotApi(Access_Token["ACCESS_TOKEN"])


def main():
    user_id = Access_Token["USER_ID"]

    messages = TextSendMessage(text=f"こんにちは😁\n\n"
                                    f"最近はいかがお過ごしでしょうか?")
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    main()