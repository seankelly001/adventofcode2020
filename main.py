from flask import Flask, render_template
from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6

app = Flask(__name__)

@app.route('/')
def run():
    links = []
    num_days = 6
    for i in range(num_days):
        j = i+1
        links.append({"name": "Day {} Part 1".format(j), "link": "day{}/part1".format(j)})
        links.append({"name": "Day {} Part 2".format(j), "link": "day{}/part2".format(j)})
    return render_template("index.html", data=links)

@app.route("/<day_v>/<part_v>")
def getDay(day_v, part_v):
    result = eval("{}.{}".format(day_v, part_v))()
    return result
    
if __name__ == "__main__":
    app.run()