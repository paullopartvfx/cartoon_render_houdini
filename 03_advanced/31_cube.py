# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""
class Object:
   def __init__(self, name):
      self.name = name

   def translate(self, t_x, t_y , t_z):
      self.t_x = t_x
      self.t_y = t_y
      self.t_z = t_z

      print("Translate set to: [{}, {}, {}]".format(t_x, t_y, t_z))

   def rotate(self, r_x, r_y , r_z):
      self.r_x = r_x
      self.r_y = r_y
      self.r_z = r_z

      print("Rotation set to:  [{}, {}, {}]".format(r_x, r_y, r_z))

   def scale(self, s_x, s_y , s_z):
      self.s_x = s_x
      self.s_y = s_y
      self.s_z = s_z

      print("Scale set to:    [{}, {}, {}]".format(s_x, s_y, s_z))


class Cube(Object):
   def color(self, clr_r, clr_g , clr_b):
      self.clr_r = clr_r
      self.clr_g = clr_g
      self.clr_b = clr_b

      print("Color set to:    [{}, {}, {}]".format(clr_r, clr_g, clr_b))

   def print_status(self):
      print("Current {} status: ".format(self.name))
      
      try:
         print("Translate set to: [{}, {}, {}]".format(self.t_x, self.t_y, self.t_z))
      except:
         print("Translate set to: [{}, {}, {}]".format(0, 0, 0))
      try:
         print("Rotation set to:  [{}, {}, {}]".format(self.r_x, self.r_y, self.r_z))
      except:
         print("Rotation set to:  [{}, {}, {}]".format(0, 0, 0))
      try:
         print("Scale set to:     [{}, {}, {}]".format(self.s_x, self.s_y, self.s_z))
      except:
         print("Scale set to:     [{}, {}, {}]".format(0, 0, 0))
      try:
         print("Color set to:     [{}, {}, {}]".format(self.clr_r, self.clr_g, self.clr_b))
      except:
         print("Color set to:     [{}, {}, {}]".format(0, 0, 0))
   
   def update_transforms(self, ttype, x, y, z):
      if ttype == "translate":
         self.translate(x, y, z)

      if ttype == "rotate":
         self.rotate(x, y, z)

      if ttype == "scale":
         self.scale(x, y, z)

#CALLING TO TEST-----------------------------------------------------------------------------------

box = Cube("cube 2")
#box.translate(1, 2, 5)
box.rotate(210, -25, 12)

box.print_status()

#box.update_transforms("rotate", 15, -25, 8)

