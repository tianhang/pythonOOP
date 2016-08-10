
def get_text(name):
    return "my name is : {0}".format(name)

def my_decortor(func):
    def func_wapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wapper

get_text = my_decortor(get_text)

print get_text('tianhang')

@my_decortor
def get_text2(name):
    return "my name is : {0}".format(name)

print get_text2('jack')