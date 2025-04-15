import ezdxf
from ezdxf.math import Vec2


class FixedBlockCreator:
    # Фиксированное имя блока, которое нельзя изменить
    BLOCK_NAME = "Скважина добывающая нефтяная"

    def __init__(self, doc, msp,x,y,rotation=0):
        """
        Инициализация создателя DXF-блоков с фиксированным именем
        :param doc: существующий документ DXF
        :param msp: пространство модели из документа
        """
        self.doc = doc
        self.msp = msp
        self.x=x
        self.y=y
        self.rotation=rotation
        self.create_fixed_block(x=self.x, y=self.y,rotation=self.rotation)

    # def create_fixed_block(self, x=0, y=0, width=10, height=5, rotation=0):
    #     """
    #     Создает блок с фиксированным именем и заданными параметрами
    #     :param x: координата X точки вставки
    #     :param y: координата Y точки вставки
    #     :param width: ширина блока
    #     :param height: высота блока
    #     :param rotation: угол поворота в градусах
    #     """
    #     if self.BLOCK_NAME in self.doc.blocks:
    #         block = self.doc.blocks.get(self.BLOCK_NAME)
    #     else:
    #         block = self.doc.blocks.new(name=self.BLOCK_NAME)
    #
    #         points = [
    #             (0, 0),
    #             (width, 0),
    #             (width, height),
    #             (0, height),
    #             (0, 0)
    #         ]
    #         block.add_lwpolyline(points)
    #         center = (width / 2, height / 2)
    #         radius = min(width, height) * 0.4
    #         block.add_circle(center, radius)
    #     self.msp.add_blockref(
    #         self.BLOCK_NAME,
    #         insert=(x, y),
    #         dxfattribs={'rotation': rotation}
    #     )
    def create_fixed_block(self, x=0, y=0, width=10, height=5, rotation=0, fill_color=1):
        """
        :param fill_color: номер цвета заливки (по умолчанию 1 - красный)
        """
        if self.BLOCK_NAME in self.doc.blocks:
            block = self.doc.blocks.get(self.BLOCK_NAME)
        else:
            block = self.doc.blocks.new(name=self.BLOCK_NAME)

            # Контур блока (прямоугольник)
            points = [
                (0, 0),
                (width, 0),
                (width, height),
                (0, height)
            ]
            block.add_lwpolyline(points, close=True)

            # Заливка прямоугольника
            hatch = block.add_hatch(color=fill_color)
            hatch.paths.add_polyline_path(points, is_closed=True)
            hatch.set_pattern_fill("SOLID")  # Сплошная заливка

            # Круг в центре (без заливки)
            center = (width / 2, height / 2)
            radius = min(width, height) * 0.4
            block.add_circle(center, radius)

        # Вставка блока
        self.msp.add_blockref(
            self.BLOCK_NAME,
            insert=(x, y),
            dxfattribs={'rotation': rotation}
        )


# Пример использования
if __name__ == "__main__":
    # 1. Создаем новый документ (это будет в основной программе)
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()

    # 2. Создаем экземпляр нашего создателя блоков
    block_creator = FixedBlockCreator(doc, msp,0,0,0)


    # 4. Сохраняем документ (это будет в основной программе)
    doc.saveas("fixed_blockwsd24.dxf")
    print("Файл fixed_blocks.dxf успешно создан")