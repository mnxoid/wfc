import numpy as np
from .helpers import load_image, tileset, all_hashes, all_rots

def rules_from_image(path_to_img, tile_size):
    source = load_image(path_to_img)
    tls = tileset(source, tile_size=tile_size)
    
    tiles = {}
    hashes = []

    src_arr = np.zeros((int(source.shape[0]/tile_size),int(source.shape[1]/tile_size)),dtype=np.int32)

    for y in range(int(source.shape[0]/tile_size)):
        for x in range(int(source.shape[1]/tile_size)):
            hs = all_hashes(tls(x,y))

            if len(set.intersection(set(hs),set(tiles.keys())))==0:
                for img in all_rots(tls(x,y)):
                    h = hash(str(img))
                    tiles[h] = img
                    hashes.append(h)

            src_arr[y,x] = hashes.index(hash(str(tls(x,y))))
    
    neighbors = []
    
    for y in range(src_arr.shape[0]):
        for x in range(src_arr.shape[1]):
            arr = np.array([
              [0,                                src_arr[(y-1)%src_arr.shape[0],x],0],
              [src_arr[y,(x-1)%src_arr.shape[1]],src_arr[y,x],                     src_arr[y,(x+1)%src_arr.shape[1]]],
              [0,                                src_arr[(y+1)%src_arr.shape[0],x],0]
            ])

            fullp = (arr // 4)*4
            neighbors.append(arr)
            neighbors.append(np.rot90((arr-fullp+1)%4+fullp))
            neighbors.append(np.rot90((arr-fullp+2)%4+fullp,2))
            neighbors.append(np.rot90((arr-fullp+3)%4+fullp,3))
    
    tileind = lambda h: list(tiles.keys()).index(h)
    
    rules = np.zeros((len(tiles.keys()), len(tiles.keys()), 4), dtype=np.uint8)

    for rule in neighbors:
        ind = tileind(hashes[rule[1,1]])
        indT = tileind(hashes[rule[0,1]])
        indR = tileind(hashes[rule[1,2]])
        indB = tileind(hashes[rule[2,1]])
        indL = tileind(hashes[rule[0,1]])

        rules[ind,indT,0] = 1
        rules[ind,indR,1] = 1
        rules[ind,indB,2] = 1
        rules[ind,indL,3] = 1
    
    return (tiles, list(tiles.keys()), rules)