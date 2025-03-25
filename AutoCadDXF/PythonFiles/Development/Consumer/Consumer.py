import os
import ezdxf
from ezdxf.addons import Importer

from PythonFiles.Development.Consumer.El_dvig import El_dvig
from PythonFiles.Development.Consumer.Wardrobe import Wardrobe


class Consumer:
    def __init__(self, msp, doc, name, x, y):
        self.doc = doc
        self.msp = msp
        self.name = name
        self.x = x
        self.y = y
        self.getConsumer()

    def getConsumer(self):
        match self.name:
            case "шкаф":
                self.two("5.dxf", '5', (self.x, self.y))
            case "коробка":
                self.two("4.dxf", '4', (self.x, self.y))
            case "э. двигатель":
                self.two("2.dxf", '2', (self.x, self.y))
            case "сх. у наружным освещением":
                self.two("3.dxf", '3', (self.x, self.y))
            case "сх. у э. двиг. с кнопочным постом и каробкой зажимов":
                self.two("blocks.dxf",'b_test',(self.x,self.y))
            case "сх. у э. двиг. с кнопочным постом":
                self.two("1.dxf", '1', (self.x, self.y))

    def move_block(self, input_file, target_coords):
        """
        Переносит блок (Block Reference) из DXF-файла на указанные координаты в новый файл.

        :param input_file: Путь к исходному DXF-файлу.
        :param target_coords: Кортеж (x, y) — целевые координаты.
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        dxf_file_path = os.path.join(current_directory, input_file)
        doc = ezdxf.readfile(dxf_file_path)
        msp = doc.modelspace()  # Получаем пространство модели исходного файла
        entities = list(msp)
        if len(entities) != 1:
            raise ValueError("Файл должен содержать ровно один объект.")
        entity = entities[0]
        if entity.dxftype() != "INSERT":
            raise ValueError("Файл должен содержать блок (Block Reference).")
        new_entity = entity.copy()
        new_entity.dxf.insert = target_coords
        block_def = doc.blocks.get(entity.dxf.name)
        if block_def:
            if entity.dxf.name not in self.doc.blocks:
                new_block = self.doc.blocks.new(name=block_def.name)
                for block_entity in block_def:
                    new_block.add_entity(block_entity.copy())
            else:
                # Если блок уже существует, используем его
                new_block = self.doc.blocks.get(entity.dxf.name)
        self.msp.add_entity(new_entity)
    def two(self,input_file,name,coord):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        dxf_file_path = os.path.join(current_directory, input_file)
        source_dxf = ezdxf.readfile(dxf_file_path)
        if name not in source_dxf.blocks:
            print("Block 'b_test' not defined.")
        importer = Importer(source_dxf, self.doc)
        importer.import_block(name)
        importer.finalize()
        self.msp.add_blockref(name, insert=coord)





