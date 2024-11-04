def all_variants(text):
    len_ = 1 # кол-во символов в подстроке
    while len_ <= len(text):
        for arg in range(len(text)):
            if len_ <= len(text[arg::1]): # пров. длину остатка строки, чтобы не взять подстроку короче len_
                yield text[arg:len_+arg]
        len_ += 1

a = all_variants("abc")
for i in a:
    print(i)

b = all_variants('qwerty')
for i in b:
    print(i, end=' ')