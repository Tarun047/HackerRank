class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def get_inputs():
    x1,y1,x2,y2 = map(int,input().split())
    p = Point(x1,y1)
    q = Point(x2,y2)
    return (p,q)

def find_if_intersect(l1,r1,l2,r2):
    if(l1.x > r2.x or l2.x > r1.x):
        return False
    if (l1.y < r2.y or l2.y < r1.y):
        return False
    return True

def find_area(p,q):
    return abs((p.x-q.x)*(p.y-q.y))

def find_common_area(p,q,a,b):
    l = min(q.x,b.x)-max(p.x,a.x)
    b = min(q.y,b.y)-max(p.y,a.y)
    a = l*b
    return abs(l*b)
t = int(input())
while t:
    p,q = get_inputs()
    a,b = get_inputs()
    TA = find_area(p,q)+find_area(a,b)
    if(find_if_intersect(Point(p.x,q.y),Point(q.x,p.y),Point(a.x,b.y),Point(b.x,a.y))):
        TA = TA - find_common_area(p,q,a,b)
    print(TA)
    t-=1
