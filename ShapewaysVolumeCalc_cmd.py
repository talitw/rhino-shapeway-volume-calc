import rhinoscriptsyntax as rs

__commandname__ = "ShapewaysVolumeCalc"

def RunCommand( is_interactive ):
    obj = rs.GetObject("Select mesh", rs.filter.mesh )
    if obj and rs.IsMeshClosed(obj):
        volume = rs.MeshVolume(obj)[1]/1000
        gold_14k = volume * 600 + 50
        gold_18k = volume * 800 + 100
        platinum = volume * 1750 + 100
        silver_polished = volume * 20 + 35
        silver_raw = volume * 20 + 30
        bronze_or_brass_polished = volume * 18 + 20
        bronze_or_brass_raw = volume * 16 + 10

        print "Gold 14k: $50 + $600 * {:0.2f} cm3 = ${:0.2f}".format(volume, gold_14k)
        print "Gold 18k: $100 + $800 * {:0.2f} cm3 = ${:0.2f}".format(volume, gold_18k)
        print "Platinum: $100 + $1750 * {:0.2f} cm3 = ${:0.2f}".format(volume, platinum)
        print "Silver -Polished: $35 + $20 * {:0.2f} cm3 = ${:0.2f}".format(volume, silver_polished)
        print "Silver -Raw: $30 + $20 * {:0.2f} cm3 = ${:0.2f}".format(volume, silver_raw)
        print "Bronze/Brass -Polished: $20 + $18 * {:0.2f} cm3 = ${:0.2f}".format(volume, bronze_or_brass_polished)
        print "Bronze/Brass -Raw $10 + $16 * {:0.2f} cm3 = ${:0.2f}".format(volume, bronze_or_brass_raw)
