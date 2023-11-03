#!/usr/bin/python3
# 5-no_c.py
# Nimona123  <argano4444@gmail.com>


def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
