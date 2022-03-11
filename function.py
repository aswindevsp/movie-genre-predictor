from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    self.init_components(**properties)

  def text_box_1_pressed_enter(self, **event_args):
    
    pass

  def button_1_click(self, **event_args):
    name=self.name_textbox
    
    genre=anvil.server.call('predictgenre',
                            name)
    if genre:
      self.genre_label.visible=True
      self.genre_label.text='The genre is '+genre.capitalize()
