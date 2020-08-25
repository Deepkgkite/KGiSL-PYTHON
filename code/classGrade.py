

import bisect
gradeChart = [
    (97, 100, 'A+'),
    (93, 96, 'A'),
    (90, 92, 'A-'),
    (87, 89, 'B+'),
    (83, 86, 'B'),
    (80, 82, 'B-'),
    (77, 79, 'C+'),
    (73, 76, 'C'),
    (70, 72, 'C-'),
    (67, 69, 'D+'),
    (63, 66, 'D'),
    (60, 62, 'D-'),
    (0, 60, 'F')
]


def calculate_grade(score, gradeChart):
    """calculate the grade given a score
    and a grading chart.

    @author kgashok

    @param score individual student's score
    @param gradeChart list of tuples
    @return a grade char 'A'-'F'
    """
    gradeChart.sort(key=lambda r: r[1])
    grade_range = [g[1] for g in gradeChart]
    print(grade_range)
    grade_letter = [g[2] for g in gradeChart]
    print(grade_letter)
    index = bisect.bisect(grade_range, score)
    print(grade_letter[index])
    return grade_letter[index]


<<<<<<< HEAD
def class_average(scores, gc):
    """returns the average grade for the entire class 
    
=======
def classAverage(scores, gc):
    """returns the average grade for the entire class

>>>>>>> 2b0d258e5b35e315e652048190018016a894fe1d
    @author kgashok
    
    @param scores list of student scores
    @param gc list of tuples
    @return a grade char 'A'-'F'
    """
    average = sum(scores) * 1.0 / len(scores)
    # print(average)

    return calculate_grade(average, gc)
