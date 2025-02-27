class Student:
    def __init__(self,studentId,name,enrolledCourses) -> None:
        self.studentId = studentId
        self.name = name
        self.enrolledCourses = []

    def enroll(self,courseCode):
        self.enrolledCourses.append(courseCode)

    def getCourses(self):
        return self.enrolledCourses

class Course:
    def __init__(self,courseCode,courseName,maxEnrollment,currentEnrollment) -> None:
        self.courseCode = courseCode
        self.courseName = courseName
        self.maxEnrollment = maxEnrollment
        self.currentEnrollment = 0
    
    def canEnroll(self):
        if self.currentEnrollment< self.maxEnrollment:
            return True
        return False


class EnrollmentManager:
    def __init__(self,student,courses) -> None:
        self.students=student
        self.courses=courses

    def enrollStudent(self,studentId,courseCode):
        for student in self.students:
            if student.studentId==studentId:
                for i in  self.courses:
                    if i.canEnroll():
                        student.enroll(courseCode)
                        i.currentEnrollment+= 1
                        return True
        return False

        
    
    def listStudentsInCourse(self,courseCode):
        new = []
        for student in self.students:
            if courseCode in student.enrolledCourses:
                new.append(student)
        return new
    




def main():
    # Create students
    student1 = Student(1, "Alice", [])
    student2 = Student(2, "Bob", [])

    # Create a course with maximum enrollment 1 to test capacity limits
    course = Course("CS101", "Intro to CS", 1, 0)

    # Create EnrollmentManager with students and the course
    em = EnrollmentManager([student1, student2], [course])

    # Test enrolling first student (should succeed)
    enroll1 = em.enrollStudent(1, "CS101")
    print("Alice enrolled in CS101:", enroll1)

    # Test enrolling second student (should fail due to capacity)
    enroll2 = em.enrollStudent(2, "CS101")
    print("Bob enrolled in CS101 (should fail):", enroll2)

    # List students in CS101
    print("Students in CS101:")
    for s in em.listStudentsInCourse("CS101"):
        print(s.name)

    # Additional: Check student's enrolled courses
    print("Alice's courses:", student1.getCourses())
    print("Bob's courses:", student2.getCourses())

if __name__ == '__main__':
    main()