<h1>Can I Snooze?</h1>
% if (delay == -2):
    <p>I have no idea, something went terribly wrong. Sorry.</p>
% elif (delay == -1):
    <p>I don't know yet, please come back later.</p>
% elif (delay == 0):
    <p>No.</p>
% else:
    <p>Yes! <b>{{delay}}</b> more minutes.</p>