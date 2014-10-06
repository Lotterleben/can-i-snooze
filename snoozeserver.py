import datetime
from bottle import route, run, template, static_file
from canisnooze import get_delay_info, next_tuesday

@route('/resources/<filename>')
def server_static(filename):
    return static_file(filename, root='resources/')

@route('/')
def display_delay():
    today = datetime.date.today()
    train_name = "ICE 1518"

    tuesday = next_tuesday(today).strftime("%d.%m.%y")
    info = get_delay_info(tuesday, train_name)
    delay = info["delay"]

    return template('snoozetemplate', delay=delay)

run(host='0.0.0.0', port=8080, debug=False)