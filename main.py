import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    try:
        # Load dataset
        df = pd.read_csv("data/student_scores.csv")

        # Subjects list
        subjects = ["math", "science", "english", "computer"]

        # Data cleaning & validation
        df[subjects] = df[subjects].apply(pd.to_numeric, errors="coerce")
        df.dropna(inplace=True)

        # Calculate averages
        df["average_score"] = df[subjects].mean(axis=1)
        subject_avg = df[subjects].mean()

        # Create output folder
        os.makedirs("visualizations", exist_ok=True)

        # -------------------------------
        # Chart 1: Subject-wise Average (Bar Chart)
        # -------------------------------
        subject_avg.plot(kind="bar", title="Average Marks by Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.tight_layout()
        plt.savefig("visualizations/subject_average_scores.png")
        plt.show()

        # -------------------------------
        # Chart 2: Student-wise Performance (Line Chart)
        # -------------------------------
        plt.plot(df["student_id"], df["average_score"], marker="o")
        plt.title("Student Performance Trend")
        plt.xlabel("Student ID")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("visualizations/student_average_scores.png")
        plt.show()

        # Print insights
        print("\n SUBJECT AVERAGES")
        print(subject_avg)

        print("\n TOP 5 STUDENTS")
        print(df.sort_values(by="average_score", ascending=False).head())

        print("\n LOW PERFORMING STUDENTS (Avg < 70)")
        print(df[df["average_score"] < 70])

    except FileNotFoundError:
        print("CSV file not found. Check the file path.")
    except Exception as e:
        print(" Error:", e)

if __name__ == "__main__":
    main()
