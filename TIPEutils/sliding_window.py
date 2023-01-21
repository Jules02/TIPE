#!/usr/bin/env python
# coding: utf-8



import cv2
import imutils

import numpy as np
from skimage import color, transform

def sliding_window(img, patch_size,
                   istep=4, jstep=4, scale=1.0):
    Ni, Nj = (int(scale * s) for s in patch_size)
    print(Ni, Nj)
    for i in range(0, img.shape[0] - Ni, istep):
        for j in range(0, img.shape[1] - Ni, jstep):
            patch = img[i:i + Ni, j:j + Nj]
            if scale != 1:
                patch = transform.resize(patch, patch_size)
            yield (i, j), patch
            


def main(img, patch_size):
    indices1, patches1 = zip(*sliding_window(img, patch_size, scale=1.0))
    indices2, patches2 = zip(*sliding_window(img, patch_size, scale=2.0))
    indices = np.array(indices1 + indices2)

    return indices, (patches1 + patches2)



