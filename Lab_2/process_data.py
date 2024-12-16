from gen_random import gen_random
from cm_timer import cm_timer_1
from print_result import print_result
from unique import Unique
from field import field


import json
import sys

path = "data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique([item['job-name'] for item in field(arg, "job-name")]).data, key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter((lambda x: x.lower().find("программист") == 0), arg))


@print_result
def f3(arg):
    return [item + " с опытом Python" for item in arg]


@print_result
def f4(arg):
    return [item + f", зарплата {gen_random(1, 100000, 200000)[0]} руб." for item in arg]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
