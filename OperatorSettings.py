from visit import *

from OperatorClip import OperatorClip
from OperatorSlice import OperatorSlice
from OperatorThreshold import OperatorThreshold
from OperatorTransform import OperatorTransform


class OperatorSettings(object):
    """Add operator and its settings."""

    def __init__(self, File, OperSet, myList, Centroids, tags, SliceProject=1):
        self.File = File
        self.tags = tags
        self.myList = myList
        self.OperSet = OperSet
        self.Centroids = Centroids
        self.SliceProject = SliceProject

    def Slice(self):
        OperatorSlice(
                      self.File,
                      self.OperSet,
                      self.myList,
                      self.Centroids,
                      self.SliceProject,
                      )

    def Clip(self):
        OperatorClip(
                     self.File,
                     self.OperSet,
                     self.myList,
                     self.Centroids,
                     )

    def Threshold(self):
        OperatorThreshold(
                          self.OperSet,
                          self.myList,
                          self.tags,
                          )

    def Transform(self):
        OperatorTransform(
                          self.File,
                          self.OperSet,
                          self.myList,
                          self.Centroids,
                          )
