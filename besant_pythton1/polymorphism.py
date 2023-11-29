##
class meta:
    def using_keyboard(self):
        print("using the keyboard")
    def sending_messages(self):
        print("messages")
    def receiving_messages(self):
        print("receiving")
class whats_app(meta):
    def sending_messages(self):
        print("send the messages in whats app!")
    def receiving_messages(self):
        print("read the msg in whatsapp!")
    def send_location(self):
        print("In whatsapp location is sending")
class insta(meta):
    def sending_messages(self):
        print("send the messages in insta!!")
    def receiving_messages(self):
        print("read the msg in insta!!")
    def tagging(self):
        print("In Insta tag is done")
class facebook(meta):
    def sending_messages(self):
        print("send a messages in fb")
    def receiving_messages(self):
        print("read the msg in fb!!")
    def liking(self):
        print("In facebook liking is a msg")
def messenger(ref):
    ref.using_keyboard()
    ref.sending_messages()
    ref.receiving_messages()
    if type(ref) == whats_app:
        ref.send_location()
    if type(ref) == insta:
        ref.tagging()
    if type(ref) == facebook:
        ref.liking()
b = whats_app()
c = insta()
d = facebook()
messenger(b)
messenger(c)
messenger(d)
