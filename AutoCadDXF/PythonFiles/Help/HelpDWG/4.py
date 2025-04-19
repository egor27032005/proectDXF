import ezdxf


def copy_layers_to_new_dxf(source_file_path, output_file_path):
    """
    Копирует все слои из исходного DXF-файла в новый файл

    :param source_file_path: Путь к исходному DXF-файлу
    :param output_file_path: Путь для сохранения нового DXF-файла
    """
    try:
        # Загружаем исходный DXF-документ
        source_doc = ezdxf.readfile(source_file_path)

        # Создаем новый DXF-документ
        new_doc = ezdxf.new(dxfversion=source_doc.dxfversion)

        # Копируем все слои из исходного документа
        for layer in source_doc.layers:
            # Проверяем, существует ли слой с таким именем в новом документе
            if layer.dxf.name not in new_doc.layers:
                new_doc.layers.add(
                    name=layer.dxf.name,
                    color=layer.dxf.color,
                    linetype=layer.dxf.linetype,
                    lineweight=layer.dxf.lineweight
                )

        # Сохраняем новый документ
        new_doc.saveas(output_file_path)
        print(f"Все слои успешно скопированы в новый файл: {output_file_path}")

    except IOError as e:
        print(f"Ошибка при работе с файлом: {str(e)}")
    except ezdxf.DXFError as e:
        print(f"Ошибка DXF: {str(e)}")
    except Exception as e:
        print(f"Неизвестная ошибка: {str(e)}")


# Пример использования
copy_layers_to_new_dxf("source.dxf", "output.dxf")