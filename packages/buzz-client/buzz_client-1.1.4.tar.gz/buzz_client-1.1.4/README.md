# buzz_client

A client for buzzAPI

## Intro

`buzz` is a client for [buzzAPI](https://git.arr.lan/gitroot/devops/apps/buzz-api), a tool to send notifications to several services, like email, pushover, slack, teams...

Syntax is:

```
Buzz client

Usage:
    buzz [options] list
    buzz [options] version
    buzz [options] send <notifier> <recipient> [--title <title>] [--severity <severity>] [--attach <file>] [<body>...]
    buzz --version


Options:
    <notifier>                   the notifier you want to use,
                                 you can see the available notifiers using `list` command

    <recipient>                  the recipient of the notification,
                                 must be valid for the notifier chosen

    -h  --help                   show this help message and exit

    -v --version                 show version and exit

    -a URL --api=URL             API URL

    --title <title>              the title of the notification. [default: You received a buzz]
    --severity <severity>        the severity of the message. [default: info]
                                 One of: 'info', 'success', 'warning', 'failure'
    --attach <file>              a file you want to attach to the notification

    --format <format>            format of the message text [default: text]
                                 One of: 'text', 'markdown', 'html'


    <body>                       Content of the notification,
                                 if not specified read from stdin
Environment variables:
    - BUZZ_API         API URL, overrides command line argument

API URL format is `http(s)://auth-token@server`
Example: http://sesame@localhost:8000
```

- URL is the URL of the buzzAPI, for example https://buzz.domain.com/
- TOKEN is the authentication token of the buzzAPI instance.

The other arguments are quite self explicative, but you have to bear in mind that the body of the notification:

- can be passed on the command line of `buzz` like

```
buzz send email --recipient me@domain.com This is the content of the notification
```

- if not passed as an argument of `buzz`, then the content of the notification is read from standard input, for example

```
echo "Content of directory"; ls | buzz send --recipient me@domain.com
```
