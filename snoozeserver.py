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

    if (delay == -2):
        answer = "I have no idea, something went terribly wrong. Sorry."
    elif (delay == -1):
        answer = "I don't know yet, please come back later."
    elif (delay == 0):
        answer = "No."
    else:
        # TODO: make delay time stand out (wo mach ich das am besten?)
        answer = "Yes! %i more minutes." % delay

    return template('snoozetemplate', answer=answer)

run(host='localhost', port=8080, debug=True)