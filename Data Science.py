from matplotlib import pyplot as plt

pupils = ['John', 'Liam', 'Noah', 'Oliver', 'Sophia', 'Olivia', 'Emma', 'Ava', 'Mia', 'Charlotte']
grades = [85, 90, 78, 92, 88, 76, 95, 89, 79, 94]


# Simple line graph where the x-axis represents the pupils and the y-axis represents the grades.
# This allow us to see a simple visualization of each pupil's grade.

def ex1():

    plt.bar(pupils, grades)
    plt.title("Grades of Pupils")  # add a title
    plt.ylabel("Grades")  # label the y-axis
    plt.xticks(pupils, pupils)  # label x-axis with  names at bar centers
    plt.show()  # Display the chart


# Bar chart using the data. The x-axis  represent the pupils and the y-axis represent the grades. This allow us to compare the pupils' grades.

def ex2():
    plt.bar(pupils, grades)  # Create a bar chart
    plt.xlabel('Pupils')  # label x-axis
    plt.ylabel('Grades')  # label the y-axis
    plt.title('Grades of Pupils')  # add a title
    plt.show()  # Display the chart


# Horizontal bar chart using the data. The y-axis represent the pupils and the x-axis represent the grades.
# This is another way to visualize and compare the pupils' grades.

def ex3():
    plt.barh(pupils, grades)
    plt.xlabel('Grades')
    plt.ylabel('Pupils')
    plt.title('Grades of Pupils')
    plt.show()


# Scatter plot of the data.
# This plot can be used to identify any correlation between the pupils
# (if they are ordered in some way, such as age) and their grades.

def ex4():
    plt.scatter(pupils, grades)
    plt.xlabel('Pupils')
    plt.ylabel('Grades')
    plt.title('Scatter Plot of Grades')
    plt.show()


# Pie chart showing the ratio of pupils who have passed-those who have failed.
# Divide the grades into pass (grade>=80) and fail (grade<80).

def ex5():
    # Calculate the count of students who passed and failed
    pass_count = sum(grade >= 80 for grade in grades)
    fail_count = len(grades) - pass_count

    # Prepare data for pie chart
    labels = ['Pass', 'Fail']
    sizes = [pass_count, fail_count]

    # Create a pie chart with the following parameters:
    # - sizes: A list representing the sizes (counts) of different sections in the pie. In this case, it's the count of students who passed and failed.
    # - labels: A list providing labels for each section of the pie. In this case, 'Pass' and 'Fail' representing the pass and fail categories.
    # - autopct: A string formatting specification for displaying percentages on the pie chart. '%1.1f%%' means one decimal place and a percentage sign.
    # - startangle: The angle in degrees at which the first wedge of the pie is drawn. In this case, 90 degrees means the 'Pass' section starts from the top.
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Add a title to the pie chart
    plt.title('Pass/Fail Ratio')

    # Display the chart (you can comment this line if you want to use the function without showing the plot immediately)
    plt.show()


# Line graph to show this pupil's performance across different subjects.
# The grade list represents the grades of a single pupil in different subjects.

def ex6():
    subjects = ['Math', 'English', 'History', 'Science', 'Geography', 'Art', 'PE', 'Music', 'Drama', 'Computing']
    plt.plot(subjects, grades, marker='o')
    plt.xlabel('Subjects')
    plt.ylabel('Grades')
    plt.title('Grades of a Pupil in Different Subjects')
    plt.show()


# Histogram of the grades.
# This show us the distribution of grades among the pupils.

def ex7():
    # Create a histogram with the following parameters:
    # - grades: The data for which the histogram is created, representing the distribution of grades among pupils.
    # - bins: The number of bins (intervals) to use in the histogram. In this case, 10 bins are specified to divide the range of grades into 10 intervals.
    # - edgecolor: The color of the edges of the bars in the histogram. 'black' is specified to outline each bar with a black border.
    plt.hist(grades, bins=10, edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.title('Grade Distribution')
    plt.show()


# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()
