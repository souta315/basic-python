text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

text = text.replace(',', '')
text = text.replace('.', '')

nonspace = text.split()
long = list(map(len, nonspace))
long_str = list(map(str,long))
output = "".join(long_str)
print(output)
