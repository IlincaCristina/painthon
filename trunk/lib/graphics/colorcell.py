import gtk
import cairo
import math
from rgbacolor import RGBAColor

class ColorCell(gtk.DrawingArea):
   WIDTH = 25
   HEIGHT = 20
   ASS = 7

   def __init__(self, red=0, green=0, blue=0, alpha=1):
      super(ColorCell, self).__init__()
      self.set_size_request(self.WIDTH, self.HEIGHT)

      self.gloss = cairo.ImageSurface.create_from_png("pixmaps/glossy-color.png")
      self.color = RGBAColor(red, green, blue, alpha)

      self.add_events(gtk.gdk.BUTTON_PRESS_MASK)
      self.connect("button-press-event", self.clicked)
      self.connect("expose-event", self.expose)


   def expose(self, widget, event):
      context = widget.window.cairo_create()

      context.rectangle(0, 0, self.WIDTH, self.HEIGHT)
      context.clip()

      context.rectangle(0, 0, self.WIDTH, self.HEIGHT)
      context.set_source_rgb(0.4, 0.4, 0.4)
      context.fill()

      context.set_source_rgb(0.6, 0.6, 0.6)
      for i in range(int(self.WIDTH/self.ASS)+1):
         for j in range(int(self.HEIGHT/self.ASS)+1):
            if i%2 == 0 and j%2 == 0:
               context.rectangle(i*self.ASS, j*self.ASS, self.ASS, self.ASS)
               context.fill()
            elif i%2 != 0 and j%2 != 0:
               context.rectangle(i*self.ASS, j*self.ASS, self.ASS, self.ASS)
               context.fill()

      context.rectangle(0, 0, self.WIDTH, self.HEIGHT)
      context.set_source_rgba(self.color.get_red(), self.color.get_green(),
         self.color.get_blue(), self.color.get_alpha())
      context.fill()

      context.set_source_surface(self.gloss)
      context.paint()


   def swap_buffers(self):
      rect = gtk.gdk.Rectangle(0, 0, self.WIDTH, self.HEIGHT)
      self.window.invalidate_rect(rect, True)

      
   def set_color(self, color):
      self.color = color

      try:
         rect = gtk.gdk.Rectangle(0, 0, self.WIDTH, self.HEIGHT)
         self.window.invalidate_rect(rect, True)
      except:
         pass


   def get_color(self):
      return self.color.copy()


   def modify_color(self, color):
      csd = gtk.ColorSelectionDialog("Choose a color")
      csd.set_modal(True)
      cs = csd.get_color_selection()
      cs.set_property("current-color", self.color.to_gtk_color())
      ok = csd.run()
      if ok == gtk.RESPONSE_OK:
         self.set_color(RGBAColor.create_from_gtk_color(cs.get_current_color()))
      csd.destroy()


   def clicked(self, widget, event):
     if event.type == gtk.gdk._2BUTTON_PRESS:
        self.modify_color(widget)

     self.emit("button-release-event", event)


   def to_string(self):
      return "ColorCell: " + self.color.to_string()


