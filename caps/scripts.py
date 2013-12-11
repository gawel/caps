import os
import cv2
import time
import tempfile
import uuid
import numpy as np


class Caps(object):

    camera_port = 0
    ramp_frames = 30
    tempdir = tempfile.mkdtemp()

    def __init__(self):
        self.images = []

    def preprocess_image(self, X):
        X = X.astype(float)
        X = X.sum(axis=2)
        return X

    def get_current_image(self):
        camera = cv2.VideoCapture(self.camera_port)

        def get_image(camera):
            retval, im = camera.read()
            return im

        for i in xrange(self.ramp_frames):
            get_image(camera)

        camera_capture = get_image(camera)

        del(camera)

        camera_capture = self.preprocess_image(camera_capture)
        return camera_capture

    def get_samples(self):
        for i in range(100):
            uid = str(uuid.uuid4())
            X = self.get_current_image()
            self.images.append(X)
            filename = os.path.join(self.tempdir, "caps_%s.npy" % uid)
            np.save(filename, X)
            print('Image', i)

    def get_sample(self):
        uid = str(uuid.uuid4())
        self.images = []
        print('First sample')
        time.sleep(1)
        X = self.get_current_image()
        self.images.append(X)
        filename = os.path.join(self.tempdir, "caps_%s_0.npy" % uid)
        np.save(filename, X)
        print('Second sample')
        time.sleep(3)
        X = self.get_current_image()
        self.images.append(X)
        filename = os.path.join(self.tempdir, "caps_%s_1.npy" % uid)
        np.save(filename, X)
        return self.images

    def get_caps_area(self, X1, X2):
        diff = np.abs(X1 - X2)
        return diff


def main():
    c = Caps()
    c.get_sample()
    return c
