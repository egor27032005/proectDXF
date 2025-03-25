class CoverNKY:
    def __init__(self,msp,x1,x2,y1,y2):
        self.msp=msp
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.lines(self.x1,self.x2,self.y1,self.y2)
    def lines(self,x1,x2,y1,y2):
        rect_points = [
            (x1, y1),  # Левый нижний угол
            (x2, y1),  # Правый нижний угол
            (x2, y2),  # Правый верхний угол
            (x1, y2),  # Левый верхний угол
            (x1, y1)  # Замыкаем прямоугольник
        ]

        # self.msp.add_lwpolyline(rect_points, dxfattribs={'color': 3})
        self.msp.add_lwpolyline(rect_points, dxfattribs={
        'color': 3,  # Зеленый цвет (3 — это индекс зеленого цвета в AutoCAD)
        'lineweight': 0.1  # Толщина линии (опционально)
         })