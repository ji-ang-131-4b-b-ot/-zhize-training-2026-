import cv2

# 读取图片
img = cv2.imread("images/test.jpg")

# 检查图片是否读取成功
if img is None:
    print("图片读取失败")
    exit()

# 输出图片信息
print("图片尺寸：", img.shape)

# 显示图片
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 裁剪图片
roi = img[100:600, 200:800]

# 显示裁剪结果
cv2.imshow("Crop", roi)

# 保存图片
cv2.imwrite("output/crop.jpg", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 增加亮度
bright = cv2.convertScaleAbs(
    img, alpha=1.0, beta=50
)

# 增加对比度
contrast = cv2.convertScaleAbs(
    img, alpha=2.0, beta=0
)

# 显示结果
cv2.imshow("Bright", bright)
cv2.imshow("Contrast", contrast)

# 保存结果
cv2.imwrite("output/bright.jpg", bright)
cv2.imwrite("output/contrast.jpg", contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 三种不同程度的高斯模糊
blur1 = cv2.GaussianBlur(img, (3, 3), 0)
blur2 = cv2.GaussianBlur(img, (9, 9), 0)
blur3 = cv2.GaussianBlur(img, (21, 21), 0)

# 显示
cv2.imshow("Blur 3", blur1)
cv2.imshow("Blur 9", blur2)
cv2.imshow("Blur 21", blur3)

# 保存
cv2.imwrite("output/blur3.jpg", blur1)
cv2.imwrite("output/blur9.jpg", blur2)
cv2.imwrite("output/blur21.jpg", blur3)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 加载人脸检测器
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# 转换灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

print("检测到的人脸数量：", len(faces))

# 绘制人脸框
face_img = img.copy()

for (x, y, w, h) in faces:
    cv2.rectangle(
        face_img,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
    )

cv2.imshow("Face Detection", face_img)
cv2.imwrite("output/face_detect.jpg", face_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# 复制原图
result = img.copy()

for (x, y, w, h) in faces:

    # 获取人脸区域
    face_roi = result[y:y+h, x:x+w]

    # 模糊人脸
    blurred = cv2.GaussianBlur(
        face_roi, (51, 51), 0
    )

    # 覆盖原来的人脸区域
    result[y:y+h, x:x+w] = blurred

# 显示和保存
cv2.imshow("Blurred Face", result)
cv2.imwrite("output/blurred_face.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()