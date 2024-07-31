import keymap
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
font = cv2.FONT_HERSHEY_SIMPLEX

# 0 for webcam input:
cap = cv2.VideoCapture(0)

def is_fist(landmarks):
    return (landmarks[mp_hands.HandLandmark.THUMB_TIP].x < landmarks[mp_hands.HandLandmark.THUMB_IP].x and
            landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.PINKY_TIP].y > landmarks[mp_hands.HandLandmark.PINKY_PIP].y)

def is_open_hand(landmarks):
    return (landmarks[mp_hands.HandLandmark.THUMB_TIP].x > landmarks[mp_hands.HandLandmark.THUMB_IP].x and
            landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y)

def is_index_finger(landmarks):
    return (landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.PINKY_TIP].y > landmarks[mp_hands.HandLandmark.PINKY_PIP].y)

def is_pinky_finger(landmarks):
    return (landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y and
            landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
            landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y)

with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)

                if is_fist(hand_landmarks.landmark):
                    print("Move forward.")
                    keymap.release_key('a')
                    keymap.release_key('d')
                    keymap.release_key('s')
                    keymap.press_key('w')
                    cv2.putText(image, "Move forward", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                elif is_open_hand(hand_landmarks.landmark):
                    print("Move backward.")
                    keymap.release_key('a')
                    keymap.release_key('d')
                    keymap.release_key('w')
                    keymap.press_key('s')
                    cv2.putText(image, "Move backward", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                elif is_index_finger(hand_landmarks.landmark):
                    print("Turn left.")
                    keymap.release_key('s')
                    keymap.release_key('d')
                    keymap.press_key('a')
                    cv2.putText(image, "Turn left", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                elif is_pinky_finger(hand_landmarks.landmark):
                    print("Turn right.")
                    keymap.release_key('s')
                    keymap.release_key('a')
                    keymap.press_key('d')
                    cv2.putText(image, "Turn right", (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    print("No specific gesture detected.")
                    keymap.release_key('w')
                    keymap.release_key('a')
                    keymap.release_key('s')
                    keymap.release_key('d')

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()