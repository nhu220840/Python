class Student:
    def __init__(self, i=None, n=None, b=None):
        self.i = i
        self.n = n
        self.b = b

    def inpf(self):
        self.i = input("Student id: ")
        self.n = input("Student name: ")
        self.b = input("Student DoB: ")

    def __str__(self):
        return f"""Student id: {self.i}\nStudent name: {self.n}\nStudent DoB: {self.b}"""


class Course:
    def __init__(self, i=None, n=None):
        self.i = i
        self.n = n
        self.m = {}  # Marks dictionary for students

    def inpf(self):
        self.i = input("Course id: ")
        self.n = input("Course name: ")

    def __str__(self):
        res = f"""Course id: {self.i}\nCourse name: {self.n}\nCourse marks:"""
        for stid, mark in self.m.items():
            res += f"\n\tStudent ID {stid}: {mark}"
        return res


def std_inpf(stlst):
    print("----------------------")
    nb = int(input("Number of students: "))
    for idx in range(nb):
        print(f"Student number {idx + 1}:")
        st = Student()
        st.inpf()
        print("----------------------")
        stlst.append(st)


def cst_inpf(cslst):
    print("----------------------")
    nb = int(input("Number of courses: "))
    for idx in range(nb):
        print(f"Course number {idx + 1}:")
        cs = Course()
        cs.inpf()
        print("----------------------")
        cslst.append(cs)


def mrk_inpf(cslst, stlst):
    print("----------------------")
    csid = input("Select the course by Course ID: ")
    cs = next((cs for cs in cslst if cs.i == csid), None)
    if not cs:
        print("Course not found.")
        return

    print("Please insert student marks:")
    for st in stlst:
        print("+++")
        mrk = input(f"Student {st.n} [{st.i}] mark: ")
        cs.m[st.i] = mrk
    print("----------------------")


def std_lstf(stlst):
    print("----------------------")
    print(f"There are {len(stlst)} students in the system:")
    for st in stlst:
        print("+++")
        print(st)
    print("----------------------")


def cs_lstf(cslst):
    print("----------------------")
    print(f"There are {len(cslst)} courses in the system:")
    for cs in cslst:
        print("+++")
        print(cs)
    print("----------------------")


def mark_lstf(cslst):
    print("----------------------")
    print("Marks information for all courses:")
    for cs in cslst:
        print("+++")
        print(cs)
    print("----------------------")


if __name__ == "__main__":
    stlst = []
    cslst = []

    input = sys.stdin.read if not sys.stdin.isatty() else input
    
    while True:
        opt = int(
            input(
                """
[Student Mark Management System]
1. Insert students
2. Insert courses
3. List student info
4. List course info
5. Add marks
6. Display marks
7. Exit
Option: """
            )
        )

        if opt == 1:
            std_inpf(stlst)
        elif opt == 2:
            cst_inpf(cslst)
        elif opt == 3:
            std_lstf(stlst)
        elif opt == 4:
            cs_lstf(cslst)
        elif opt == 5:
            mrk_inpf(cslst, stlst)
        elif opt == 6:
            mark_lstf(cslst)
        elif opt == 7:
            break
        else:
            print("Invalid option.")
