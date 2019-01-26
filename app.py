from linebot import LineBotApi
from linebot.models import TextSendMessage
import flask

LINE_CHANNEL_ACCESS_TOKEN = "fqlgBVLmeeArUi03DQDKL5ucc80VOvJUMeaRTskfdK3DN9lrDHHkDKxA6Be8p32RBw2agZL90uQrsn2cRusqL0zG/TaFi5B/jZnGwRwPYEfNPD3TqD7I24xh5Bj9cCwOKTZ/po/0+kW8V5xaiGXeRAdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main():
    user_id = "itaku21"

    message = TextSendMessage(text=f"こんにちは\n\n"
                                    f"おはよう")
    line_bot_api.push_message(user_id,messages=message)

    if __name__ == "__main__":
        main()
