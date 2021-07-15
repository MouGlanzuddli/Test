<<<<<<< HEAD
2.
def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    c = "".join(a)
    return c

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
=======
#thay thế chuỗi lmao
def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    c = "".join(a)
    return c

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
>>>>>>> 137c05d5d44d2356f9002d9b8634d1bfdaeee71b
