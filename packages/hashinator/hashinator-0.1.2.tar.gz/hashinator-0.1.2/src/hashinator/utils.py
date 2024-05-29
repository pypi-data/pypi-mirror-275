import numpy


def compare_hashes(hash1: str, hash2: str) -> float:
    # if len(hash1) != len(hash2):
    #     raise ValueError('Hash length mismatch')
    if len(hash1) == 0:
        raise ValueError('Hash length zero')
    return len("".join(char1 for char1, char2 in zip(hash1, hash2) if char1 == char2)) / len(hash1) * 100


def _find_region(remaining_pixels, segmented_pixels):
    in_region = set()
    not_in_region = set()
    # Find the first pixel in remaining_pixels with a value of True
    available_pixels = numpy.transpose(numpy.nonzero(remaining_pixels))
    start = tuple(available_pixels[0])
    in_region.add(start)
    new_pixels = in_region.copy()
    while True:
        try_next = set()
        # Find surrounding pixels
        for pixel in new_pixels:
            x, y = pixel
            neighbours = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1)
            ]
            try_next.update(neighbours)
        # Remove pixels we have already seen
        try_next.difference_update(segmented_pixels, not_in_region)
        # If there's no more pixels to try, the region is complete
        if not try_next:
            break
        # Empty new pixels set, so we know whose neighbour's to check next time
        new_pixels = set()
        # Check new pixels
        for pixel in try_next:
            if remaining_pixels[pixel]:
                in_region.add(pixel)
                new_pixels.add(pixel)
                segmented_pixels.add(pixel)
            else:
                not_in_region.add(pixel)
    return in_region


def _find_all_segments(pixels, segment_threshold, min_segment_size):
    img_width, img_height = pixels.shape
    # threshold pixels
    threshold_pixels = pixels > segment_threshold
    unassigned_pixels = numpy.full(pixels.shape, True, dtype=bool)

    segments = []
    already_segmented = set()

    # Add all the pixels around the border outside the image:
    already_segmented.update([(-1, z) for z in range(img_height)])
    already_segmented.update([(z, -1) for z in range(img_width)])
    already_segmented.update([(img_width, z) for z in range(img_height)])
    already_segmented.update([(z, img_height) for z in range(img_width)])

    # Find all the "hill" regions
    while numpy.bitwise_and(threshold_pixels, unassigned_pixels).any():
        remaining_pixels = numpy.bitwise_and(threshold_pixels, unassigned_pixels)
        segment = _find_region(remaining_pixels, already_segmented)
        # Apply segment
        if len(segment) > min_segment_size:
            segments.append(segment)
        for pix in segment:
            unassigned_pixels[pix] = False

    # Invert the threshold matrix, and find "valleys"
    threshold_pixels_i = numpy.invert(threshold_pixels)
    while len(already_segmented) < img_width * img_height:
        remaining_pixels = numpy.bitwise_and(threshold_pixels_i, unassigned_pixels)
        segment = _find_region(remaining_pixels, already_segmented)
        # Apply segment
        if len(segment) > min_segment_size:
            segments.append(segment)
        for pix in segment:
            unassigned_pixels[pix] = False

    return segments
