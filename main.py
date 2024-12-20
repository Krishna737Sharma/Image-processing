import cv2
import numpy as np
from google.colab.patches import cv2_imshow

"""Task 1"""

#color_image = cv2.imread('a_1_task_1.png')
yuv_image = cv2.imread('a_1_task_1.png')
cv2_imshow(yuv_image)
color_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
cv2_imshow(yuv_image[:, :, 0])
cv2_imshow(yuv_image[:, :, 1])
cv2_imshow(yuv_image[:, :, 2])
ycrcb_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2YCR_CB)

r = 1.0 * yuv_image[:, :, 0] + 0.0 * yuv_image[:, :, 1] + 1.13983 * yuv_image[:, :, 2]
g = 1.0 * yuv_image[:, :, 0] - 0.39465 * yuv_image[:, :, 1] - 0.58060 * yuv_image[:, :, 2]
b = 1.0 * yuv_image[:, :, 0] + 2.03211 * yuv_image[:, :, 1] + 0.0 * yuv_image[:, :, 2]

#cv2_imshow(np.array([b, g, r]).transpose(1, 2, 0))

y = 0.299 * r + 0.587 * g + 0.114 * b
cb = -0.168736 * r - 0.331264 * g + 0.5 * b
cr = 0.5 * r - 0.418688 * g - 0.081312 * b

cv2_imshow(ycrcb_image[:, :, 0])
cv2_imshow(y)
cv2_imshow(ycrcb_image[:, :, 1])
cv2_imshow(cr)
cv2_imshow(ycrcb_image[:, :, 2])
cv2_imshow(cb)

cv2.imwrite("output_a_1_task_1_y_opencv.png", ycrcb_image[:, :, 0])
cv2.imwrite("output_a_1_task_1_y_scratch.png", y)
cv2.imwrite("output_a_1_task_1_cr_opencv.png", ycrcb_image[:, :, 1])
cv2.imwrite("output_a_1_task_1_cr_scratch.png", cr)
cv2.imwrite("output_a_1_task_1_cb_opencv.png", ycrcb_image[:, :, 2])
cv2.imwrite("output_a_1_task_1_cb_scratch.png", cb)
#cv2.imwrite("outputt.png", yuv_image)

output1 = yuv_image.copy()
output1[:, :, 0] = y
output1[:, :, 1] = cb
output1[:, :, 2] = cr

cv2_imshow(output1)
cv2_imshow(ycrcb_image)

"""Task 2 Solution"""

xor_image_1_input = cv2.imread('a_1_task_2_a.png', cv2.IMREAD_GRAYSCALE)
xor_image_2_input = cv2.imread('a_1_task_2_b.png', cv2.IMREAD_GRAYSCALE)

xor_image_output_opencv = cv2.bitwise_xor(xor_image_1_input, xor_image_2_input)
xor_image_output = xor_image_1_input ^ xor_image_2_input
cv2_imshow(xor_image_output_opencv)
cv2_imshow(xor_image_output)

cv2.imwrite("output_a_1_task_2_opencv.png", xor_image_output_opencv)
cv2.imwrite("output_a_1_task_2_scratch.png", xor_image_output)

"""Task 3 Solution"""

rotate_image_input = cv2.imread('a_1_task_3.png')

