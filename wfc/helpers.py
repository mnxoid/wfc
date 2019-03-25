import numpy as np
import pygame
from matplotlib import pyplot as plt

def load_image(path, mode="numpy"):
  img = pygame.image.load(path)
  if mode=="numpy":
    img_data = np.array(pygame.surfarray.array3d(img), np.uint8).transpose(1,0,2)
    return img_data
  elif mode=="pygame":
    return img

def show_image(img_data, tile_size=16, manual=False):
  if not manual:
    plt.figure()
  plt.imshow(img_data)

  ax = plt.gca()
  ax.set_xticks(np.arange(-0.5, img_data.shape[1], tile_size), minor=True)
  ax.set_yticks(np.arange(-0.5, img_data.shape[0], tile_size), minor=True)
  ax.grid(which='minor', color='gray', linestyle='--', linewidth=2)

def tileset(img, tile_size=16):
  return (lambda x,y: img[y*tile_size:(y+1)*tile_size,x*tile_size:(x+1)*tile_size,:])

def all_rots(img):
  return [
    img,
    np.rot90(img,1),
    np.rot90(img,2),
    np.rot90(img,3)
  ]

def all_hashes(img):
  return [ hash(str(x)) for x in allRots(img) ]

def visualizer(tiles, hashes):
  def visualize(arr, manual=False):
    x_sz = arr.shape[1]
    y_sz = arr.shape[0]
    show_image(np.hstack([np.vstack([tiles[hashes[int(arr[y,x])]] for y in range(y_sz)]) for x in range(x_sz)]),manual=manual)
  
  return visualize