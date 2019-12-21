import cv2

cap = cv2.VideoCapture('output.avi')

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Ou com esta notação ('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(cap.isOpened())

while cap.isOpened():

    ret, frame = cap.read()
    if ret == 1:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            break
    else:
        break

cv2.destroyAllWindows()
