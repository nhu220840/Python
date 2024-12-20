# Student = [id, name, DoB]
# Course [id, name, {stid: stmark}]

# stlst = [Student, etc.]
# cslst = [Course, etx.]

class Student:
    def __init__(self, i, n, b):
        self.i = i
        self.n = n
        self.b = b

    def inpf(self):
        self.i = input("Student id: ")
        self.n = input("Student name: ")
        self.b = input("Student DoB: ")

    def __str__(self):
            return f"""Student id: {self.i}
Student name: {self.n}
Student DoB: {self.b}"""
    

class Course:
    def __init__(self, i = None, n = None):
        self.i = i
        self.n = n
        self.m = {}
    
    def inpf(self):
        self.n = input("Course name: ")
        self.i = input("Course id: ")

    def __str__(self):
        res = f"""Course id: {self.i}
Course name: {self.n}
Course mark:"""
        for k, v in self.m.items():
            res += f"\t Student {st.n}[{st.i}] mark: {v}\n"
        return res
    

def std_inpf(stlst):
    print("----------------------")
    nb = int(input("Number students: "))
    for idx in range(nb):
        print(f"Student number: {idx + 1}")
        st = Student() 
        st.inpf()
        print("----------------------")
        stlst.append(st)

def cst_inpf(cslst):
    print("----------------------")
    nb = int(input("Number courrses: "))
    for idx in range(nb):
        print(f"Courses number: {idx + 1}")
        cs = Course()
        cs.inpf()
        print("----------------------")
        stlst.append(cs)

def mrk_inpf(cslst, stdlst):
    print("----------------------")
    csid - input("Select the couse by courst ID: ")
    cs = [cs for cs in cslst if cs[0] == csid][0]
    print("Please insert student marks: ")
    for st in stlist:
        print("+++")
        mrk = input(f"Student {st.n}[{st.i}] mark: ")
        cs[2][st.i] = mrk
    print("----------------------")

def std_lstf(stlst):
    print("----------------------")
    print(f"There are {len(stlst)} in system: ")
    for st in stlst:
        print("+++")
        print(st)
    print("----------------------")

def cs_lstf(cslst):
    print("----------------------")
    print(f"There are {len(cslst)} in system: ")
    for cs in cslst:
        print("+++")
        print(cs) 
    print("----------------------")



if __name__ == "__main__":
    stlst = []
    cslst = []
    while True:
        opt = int(
            input(
            """
[Student mark managament]
1. Insert students
2. Insert courses
3. List student info
4. List course info
5. Add mark
6. List mark
7. Exit
Opt:
""" 
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
            pass
        elif opt == 7:
            break
        else:
            print("Option does not exist")

