from PythonFiles.Stamp.Stamp import Stamp


class PreparationTit:
    def __init__(self,doc,msp,data,points):
        self.doc=doc
        self.msp=msp
        self.data=data
        self.points=points
        self.new_array = self.convert_to_strings(self.data)
        self.stamp=Stamp(self.doc,self.msp,self.points)

    def convert_to_strings(self, nested_list):
        ar = [[str(item) if str(item) != "nan" else "" for item in sublist] for sublist in nested_list]
        a = [self.remove_trailing_empty_strings(x) for x in ar]
        return a
    def remove_trailing_empty_strings(self, strings):
        strings_copy = strings.copy()
        while strings_copy and strings_copy[-1] == "":
            strings_copy.pop()
        return strings_copy