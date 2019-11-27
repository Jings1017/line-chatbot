from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

##### is going state
    def is_going_to_state1(self, event):
        text = event.message.text
        print("state1 text: "+text.lower())
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        #text = event.message.text
        #print("state2 text: "+text.lower())
        #return text.lower() == "go to state2"
        if event.get("message"):
            text = event.message.text
            return text.lower() == 'go to state2'
        return False


    def is_going_to_state3(self, event):
        
        text = event.message.text
        print("state3 text: "+text.lower())
        return text.lower() == "go to state3"

######
    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")
######
    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()


    def on_exit_state2(self):
        print("Leaving state2")
######
    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")