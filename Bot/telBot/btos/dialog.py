import os
import dialogflow_v2 as dialogFlow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="news-agent-nai9-70f2f172375f.json"
dialogflow_session_client=dialogFlow.SessionsClient()
projectid='news-agent-nai9'

def detect_intent_from(text,session_id,language_code='en'):
    session=dialogflow_session_client.session_path(projectid,session_id)
    testinput=dialogFlow.types.TextInput(text=text,language_code=language_code)
    query=dialogFlow.types.QueryInput(text=testinput)
    response=dialogflow_session_client.detect_intent(session=session,query_input=query)
    return response.query_result
def get_reply(query,chat_id):
    response=detect_intent_from(query,chat_id)
    if response.intent.display_name=='get_news':
        return "get_news",  dict(response.parameters)
    else:
        return "small_talk", response.fulfillment_text
if __name__ == '__main__':

    response=detect_intent_from("hi",1234)
    print(response)