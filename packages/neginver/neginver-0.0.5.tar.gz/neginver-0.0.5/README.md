# neginver

**Read this in other languages: [中文](README.md), [English](README_EN.md), [日本語](README_JP.md).**

国内胶片之风盛行多日。由于不满时下大多店铺扫描与去色罩质量，已经有部分人开始自己尝试胶片翻拍，但是去色罩对于大多数艺术家们来讲就成了一个“难题”或者说是“麻烦事”。尽管[Negative Lab Pro](https://www.negativelabpro.com)确实方便，但是$99.00的价格让我这种穷人望而却步，并且个人不是太欣赏它那过于讨喜的校色思路，于是乎开发了这个简单的负片去色罩小程序，希望也可以帮助到大家！

原图 ⬇️
![raw color negative film](pic/image_info_raw.png "Raw color negative film")
![raw bw negative film](pic/bw_info_raw.png "Raw bw negative film")
去色罩后 ⬇️
![inversed color negative film](pic/image_info_inver.png "Inversed color negative film")
![inversed color negative film](pic/bw_info_inver.png "Inversed bw negative film")

本项目完全基于Python对图片的原始直方图的统计信息去色罩，不带有人为的控制，力求展示底片本应有的**最自然的颜色**！以下是与nlp对比的样片：

Negative Lab Pro⬇️
![Negative Lab Pro samples](pic/nlp.jpg "Negative Lab Pro samples")
Neginver⬇️
![Neginver samples](pic/neginver.jpg "Neginver samples")

这里是样片的 **[原图](pic/raw_sample)**，欢迎大家自行尝试👏

E-mail: <flemyng1999@outlook.com>

## 安装

使用pip安装即可：

```sh
pip install neginver
```

比较懒，目前没有conda。

## 使用

这个项目目前没有开发GUI，所以仍然要求使用者有一定的python基础。

读取Tif文件。这一步基于[tifffile](https://pypi.org/project/tifffile/)读取tif文件为numpy数组：

```python
import tifffile as tiff

img = tiff.imread(tif_path)
```

由于本人习惯于[band, height, wight]的格式，而tiff.imread()读取的是[height, wight, band]的格式，所以需要用numpy简单处理一下：

```python
import numpy as np

img = np.moveaxis(img, 0, -1)
```

然后将本模块引入：

```python
import neginver as ni

img_inversed = ni.negative_inverse(img_raw, film_type='color', mode='default')
```

最后将img_inversed数组保存为无损的tif文件：

```python
img_final = np.moveaxis(img_inversed, 0, -1)
tiff.imwrite('img.tif', img_final)
```

以上是一张图的流程，本人基于M2 Pro的MacBook Pro测试，一张1200w的图片只需要2.5秒。
使用循环可以批处理：

```python
import os
from pathlib import Path
from datetime import datetime

import tifffile as tiff
import numpy as np
import neginver as ni


# Directory path
data_dir = Path('/Users/flemyng/Desktop/Phocus/2024_05_24')
save_dir = Path('/Users/flemyng/Desktop/Film')

# Get all *.tif files in the directory
tif_files = list(data_dir.glob('*.tif'))

# Resort the list of files
tif_files = sorted(tif_files)

# Get now time
current_date = datetime.now()

# Change date to YYYY_MM_DD
folder_name = current_date.strftime('%Y_%m_%d')

# Initialize a new folder
os.makedirs(save_dir / folder_name, exist_ok=True)

for tif_path in tqdm(tif_files):
    img_raw = np.moveaxis(tiff.imread(tif_path), -1, 0)
    img_inversed = ni.negative_inverse(img_raw, film_type='color', mode='default')

    img = np.moveaxis(img_inversed, 0, -1)

    tiff.imwrite(
        save_dir / folder_name / f'{tif_path.stem}.tif',
        img
    )
```

最后，我建议可以在Lightroom里面再调整一下色调曲线，加入自己的艺术偏好。

## negative_inverse()

negative_inverse()函数是本模块的核心函数。关于negative_inverse()函数的参数，以及如何使用如下：

### 输入参数

```python
img: np.ndarray,
film_type: str = 'color', # 'color', 'bw'
mode: str = 'default',
rates: tuple[float] = (1.195, 1.155),
percentile: float = 0.1,
crop_percentage: float = 0.02,
```

### 参数介绍

**img**：是一个形状为 **[3, height, width]** 的numpy数组，包含图片的原始信息。数组的dtype只支持 **uint8** 和 **uint16** ，uint16完全够用了。不支持float，因为负数比较麻烦；

**film_type**：是底片的类型。如果是彩色胶片选'color'；黑白胶片选'bw'，黑白用'color'也可以；

**mode**：是校色的模式。有'auto', 'default', 'manual'三种选择：默认就是'default'；'auto'一般会偏绿偏蓝，你需要自己再调一下曲线（简单把中心往下调一点就可以）；'manual'不推荐，这是我自己用的。

**crop_percentage**：是胶片外一圈黑边所占的比例（从0～1）。比如，0.05就是补考虑图片外围5%的范围的信息。
