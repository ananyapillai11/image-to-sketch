import cv2

def pencil_sketch(input_image):
    img = cv2.imread(input_image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    inverted_gray = cv2.bitwise_not(gray_img)
    blurred_img = cv2.GaussianBlur(inverted_gray, (111,111),0)
    inverted_blurred = cv2.bitwise_not(blurred_img)
    pencil_sketch = cv2.divide(gray_img, inverted_blurred, scale=256.0)

    return pencil_sketch
# add the image name here
input_image_path = "image.jpg"
output_sketch_path = "pencil_sketch.jpg"

sketch = pencil_sketch(input_image_path)
cv2.imwrite(output_sketch_path, sketch)

print("Pencil sketch saved as 'pencil_sketch.jpg'")
