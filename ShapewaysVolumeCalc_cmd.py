import rhinoscriptsyntax as rs

__commandname__ = "ShapewaysVolumeCalc"
def compute_from_material(material_name, handling_cost, volume_cost, volume):
    cost = handling_cost + volume_cost * volume
    print "{}: ${} + ${} * {:0.2f} cm3 = ${:0.2f}".format(material_name, handling_cost, volume_cost, volume, cost)

def RunCommand( is_interactive ):
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    if obj and rs.IsMeshClosed(obj):
        volume = rs.MeshVolume(obj)[1]/1000
        compute_from_material("Gold 14k", 50, 600, volume)
        compute_from_material("Gold 18k", 100, 800, volume)
        compute_from_material("Platinum", 100, 1750, volume)
        compute_from_material("Silver Polished", 35, 20, volume)
        compute_from_material("Silver -Raw", 30, 20, volume)
        compute_from_material("Bronze/Brass -Polished", 20, 18, volume)
        compute_from_material("Bronze/Brass -Raw", 10, 16, volume)
