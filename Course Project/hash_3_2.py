import timeit

starttime = timeit.default_timer()

list = [None] * 370105

print("Initializing the list took", timeit.default_timer() - starttime)
starttime = timeit.default_timer()

file = open("words_alpha.txt", "r")
for line in file:
    list.append(line.strip())

print("The appends took", timeit.default_timer() - starttime)

starttime = timeit.default_timer()

file = open("kaikkisanat.txt", "r")
matching = 0
for line in file:
    for word in list:
        if word == line.strip():
            matching += 1
            break
print(f"{matching} matching words found")


print("Finding the common words took", timeit.default_timer() - starttime)