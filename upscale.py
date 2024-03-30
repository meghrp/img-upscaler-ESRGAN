"""
This file includes code from the ESRGAN project (https://github.com/xinntao/ESRGAN).
Original authors: Xintao Wang, Ke Yu, Shixiang Wu, Jinjin Gu, Yihao Liu, Chao Dong, Chen Change Loy, Yu Qiao, and Xiaoou Tang
License: Apache License 2.0
"""

from ESRGAN import RRDBNet_arch as arch
import os.path as osp
import torch
import numpy as np
import cv2
from PIL import Image

model_path = 'ESRGAN/models/RRDB_ESRGAN_x4.pth' # replace with your model path
device = torch.device('cpu') # if you want to run on CPU, change 'cuda' -> 'cpu'

model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
model = model.to(device)

def upscale(file):
    filestr = file.read()
    npimg = np.fromstring(filestr, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 255).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    return output