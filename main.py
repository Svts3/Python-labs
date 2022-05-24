
import models as md
def main():
    sphere = md.Sphere(2.5,7.6,1.2,4)
    segment = md.Segment(x=2.5, y = 6.6, ending_x=6.6, ending_y=8.7)
    dot = md.Dot(2.5,12.5)
    circle = md.Circle(2.5,1.6,5)
    parallelepiped = md.Parallelepiped(20,25,8)
    rectangle = md.Rect(side=5,top_side=7)
    list_of_figures = [sphere,segment,dot,circle,parallelepiped,rectangle]
    for i in list_of_figures:
        
        print(i)
        print('\n')

if __name__=="__main__":
    main()