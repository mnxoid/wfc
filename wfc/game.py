import pygame as _pygame
from .helpers import mean_surface, load_image

def SchrodingerSpriteGen(tiles, hashes, error_sprite):
    class SchrodingerSprite(_pygame.sprite.Sprite):
      """ The class is the simple sprite. """

      def __init__(self, x, y, codes):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
     
        # Set height, width
        #self.image = _pygame.Surface([15, 15])
        if len(codes)>0:
          self.image = meanSurface([_pygame.pixelcopy.make_surface(tiles[hashes[code]]) for code in codes])
        else:
          self.image = load_image(error_sprite, mode="pygame")
        #self.image.fill(BLACK)
     
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.codes = codes
      
      def setCode(self, codes):
        self.codes = codes
        if len(codes)>0:
          self.image = meanSurface([_pygame.pixelcopy.make_surface(tiles[hashes[code]]) for code in codes])
        else:
          self.image = load_image(error_sprite, mode="pygame")

    return SchrodingerSprite

__all__ = ["SchrodingerSpriteGen"]