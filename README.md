# Gesture-Based Racing Game Control using OpenCV and MediaPipe

This project uses OpenCV and MediaPipe to detect hand gestures, allowing users to control racing games with finger movements. The program captures live video input, recognizes specific hand gestures, and maps them to keyboard inputs to control the game.

## Prerequisites

To run this project, you need the following packages installed:

- Python 3.x
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- `keymap` module (for sending keyboard inputs)

You can install these packages using pip:

```sh
pip install opencv-python mediapipe keymap
```

## How It Works

1. **Hand Detection:** The program uses MediaPipe's Hands module to detect hand landmarks in real-time.
2. **Gesture Recognition:** It identifies specific hand gestures such as a fist, open hand, index finger pointing, and pinky finger pointing.
3. **Game Control:** Depending on the detected gesture, the program sends corresponding keyboard inputs to control the racing game.

## Running the Program

1. Clone this repository or copy the provided code.
2. Make sure you have the necessary dependencies installed.
3. Run the script:

```sh
python main.py
```

Replace `main.py` with the name of your Python file.

## Usage

- **Start the program:** The program will start capturing video from the webcam.
- **Gesture Detection:** Use the following gestures to control the game:
  - **Fist:** Move forward
  - **Open Hand:** Move backward
  - **Index Finger:** Turn left
  - **Pinky Finger:** Turn right
- **Exit:** Press 'q' to exit the program.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking.
- [OpenCV](https://opencv.org/) for video processing.