def send_email(message, recipient, sender="university.help@gmail.com"):
    # if ("@" and (".com" or ".ru" or ".net") not in (recipient or sender)) or\
    # вопрос " Почему выражение (if "@" not in (recipient or sender)) не работало также ?

   # if ("@" not in recipient
    #        or "@" not in sender
    if ((recipient[(len(recipient) - 4):] == '.com'
            or recipient[(len(recipient) - 4):] == '.net'
            or recipient[(len(recipient) - 3):] == '.ru')
            and (sender[(len(sender) - 4):] == '.com'
            or sender[(len(sender) - 4): ] == '.net'
            or sender[(len(sender) - 3): ] == '.ru')
            and '@' in recipient and sender):
            if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
            elif sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            elif sender != "university.help@gmail.com":
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Привет', 'university.help@gmail.com', 'university.help@gmail.com')