from enum import Enum

class DeviceEnum(str, Enum):
    cpu = 'cpu'
    cuda = 'cuda'
    mps = 'mps'
    ipu = 'ipu'
    xpu = 'xpu'
    mkldnn = 'mkldnn'
    opengl = 'opengl'
    opencl = 'opencl'
    ideep = 'ideep'
    hip = 'hip'
    ve = 've'
    fpga = 'fpga'
    maia = 'maia'
    xla = 'xla'
    lazy = 'lazy'
    vulkan = 'vulkan'
    meta = 'meta'
    hpu = 'hpu'
    mtia = 'mtia'
    