
    resized_face = cv2.resize(face, (96,96), interpolation = cv2.INTER_AREA)
    resized_face_image = Image.fromarray(resized_face, 'RGB')