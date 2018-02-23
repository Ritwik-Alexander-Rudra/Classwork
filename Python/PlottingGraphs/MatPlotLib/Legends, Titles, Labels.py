import matplotlib.pyplot as plt

##
##x = [2,4,6,8,10]
##y = [6,7,3,5,3]
##
##plt.bar(x,y, label = "Bars1", color = "b")
##
##x2 = [1,3,5,7,11]
##y2 = [1,5,3,6,3]
##
##plt.bar(x2,y2, label = "Bars2", color = "c")
##
##plt.xlabel("X")
##plt.ylabel("Y")
##plt.title("Interesting Graph\nCompleted")
##plt.legend()
##plt.show()


##
##population_ages = [22,55,23,23,66,33,74,74,23,57,32,65,18,35,65,38,110,25,113,120,102,12,18,26,74,93,37,58,39,57,94,73,103,103]
##
##bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
##plt.hist(population_ages,bins, histtype = "bar", rwidth = 0.8)
##
##
##plt.xlabel("X")
##plt.ylabel("Y")
##plt.title("Interesting Graph\nCompleted")
##plt.legend()
##plt.show()


ages = [10, 28, 33, 49, 57, 29, 69, 38, 48, 95, 37, 100, 48, 93, 28, 49, 76, 47, 10, 28, 47, 49, 72, 92, 88, 48, 82]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Excellent Graph\nTest")

plt.hist(ages, bins, histtype = "bar", rwidth = 0.8)

plt.show()
