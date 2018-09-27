  
#Python libraries that we need to import for our bot
import random
from google_api import make_api
from flask import Flask, request
from pymessenger.bot import Bot
from weather import make_crawl
import os
app = Flask(__name__)
ACCESS_TOKEN = 'EAAEZARzg2uPUBAAUPJ4rK3p7SSSsKSIXTeOrqeXqZC3b9E0QzHJQc4VLKt9vUTRZBeZA638DyZAiAI0p66Am241CYpdhoTDSYNks0wma4S53tiRvgWdT5JI5vajZCu8FU6pep74vRboN20UoiMnnCZAXfiSWXZBmTgXU0XZCRP4p5CH1zOYxBzDbr'
VERIFY_TOKEN = 'GHGJIKMNB123'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    text = message['message']['text']
                    for text in [text]:
                        if text.lower() == 'hi':
                            response_sent_text = "Hiii em là Ravenn bé Bot siêu cute nèy \n( ≥^o^≤), tâm hự với em tý nhaaa.\n-Chat 'Thời tiết' để hỏi em thời tiết hôm nay nè\n-Chat 'Coffe' hoặc 'Tea' em sẽ chỉ danh sách các quán cà phê và trà sữa quanh trường PTIT nè\n-Chat 'Búa', 'Bao', 'Kéo' để chơi oẳn tù tì với em nè \n(ﾉ≧ڡ≦)\n-Nhớ nói chuyện nhẹ nhàng với iem nhaa, bé mỏng manh dễ vỡ lắm nè 😚😚😚"
                            send_message(recipient_id, response_sent_text)
                        elif text.lower() == "thời tiết":
                            response_sent_text = make_crawl()
                            send_message(recipient_id, response_sent_text)
                            if 'mưa' in response_sent_text:
                                send_message(recipient_id,'có mưa thì nhớ mang ô hay áo mưa nhaa, dính mưa mà ốm thì em lo lắm ý :(')
                        elif text.lower() in ["coffe", "tea", "cake", "candy", "cgv", "lotte"]:
                            response_sent_text = '\n'.join(make_api(text.lower()))
                            send_message(recipient_id, response_sent_text)
                            send_message(recipient_id, 'có đi chơi nhớ mua phần cho em với nhaaa, mãi iu ^^')
                        elif  text.lower() == 'hello':
                            response_sent_text = 'Lô con ...'
                            send_message(recipient_id, response_sent_text)
                        
                        elif text.lower() == 'búa':
                            response_sent_text = choice_one()
                            send_message(recipient_id, response_sent_text)
                            if response_sent_text == 'Búa':
                                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
                            if response_sent_text == 'Bao':
                                sent_text = 'ahihi ngu vclon` :))'
                            if response_sent_text == 'Kéo':
                                sent_text = 'Hay lắm đmm chơi lại!'
                            send_message(recipient_id, sent_text)
                        elif text.lower() == 'bao':
                            response_sent_text = choice_one()
                            send_message(recipient_id, response_sent_text)
                            if response_sent_text == 'Bao':
                                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
                            if response_sent_text == 'Kéo':
                                sent_text = 'ahihi ngu vclon` :))'
                            if response_sent_text == 'Búa':
                                sent_text = 'Hay lắm đmm chơi lại!'
                            send_message(recipient_id, sent_text)
                        elif text.lower() == 'kéo':
                            response_sent_text = choice_one()
                            send_message(recipient_id, response_sent_text)
                            if response_sent_text == 'Kéo':
                                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
                            if response_sent_text == 'Búa':
                                sent_text = 'ahihi ngu vclon` :))'
                            if response_sent_text == 'Bao':
                                sent_text = 'Hay lắm đmm chơi lại!'
                            send_message(recipient_id, sent_text)
                        elif text.lower() == 'tung do':
                            response_sent_text = 'yêu màu tím, sống nội tâm,ngây thơ dễ tin người lắm nè 😙😙😙...'
                            send_message(recipient_id, response_sent_text)
                            send_message(recipient_id, 'Ủa hỏi sếp em chi vậy, kết rồi phải honggg 🤔🤔🤔???')
                        else :
                            send_message(recipient_id,"Hic từ này sếp em chưa dạy, đừng mắng em nhaaa :(")

                    #if send somthing can't understand
                
                #if user sends us a GIF, photo,video, or any other non-text ite
                if message['message'].get('attachments'):
                    response_sent_nontext = 'Nói chuyện bằng miệng nhaa, hong có hiểu đâu 😒 '
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def choice_one():
    list_ = ['Búa', 'Bao', 'Kéo']
    # return selected item to the user
    return random.choice(list_)



#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

