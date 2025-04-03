sent_message = "Hey there! This is a secret message."

with open("sent_message.txt", "w") as file:
    file.write(sent_message)

with open("sent_message.txt", "r+") as file:
    content = file.read()
    print(f"Secret Message: {content}")
    file.seek(0)

    unsent_messages = "This message has been unsent"

    file.write(unsent_messages)
    file.truncate()
    file.seek(0)

    file_after = file.read()
    print(f"Message After: ", file_after)




