# Lesson 7: Contours & Basic Hand Detection

### 1. **Importing Libraries:**
```python
import cv2
import mediapipe as mp
```
- **`cv2`**: This is OpenCV, a library used for computer vision tasks like reading images, detecting faces, or in your case, detecting hands.
- **`mediapipe`**: This is another library that simplifies tasks like hand detection. It has pre-trained models to help detect hand landmarks, which are points on your hand (like fingertips and knuckles).

### 2. **Setting up MediaPipe and OpenCV tools:**
```python
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands
```
- **`mp_drawing`**: Used for drawing the landmarks on the detected hand in the image.
- **`mp_drawing_styles`**: Provides styling options for drawing (like color, thickness).
- **`mphands`**: Contains the hand detection features, like detecting hand landmarks and connections between them.

You're using a library called **MediaPipe**, which is a tool made by Google that helps you do complex tasks like detecting hands, faces, poses, etc., using machine learning models. It gives you ready-made solutions that are easy to integrate into your code.

In MediaPipe, there are multiple tools (called **solutions**) that help with different tasks. For hand detection, you need to use the **hands** solution.

Now, let’s look at the three lines you asked about:

#### **`mp_drawing = mp.solutions.drawing_utils`**

- **`mp.solutions.drawing_utils`**: This part is a set of helper functions in MediaPipe that makes it easy to **draw** things (like hand landmarks, lines, or shapes) on an image. In this case, we're going to use it to draw the landmarks (points) on the hands detected by MediaPipe.
  
- **`mp_drawing`**: By giving this a shorter name (`mp_drawing`), you're simply making it easier to call the functions later. Instead of typing `mp.solutions.drawing_utils` every time, you just type `mp_drawing`.

#### Example:
- **Without this line**: You’d have to write `mp.solutions.drawing_utils.draw_landmarks(...)` every time you want to draw something.
- **With this line**: You can just write `mp_drawing.draw_landmarks(...)`, which is simpler and saves time.

#### **`mp_drawing_styles = mp.solutions.drawing_styles`**

- **`mp.solutions.drawing_styles`**: This is another part of MediaPipe's drawing tools. It allows you to customize the **style** of your drawings—things like **line thickness**, **color**, or **point style**. 

- **`mp_drawing_styles`**: Just like the previous example, this is a shortcut to make it easier to use the drawing styles. So, instead of typing out `mp.solutions.drawing_styles`, you can simply type `mp_drawing_styles`.

#### Why is this useful?
Let’s say you want to draw hand landmarks with red color and thicker lines. Instead of setting these styles manually every time, you can use **`mp_drawing_styles`** to define them once and apply them in a simpler way.

#### **`mphands = mp.solutions.hands`**

- **`mp.solutions.hands`**: This is the part of MediaPipe that handles **hand detection**. It uses a machine learning model to detect the **landmarks** (specific points) on the hands in real-time. This model can detect a hand in an image and give you key points like the **wrist**, **fingers**, and **knuckles**.

- **`mphands`**: Again, this is just a shortcut to make it easier to call the hand detection functions. Instead of typing `mp.solutions.hands` every time, you use `mphands`.


### 3. **Setting up the Camera:**
```python
cap = cv2.VideoCapture(1)
```
- **`cv2.VideoCapture(1)`**: This opens the camera so that you can grab real-time video from your webcam. The `0` is the default camera; if you have multiple cameras, you can change this number to use a different one.

### 4. **Starting Hand Detection:**
```python
hands = mphands.Hands()
```
- **`hands = mphands.Hands()`**: This is creating an object that will handle hand detection. It uses MediaPipe's hand detection model to find hands in the video feed.

### 5. **Main Loop (Processing the Video Feed):**
```python
while True:
    data, image = cap.read()
```
- **`cap.read()`**: Captures one frame (image) from the camera. `data` checks if the frame is successfully captured, and `image` contains the image data.

### 6. **Preprocessing the Image:**
```python
image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
```
- **`cv2.flip(image, 1)`**: Flips the image horizontally. This makes it behave like a mirror, which is useful for hand gestures that you want to be mirrored.
- **`cv2.cvtColor(..., cv2.COLOR_BGR2RGB)`**: Converts the image from OpenCV's default color format (BGR) to RGB. MediaPipe works in RGB, so this step is necessary.

