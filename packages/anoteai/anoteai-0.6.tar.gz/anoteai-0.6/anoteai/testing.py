import time
#from anoteai import anote
from core import Anote


if __name__ == "__main__":
    api_key = '56bf88500d3622b97a1210844457bf32'

    anote = Anote(api_key, is_private=False)
    # anote = anote(api_key, is_private=True)

    file_paths = ['sample_docs/doc1.pdf', 'sample_docs/doc2.pdf']

    upload_result = anote.upload(task_type="documents", model_type="gpt", file_paths=file_paths)
    print("output from upload: ", upload_result)
    chat_id = upload_result['id']
    chat_result = anote.chat(chat_id, "What is this paper classification performance about?")
    print("output from chat: ", chat_result)
    message_id = chat_result['message_id']
    print("output from evaluate:", anote.evaluate(message_id))

    #PUBLIC
    # file_paths = ['sample_docs/doc1.pdf', 'sample_docs/doc2.pdf', 'https://docs.anote.ai/']
    # chat_id = anote.upload(task_type="documents", model_type="gpt", file_paths=file_paths)['id']

    # response1 = anote.chat(chat_id, "Who wrote the paper on Improving Classification performance?")
    # print("Answer:", response1['answer'])
    # print("Sources:", response1['sources'])
    # message_id1 = response1['message_id']

    # print(anote.evaluate(message_id1))

    # print("-------------------------------------------------")

    # response2 = anote.chat(chat_id, "What is Private Chatbot?")
    # print("Answer:", response2['answer'])
    # print("Sources:", response2['sources'])
    # message_id2 = response2['message_id']

    # print(anote.evaluate(message_id2))

    #PRIVATE
    # file_paths = ['sample_docs/doc1.pdf', 'sample_docs/doc2.pdf', 'https://docs.anote.ai/']
    # chat_id = anote.upload(task_type="documents", model_type="llama", file_paths=file_paths)['id']

    # response1 = anote.chat(chat_id, "Who are the authors of the paper on Improving Classification performance?")
    # print("Answer:", response1['answer'])
    # print("Sources:", response1['sources'])
    # message_id1 = response1['message_id']

    # print(anote.evaluate(message_id1))

    # print("-------------------------------------------------")

    # response2 = anote.chat(chat_id, "What is Private Chatbot?")
    # print("Answer:", response2['answer'])
    # print("Sources:", response2['sources'])
    # message_id2 = response1['message_id']

    # print(anote.evaluate(message_id2))