
def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" not in recipient or '@' not in sender or not recipient.endswith((".com", ".ru", ".net"))
            or not sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient==sender:
        print('Нельзя отправить письмо самому себе')
    elif sender!="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

send_email('mess','university.help@gmail.com','@.com')
send_email('mess','university.help@gmail.com')
send_email('mess','universi@.com')
send_email('messe','universi@.co')
send_email('mess','universi.com')
