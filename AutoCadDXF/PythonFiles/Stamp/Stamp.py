class Stamp:
    def __init__(self,doc,msp,points):
        self.doc=doc
        self.msp=msp
        self.block = self.doc.blocks.new(name='штамп')
        self.points=points
        self.max_y, self.min_y, self.max_x, self.min_x = self.points[0], self.points[1], self.points[2], self.points[-1]
        self.sheet_sizes = {
    'A4': (210, 297),
    'A3': (297, 420),
    'A2': (420, 594),
    'A1': (594, 841),
}
        self.get_size()


    def get_size(self):
        self.size_x=self.max_x-self.min_x
        self.size_y=self.max_y-self.min_y
        print(self.find_minimal_paper_size(self.size_x,self.size_y))
        print(self.size_x,self.size_y)

    def find_minimal_paper_size(self,x_size, y_size):
        paper_sizes = {
            'A4': (210, 297),
            'A3': (297, 420),
            'A2': (420, 594),
            'A1': (594, 841)
        }

        if x_size > y_size:
            drawing_width = x_size
            drawing_height = y_size
        else:
            drawing_width = y_size
            drawing_height = x_size
        for format_name, (width, height) in sorted(paper_sizes.items(), key=lambda x: x[1][0]):
            if drawing_width <= width and drawing_height <= height:
                return format_name
        for format_name, (width, height) in sorted(paper_sizes.items(), key=lambda x: x[1][0]):
            if drawing_width <= width * 2 and drawing_height <= height:
                return f"2x {format_name} (соединены по ширине)"
            if drawing_width <= width and drawing_height <= height * 2:
                return f"2x {format_name} (соединены по высоте)"
        return "Чертеж слишком большой для стандартных форматов"

