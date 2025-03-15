import ezdxf
from ezdxf import units

class CxWithOutdoorLighting:
    def __init__(self, msp, x, y,str="Текст"):
        self.msp = msp
        self.x = x
        self.y = y
        self.textArray=["К-ФР\nКВВГнг(А)-ХЛ 2х2,5-10м","Н-ЯУО\nВВГнг(А)-LS 5х6-10м","К-SB\n"+str]
        self.textArrayCord=[(self.x-17,self.y+6),(self.x-4,self.y+6),(self.x+22,self.y+6)]
        self.printer()
        self.text()
        self.lamp(x-13,y+40)
    def printer(self):
        points=[self.x-3,self.y-3,self.x-13,self.y-3,self.x-13,self.y+40]
        formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
        self.msp.add_lwpolyline(formatted_points)

        points = [self.x + 3, self.y - 3, self.x + 13, self.y - 3, self.x + 13, self.y + 40,self.x + 27, self.y + 40,self.x + 27, self.y + 4]
        formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
        self.msp.add_lwpolyline(formatted_points)

        hatch1 = self.msp.add_hatch(color=2)
        hatch1.paths.add_polyline_path([(self.x-3, self.y-3), (self.x-3, self.y-6),(self.x+3, self.y-6), (self.x+3, self.y-3)], is_closed=True)

        points = [self.x - 3, self.y, self.x -3, self.y - 6, self.x +3, self.y -6,self.x+3,self.y,self.x - 3,self.y]
        formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
        self.msp.add_lwpolyline(formatted_points, dxfattribs={'color': 2})

        x=self.x+27
        y=self.y+4
        points = [x-2,y,x-2,y-8,x+2,y-8,x+2,y,x-2,y]
        formatted_points = [(points[i], points[i + 1]) for i in range(0, len(points), 2)]
        self.msp.add_lwpolyline(formatted_points,dxfattribs={'color': 2})

        self.msp.add_circle((x,y-2), 1, dxfattribs={'color': 2})
        self.msp.add_circle((x,y-6), 1, dxfattribs={'color': 2})
    def lamp(self,x,y):
        center = (x, y)  # Центр полукруга
        radius = 2.5  # Радиус полукруга
        start_angle = 0  # Начальный угол (0 градусов)
        end_angle = 180  # Конечный угол (180 градусов)

        # Добавляем дугу (полукруг) с желтым цветом
        arc = msp.add_arc(center, radius, start_angle, end_angle)
        arc.dxf.color = 2

    def text(self):
        for i, text in enumerate(self.textArray):
            self.msp.add_mtext(text, dxfattribs={
                'insert': self.textArrayCord[i],
                'char_height': 2.5,
                'line_spacing_factor': 1.2,
                'rotation': 90,
                'color': 1,
                'style': 'RomansStyle',  # Применяем стиль Romans
                'attachment_point': 1  # Аналог AttachmentPoint в pyautocad
            })



# Пример использования
doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

# Устанавливаем единицы измерения (опционально)
doc.units = units.MM

# Создаем экземпляр класса с координатами (100, 100)
cx_schema = CxWithOutdoorLighting(msp, 100, 100)

# Сохраняем DXF-файл
doc.saveas('outdoor_lighting_schema9.dxf')