### 7. **Running the Hand Detection:**
```python
results = hands.process(image)
```
- **`hands.process(image)`**: This runs MediaPipe's hand detection on the image. It looks for any hands and returns data about their position and landmarks (like wrist, fingers, etc.).

### 8. **Converting the Image Back:**
```python
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
```
- **`cv2.cvtColor(..., cv2.COLOR_RGB2BGR)`**: Converts the image back to BGR (so OpenCV can display it correctly).

### 9. **Drawing Hand Landmarks:**
```python
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mphands.HAND_CONNECTIONS
        )
```

### What does this part do?
This part is checking if any hands were detected in the image, and then it draws landmarks (specific points on the hand) and connections between them.

<div align="center">
  <img src="img/L7_1.png" alt="Hand Values" width="1000"/>
</div>

### Step-by-Step Explanation:

#### - **`if results.multi_hand_landmarks:`**
   - **What it means**: This checks if there are any hand landmarks detected by the MediaPipe model.
   - **Why it’s important**: When MediaPipe processes an image, it looks for hands and returns landmarks for any detected hands. The `results.multi_hand_landmarks` will hold the landmarks of all the hands detected in the image. If no hands are detected, `multi_hand_landmarks` will be empty or `None`.
   - **Think of it like**: A filter to make sure that there are hands in the image before trying to do anything with them. If no hands are found, the code skips to the next frame.

#### - **`for hand_landmarks in results.multi_hand_landmarks:`**
   - **What it means**: This line starts a loop that goes through each hand that has been detected. The variable `hand_landmarks` represents the landmarks for a single hand.
   - **Why it’s important**: MediaPipe can detect multiple hands at once, so this loop makes sure we draw landmarks for each hand detected in the frame.
   - **Think of it like**: If you were drawing points for multiple objects (hands) in an image, this loop ensures that we handle each hand separately and draw its landmarks.

#### - **`mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)`**
   - **What it means**: This line draws the landmarks and connections for a detected hand on the image.
     - **`image`**: This is the image (frame from the webcam) where the landmarks will be drawn.
     - **`hand_landmarks`**: These are the specific points (landmarks) on the detected hand (like the wrist, fingertips, etc.) that will be drawn on the image.
     - **`mphands.HAND_CONNECTIONS`**: This is a predefined list of connections between the hand landmarks that show how the points are related to each other (for example, how the thumb connects to the palm, or how the fingers connect to each other). It draws lines between these points.
   - **Why it’s important**: This is the part that visually marks the hand on the image. By connecting the landmarks with lines, it shows a skeleton-like structure for the hand, which helps us understand where each part of the hand is.
   - **Think of it like**: Drawing dots on a piece of paper (the landmarks), and then connecting those dots with lines (the connections) to make the hand's shape clearer. Without this, you'd only see a bunch of random points, but with it, you get a clear outline of the hand.

---

### 10. **Displaying the Image:**
```python
cv2.imshow('Handtracker', image)
cv2.waitKey(1)
```
- **`cv2.imshow('Handtracker', image)`**: Displays the image with the hand landmarks drawn on it in a window called "Handtracker."
- **`cv2.waitKey(1)`**: Waits for 1 millisecond before moving to the next frame. This keeps the video feed running smoothly.

### **Mini Task: Show Number of Fingers:**
In your lesson, you'll use **contours** (outlines of shapes) and **convex hull** (the shape around a set of points) to calculate the number of fingers. You can do this by:
1. Finding the contours of the hand.
2. Calculating the convex hull to find the shape of the hand.
3. Detecting "defects" (gaps) between the convex hull and the hand contours (these defects tell you where the fingers are).
4. Counting how many gaps (defects) there are, which corresponds to the number of fingers.

#### Here is the Full Code `(python/opencv/lesson7_hand_detection_contours.py)`:



This part isn't in the code yet, but it will involve using **contours** and **convexity defects** to count the fingers.

### Summary for Lesson 7:
- You're capturing video from the webcam.
- MediaPipe detects the landmarks on the hand.
- The code currently shows the landmarks and hand connections.
- The next step will involve using the **convex hull** and **contours** to detect fingers and display the finger count.

