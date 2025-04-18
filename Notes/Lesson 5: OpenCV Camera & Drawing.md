# Lesson 5: OpenCV Camera & Drawing

---

## 📷 5.1 OpenCV Camera 

## 🛠 Step 1: Install OpenCV

Before using OpenCV, you need to install it. Open your terminal or command prompt and run this:

```
pip install opencv-python
```

This tells Python: “Hey! Please download and install OpenCV so I can use it in my code.”

---

## 📷 Step 2: Opening the Camera

In Python, we use this line to open the webcam:

```python
cap = cv2.VideoCapture(1)
```

- `cv2.VideoCapture()` is like turning on your camera.
- The number `1` means: "Use the *second* camera you have."  
  👉 Use `0` if you're on a laptop with just one webcam.  
  👉 Use `1` if you're using an external webcam like on a MacBook Air M1.

---

## 📸 Step 3: Reading the Camera Feed

```python
ret, frame = cap.read()
```

- This grabs **one frame** (a single image) from the camera.
- `ret` is **True** if it worked, **False** if it failed.
- `frame` is the actual image (like a snapshot) from the camera.

We check `if not ret:` to stop the program if the camera fails.

---

## 🪟 Step 4: Showing the Camera Image

```python
cv2.imshow("Webcam", frame)
```

This pops up a window named **"Webcam"** that shows the live camera video. It updates every time a new frame is read.

---

## 🔴 Step 5: Press ‘q’ to Quit

```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```

This checks if the **'q' key** is pressed. If yes, it breaks the loop and exits.  
🔁 `cv2.waitKey(1)` waits **1 millisecond** between frames.

---

## 🔚 Step 6: Cleanup Time!

```python
cap.release()
cv2.destroyAllWindows()
```

- `cap.release()` turns off the camera.
- `cv2.destroyAllWindows()` closes the camera window.

ALWAYS do this when you're done — it’s like saying "Bye!" to your webcam.

---

## 🧠 Full Code (With Comments)

```python
import cv2

# Start the camera (1 = second camera)
cap = cv2.VideoCapture(1)

while True:
    # Read one frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Show the frame in a window
    cv2.imshow("Webcam", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Turn off camera and close the window
cap.release()
cv2.destroyAllWindows()
```

---
## 5.2 OpenCV Drawing on Camera

## ✨ What Are We Doing?

We’re using OpenCV to **draw shapes and text ON the webcam video** — like doodling on a window while looking outside.

---

## 👇 Full Code with Explanation:

## 🟦 Drawing a Rectangle

```python
cv2.rectangle(frame, (50, 50), (200, 200), (255, 0, 0), 2)
```

🧱 **Analogy:** Imagine putting blue masking tape on your camera screen.

- `frame` = the image we’re drawing on.
- `(50, 50)` = top-left corner of the rectangle.
- `(200, 200)` = bottom-right corner.
- `(255, 0, 0)` = blue color (remember: OpenCV uses BGR, not RGB!).
- `2` = thickness of the lines.

---

## 🟢 Drawing a Circle

```python
cv2.circle(frame, (300, 200), 50, (0, 255, 0), 3)
```

🟢 **Analogy:** You're drawing a green sticker on the screen.

- `(300, 200)` = center of the circle.
- `50` = radius (how big it is).
- `(0, 255, 0)` = green color.
- `3` = thickness of the circle border.

---

## ✍️ Writing Text

```python
cv2.putText(frame, 'Hello OpenCV', (50, 400),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```

💬 **Analogy:** It’s like typing "Hello OpenCV" with white chalk.

- `'Hello OpenCV'` = what you want to say.
- `(50, 400)` = where the text starts (bottom-left corner of the text).
- `cv2.FONT_HERSHEY_SIMPLEX` = the font style (like Arial for OpenCV).
- `1` = font size.
- `(255, 255, 255)` = white color.
- `2` = thickness of the text.

---

## 🪟 Showing Everything

```python
cv2.imshow("Webcam", frame)
```

🖥️ This opens a window named "Webcam" and shows all your drawings on the live video.


## 🧠 Final Code (Nicely Commented) 
`/python/opencv/lesson5_camera_drawing.py`

```python
import cv2

# Start camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Draw a blue rectangle
    cv2.rectangle(frame, (50, 50), (200, 200), (255, 0, 0), 2)

    # Draw a green circle
    cv2.circle(frame, (300, 200), 50, (0, 255, 0), 3)

    # Write some white text
    cv2.putText(frame, 'Hello OpenCV', (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the result in a window
    cv2.imshow("Webcam", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Turn off the camera and close the window
cap.release()
cv2.destroyAllWindows()
```

---

# Lesson 5: Summary

## 📷 5.1 OpenCV Camera

1. **Install OpenCV**:
   ```bash
   pip install opencv-python
   ```

2. **Open the Camera**:
   ```python
   cap = cv2.VideoCapture(1)
   ```

3. **Read Camera Feed**:
   ```python
   ret, frame = cap.read()
   ```

4. **Show the Feed**:
   ```python
   cv2.imshow("Webcam", frame)
   ```

5. **Press 'q' to Quit**:
   ```python
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   ```

6. **Cleanup**:
   ```python
   cap.release()
   cv2.destroyAllWindows()
   ```

---

## 5.2 OpenCV Drawing on Camera

1. **Draw a Rectangle**:
   ```python
   cv2.rectangle(frame, (50, 50), (200, 200), (255, 0, 0), 2)
   ```

2. **Draw a Circle**:
   ```python
   cv2.circle(frame, (300, 200), 50, (0, 255, 0), 3)
   ```

3. **Add Text**:
   ```python
   cv2.putText(frame, 'Hello OpenCV', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
   ```

4. **Show Everything**:
   ```python
   cv2.imshow("Webcam", frame)
   ```

