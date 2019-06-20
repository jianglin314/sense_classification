from easydict import EasyDict as edict
import numpy as np
import tensorflow as tf
import os

cfg = edict()

cfg.classes = 45
cfg.batch_size = 128
# cfg.batch_size = 256

cfg.data_path = '../data/tf_records/train.records'
cfg.ckpt_path = '../ckpt/'

# training options
cfg.train = edict()

cfg.train.ignore_thresh = .5
cfg.train.ohem_ratio = 0.8
cfg.train.momentum = 0.9
cfg.train.bn_training = True
cfg.train.weight_decay = 0.0001
cfg.train.learning_rate = [1e-3, 1e-4, 1e-5]
cfg.train.max_batches = 30000
cfg.train.lr_steps = [10000., 20000.]
cfg.train.lr_scales = [.1, .1]
cfg.train.num_gpus = 1
cfg.train.tower = 'tower'

cfg.train.learn_rate = 0.001
cfg.train.learn_rate_decay = 0.8
cfg.train.learn_rate_decay_epoch = 2
cfg.train.num_samples = 177408
cfg.epochs = 100
cfg.PRINT_LAYER_LOG = True
