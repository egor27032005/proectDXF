import ezdxf


doc=ezdxf.new("R2000")
msp=doc.modelspace()
hatch=msp.add_hatch(color=2)
hatch.paths.add_polyline_path([(0,0),(10,0),(10,10),(0,10)],is_closed=True)

doc.saveas("solid_hatch.dxf")