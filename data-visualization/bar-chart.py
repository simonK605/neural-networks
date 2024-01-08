from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

# add a title
plt.title("My Favorite Movies")

# label the y-axis
plt.ylabel("# of Academy Awards")

# label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)
plt.show()