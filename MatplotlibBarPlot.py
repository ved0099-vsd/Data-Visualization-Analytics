import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","python"]
    students = [30,40,45,55] 

    plt.bar(
        language,                 #valuea of  x axis
        students,                  #values of Y axis
        width= 0.6,           #Width of bars
        edgecolor = "black",      #Border colour of bars
        linewidth = 1,                   #width of bar border
        alpha = 0.8,              #Transparency 0.0 to 1
        label = "students"                  #Legent Text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Lamguages")
    plt.ylabel("No. of students")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
