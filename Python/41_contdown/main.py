import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2025,9,28)

days_away = next_birthday - today

if next_birthday == today:
    print(bday_messages.random_message())
else:
    print(f"My next birthday is {days_away.days} days away!")

