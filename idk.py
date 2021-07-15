import textwrap




# def swap_case(s):
#     sw = s.swapcase()
#     return sw
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


def wrap(string, max_width):
        string = input()
        max_width = int(input().strip())
        print(textwrap.fill(string, width=max_width))
        return wrap
wrap('','')

