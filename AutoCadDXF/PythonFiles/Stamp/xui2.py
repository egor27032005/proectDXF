import ezdxf
from collections import defaultdict

doc = ezdxf.readfile("Python.dxf")
msp = doc.modelspace()

block_usage_count = defaultdict(int)

inserts = msp.query('INSERT')

def get_xdata_name(name):
    try:
        xdata = doc.blocks[name].block_record.get_xdata('AcDbBlockRepBTag')
    except Exception as exc:
        print(f"Error reading xdata for {name}")
        print(exc)
        return name
    for tag, value in xdata:
        if tag == 1005:
            new_name = doc.entitydb[value].dxf.name
            print(f"new name {new_name}")
    return new_name

for insert in inserts:
    block_name = insert.dxf.name
    if block_name.startswith('*'):
        print(f"anonymous name {block_name}")
        name = get_xdata_name(block_name)
    else:
        name = block_name
    block_usage_count[name] += 1


print("Block Name | Usage Count")
print("------------------------")
for block_name, usage_count in block_usage_count.items():
    print(f"{block_name} | {usage_count}")