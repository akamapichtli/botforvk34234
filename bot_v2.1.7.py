import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

bot_token = '' 

vk_session = VkApi(token=bot_token)
longpoll = VkBotLongPoll(vk_session, "198288640")
vk = vk_session.get_api()



def send_message_text (random_id, chat_id, message):
    vk.messages.send(
        random_id=random_id,
        chat_id=chat_id,
        message=message,
    )



#def send_message_set(self_get, event_object_text, event_object_from_id):
def send_message_set(self):

    print("Username: " + self_get(event_object_from_id))
    print("Text: " + event_object_text)
    print(" ------- ")




for event in longpoll.listen():
    print('===Message===')
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
        if event.object['text'] == '/dz':
            print('\n/dz\n')

            msg_text=open(u'/home//dz.txt', 'r')
            msg_text=msg_text.read()

            random_id = round(random.random() * 10 ** 9)
            chat_id = int(event.chat_id)
            message = msg_text

            print(msg_text)

            #отправка
            send_message_text(random_id, chat_id, message)
            send_message_set(
                self.get_user_name,
                event.object.text,
                event.object.from_id
            )

        if event.object['text'] == '/help':
            print('\n/help\n')

            msg_text=open(u'/home//sp.txt','r')
            msg_text=msg_text.read()

            random_id = round(random.random() * 10 ** 9)
            chat_id = int(event.chat_id)
            message = msg_text

            print(msg_text)

            vk.messages.send(
                random_id=random_id,
                chat_id=chat_id,
                message=message,
            )

        if '/бот' in event.object['text']:
            print('\n/бот\n')

            ver=random.randint(1, 100)
            ver=int(ver)
            if ver < 20:
                comment = '\n так что хз'
            elif ver < 40:
                comment = '\n вполне возможно'
            elif ver < 60:
                comment = '\n скорее да'
            elif ver < 80:
                comment = '\n очевидно же'

            msg_text='Вероятность - '+str(ver) + '%' + comment

            random_id = round(random.random() * 10 ** 9)
            chat_id = int(event.chat_id)
            message = msg_text

            print(msg_text)

            vk.messages.send(
                random_id=random_id,
                chat_id=chat_id,
                message=message,
            )

        if '/hi' in event.object['text']:
            print('\nhi\n')

            msg_text=open(u'/home//priv.txt','r')
            msg_text=msg_text.read()

            random_id = round(random.random() * 10 ** 9)
            chat_id = int(event.chat_id)
            message = msg_text

            print(msg_text)

            vk.messages.send(
                random_id=random_id,
                chat_id=chat_id,
                message=message,
            )
        if '/dz.add' in event.object['text']:

            msg = str(event.object['text'])
            msg=msg.replace('/dz.add', '')
            msg_text.write('\n'+msg)

