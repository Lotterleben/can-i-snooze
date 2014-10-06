import datetime
from bottle import route, run, template
from canisnooze import get_delay_info, next_tuesday

@route('/')
def display_delay():
    today = datetime.date.today()
    train_name = "ICE 1518"

    tuesday = next_tuesday(today).strftime("%d.%m.%y")
    info = get_delay_info(tuesday, train_name)
    delay = info["delay"]

    return template('snoozetemplate', delay=delay)

run(host='localhost', port=8080, debug=True)