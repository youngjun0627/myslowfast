# -*- coding: utf-8 -*-
"""opts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dc1hM4VbgZkncEoNlnMsQMRMgIarvSoO
"""
class opts():
  def __init__(self):
    self.root_path = '/content'
    self.train_video_path = self.root_path + '/' + 'data' + '/' + 'train'
    self.valid_video_path = self.root_path + '/' + 'data' + '/' + 'valid'
    self.name_path = None
    self.train_list = None
    self.file_path = None
    self.val_list=None
    self.result_path='result'
    self.data_name='violence'
    self.gpus=1
    self.log_dir='log'
    self.num_classes =2
    self.crop_size=224
    self.n_samples_for_each_video=1
    self.lr=0.1 #원래 1.6
    self.momentum=0.9
    self.lr_decay=0.5 #원래 0.8
    self.weight_decay=0.001
    self.cycle_length=10
    self.multi_factor=1.5
    self.warm_up_epoch=5
    self.optimizer="SGD"
    self.batch_size=4
    self.epochs=30
    self.worker=4
    self.pretrained_weights =None
    self.alpah = 8
    self.beta=1/8
    self.tau=16

  def get_opts():
    return self

def get_opt():
  return opts().get_opts()