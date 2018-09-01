import matplotlib.pyplot as plt

import publishers
list_of_books=publishers.get_books()
nonfiction = 0
children = 0
comics = 0
genrefiction = 0
foreignlang = 0
rate= []
sales= []

for libro in list_of_books:
    r = libro["statistics"]["average rating"]
    rate.append(r)

num_bins=50
def ratings():
    n, bins, patches = plt.hist(rate, num_bins, facecolor="aqua", alpha=0.5)
    plt.title("Histogram of Average Ratings")
    plt.xlabel("Average Ratings")
    plt.ylabel("Number of Books")
    plt.axis([0, 5, 0, 3800])
    plt.show()


for livre in list_of_books:
    v = livre["daily average"]["gross sales"]
    sales.append(v)


num_bins=50
def grossSales():
    n, bins, patches = plt.hist(sales, num_bins, facecolor="#4717F6", alpha=0.5)
    plt.title("Histogram of Daily Average Gross Sales")
    plt.xlabel("Average Sales per Day")
    plt.ylabel("Number of Books")
    plt.axis([ 0, 3000, 0, 27500])
    plt.show()


for book in list_of_books:
    genre = book["genre"]
    if book["genre"]=="nonfiction":
        nonfiction += 1
    if book["genre"]=="children":
        children += 1
    if book["genre"]=="comics":
        comics += 1
    if book["genre"]=="genre fiction":
        genrefiction += 1
    if book["genre"]=="foreign language":
        foreignlang += 1

def print_func():
    print (nonfiction)
    print (children)
    print (comics)
    print (genrefiction)
    print (foreignlang)

def pieChart():
    labels = "nonfiction", 'children', 'comics', 'fiction', 'foreign language'
    sizes = [53.8, 9.7, 2.14, 33.9, 0.46]
    fig1, ax1 = plt.subplots()
    explode = (0, 0, 0, 0.1, 0)
    ax1.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Pie Chart of Distribution of Genres")
    plt.show()

import matplotlib.pyplot
import pylab
def scatterPlot():
    x = [i for i in range(27027)]
    y = [sales]
    matplotlib.pyplot.scatter(x,y)
    matplotlib.pyplot.title("Scatter Plot of Aver. Daily Gross Sales")
    matplotlib.pyplot.xlabel("Number of books")
    matplotlib.pyplot.ylabel("Average Sales per Day")
    matplotlib.pyplot.axis([ 0, 10000, 0, 30000])
    matplotlib.pyplot.show()

print("The dataset we analysed today was the Publishers Python Library. Here are some graphs to visualize the data:")
pieChart()
ratings()
grossSales()
