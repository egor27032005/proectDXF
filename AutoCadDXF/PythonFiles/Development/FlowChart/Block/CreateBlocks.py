from math import cos, sin

import ezdxf

from PythonFiles.Development.FlowChart.Block.BlockSettings import BlockSettings


class CreateBlocks:
    def __init__(self,doc,msp,x,y,ind,rotation,scale):
        self.doc=doc
        self.msp=msp
        self.x=x
        self.y=y
        self.ind=ind
        self.rotation=rotation
        self.scale=scale
        settings=BlockSettings()
        self.BLOCK_NAME=(str)(self.ind)
        print(self.ind)
        self.create_block()
        self.insert_block()
    def create_block(self):
        block_handlers = {
            14: self.block14,
            20: self.block20,
            21: self.block21,
            23: self.block23,
            24: self.block24,
            25: self.block25,
            26: self.block26,
            27: self.block27,
            28: self.block28,
            29: self.block29,
            30: self.block30,
            31: self.block31,
            32: self.block32,
            33: self.block33,
            34: self.block33,
            35: self.block35,
            36: self.block36,
            37: self.block37,
            40: self.block40,
            41: self.block41,
            51: self.block51,
        }
        handler = block_handlers.get(self.ind)
        if handler:
            handler()

    def insert_block(self):
        """Вставляет блок в указанные координаты"""
        self.msp.add_blockref(
            name=self.BLOCK_NAME,
            insert=(self.x, self.y),
            dxfattribs={'rotation': self.rotation,
                        'xscale': self.scale,
                        'yscale': self.scale,
                        'zscale': self.scale,
                        'color': 1
                        }
        )

    def create_fixed_block(self, x=0, y=0, width=10, height=5, rotation=0):
        if self.BLOCK_NAME in self.doc.blocks:
            block = self.doc.blocks.get(self.BLOCK_NAME)
        else:
            block = self.doc.blocks.new(name=self.BLOCK_NAME)
            points = [
                (0, 0),
                (width, 0),
                (width, height),
                (0, height),
                (0, 0)
            ]
            block.add_lwpolyline(points)
            center = (width / 2, height / 2)
            radius = min(width, height) * 0.4
            block.add_circle(center, radius)

            hatch = block.add_hatch(color=7)
            hatch.paths.add_polyline_path(points, is_closed=True)
            hatch.set_pattern_fill("SOLID")

        self.msp.add_blockref(
            self.BLOCK_NAME,
            insert=(x, y),
            dxfattribs={'rotation': rotation}
        )

    def block14(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        rect = block.add_lwpolyline(
            [(0, 0), (0, 2.43), (4.86, 0), (4.86, 2.43), (0, 0)],
            close=True,
            dxfattribs={'color': 7}  # Красный цвет контура
        )
        block.add_line((-0.61, 0), (-0.61, 2.43), dxfattribs={'color': 7})
        block.add_line((5.47, 0), (5.47, 2.43), dxfattribs={'color': 7})
        block.add_line((2.43, 2.67), (2.43, 4.23), dxfattribs={'color': 7})

        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [(2.43, 1.22), (2.04, 4.23), (2.82, 4.23), (2.43, 1.22)],
            is_closed=True
        )

    def block20(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline(
            [(0, 0), (-3.5, 3.5), (0, 7), (3.5, 3.5), (0, 0)],
            close=True,
            dxfattribs={'color': 7}
        )
        block.add_line((-3.5, 3.5), (3.5, 3.5), dxfattribs={'color': 7, 'linetype': "DASHED"})

    def block21(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_circle((0, 0), 3)

        arrow_inside = block.add_hatch()
        arrow_inside.set_solid_fill(color=7)
        arrow_inside.paths.add_polyline_path(
            [(0, 3), (0.75, 1.5), (-0.75, 1.5), (0, 3)],
            is_closed=True
        )
        block.add_line((-3.5, -3.5), (3.5, 3.5), dxfattribs={'color': 7})
        arrow_outside = block.add_hatch()
        arrow_outside.set_solid_fill(color=7)
        arrow_outside.paths.add_polyline_path(
            [(3.5, 3.5), (3, 2), (2, 3), (3.5, 3.5)],
            is_closed=True
        )

    def block23(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (2, 0), (1, 2), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_lwpolyline([(0, 2), (2, 2), (1, 4), (0, 2)], close=True, dxfattribs={'color': 7})
        block.add_lwpolyline([(0, 4), (2, 4), (1, 6), (0, 4)], close=True, dxfattribs={'color': 7})
        block.add_circle((1, 7), 1)

        block.add_lwpolyline([(0.65, 6.5), (0.65, 7.5), (1, 7), (1.35, 7.5), (1.35, 6.5)], close=False,
                             dxfattribs={'color': 7})

    def block24(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 3), (7, 0), (7, 3), (0, 0)], close=True, dxfattribs={'color': 7})

        hatch = block.add_hatch()
        hatch.set_solid_fill(color=7)  # Сплошная заливка цветом 7

        # 3. Добавляем контур круга (правильный способ)
        edge_path = hatch.paths.add_edge_path()
        edge_path.add_ellipse(
            center=(3.5, 1.5),  # Центр круга
            major_axis=(1.0, 0),  # Радиус = 1.0 по оси X
            ratio=1.0,  # Соотношение осей (1.0 = круг)
            start_angle=0,
            end_angle=360,
        )

    def block25(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [(0, 0), (0, 3), (3.5, 1.5), (0, 0)],
            is_closed=True
        )
        block.add_lwpolyline(
            [(7, 0), (7, 3), (3.5, 1.5), (7, 0)],
            close=True,
            dxfattribs={'color': 7}
        )

    def block26(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 1.5), (3.5, 0), (3.5, 1.5), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_line((1.75, 0), (1.75, 3.15), dxfattribs={'color': 7})

        block.add_lwpolyline([(1.75, 1.3), (1.37, 1.53), (2.13, 1.95), (1.37, 2.41), (1.75, 2.64)], close=False,
                             dxfattribs={'color': 7})

        block.add_circle((1.75, 4.2), 1.05)

        block.add_lwpolyline([(1.4, 3.7), (1.4, 4.7), (1.75, 4.2), (2.1, 4.7), (2.1, 3.7)], close=False,
                             dxfattribs={'color': 7})

    def block27(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_circle((0, 0), 3.5)
        block.add_circle((0, 0), 0.7)
        block.add_line((0.7 * cos(0.7854), 0.7 * sin(0.7854)), (3.5 * cos(0.7854), 3.5 * sin(0.7854)),
                       dxfattribs={'color': 7})
        block.add_line((0.7 * cos(2.3562), 0.7 * sin(2.3562)), (3.5 * cos(2.3562), 3.5 * sin(2.3562)),
                       dxfattribs={'color': 7})
        block.add_line((0.7 * cos(3.927), 0.7 * sin(3.927)), (3.5 * cos(3.927), 3.5 * sin(3.927)),
                       dxfattribs={'color': 7})
        block.add_line((0.7 * cos(5.498), 0.7 * sin(5.498)), (3.5 * cos(5.498), 3.5 * sin(5.498)),
                       dxfattribs={'color': 7})

    def block28(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 3), (7, 0), (7, 3), (0, 0)], close=True, dxfattribs={'color': 7})

    def block29(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (2.168, 0), (1.084, 2), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_lwpolyline([(1.084, 2), (3.255, 1), (3.255, 3), (1.084, 2)], close=True, dxfattribs={'color': 7})
        block.add_lwpolyline([(1.084, 2), (1.084, 3.4), (-0.916, 4), (1.9, 5), (0.176, 5.75), (0.176, 6.75)],
                             close=False, dxfattribs={'color': 7})

    def block30(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 2.43), (4.86, 0), (4.86, 2.43), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_line((-0.6, 0), (-0.6, 2.43), dxfattribs={'color': 7})
        block.add_line((5.46, 0), (5.46, 2.43), dxfattribs={'color': 7})
        block.add_line((2.43, 1.215), (2.43, 4.215), dxfattribs={'color': 7})

        hatch = block.add_hatch()
        hatch.set_solid_fill(color=7)
        hatch.paths.add_polyline_path([(2.43, 1.215), (2, 2.673), (2.86, 2.673), (2.43, 1.215)], is_closed=True)

    def block31(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (2.4, 0), (0, 4.8), (2.4, 4.8), (0, 0)], close=True, dxfattribs={'color': 7})

        hatch = block.add_hatch()
        hatch.set_solid_fill(color=7)
        hatch.paths.add_polyline_path([(1.2, 2.4), (3.6, 1.2), (3.6, 3.6), (1.2, 2.4)], is_closed=True)

    def block32(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 2.43), (4.86, 0), (4.86, 2.43), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_line((-0.3, 0), (-0.3, 2.43), dxfattribs={'color': 7})
        block.add_line((5.16, 0), (5.16, 2.43), dxfattribs={'color': 7})
        block.add_line((2.43, 0), (2.43, 3.4), dxfattribs={'color': 7})

        block.add_circle((2.43, 4.8), 1.4)

        block.add_lwpolyline([(2, 4), (2, 5.6), (2.43, 4.8), (2.86, 5.6), (2.86, 4)], close=False,
                             dxfattribs={'color': 7})

    def block33(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 3.3), (6, 0), (6, 3.3), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_line((-0.6, 0), (-0.6, 3.3), dxfattribs={'color': 7})
        block.add_line((6.6, 0), (6.6, 3.3), dxfattribs={'color': 7})
        block.add_line((3, -0.3), (3, 3.6), dxfattribs={'color': 7})

    def block35(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)
        hatch_left.paths.add_polyline_path([(0, 0), (0, 3.35), (6.7, 0), (6.7, 3.35), (0, 0)],is_closed=True)

        block.add_line((3.35, 0), (3.35, 3.35), dxfattribs={'color': 7})

    def block36(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (0, 1.575), (4.5, 3.038), (4.5, -1.463), (0, 0)], close=True, dxfattribs={'color': 7})

    def block37(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_circle((0, 0), 1.35)
        block.add_line((0, -1.35), (0, 1.35), dxfattribs={'color': 7})

        block.add_line((1.35, 0), (2.75, 0), dxfattribs={'color': 7})
        block.add_lwpolyline([(2.75, -1.35), (2.75, 1.35), (6.9, -1.35), (6.9, 1.35), (2.75, -1.35)], close=True, dxfattribs={'color': 7})
        block.add_line((6.9, 0), (8.3, 0))

    def block38(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [(0, 0), (2.63, 0), (4.15, 0), (4.15, 2.63), (0, 0)],
            is_closed=True
        )
        block.add_line((4.15, 1.32), (5.56, 1.32), dxfattribs={'color': 7})
        block.add_line((0, 1.32), (-1.41, 1.32), dxfattribs={'color': 7})

        block.add_line((-2.76, 0), (-2.76, 2.7), dxfattribs={'color': 7})
        block.add_circle((-2.76, 1.32), 1.35)

    def block40(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_lwpolyline([(0, 0), (2.5, 0), (2.5, 5), (0, 5), (0, 0)], close=True, dxfattribs={'color': 7})
        block.add_line((0, 0.625), (2.5, 3.125), dxfattribs={'color': 7})
        block.add_line((0.625, 0), (2.5, 1.875), dxfattribs={'color': 7})
        block.add_line((1.875, 0), (2.5, 0.625), dxfattribs={'color': 7})
        block.add_line((0, 1.875), (2.5, 4.375), dxfattribs={'color': 7})
        block.add_line((0, 3.125), (1.875, 5), dxfattribs={'color': 7})
        block.add_line((0, 4.375), (0.625, 5), dxfattribs={'color': 7})

        block.add_line((0, 0.625), (0.625, 0), dxfattribs={'color': 7})
        block.add_line((0, 1.875), (1.875, 0), dxfattribs={'color': 7})
        block.add_line((0, 3.125), (2.5, 0.625), dxfattribs={'color': 7})
        block.add_line((0, 4.375), (2.5, 1.875), dxfattribs={'color': 7})
        block.add_line((0.625, 5), (2.5, 3.125), dxfattribs={'color': 7})
        block.add_line((1.875, 5), (2.5, 4.375), dxfattribs={'color': 7})

    def block41(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        center = (-1.81, 0)
        radius = 1.81
        start_angle = 0
        end_angle = 180
        block.add_arc(
            center=center,
            radius=radius,
            start_angle=start_angle,
            end_angle=end_angle,
        )
        block.add_line((0, 0), (0, -4), dxfattribs={'color': 7})

    def block51(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        block.add_circle(
            center=(0, 0),
            radius=2.75,
            dxfattribs={
                'color': 1,
                'layer': '0'
            }
        )
        block.add_text(
            text="PG",
            height=2.0,
            dxfattribs={
                'insert': (0, 0),
                'style': 'Standard',
                'layer': '0',
                'color': 1,
                'halign': 1,
                'valign': 3
            }
        )




if __name__ == "__main__":
    # 1. Создаем новый документ (это будет в основной программе)
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()
    ar=[14,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,40,41,51]
    for ind,a in enumerate(ar):
        c=CreateBlocks(doc,msp,ind*10,0,a,0,1)





    # 4. Сохраняем документ (это будет в основной программе)
    doc.saveas("11.dxf")
    print("Файл fixed_blocks.dxf успешно создан")
