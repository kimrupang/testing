from slack_sdk import WebClient

#const value
s_token = ''
s_channel = 'C04J4ABPE49'

client = WebClient(token=s_token, timeout=300)

#slack files upload
def file_update(text):
    client.files_upload_v2(
        channel=s_channel,
        file=text,
        title="Test upload"
    ).get(text)


#slack message
def post_message(texts):
    client.chat_postMessage(
        channel=s_channel,
        text=texts)
