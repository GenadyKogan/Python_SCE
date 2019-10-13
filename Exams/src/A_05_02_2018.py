'''Task_1'''
from _functools import reduce
from textwrap import indent
class Tree():
    def __init__(self,entry, nodes=None):
        self.entry = entry
        self.nodes = nodes
    def __repr__(self):
        if self.nodes:
            return 'Tree({0},{1})'.format(self.entry,repr(self.nodes))
        return 'Tree({0})'.format(self.entry)
    
def map_transform(tree,g=lambda x,y:x+y):
    if type(tree)!= tuple:
        return Tree(tree)
    
    nodes = list(map_transform(branch, g) for branch in tree)
    
    return Tree(reduce(g,(n.entry for n in nodes)),nodes)
        
def safe_map_transform(tree,g):
    try:
        map_transform(tree, g)
    except TypeError as fee:
        print(fee)

'''print(map_transform(((2, 3), (4, (5, 6)))))
Tree(20,[Tree(5,[Tree(2), Tree(3)]), Tree(15,[Tree(4), Tree(11,[Tree(5), Tree(6)])])])
print(map_transform(((2, 3), (4, (5, 6, (8, 2)))),lambda x,y: x if x>y else y))
Tree(8,[Tree(3,[Tree(2), Tree(3)]), Tree(8,[Tree(4), Tree(8,[Tree(5), Tree(6), Tree(8,[Tree(8), Tree(2)])])])])
print(safe_map_transform(((2, 'a'), (4, (8, 2))),min))'''
        
'''Task_2'''

def make_student_statistics(list):
    def max_course(course):
        max_grade = max(map(lambda x: x[2],filter(lambda x: x[1] == course, lst)))
        return tuple(map(lambda x: (x[0],x[2]),filter(lambda x: x[2] == max_grade and x[1] == course, lst)))
    #return 
    def avg_course(course):
        course_grades = tuple(map(lambda x:(x[2]),filter(lambda x: x[1]==course,list)))
        return  sum(course_grades)/len(course_grades)
        
    def avg_student(stud):
        stud_grades =  tuple(map(lambda x: x[2],filter(lambda x: x[0]==stud,list)) )
        return sum(stud_grades)/len(stud_grades)
    def course_grades(course):
        sorted_c_grades =  tuple(map(lambda x: x[2],filter(lambda x: x[1] == course, lst)))
        ind =0
        def next():
            nonlocal ind
            try:
                item = sorted_c_grades[ind]
                ind+=1
                return item
            except (IndexError):
                return 'End of list'
            return 0
        def hasNext():
            return ind<len(sorted_c_grades)
        return {'nextGrade':next, 'hasNext':hasNext}
    return {'get_course_avg': avg_course,'get_course_max': max_course,'get_student_avg': avg_student,'get_student_avg':avg_student,'get_course_grades':course_grades}
        
lst = (('Moshe','PPL',60),('Sara','DS',80),
        ('Itzhak','PPL',100),('Moshe','Alg',75),
         ('Sara','PPL',100),('Moshe','DS',80),
         ('Sara','Alg',60),('Itzhak','DS',100),
         ('Itzhak','Alg',100))

stats = make_student_statistics(lst)

print(stats['get_course_avg']('PPL'))  
print(stats['get_course_max']('PPL'))
print(stats['get_student_avg']('Moshe'))
grades = stats['get_course_grades']('Alg')
while grades['hasNext']():
    print(grades['nextGrade']())
'''grades = stats['get_course_grades']('Alg')
for _ in range(1,6):
    print(grades['nextGrade']())'''