import ezdxf
from ezdxf import units
from ezdxf.colors import RGB

import ezdxf


class Pipe:
    def __init__(self, doc, msp):
        self.doc = doc
        self.msp = msp
        self.layer_name = "ТХ_С_ДРЕНАЖ_035"
        self.color = 40

        self._create_layer_if_not_exists()

    def _create_layer_if_not_exists(self):
        """Создает слой 'TX_DRENAG', если его нет."""
        if self.layer_name not in self.doc.layers:
            self.doc.layers.add(
                name=self.layer_name,
                color=self.color,  # True Color (0x802203)
            )

    def draw_line(self, start_point, end_point):
        """Рисует линию на слое 'TX_DRENAG' с заданным цветом."""
        line = self.msp.add_line(
            start=start_point,
            end=end_point,
            dxfattribs={
                "layer": self.layer_name,
            }
        )
        return line
# Создаем новый DXF-документ
# doc = ezdxf.new(dxfversion='R2010', setup=True)
# msp = doc.modelspace()
#
# # Создаем объект Pipe
# pipe = Pipe(doc, msp)
#
# # Рисуем линию от (0, 0, 0) до (10, 10, 0)
# pipe.draw_line((0, 0, 0), (10, 10, 0))
#
# # Сохраняем документ
# doc.saveas("output.dxf")