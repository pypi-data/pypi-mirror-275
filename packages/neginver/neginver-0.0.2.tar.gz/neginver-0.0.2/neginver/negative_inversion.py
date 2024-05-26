#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   negative_reverse.py
@Time    :   2024/05/24 21:38:02
@Author  :   Flemyng 
@Version :   1.0
@Desc    :   Negative image inverse
'''
import os
from pathlib import Path
from typing import Union
from datetime import datetime

import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from scipy.optimize import minimize
from skimage.transform import resize
from tqdm import tqdm
import tifffile as tiff


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


def crop_image(
    image: np.ndarray,
    crop_percentage: float = 0.02,
) -> np.ndarray:
    '''
    Crop the image to remove the black sides.

    :param image: np.ndarray, The image to crop [band, height, width].
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The cropped image.
    '''
    # Get the size of the image
    height, width = image.shape[1:]

    # Calculate the number of pixels to crop
    crop_width = int(width * crop_percentage)

    return image[:, crop_width:-crop_width, crop_width:-crop_width]


def crop_channel(
    channel: np.ndarray,
    crop_percentage: float = 0.02,
) -> np.ndarray:
    '''
    Crop the image to remove the black sides.

    :param channe: np.ndarray, The channel to crop [height, width].
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The cropped image.
    '''
    # Get the size of the image
    height, width = channel.shape

    # Calculate the number of pixels to crop
    crop_width = int(width * crop_percentage)

    return channel[crop_width:-crop_width, crop_width:-crop_width]


def tone_curve(
    img: np.ndarray,
    control_points: list[tuple[float, float]],
    kind: str = 'linear',  # 'linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic'
) -> np.ndarray:
    '''
    Adjust the tone curve of an image.

    :param img: np.ndarray, The image to adjust the tone curve of.
    :param control_points: list[tuple[int, int]], The control points for the tone curve.
    :return: np.ndarray, The adjusted image.
    '''
    # Extract the input and output values
    x, y = zip(*control_points)

    # Use spline interpolation to construct the curve function
    curve_function = interp1d(x, y, kind=kind, fill_value="extrapolate")

    # Create a new array to store the adjusted pixel values
    img_adjusted = curve_function(img)
    img_adjusted = img_adjusted.astype(np.uint16)

    return img_adjusted


def adjust_channel_hist(
    channel: np.ndarray,
    point_left: tuple[float, float],
    point_right: tuple[float, float],
) -> np.ndarray:
    '''
    Cut the channel values to be within the range of the dtype.

    :param channel: np.ndarray, The channel to cut the values of.
    :param point_left: tuple(float, float), The point to cut the left side of the channel.
    :param point_right: tuple(float, float), The point to cut the right side of the channel.
    :return: np.ndarray, The channel with the values cut.
    '''
    # Get the min and max values of the dtype
    if np.issubdtype(channel.dtype, np.integer):
        dtype_min = np.iinfo(channel.dtype).min
        dtype_max = np.iinfo(channel.dtype).max
    else:
        dtype_min = np.finfo(channel.dtype).min
        dtype_max = np.finfo(channel.dtype).max

    points_list: list[tuple] = []

    # Check points x value
    # point_left's should be dtype_min
    # point_right's should be dtype_max
    if point_left[0] != dtype_min:
        points_list.append((dtype_min, point_left[1]))
    else:
        pass

    points_list.append(point_left)
    points_list.append(point_right)

    if point_right[0] != dtype_max:
        points_list.append((dtype_max, point_right[1]))
    else:
        pass

    # Adjust the tone curve
    channel_adjusted = tone_curve(channel, points_list)

    return channel_adjusted.astype(channel.dtype)


def convert_channel_hist(channel: np.ndarray) -> np.ndarray:
    '''
    Convert the channel histogram

    :param channel: np.ndarray, The channel to convert.
    :return: np.ndarray, The channel converted.
    '''
    # Get the min and max values of the dtype
    dtype_min = np.iinfo(channel.dtype).min
    dtype_max = np.iinfo(channel.dtype).max

    return adjust_channel_hist(
        channel,
        (dtype_min, dtype_max),
        (dtype_max, dtype_min)
    )


def convert_image_hist(image: np.ndarray) -> np.ndarray:
    '''
    Convert the image histogram

    :param image: np.ndarray, The image to convert.
    :return: np.ndarray, The image converted.
    '''
    # Convert the RGB channels
    r = convert_channel_hist(image[0])
    g = convert_channel_hist(image[1])
    b = convert_channel_hist(image[2])

    return np.array([r, g, b])


def auto_find_channel_control_points(
    channel: np.ndarray,
    percentile: float = 0.1,
    crop_percentage: float = 0.0,
) -> np.ndarray:
    '''
    Cut the channel values to be within the range of the dtype.

    :param channel: np.ndarray, The channel to cut the values of.
    :param percentile: float, The percentile of the histogram to cut.
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The channel with the values cut.
    '''
    # Crop the channel black side
    channel = crop_channel(channel, crop_percentage)

    # Get the min and max values of the dtype
    if np.issubdtype(channel.dtype, np.integer):
        dtype_min = np.iinfo(channel.dtype).min
        dtype_max = np.iinfo(channel.dtype).max
    else:
        dtype_min = np.finfo(channel.dtype).min
        dtype_max = np.finfo(channel.dtype).max

    # Delta
    delta = 0.02 * (dtype_max - dtype_min)

    channel_min = np.percentile(channel, percentile)
    channel_max = np.percentile(channel, 99.9)

    return [
        (channel_min, dtype_min + delta),
        (channel_max, dtype_max - delta)
    ]


def auto_image_hist(
    image: np.ndarray,
    percentile: float = 0.1,
    crop_percentage: float = 0.0,
) -> np.ndarray:
    '''
    Convert the image histogram

    :param image: np.ndarray, The image to to cut the values of.
    :param percentile: float, The percentile of the histogram to cut.
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The image with the values cut.
    '''
    # Get the dtype of the image
    dtype = image.dtype

    # Find the RGB channels control points
    r_cp = auto_find_channel_control_points(image[0], percentile, crop_percentage)
    g_cp = auto_find_channel_control_points(image[1], percentile, crop_percentage)
    b_cp = auto_find_channel_control_points(image[2], percentile*4, crop_percentage)

    # Adjust
    r = adjust_channel_hist(image[0], r_cp[0], r_cp[1])
    g = adjust_channel_hist(image[1], g_cp[0], g_cp[1])
    b = adjust_channel_hist(image[2], b_cp[0], b_cp[1])

    return np.array([r, g, b]).astype(dtype)


def one_control_point(
    img: np.ndarray,
    rates: tuple[float] = (1.0, 1.0),
) -> np.ndarray:
    '''
    Adjust the tone curve of an image.

    :param img: np.ndarray, The image to adjust the tone curve of.
    :param rates: tuple[float], The rate of the control points.
    :return: np.ndarray, The adjusted image.
    '''
    dtype = img.dtype

    # Get the min and max values of the dtype
    if np.issubdtype(dtype, np.integer):
        dtype_min = np.iinfo(dtype).min
        dtype_max = np.iinfo(dtype).max
    else:
        dtype_min = np.finfo(dtype).min
        dtype_max = np.finfo(dtype).max

    dtype_medium = (dtype_max - dtype_min) / 2

    rgb: list = [img[1]]
    channel: list = [0, 2]

    # Create a new array to store the adjusted pixel values
    for i, rate in enumerate(rates):
        # Initialize control points list
        control_points = [
            (dtype_min, dtype_min),
            (dtype_medium, dtype_medium * rate),
            (dtype_max, dtype_max)
        ]

        # Extract the input and output values
        x, y = zip(*control_points)

        # Use spline interpolation to construct the curve function
        curve_function = CubicSpline(x, y, bc_type='natural')

        rgb.append(curve_function(img[channel[i]]))

    # Move fisrt place to second place
    rgb.insert(1, rgb.pop(0))

    return np.array(rgb).astype(dtype)


def tone_curve_loss(rates, img, target_img):
    '''
    计算调整后图像与目标图像之间的损失函数
    
    :param rates: tuple[float], 要优化的控制点率
    :param img: np.ndarray, 要调整的原始图像
    :param target_img: np.ndarray, 目标图像
    :return: float, 损失函数值
    '''
    # 调整图像的色调曲线
    adjusted_img = one_control_point(img, rates=rates)

    # 计算调整后图像与目标图像之间的均方误差
    loss = np.mean((adjusted_img - target_img) ** 2)
    return loss


def downsample(
    img: np.ndarray,
    scale: float
) -> np.ndarray:
    '''
    缩小图像尺寸
    
    :param img: np.ndarray, 要缩小的图像
    :param scale: float, 缩小的比例
    :return: np.ndarray, 缩小后的图像
    '''
    dtype = img.dtype

    # Get the min and max values of the dtype
    if np.issubdtype(dtype, np.integer):
        dtype_min = np.iinfo(dtype).min
        dtype_max = np.iinfo(dtype).max
    else:
        dtype_min = np.finfo(dtype).min
        dtype_max = np.finfo(dtype).max

    # 缩小图像尺寸
    img_downsampled = resize(
        img,
        (
            img.shape[0],
            int(img.shape[1] * scale),
            int(img.shape[2] * scale)
        ),
        anti_aliasing=True
    ) * (dtype_max - dtype_min) + dtype_min

    return img_downsampled.astype(dtype)


def auto_find_rates(
    img: np.ndarray,
):
    '''
    使用梯度下降法自动找到最佳的rates参数
    
    :param img: np.ndarray, 要调整的原始图像
    :return: tuple[float], 最佳的rates参数
    '''
    # 初始猜测值
    initial_guess = (1.0, 1.0)

    # 缩小图像尺寸
    if img.shape[1] > 2400:
        scale = 2400 / img.shape[1]

    img = downsample(img, scale)

    # Set target
    target_img = np.array([img[1], img[1], img[1]])

    # 最小化损失函数，寻找最佳的rates参数
    result = minimize(
        tone_curve_loss,
        initial_guess,
        args=(img, target_img),
        method='Nelder-Mead'
    )

    best_rates = result.x

    rates_list: list[float] = [1]
    rates_list.extend(best_rates)

    return best_rates


def bw_inverse(
    img: np.ndarray,
    percentile: float = 0.1,
    crop_percentage: float = 0.02,
) -> np.ndarray:
    '''
    Convert the negative image to positive image

    :param img: np.ndarray, The negative image to convert.
    :param percentile: float, The percentile of the histogram to cut.
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The positive image.
    '''
    dtype = img.dtype

    # Combine the RGB channels
    img = np.mean(img, axis=0).astype(dtype)

    # Convert the image histogram
    img_conversion = convert_channel_hist(img)

    # Adjust the image histogram
    control_points = auto_find_channel_control_points(
        img_conversion,
        percentile=percentile,
        crop_percentage=crop_percentage
    )
    img_adjusted = adjust_channel_hist(img_conversion, *control_points)

    return img_adjusted.astype(dtype)


def color_inverse(
    img: np.ndarray,
    percentile: float = 0.1,
    crop_percentage: float = 0.02,
    auto_rates: bool = False,
    rates: tuple[float] = (1.0, 1.0),
) -> np.ndarray:
    '''
    Convert the negative image to positive image

    :param img: np.ndarray, The negative image to convert.
    :param percentile: float, The percentile of the histogram to cut.
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The positive image.
    '''
    dtype = img.dtype

    # Convert the image histogram
    img_conversion = convert_image_hist(img)

    # Adjust the image histogram
    img_adjusted = auto_image_hist(
        img_conversion,
        percentile=percentile,
        crop_percentage=crop_percentage
    )

    if auto_rates:
        # Find the best rates
        rates = auto_find_rates(img_adjusted)
        print(f'Red control point rate: {rates[0]:.3f}')
        print(f'Blue control point rate: {rates[1]:.3f}')
    else:
        pass

    # Adjust the tone curve
    img_adjusted = one_control_point(
        img_adjusted,
        rates=rates
    )

    return img_adjusted.astype(dtype)


def negative_inverse(
    img: np.ndarray,
    film_type: str = 'color', # 'color', 'bw'
    mode: str = 'default',
    rates: tuple[float] = (1.195, 1.155),
    percentile: float = 0.1,
    crop_percentage: float = 0.02,
) -> np.ndarray:
    '''
    Convert the negative image to positive image

    :param img: np.ndarray, The negative image to convert.
    :param film_type: str, The type of the film, 'color' or 'bw'.
    :param mode: str, The mode of the conversion, 'auto', 'default' or 'manual'.
    :param rates: tuple[float], The control points rate.
    :param percentile: float, The percentile of the histogram to cut.
    :param crop_percentage: float, The percentage of the black side to crop.
    :return: np.ndarray, The positive image.
    '''
    # Check the img shape
    if img.shape[0] == 3:
        pass
    else:
        raise ValueError('Invalid image shape, must be [3, height, width]!')

    # Check the film type
    if film_type == 'color':
        if mode == 'auto':
            return color_inverse(
                img,
                auto_rates=True,
                percentile=percentile,
                crop_percentage=crop_percentage
            )
        elif mode == 'default':
            return color_inverse(
                img,
                rates=(1.195, 1.155),
                percentile=percentile,
                crop_percentage=crop_percentage
            )
        elif mode == 'manual':
            if rates == (1.195, 1.155):
                print('The default rates are (1.195, 1.155), you can change it by setting the rates parameter.')
                return color_inverse(
                    img,
                    rates=rates,
                    percentile=percentile,
                    crop_percentage=crop_percentage
                )
            else:
                return color_inverse(
                    img,
                    rates=rates,
                    percentile=percentile,
                    crop_percentage=crop_percentage
                )
        else:
            raise ValueError('Invalid mode, must be "auto", "default" or "manual"!')
    elif film_type == 'bw':
        return bw_inverse(
            img,
            percentile=percentile,
            crop_percentage=crop_percentage
        )
    else:
        raise ValueError('Invalid film type, must be "color" or "bw"!')


if __name__ == "__main__":
    # Directory path
    data_dir = Path('/Users/flemyng/Desktop/Phocus/2024_05_24')
    save_dir = Path('/Users/flemyng/Desktop/Film')

    # Get all *.tif files in the directory
    tif_files = list(data_dir.glob('*.tif'))

    # Resort the list of files
    tif_files = sorted(tif_files)

    # 获取当前日期
    current_date = datetime.now()

    # 格式化日期为 YYYY_MM_DD
    folder_name = current_date.strftime('%Y_%m_%d')

    # 创建文件夹
    os.makedirs(save_dir / folder_name, exist_ok=True)

    for tif_path in tqdm(tif_files):
        img_raw = np.moveaxis(tiff.imread(tif_path), -1, 0)
        img_inversed = negative_inverse(img_raw, film_type='color', mode='default')

        img = np.moveaxis(img_inversed, 0, -1)

        tiff.imwrite(
            save_dir / folder_name / f'{tif_path.stem}.tif',
            img
        )
