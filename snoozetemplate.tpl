<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, user-scalable=no">
    <title></title>
    <style type="text/css">
        body {
            text-align: center;
            font-family: sans-serif;
        }

        h1 {
            font-weight: lighter;
            font-size: 40px;
            color: #666;
        }

        p {
            font-size: 80px;
        }
    </style>
</head>
<body>

    <h1>Can I Snooze?</h1>
    % if (delay == -2):
        <p>I have no idea. :( <br> Something went terribly wrong. Sorry.</p>
    % elif (delay == -1):
        <p>I don't know yet. <br> Please come back later.</p>
    % elif (delay == 0):
        <p>No.</p>
    % else:
        <p>Yes! <b>{{delay}}</b> more minutes.</p>

</body>
</html>