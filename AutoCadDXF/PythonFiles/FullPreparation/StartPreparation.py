import os

import ezdxf

from PythonFiles.FullPreparation.PreparationKTPN1 import PreparationKTPN1
from PythonFiles.FullPreparation.PreparationKTPN2 import PreparationKTPN2
from PythonFiles.FullPreparation.PreparationNKY import PreparationNKY
from PythonFiles.FullPreparation.PreparationTit import PreparationTit


class StartPreparation:
    def __init__(self,data,type,msp,doc):
        self.data=data
        self.type=type
        self.msp=msp
        self.doc=doc
        self.copy_styles_to_new_doc()

        # self.doc.styles.new(name="RomansStyle", dxfattribs={
        #     'font': 'Romans.shx',  # Указываем шрифт Romans
        #     'width': 1.0  # Ширина шрифта (можно настроить)
        # })
        self.distribution()
        self.min_x = float('inf')  # Самая левая точка
        self.max_x = float('-inf')  # Самая правая точка
        self.min_y = float('inf')  # Самая нижняя точка
        self.max_y = float('-inf')
        self.get_point()

        self.points=[self.max_y,self.min_y,self.max_x,self.min_x]
        # self.pr=PreparationTit(self.doc,self.msp, self.data,self.points)
    def distribution(self):
        match self.type:
            case "КТПН1":
                self.pr=PreparationKTPN1(self.data,self.msp)
            case "КТПН2":
                self.pr=PreparationKTPN2(self.data,self.msp)
            case "НКУ":
                self.pr = PreparationNKY(self.data, self.msp)

    import ezdxf

    def copy_styles_to_new_doc(self):
        """
        Копирует стили текста (шрифты) из исходного DXF-файла в новый документ версии R2000.
        Возвращает кортеж: (новый документ, его Model Space).
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path1 = os.path.join(current_dir, "../../PythonFiles/FullPreparation/shrivt.dxf")
        source_filename = file_path1
        source_doc = ezdxf.readfile(source_filename)
        source_styles = source_doc.styles

        new_styles = self.doc.styles

        # Копирование нестандартных стилей
        for style in source_styles:
            if style.dxf.name.upper() == "STANDARD":
                continue
            new_style = new_styles.new(name=style.dxf.name)
            new_style.dxf.font = style.dxf.font
            new_style.dxf.width = style.dxf.width
            new_style.dxf.oblique = style.dxf.oblique
            new_style.dxf.bigfont = style.dxf.bigfont

    def update_bounds(self,x, y):
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y

    def get_point(self):
        for entity in self.msp:
            # Обрабатываем линии
            if entity.dxftype() == 'LINE':
                self.update_bounds(entity.dxf.start[0], entity.dxf.start[1])
                self.update_bounds(entity.dxf.end[0], entity.dxf.end[1])

            # Обрабатываем полилинии
            elif entity.dxftype() == 'LWPOLYLINE':
                for point in entity.get_points():
                    self.update_bounds(point[0], point[1])




