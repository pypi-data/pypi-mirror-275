import math

import numpy
from PIL import Image, ImageFilter
from scipy.fftpack import dct

from hashinator import utils

__all__ = [
    'ahash',
    'mhash',
    'phash',
    'dhash',
    'whash',
    'colorhash',
    'crop_resistant_hash',
    'blockhash',
    'blockhash_even'
]


def ahash(img: Image.Image) -> str:
    img = img.resize((8, 8)).convert('L')
    pixels = numpy.array(img)
    mean_color = numpy.mean(pixels)
    return "".join(str(int(px >= mean_color)) for px in pixels.ravel())


def mhash(img: Image.Image) -> str:
    img = img.resize((8, 8)).convert('L')
    pixels = numpy.array(img)
    median_color = numpy.median(pixels)
    return "".join(str(int(px >= median_color)) for px in pixels.ravel())


def phash(img: Image.Image) -> str:
    img = img.resize((32, 32)).convert('L')
    pixels = numpy.array(img)
    img_dct = dct(dct(pixels.T).T).ravel()
    mean_color = numpy.mean(img_dct)
    return "".join(str(int(px >= mean_color)) for px in img_dct)


def dhash(img: Image.Image) -> str:
    img = img.resize((8, 9)).convert('L')
    pixels = numpy.array(img)
    res = "".join(str(int(e >= row[i + 1])) for row in pixels for i, e in enumerate(row[:-1]))
    return res


def whash(img: Image.Image) -> str:
    import pywt
    hash_len = 8

    image_natural_scale = 2 ** int(numpy.log2(min(img.size)))
    image_scale = max(image_natural_scale, hash_len)

    ll_max_level = int(numpy.log2(image_scale))

    level = int(numpy.log2(hash_len))

    dwt_level = ll_max_level - level

    image = img.convert('L').resize((image_scale, image_scale))
    pixels = numpy.asarray(image) / 255.

    # Remove low level frequency LL(max_ll) if @remove_max_haar_ll using haar filter
    if True:
        coeffs = pywt.wavedec2(pixels, 'haar', level=ll_max_level)
        coeffs = list(coeffs)
        coeffs[0] *= 0
        pixels = pywt.waverec2(coeffs, 'haar')

    # Use LL(K) as freq, where K is log2(@hash_size)
    coeffs = pywt.wavedec2(pixels, 'haar', level=dwt_level)
    dwt_low = coeffs[0]

    # Subtract median and compute hash
    med = numpy.median(dwt_low)
    diff = dwt_low > med
    return "".join(str(int(x)) for x in diff.ravel())


