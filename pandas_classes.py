import pandas as pd


def classes_with_five_students(courses: pd.DataFrame) -> pd.DataFrame:
    """
    LeetCode Pandas: Classes With at Least 5 Students

    courses: DataFrame with columns ['student', 'class']
    returns: DataFrame with a single column ['class'] containing
             all classes that have at least 5 students.
    """
    # 1) Group by 'class' and count how many rows (students) in each class.
    #    .groupby('class').size() gives a Series:
    #    class
    #    Biology     1
    #    Computer    1
    #    English     1
    #    Math        6
    counts = courses.groupby("class").size()

    # 2) Keep only the classes where the count is >= 5.
    big_classes = counts[counts >= 5]

    # 3) The index of 'big_classes' is the class name.
    #    Reset the index to convert it back to a DataFrame with a 'class' column.
    result = big_classes.reset_index()[["class"]]

    return result


if __name__ == "__main__":
    # Small example so you can run this file locally and see the result.
    data = {
        "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "class": [
            "Math",
            "English",
            "Math",
            "Biology",
            "Math",
            "Computer",
            "Math",
            "Math",
            "Math",
        ],
    }
    df = pd.DataFrame(data)
    print(classes_with_five_students(df))