def rotate_image(image_array, angle):
  """
  Rotate the image using numpy.

  :param image_array: The image array to rotate
  :param angle: The angle in degrees to rotate the image
  :return: Rotated image array
  """
  # Convert the angle from degrees to radians
  angle_rad = np.deg2rad(angle)

  # Get the dimensions of the image
  h, w = image_array.shape[:2]

  # Compute the center of the image
  center = (w // 2, h // 2)

  # Create the rotation matrix
  M = np.array([[np.cos(angle_rad), -np.sin(angle_rad)], [np.sin(angle_rad), np.cos(angle_rad)]])

  # Create an empty array for the rotated image
  rotated_image = np.zeros_like(image_array)

  for i in range(h):
    for j in range(w):
      x, y = i - center[1], j - center[0]
      old_x, old_y = np.linalg.inv(M) @ [x, y]
      old_x, old_y = int(old_x + center[1]), int(old_y + center[0])
      if 0 <= old_x < h and 0 <= old_y < w:
        rotated_image[i, j] = image_array[old_x, old_y]

  return rotated_image

for i in range (8):
  (h, w) = rotate_image_input.shape[:2]
  center = (w // 2, h // 2)
  matrix = cv2.getRotationMatrix2D(center, 45.0 * i, 1.0)
  rotated_image = cv2.warpAffine(rotate_image_input, matrix, (w, h))
  cv2_imshow(rotated_image)
  cv2.imwrite("output_a_1_task_3_" + str(int(i * 45)).zfill(3) + "_opencv.png", rotated_image)

  rotated_image_array_r = rotate_image(rotate_image_input[:, :, 2], 45.0 * i)
  rotated_image_array_g = rotate_image(rotate_image_input[:, :, 1], 45.0 * i)
  rotated_image_array_b = rotate_image(rotate_image_input[:, :, 0], 45.0 * i)
  rotated_image_array = np.array([rotated_image_array_b, rotated_image_array_g, rotated_image_array_r], dtype = np.uint8)
  rotated_image_array = np.transpose(rotated_image_array, axes=[1, 2, 0])
  cv2_imshow(rotated_image_array)
  cv2.imwrite("output_a_1_task_3_" + str(int(i * 45)).zfill(3) + "_scratch.png", rotated_image_array)

"""Task 4 Solution"""

bit_image_1_input = cv2.imread('a_1_task_4_a.png', cv2.IMREAD_GRAYSCALE)
bit_image_2_input = cv2.imread('a_1_task_4_b.png', cv2.IMREAD_GRAYSCALE)

def bit_plane_slicing(image, bit_plane):
  rows, cols = image.shape
  bit_plane_image = np.zeros((rows, cols), dtype=np.uint8)
  for i in range(rows):
    for j in range(cols):
      bit_plane_image[i, j] = (image[i, j] & (1 << bit_plane)) >> bit_plane
  return bit_plane_image

image_1_bit_planes = [bit_plane_slicing(bit_image_1_input, i) for i in range(8)]
image_2_bit_planes = [bit_plane_slicing(bit_image_2_input, i) for i in range(8)]

image_1_bit_planes[0] = image_2_bit_planes[7]
reconstructed_image = [image_1_bit_planes[i] << i for i in range(8)]
reconstructed_image = np.sum(np.array(reconstructed_image, dtype=np.uint8), axis=0, dtype=np.uint8)
cv2_imshow(bit_image_1_input)
cv2_imshow(reconstructed_image)

cv2.imwrite("output_a_1_task_4_original.png", bit_image_1_input)
cv2.imwrite("output_a_1_task_4_edited.png", reconstructed_image)

"""Task 5 Solution"""

interp_image_input = cv2.imread('a_1_task_5.png', cv2.IMREAD_GRAYSCALE)

resized_image_opencv = cv2.resize(interp_image_input, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
cv2_imshow(resized_image_opencv)

def upscale_image_bicubic(image_array, scale_factor):
  w, h = image_array.shape[0], image_array.shape[1]

  b_im_ar = np.zeros(shape=(w + 3, h + 3))
  b_im_ar[1:-2, 1:-2] = image_array[:, :]

  temp_upscale_array = np.zeros(shape=(int(w * scale_factor), h + 3))
  upscale_array = np.zeros(shape=(int(w * scale_factor), int(h * scale_factor)))

  b_im_ar[0, :] = b_im_ar[1, :]
  b_im_ar[-2, :] = b_im_ar[-3, :]
  b_im_ar[-1, :] = b_im_ar[-3, :]

  for i in range(upscale_array.shape[0]):
    t = (i * (w / upscale_array.shape[0])) - int(i * (w / upscale_array.shape[0]))
    coef_1 = (t ** 3) / 6
    t += 1
    coef_2 = ((-3 * (t ** 3)) + (12 * (t ** 2)) + (-12 * t) + 4) / 6
    t += 1
    coef_3 = ((3 * (t ** 3)) + (-24 * (t ** 2)) + (60 * t) - 44) / 6
    t += 1
    coef_4 = ((4 - t) ** 3) / 6
    for j in range(upscale_array.shape[1]):
      temp_upscale_array[i, :] = coef_4 * b_im_ar[int(i / scale_factor) - 1, :] + coef_3 * b_im_ar[int(i / scale_factor), :] + coef_2 * b_im_ar[int(i / scale_factor) + 1, :] + coef_1 * b_im_ar[int(i / scale_factor) + 2, :]

  temp_upscale_array[:, 0] = temp_upscale_array[:, 1]
  temp_upscale_array[:, -2] = temp_upscale_array[:, -3]
  temp_upscale_array[:, -1] = temp_upscale_array[:, -3]

  for i in range(upscale_array.shape[1]):
    t = (i * (h / upscale_array.shape[1])) - int(i * (h / upscale_array.shape[1]))
    coef_1 = (t ** 3) / 6
    t += 1
    coef_2 = ((-3 * (t ** 3)) + (12 * (t ** 2)) + (-12 * t) + 4) / 6
    t += 1
    coef_3 = ((3 * (t ** 3)) + (-24 * (t ** 2)) + (60 * t) - 44) / 6
    t += 1
    coef_4 = ((4 - t) ** 3) / 6
    for j in range(upscale_array.shape[0]):
      upscale_array[:, i] = coef_4 * temp_upscale_array[:, int(i / scale_factor) - 1] + coef_3 * temp_upscale_array[:, int(i / scale_factor)] + coef_2 * temp_upscale_array[:, int(i / scale_factor) + 1] + coef_1 * temp_upscale_array[:, int(i / scale_factor) + 2]

  return upscale_array

# Upscale the image
scale_factor = 4
upscaled_image_array = upscale_image_bicubic(interp_image_input, scale_factor)
cv2_imshow(upscaled_image_array)

cv2.imwrite("output_a_1_task_5_opencv.png", resized_image_opencv)
cv2.imwrite("output_a_1_task_5_scratch.png", upscaled_image_array)

