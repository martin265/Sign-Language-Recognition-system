import pickle

import cv2
import mediapipe as mp
import numpy as np


class AllSigns:
    def start_inference(self):
        model_dict1 = pickle.load(open('pages/Sign_language_detection/model_ASL.p', 'rb'))
        # model_dict2 = pickle.load(open('./model2.p', 'rb'))
        model1 = model_dict1['model1']
        # model2 = model_dict2['model2']

        cap = cv2.VideoCapture(0)

        

        mp_hands = mp.solutions.hands
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles

        hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.3)

        labels_dict1 = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H",
            8: "I",
            9: "J",
            10: "K",
            11: "L",
            12: "M",
            13: "N",
            14: "O",
            15: "P",
            16: "Q",
            17: "R",
            18: "S",
            19: "T",
            20: "U",
            21: "V",
            22: "0",
            23: "1",
            24: "2",
            25: "3",
            26: "4",
            27: "5",
            28: "6",
            29: "7",
            30: "8"
        }
        # labels_dict2 = {0: 'A', 1: 'B', 2: 'D',3: 'E', 4: 'F',5:'G',6: 'H', 7: 'J', 8: 'K',9: 'M', 10: 'N',11:'P',12: 'Q', 13: 'R',14:'S',15: 'T', 16: 'W', 17: 'X',18: 'Y', 19: 'Z'}
        while True:

            data_aux = []
            x_ = []
            y_ = []

            ret, frame = cap.read()

            H, W, _ = frame.shape

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                n = len(results.multi_hand_landmarks)
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,  # image to draw
                        hand_landmarks,  # model output
                        mp_hands.HAND_CONNECTIONS,  # hand connections
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))
                if n == 1:

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10

                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10

                    prediction1 = model1.predict([np.asarray(data_aux)])

                    predicted_character1 = labels_dict1[int(prediction1[0])]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, predicted_character1, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3,
                                (0, 0, 0), 3,
                                cv2.LINE_AA)
                else:
                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10

                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10

                    #  prediction2 = model2.predict([np.asarray(data_aux)])

                    #  predicted_character2 = labels_dict2[int(prediction2[0])]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, "two hands detected", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3,
                                (0, 0, 0), 3,
                                cv2.LINE_AA)

            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            #  ------------------breaking the camera framw here when the inference is completed----------//
            if cv2.waitKey(1) == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

