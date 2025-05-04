def show_message(my_messages, received_messages):
    while my_messages:
        current_list = my_messages.pop()
        print(f"Send messages: {current_list}")
        received_messages.append(current_list)
def send_messages(received_messages):
    for received_message in received_messages:
        print(f"Received messages: {received_message}")
my_messages = ['hello kolya', 'hello aslan', 'hello kayl']
received_messages = []
show_message(my_messages, received_messages)
send_messages(received_messages)