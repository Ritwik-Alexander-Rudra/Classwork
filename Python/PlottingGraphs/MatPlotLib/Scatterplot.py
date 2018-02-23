import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [1,4,3,6,3,7,3,6]

plt.scatter(x,y, label = "SkitScat", color = "k", marker = "*", s =3)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatterplot")
plt.legend()
plt.show()
