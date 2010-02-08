import gtk
from lib.graphics.rgbacolor import RGBAColor

# Class
# ==============================================================================
class Tool:
   CURSOR = gtk.gdk.Cursor(gtk.gdk.ARROW)

   def __init__(self, canvas):
      self.canvas = canvas
      self.primary = RGBAColor(0, 0, 0)
      self.secondary = RGBAColor(1, 1, 1)

   def drag(self, x, y): pass

   def select(self):
      self.canvas.window.set_cursor(self.CURSOR)

   def begin(self, x, y): pass

   def end(self, x, y): pass

   def draw(self, context): pass

   def __use_color(self, context, color):
      context.set_source_rgba(color.get_red(), color.get_green(),
         color.get_blue(), color.get_alpha())

   def use_primary_color(self, context):
      self.__use_color(context, self.primary)

   def use_secondary_color(self, context):
      self.__use_color(context, self.secondary)

   def set_primary_color(self, color):
      self.primary = color

   def set_secondary_color(self, color):
      self.secondary = color


# Class 
# ==============================================================================
class DragAndDropTool(Tool):
   CURSOR = gtk.gdk.Cursor(gtk.gdk.CROSSHAIR)

   initial_x = 0
   initial_y = 0
   final_x = 0
   final_y = 0


   def begin(self, x, y):
      self.initial_x = x
      self.initial_y = y
      self.final_x = x
      self.final_y = y


   def end(self, x, y):
      self.final_x = x
      self.final_y = y


   def drag(self, x, y):
      self.end(x, y)


# Class 
# ==============================================================================
class BothScalingTool(Tool):
   CURSOR = gtk.gdk.Cursor(gtk.gdk.BOTTOM_RIGHT_CORNER)

   def drag(self, x, y):
      self.canvas.set_size(int(x), int(y))


# Class
# ==============================================================================
class HorizontalScalingTool(Tool):
   CURSOR = gtk.gdk.Cursor(gtk.gdk.RIGHT_SIDE)

   def drag(self, x, y):
      self.canvas.set_size(int(x), self.canvas.get_height())


# Class
# ==============================================================================
class VerticalScalingTool(Tool):
   CURSOR = gtk.gdk.Cursor(gtk.gdk.BOTTOM_SIDE)

   def drag(self, x, y):
      self.canvas.set_size(self.canvas.get_width(), int(y))

