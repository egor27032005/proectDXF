import ezdxf

from PythonFiles.Development.FlowChart.Block.BlockSettings import BlockSettings


class CreateBlocks:
    def __init__(self,doc,msp,x,y,ind,rotation=0):
        self.doc=doc
        self.msp=msp
        self.x=x
        self.y=y
        self.ind=ind
        self.rotation=rotation
        settings=BlockSettings()
        self.BLOCK_NAME=(str)(self.ind)
        self.create_block()
        self.insert_block()
    def create_block(self):
        match self.ind:
            case 14:
                self.block14()
            case 33:
                self.block33()
            case 35:
                self.block35()
            case 36:
                self.block36()
    def insert_block(self):
        """Вставляет блок в указанные координаты"""
        self.msp.add_blockref(
            name=self.BLOCK_NAME,
            insert=(self.x, self.y),
            dxfattribs={'layer': '0'}
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
        if self.BLOCK_NAME in doc.blocks:
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
    def block26(self):
        if self.BLOCK_NAME in doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        rect = block.add_lwpolyline(
            [(0, 0), (0, 1.75), (3.5, 0), (3.5, 1.75), (0, 0)],
            close=True,
            dxfattribs={'color': 7}  # Красный цвет контура
        )
        block.add_line((1.75, 0), (1.75, 3.15), dxfattribs={'color': 7})
        block.add_circle((1.75,4.2), 1)
        rect = block.add_lwpolyline(
            [(1.75, 1.28), (1.37, 1.52), (3.5, 0), (3.5, 1.75), (0, 0)],
            close=True,
            dxfattribs={'color': 7}  # Красный цвет контура
        )

    def block32(self):
        if self.BLOCK_NAME in doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        rect = block.add_lwpolyline(
            [(0, 0), (1.37, 3.55), (0, 3.55), (2.37, 0), (0, 0)],
            close=True,
            dxfattribs={'color': 7}  # Красный цвет контура
        )
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [(1.18,2.37), (3.55, 3.55), (3.55, 1.18), (1.18,2.37)],
            is_closed=True
        )
    def block33(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        rect = block.add_lwpolyline(
            [(0, 0), (0, 3), (7, 0), (7, 3), (0, 0)],
            close=True,
            dxfattribs={'color': 7}  # Красный цвет контура
        )
        block.add_line((3.5,0), (3.5,4), dxfattribs={'color': 7})

        block.add_line((8,0), (8,3), dxfattribs={'color': 7})
        block.add_line((-1,0), (-1,3), dxfattribs={'color': 7})

        block.add_circle((3.5,5.5), 1.5)


        
    def block35(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        rect = block.add_lwpolyline(
            [(0, 0), (0, 3), (7, 0), (7, 3), (0, 0)],
            close=True,
            dxfattribs={'color': 1}  # Красный цвет контура
        )
        block.add_line((3.5,0), (3.5,3), dxfattribs={'color': 7})

        block.add_line((8,0), (8,3), dxfattribs={'color': 7})
        block.add_line((-1,0), (-1,3), dxfattribs={'color': 7})
    def block36(self):
        if self.BLOCK_NAME in self.doc.blocks:
            return
        block = self.doc.blocks.new(name=self.BLOCK_NAME)
        hatch_left = block.add_hatch()
        hatch_left.set_solid_fill(color=7)  # Сплошная заливка красным
        hatch_left.paths.add_polyline_path(
            [(0, 0), (0, 3), (7, 0), (7, 3), (0, 0)],
            is_closed=True
        )
        block.add_line((3.5,0), (3.5,3), dxfattribs={'color': 7})

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
        block.add_circle((-2.76,1.32), 1.35)




if __name__ == "__main__":
    # 1. Создаем новый документ (это будет в основной программе)
    doc = ezdxf.new('R2010', setup=True)
    doc.units = ezdxf.units.MM
    msp = doc.modelspace()

    # 2. Создаем экземпляр нашего создателя блоков

    block_creator3 = CreateBlocks(doc, msp,-15,0,36)
    block_creator4 = CreateBlocks(doc, msp,0,0,35)
    block_creator5 = CreateBlocks(doc, msp,15,0,33)


    # 4. Сохраняем документ (это будет в основной программе)
    doc.saveas("1111111111111.dxf")
    print("Файл fixed_blocks.dxf успешно создан")
    #
    # 1.7543965192890028
    # 1.2938709316491668
    # 1.3729010702952564
    # 1.5283537241191425
    # 2.135891968282749
    # 1.9639609373163012
    # 1.3729010702952564
    # 2.4329265222562526
    # 1.7543965192890028
    # 2.650730128854889