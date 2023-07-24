import time,random,string
def filename_gen(extention):
    a = int(time.time())
    b = string.ascii_letters
    b = "".join(random.choices(list(b),k=8))
    g = list(f"{a}{b}")
    random.shuffle(g)
    return "".join(g)+extention