def colorhash(image, binbits=3):
    """
    Color Hash computation.

    Computes fractions of image in intensity, hue and saturation bins:

    * the first binbits encode the black fraction of the image
    * the next binbits encode the gray fraction of the remaining image (low saturation)
    * the next 6*binbits encode the fraction in 6 bins of saturation, for highly saturated parts of the remaining image
    * the next 6*binbits encode the fraction in 6 bins of saturation, for mildly saturated parts of the remaining image

    @binbits number of bits to use to encode each pixel fractions
    """

    # bin in hsv space:
    intensity = numpy.asarray(image.convert('L')).flatten()
    h, s, v = [numpy.asarray(v).flatten() for v in image.convert('HSV').split()]
    # black bin
    mask_black = intensity < 256 // 8
    frac_black = mask_black.mean()
    # gray bin (low saturation, but not black)
    mask_gray = s < 256 // 3
    frac_gray = numpy.logical_and(~mask_black, mask_gray).mean()
    # two color bins (medium and high saturation, not in the two above)
    mask_colors = numpy.logical_and(~mask_black, ~mask_gray)
    mask_faint_colors = numpy.logical_and(mask_colors, s < 256 * 2 // 3)
    mask_bright_colors = numpy.logical_and(mask_colors, s > 256 * 2 // 3)

    c = max(1, mask_colors.sum())
    # in the color bins, make sub-bins by hue
    hue_bins = numpy.linspace(0, 255, 6 + 1)
    if mask_faint_colors.any():
        h_faint_counts, _ = numpy.histogram(h[mask_faint_colors], bins=hue_bins)
    else:
        h_faint_counts = numpy.zeros(len(hue_bins) - 1)
    if mask_bright_colors.any():
        h_bright_counts, _ = numpy.histogram(h[mask_bright_colors], bins=hue_bins)
    else:
        h_bright_counts = numpy.zeros(len(hue_bins) - 1)

    # now we have fractions in each category (6*2 + 2 = 14 bins)
    # convert to hash and discretize:
    maxvalue = 2 ** binbits
    values = [min(maxvalue - 1, int(frac_black * maxvalue)), min(maxvalue - 1, int(frac_gray * maxvalue))]
    for counts in list(h_faint_counts) + list(h_bright_counts):
        values.append(min(maxvalue - 1, int(counts * maxvalue * 1. / c)))

    bitarray = []
    for v in values:
        bitarray += [v // (2 ** (binbits - i - 1)) % 2 ** (binbits - i) > 0 for i in range(binbits)]
    result = numpy.asarray(bitarray).reshape((-1, binbits))
    return "".join(str(int(x)) for x in result.ravel())


def crop_resistant_hash(
        image,  # type: Image.Image
        hash_func=None,  # type: HashFunc
        limit_segments=None,  # type: int | None
        segment_threshold=128,  # type: int
        min_segment_size=500,  # type: int
        segmentation_image_size=300  # type: int
):
    if hash_func is None:
        hash_func = dhash

    orig_image = image.copy()
    # Convert to gray scale and resize
    image = image.convert('L').resize((segmentation_image_size, segmentation_image_size), Image.Resampling.LANCZOS)
    # Add filters
    image = image.filter(ImageFilter.GaussianBlur()).filter(ImageFilter.MedianFilter())
    pixels = numpy.array(image).astype(numpy.float32)

    segments = utils._find_all_segments(pixels, segment_threshold, min_segment_size)

    # If there are no segments, have 1 segment including the whole image
    if not segments:
        full_image_segment = {(0, 0), (segmentation_image_size - 1, segmentation_image_size - 1)}
        segments.append(full_image_segment)

    # If segment limit is set, discard the smaller segments
    if limit_segments:
        segments = sorted(segments, key=lambda s: len(s), reverse=True)[:limit_segments]

    # Create bounding box for each segment
    hashes = []
    for segment in segments:
        orig_w, orig_h = orig_image.size
        scale_w = float(orig_w) / segmentation_image_size
        scale_h = float(orig_h) / segmentation_image_size
        min_y = min(coord[0] for coord in segment) * scale_h
        min_x = min(coord[1] for coord in segment) * scale_w
        max_y = (max(coord[0] for coord in segment) + 1) * scale_h
        max_x = (max(coord[1] for coord in segment) + 1) * scale_w
        # Compute robust hash for each bounding box
        bounding_box = orig_image.crop((min_x, min_y, max_x, max_y))
        hashes.append(hash_func(bounding_box))
    return "".join(hashes)


def _median(data):
    data = sorted(data)
    length = len(data)
    if length % 2 == 0:
        return (data[length // 2 - 1] + data[length // 2]) / 2.0
    return data[length // 2]


def _total_value_rgba(im, data, x, y):
    r, g, b, a = data[y * im.size[0] + x]
    if a == 0:
        return 765
    else:
        return r + g + b


def _total_value_rgb(im, data, x, y):
    r, g, b = data[y * im.size[0] + x]
    return r + g + b


def _translate_blocks_to_bits(blocks, pixels_per_block):
    half_block_value = pixels_per_block * 256 * 3 / 2

    # Compare medians across four horizontal bands
    bandsize = len(blocks) // 4
    for i in range(4):
        m = _median(blocks[i * bandsize: (i + 1) * bandsize])
        for j in range(i * bandsize, (i + 1) * bandsize):
            v = blocks[j]

            # Output a 1 if the block is brighter than the median.
            # With images dominated by black or white, the median may
            # end up being 0 or the max value, and thus having a lot
            # of blocks of value equal to the median.  To avoid
            # generating hashes of all zeros or ones, in that case output
            # 0 if the median is in the lower value space, 1 otherwise
            blocks[j] = int(v > m or (abs(v - m) < 1 and m > half_block_value))


def blockhash_even(im, bits=16):
    if im.mode == 'RGBA':
        total_value = _total_value_rgba
    elif im.mode == 'RGB':
        total_value = _total_value_rgb
    else:
        raise RuntimeError('Unsupported image mode: {}'.format(im.mode))

    data = im.getdata()
    width, height = im.size
    blocksize_x = width // bits
    blocksize_y = height // bits

    result = []

    for y in range(bits):
        for x in range(bits):
            value = 0

            for iy in range(blocksize_y):
                for ix in range(blocksize_x):
                    cx = x * blocksize_x + ix
                    cy = y * blocksize_y + iy
                    value += total_value(im, data, cx, cy)

            result.append(value)

    _translate_blocks_to_bits(result, blocksize_x * blocksize_y)
    return "".join(map(str, result))


def blockhash(im, bits=16):
    if im.mode == 'RGBA':
        total_value = _total_value_rgba
    elif im.mode == 'RGB':
        total_value = _total_value_rgb
    else:
        raise RuntimeError('Unsupported image mode: {}'.format(im.mode))

    data = im.getdata()
    width, height = im.size

    even_x = width % bits == 0
    even_y = height % bits == 0

    if even_x and even_y:
        return blockhash_even(im, bits)

    blocks = [[0 for col in range(bits)] for row in range(bits)]

    block_width = float(width) / bits
    block_height = float(height) / bits

    for y in range(height):
        if even_y:
            # don't bother dividing y, if the size evenly divides by bits
            block_top = block_bottom = int(y // block_height)
            weight_top, weight_bottom = 1, 0
        else:
            y_frac, y_int = math.modf((y + 1) % block_height)

            weight_top = (1 - y_frac)
            weight_bottom = (y_frac)

            # y_int will be 0 on bottom/right borders and on block boundaries
            if y_int > 0 or (y + 1) == height:
                block_top = block_bottom = int(y // block_height)
            else:
                block_top = int(y // block_height)
                block_bottom = int(-(-y // block_height)) # int(math.ceil(float(y) / block_height))

        for x in range(width):
            value = total_value(im, data, x, y)

            if even_x:
                # don't bother dividing x, if the size evenly divides by bits
                block_left = block_right = int(x // block_width)
                weight_left, weight_right = 1, 0
            else:
                x_frac, x_int = math.modf((x + 1) % block_width)

                weight_left = (1 - x_frac)
                weight_right = (x_frac)

                # x_int will be 0 on bottom/right borders and on block boundaries
                if x_int > 0 or (x + 1) == width:
                    block_left = block_right = int(x // block_width)
                else:
                    block_left = int(x // block_width)
                    block_right = int(-(-x // block_width)) # int(math.ceil(float(x) / block_width))

            # add weighted pixel value to relevant blocks
            blocks[block_top][block_left] += value * weight_top * weight_left
            blocks[block_top][block_right] += value * weight_top * weight_right
            blocks[block_bottom][block_left] += value * weight_bottom * weight_left
            blocks[block_bottom][block_right] += value * weight_bottom * weight_right

    result = [blocks[row][col] for row in range(bits) for col in range(bits)]

    _translate_blocks_to_bits(result, block_width * block_height)
    return "".join(map(str, result))
