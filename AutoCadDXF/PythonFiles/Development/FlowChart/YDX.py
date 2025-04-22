from PythonFiles.Development.FlowChart.Block.CreateBlocks import CreateBlocks


class YDX:
    def __init__(self,doc,msp,startX,startY,name):
        self.doc=doc
        self.msp=msp
        self.startX=startX
        self.startY=startY
        self.name="УДХ-"+name
        self.part1()
        self.tex()
        self.blue_line()
        self.left_pink_line()
        self.right_yellow()
        self.right_pink()

    def put_line(self, x1, y1, x2, y2, color=7):
        layer_name = "Tehnolog"
        self.msp.add_line(
            start=(x1, y1),
            end=(x2, y2),
            dxfattribs={
                "layer": layer_name,
                "color": color,
            }
        )

    def part1(self):
        self.length = 95
        self.hight = 75
        self.put_line(self.startX, self.startY, self.startX + self.length, self.startY)
        self.put_line(self.startX + self.length, self.startY, self.startX + self.length, self.startY + self.hight)
        self.put_line(self.startX, self.startY + self.hight, self.startX + self.length, self.startY + self.hight)
        self.put_line(self.startX, self.startY + self.hight, self.startX, self.startY)

        if 'DGNSTYLE4' not in self.doc.linetypes:
            self.doc.linetypes.new(
                name='DGNSTYLE4',
                dxfattribs={
                    'description': 'DGN Style 4 - Dash 10, Gap 5, Dot, Gap 5',
                    'pattern': 'A,10,-5,0,-5',  # Черта (10), Пробел (5), Точка (0), Пробел (5)
                    'length': 20.0  # Общая длина шаблона (10 + 5 + 0 + 5 = 20)
                }
            )

        self.msp.add_lwpolyline([
            (self.startX - 6, self.startY - 10),
            (self.startX - 6, self.startY + 89),
            (self.startX + 97, self.startY + 89),
            (self.startX + 97, self.startY - 10),
            (self.startX - 6, self.startY - 10),
        ], dxfattribs={"layer": "Tehnolog", "color": 7, "linetype": "DGNSTYLE4"})

    def blue_line(self):
        self.put_line(self.startX, self.startY + 68, self.startX - 12, self.startY + 68, 5)
        self.put_line(self.startX - 12, self.startY + 68, self.startX - 12, self.startY + 111, 5)

        start_cube_x = self.startX - 13.5
        start_cube_y = self.startY + 111
        self.msp.add_lwpolyline(
            [(start_cube_x, start_cube_y),
             (start_cube_x, start_cube_y + 3),
             (start_cube_x + 3, start_cube_y + 3),
             (start_cube_x + 3, start_cube_y),
             (start_cube_x, start_cube_y),
             (start_cube_x + 3, start_cube_y + 3),
             (start_cube_x, start_cube_y + 3),
             (start_cube_x + 3, start_cube_y),
             (start_cube_x, start_cube_y)
             ], close=True, dxfattribs={"layer": "Tehnolog", "color": 7})

        CreateBlocks(self.doc, self.msp, self.startX - 13.5, self.startY + 114, 40, 0, 3/2.5)

        CreateBlocks(self.doc, self.msp, self.startX - 12, self.startY + 124, 41, 0, 1)

    def left_pink_line(self):
        self.put_line(self.startX, self.startY + 37, self.startX - 1, self.startY + 37, 6)
        self.msp.add_circle((self.startX - 2.5, self.startY + 37), 1.5, dxfattribs={"layer": "Tehnolog", "color": 6})

        self.put_line(self.startX, self.startY + 27, self.startX - 3, self.startY + 27, 6)
        hatch = self.msp.add_hatch(dxfattribs={"layer": "Tehnolog"})
        hatch.set_solid_fill(color=7)  # Сплошная заливка
        hatch.paths.add_polyline_path([
            (self.startX - 3, self.startY + 27),  # Вершина 1
            (self.startX - 5.25, self.startY + 28),  # Вершина 2
            (self.startX - 5.25, self.startY + 26),  # Вершина 3
            (self.startX - 3, self.startY + 27)  # Замыкаем треугольник
        ])

    def right_yellow(self):
        start_x = self.startX + self.length
        start_y = self.startY
        self.put_line(start_x, start_y + 11, start_x + 1, start_y + 11, 2)
        self.put_line(start_x + 1, start_y + 9.75, start_x + 1, start_y + 12.25, 2)
        self.put_line(start_x + 1.675, start_y + 9.75, start_x + 1.675, start_y + 12.25, 2)
        self.put_line(start_x + 1.675, start_y + 11, start_x + 7.2, start_y + 11, 2)

        CreateBlocks(self.doc, self.msp, start_x + 7.8, start_y + 9.4, 34, 0, 1)

        self.put_line(start_x + 14.4, start_y + 11, start_x + 16.4, start_y + 11, 2)
        self.put_line(start_x + 16.4, start_y + 9.125, start_x + 16.4, start_y + 12.875, 2)
        self.put_line(start_x + 16.4, start_y + 9.125, start_x + 17.4, start_y + 9.125, 2)
        self.put_line(start_x + 16.4, start_y + 12.875, start_x + 17.4, start_y + 12.875, 2)

        self.put_line(start_x, start_y + 22, start_x + 1, start_y + 22, 2)
        self.put_line(start_x + 1, start_y + 20.75, start_x + 1, start_y + 23.25, 2)
        self.put_line(start_x + 1.675, start_y + 20.75, start_x + 1.675, start_y + 23.25, 2)
        self.put_line(start_x + 1.675, start_y + 22, start_x + 7.2, start_y + 22, 2)

        CreateBlocks(self.doc, self.msp, start_x + 7.8, start_y + 20.4, 34, 0, 1)

        self.put_line(start_x + 14.4, start_y + 22, start_x + 16.4, start_y + 22, 2)
        self.put_line(start_x + 16.4, start_y + 20.125, start_x + 16.4, start_y + 23.875, 2)
        self.put_line(start_x + 16.4, start_y + 20.125, start_x + 17.4, start_y + 20.125, 2)
        self.put_line(start_x + 16.4, start_y + 23.875, start_x + 17.4, start_y + 23.875, 2)


    def right_pink(self):
        start_x = self.startX + self.length
        start_y = self.startY
        self.put_line(start_x, start_y + 42, start_x + 69, start_y + 42, 6)
        self.msp.add_lwpolyline(
            [(start_x + 69, start_y + 40.125),
             (start_x + 69, start_y + 43.875),
             (start_x + 78, start_y + 43.875),
             (start_x + 78, start_y + 40.125),
             (start_x + 69, start_y + 40.125)
             ], close=True, dxfattribs={"layer": "Tehnolog", "color": 7})
        self.put_line(start_x + 78, start_y + 42, start_x + 92, start_y + 42, 6)

        CreateBlocks(self.doc, self.msp, start_x + 92.35, start_y + 40.25, 32, 0, 7/4.5)

        self.put_line(start_x + 100.3, start_y + 42, start_x + 114, start_y + 42, 6)




    def tex(self):
        self.msp.add_mtext(self.name, dxfattribs={
            'insert': (self.startX+40,self.startY+50),
            'char_height': 16,

            'color': 7,
            'style': 'ROMANS',  # Применяем стиль Romans
            'attachment_point': 5  # Аналог AttachmentPoint в pyautocad
        })