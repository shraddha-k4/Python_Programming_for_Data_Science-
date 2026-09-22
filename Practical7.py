#Practical No 7 : Create line plots, bar charts, and histograms using Matplotlib for visualization of data
#distributions.

import matplotlib.pyplot as plt

days =["Mon", "Tue", "Wed", "Thu", "Fri"]
hours_studied = [1,2,3,4,5]

students = ["Shraddha","Rutuja","Bhumika","Sai"]
books_read=[4,7,2,5]

test_scores = [55,62,65,70,72,75,7885,88,95]

fig,axes=plt.subplots(figsize=(12,4), nrows=1,ncols=3)
fig.suptitle("Student Data Visualization",fontsize=14)


axes[0].plot(days,hours_studied,marker="o",color="blue",linewidth=2)
axes[0].set_title("Line Plot:Study Hours")
axes[0].set_xlabel("Day of week")
axes[0].set_ylabel("Hours Studied")
axes[0].grid(True)

axes[1].bar(students,books_read,color=["pink","skyblue","lightgreen","orange"])
axes[1].set_title("Bar Charts: Bools Read")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Number of Books")

axes[2].hist(test_scores,bins=[50,60,70,80,90,100],color="purple",edgecolor="black")
axes[2].set_title("Histrogram : Score Distribution")
axes[2].set_xlabel("Scores Ranges")
axes[2].set_ylabel("Number of Students")

plt.tight_layout()
plt.show()
