import os
import cv2


class CollectStudentImage:
    """collecting the image for the student here---------------//"""
    def collect_student_image(self, student_username: str):
        try:
            DATA_DIR = 'C:/FinalProject/data'
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)

            number_of_classes = 1
            dataset_size = 1

            cap = cv2.VideoCapture(0)
            for j in range(number_of_classes):
                if not os.path.exists(os.path.join(DATA_DIR, str(student_username))):
                    os.makedirs(os.path.join(DATA_DIR, str(student_username)))

                print('Collecting data for class {}'.format(student_username))

                done = False
                while True:
                    ret, frame = cap.read()
                    cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0),
                                3,
                                cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(25) == ord('q'):
                        break

                counter = 0
                while counter < dataset_size:
                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    cv2.waitKey(25)
                    cv2.imwrite(os.path.join(DATA_DIR, str(student_username), '{}.jpg'.format(student_username)), frame)

                    counter += 1

            cap.release()
            cv2.destroyAllWindows()
            #  ----------------closing the camera here for the system-----------------//
        except Exception as ex:
            print(ex)


# img = CollectStudentImage()
# img.collect_student_image("james")


