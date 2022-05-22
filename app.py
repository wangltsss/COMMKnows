from flask import Flask, render_template, redirect, url_for
from news import NewsFetcher
import time

app = Flask(__name__)


def get_date():
    localtime = time.localtime(time.time())
    year = localtime.tm_year
    mon = localtime.tm_mon
    if mon == 1:
        mon = "January"
    elif mon == 2:
        mon = "February"
    elif mon == 3:
        mon = "March"
    elif mon == 4:
        mon = "April"
    elif mon == 5:
        mon = "May"
    elif mon == 6:
        mon = "June"
    elif mon == 7:
        mon = "July"
    elif mon == 8:
        mon = "August"
    elif mon == 9:
        mon = "September"
    elif mon == 10:
        mon = "October"
    elif mon == 11:
        mon = "November"
    elif mon == 12:
        mon = "December"
    dat = localtime.tm_mday
    day = localtime.tm_wday
    if day == 0:
        day = "Monday"
    elif day == 1:
        day = "Tuesday"
    elif day == 2:
        day = "Wednesday"
    elif day == 3:
        day = "Thursday"
    elif day == 4:
        day = "Friday"
    elif day == 5:
        day = "Saturday"
    else:
        day = "Sunday"
    return [day, mon, dat, year]


@app.route('/COMMKnows/')
def comm_knows():  # put application's code here
    fetcher = NewsFetcher()
    fetcher.fetch()
    fetcher.load_news()
    date = get_date()
    return render_template("home.html", day=date[0], month=date[1], date=date[2], year=date[3], newslist=fetcher.newsfeed)


@app.route('/commknows/')
def ambiguate():
    return redirect(url_for("comm_knows"))


if __name__ == '__main__':
    app.run()
