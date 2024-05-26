#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   image_info.py
@Time    :   2024/05/25 15:46:24
@Author  :   Flemyng 
@Version :   1.0
@Desc    :   None
'''

from typing import Union

import numpy as np
import matplotlib.pyplot as plt


def print_array_info(
    img_array: np.ndarray,
) -> None:
    '''
    Print the image information.

    :param img_array: np.ndarray, The image to print the information of.
    '''
    print(
        f'Image shape: {img_array.shape};\nImage data type: {img_array.dtype} '+
        f'({img_array.dtype} type range: {np.iinfo(img_array.dtype).min} to {np.iinfo(img_array.dtype).max});\n'+
        f'Red channel range: {img_array[0].min()} to {img_array[0].max()};\n'+
        f'Green channel range: {img_array[1].min()} to {img_array[1].max()};\n'+
        f'Blue channel range: {img_array[2].min()} to {img_array[2].max()}'
    )


def normalize(
    data: np.ndarray
) -> np.ndarray:
    '''
    Normalizes the data to be between 0 and 1

    :param data: The data to normalize
    :return: The normalized data
    '''
    data = data.astype(np.float32)
    return (data - data.min()) / (data.max() - data.min())


def plot_one_channel_hist(
    channel: np.ndarray,
    color: str,
    axis: plt.Axes,
) -> None:
    '''
    Plot the histogram of a single channel of an image.

    :param channel: np.ndarray, The channel to plot the histogram of.
    :param color: str, The color to plot the histogram in.
    :param axis: plt.Axes, The axis to plot the histogram on.
    '''
    # Get the histogram of the channel
    hist, bins = np.histogram(channel, bins=1000)

    # Smooth the histogram
    hist = np.convolve(hist, np.ones(5)/5, mode='same')

    # Plot the histogram
    axis.plot(bins[:-1], hist, color=color, alpha=0.8, linewidth=0.5)
    axis.fill_between(bins[:-1], hist, color=color, alpha=0.3333)


def plot_rgb_hist(
    data: np.ndarray,
    axis: plt.Axes,
) -> None:
    '''
    Plot the histogram of the RGB channels of an image.

    :param data: np.ndarray, The image which shape is [3, height, width] to plot the histogram of.
    :param axis: plt.Axes, The axis to plot the histogram on.
    '''
    r = data[0]
    g = data[1]
    b = data[2]

    plot_one_channel_hist(r, 'tab:red', axis)
    plot_one_channel_hist(g, 'tab:green', axis)
    plot_one_channel_hist(b, 'tab:blue', axis)

    axis.set_xlabel('Pixel value')
    axis.set_ylabel('Count')


def plot_image_info(
    image: np.ndarray,
) -> None:
    '''
    Plot the image and its histogram.

    :param image: np.ndarray, The image to plot, shape is [3, height, width].
    '''
    # Plot the image
    fig, axes = plt.subplots(1, 2, figsize=(22, 7))
    axes[0].imshow(np.moveaxis(normalize(image), 0, -1))
    axes[0].axis('off')

    # Plot the histogram
    plot_rgb_hist(image, axes[1])

    if image.dtype == np.uint16:
        axes[1].set_xlim([0, 65535])
    elif image.dtype == np.uint8:
        axes[1].set_xlim([0, 255])
