# coding: utf-8


def func_arg(a, b=3, s="spam"):
    print("a:"+str(a)+", b:" + str(b)+", s:"+str(s))


func_arg(1)
func_arg(a=5, b=7, s="egg")
func_arg(s="ham", a=2)
