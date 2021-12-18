import functools

txt = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
d = functools.reduce(lambda i, j: i + j, list(map(lambda x: x.count("a") + x.count("A"), txt)))
print(d)
# solution 1
print([sum(list(map(lambda x: x.count("a") + x.count("A"), txt)))])
# solution 2
