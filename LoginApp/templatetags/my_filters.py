# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/18 15:47
    file   : my_filters.py
    
"""
import re
from django import template
from datetime import datetime
import time

register = template.Library()


@register.filter
def convert_time(value):
    ret = re.findall(r"(\d{2,4}).*?(\d{1,2}).*?(\d{1,2})", value)
    return "%s年%s月%s日" % ret[0]


@register.filter
def replace_character(value, args):
    args1, args2 = args.split(",")
    result = value.replace(args1, args2)
    return result


@register.tag
def addNum(parser, token):
    try:
        content = token.split_contents()
        tag_name, tag_content = content
    except ValueError as e:
        msg = str(e)
        raise template.TemplateSyntaxError(msg)
    return AddNum(tag_content[1:-1])


class AddNum(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        ret = int(self.format_string) + 1
        return ret


@register.filter
def age(birthday):
    tm_year = datetime.today().year
    birth_year = datetime.strptime(birthday, u'%Y年%m月%d日').year
    age = tm_year - birth_year

    # 或者
    # tm_year = time.localtime().tm_year
    # birth_year = time.strptime(birthday, u'%Y年%m月%d日').tm_year
    # age = tm_year - birth_year

    ret = '少年'
    if 1 < age <= 12:
        ret = '少年'
    elif age <= 22:
        ret = '青年'
    elif age <= 35:
        ret = '壮年'
    elif age <= 45:
        ret = '中年'
    elif age <= 60:
        ret = '老年'
    elif age <= 100:
        ret = '太古'
    return age, ret
