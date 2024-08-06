# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    colors = {  "1"  : 4,
                "2"  : 13,
                "3"  : 25,
                "4"  : 17,
                "5"  : 17,
                "6"  : 15,
                "7"  : 6,
                "8"  : 16}
    
    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass

        mc.setAttr(ctrlName + 'Shape.overrideColor', colors[color])



# EXAMPLE
# set_color(['circle','circle1'], 8)
