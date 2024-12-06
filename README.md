# Image Processing Assignment

This repository contains the solution to the Image Processing Assignment, where various image processing tasks such as color space conversion, logical operations, image rotation, bit plane slicing, and bicubic interpolation are implemented. The tasks are implemented manually without using OpenCV's high-level functions for the core operations.

## Tasks

### Task 1: Color Space Conversion
- **Objective**: Convert an image from YUV to YCbCr color space using the provided conversion matrices.
- **Input**: `a_1_task_1.png`
- **Approach**: Implemented the conversion manually using the matrix multiplication method.
- **Verification**: The result is compared with OpenCV's `cv2.COLOR_BGR2YCrCb` function for accuracy.

### Task 2: Logical XOR Operation
- **Objective**: Perform a logical XOR operation on two grayscale images.
- **Input**: `a_1_task_2_a.png` and `a_1_task_2_b.png`
- **Approach**: Implemented XOR manually by comparing pixel values and performing the XOR operation bit by bit.
- **Verification**: The result is compared with OpenCV's bitwise XOR function.

### Task 3: Image Rotation
- **Objective**: Rotate an image by varying angles (0°, 45°, 90°, 135°, 180°).
- **Input**: `a_1_task_3.png`
- **Approach**: Implemented manual image rotation by computing the new coordinates and interpolating pixel values.
- **Verification**: The rotated images are compared with OpenCV's `cv2.getRotationMatrix2D` and `cv2.warpAffine` for accuracy.

### Task 4: Bit Plane Slicing
- **Objective**: Hide the most significant bit plane of image B in one of the bit planes of image A to generate a visually identical image A'.
- **Input**: `a_1_task_4_a.png` and `a_1_task_4_b.png`
- **Approach**: The most significant bit (MSB) of image B is hidden in one of the bit planes of image A.
- **Output**: `a_1_task_4_a.png` is transformed into a new image A' which appears identical to A.

### Task 5: Bicubic Interpolation
- **Objective**: Upsample an image by a factor of 4 for both width and height using bicubic interpolation.
- **Input**: `a_1_task_5.png`
- **Approach**: Implemented bicubic interpolation manually to upscale the image by a factor of 4.
- **Verification**: The result is compared with OpenCV's `cv2.resize` function with the `cv2.INTER_CUBIC` option.

## Requirements
- Python 3.x
- NumPy
- OpenCV
- Matplotlib

## Installation

Clone the repository:

```bash
git clone https://github.com/Krishna737Sharma/Image-processing
cd image-processing-assignment
