import numpy as _np
import pygame as _pygame
from matplotlib import pyplot as _plt

def load_image(path, mode="numpy"):
  img = _pygame.image.load(path)
  if mode=="numpy":
    img_data = _np.array(_pygame.surfarray.array3d(img), _np.uint8).transpose(1,0,2)
    return img_data
  elif mode=="pygame":
    return img

def show_image(img_data, tile_size=16, manual=False):
  if not manual:
    _plt.figure()
  _plt.imshow(img_data)

  ax = _plt.gca()
  ax.set_xticks(_np.arange(-0.5, img_data.shape[1], tile_size), minor=True)
  ax.set_yticks(_np.arange(-0.5, img_data.shape[0], tile_size), minor=True)
  ax.grid(which='minor', color='gray', linestyle='--', linewidth=2)

def tileset(img, tile_size=16):
  return (lambda x,y: img[y*tile_size:(y+1)*tile_size,x*tile_size:(x+1)*tile_size,:])

def all_rots(img):
  return [
    img,
    _np.rot90(img,1),
    _np.rot90(img,2),
    _np.rot90(img,3)
  ]

def all_hashes(img):
  return [ hash(str(x)) for x in all_rots(img) ]

def visualizer(tiles, hashes):
  def visualize(arr, manual=False):
    x_sz = arr.shape[1]
    y_sz = arr.shape[0]
    show_image(_np.hstack([_np.vstack([tiles[hashes[int(arr[y,x])]] for y in range(y_sz)]) for x in range(x_sz)]),manual=manual)
  
  return visualize

def show_tiles(hashes, tiles):
    s = int(_np.ceil(_np.sqrt(len(hashes))))
    w = min(s*2,18)
    _plt.figure(figsize=(w,w))
    for i in range(len(hashes)):
        _plt.subplot(s,s,i+1)
        _plt.tick_params(labelleft=False, labeltop=False, labelright=False, labelbottom=False)
        _plt.gca().set_title("Tile %d" % i)
        show_image(tiles[hashes[i]], manual=True)

def mean_surface(sfcs):
  arrs = [np.array(pygame.surfarray.array3d(s), np.float) for s in sfcs]
  avg_s = np.array(np.mean( np.array(arrs), axis=0 ), np.uint8)
  return pygame.surfarray.make_surface(avg_s)

__all__ = [
  "load_image",
  "show_image",
  "tileset",
  "all_rots",
  "all_hashes",
  "visualizer",
  "show_tiles",
  "mean_surface"
]