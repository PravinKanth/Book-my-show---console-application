import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=4)

    word_list = wrapper.wrap(text=value)
    a = ''

    for element in word_list:
        a += "\n"


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)