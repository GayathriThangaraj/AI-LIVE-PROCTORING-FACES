from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Adjusting scaleFactor and minNeighbors for better face detection
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

            alert = ""
            # If no faces are detected
            if len(faces) == 0:
                alert = "No face detected"
            # If multiple faces are detected
            elif len(faces) > 1:
                alert = "Multiple faces detected"

            # Filter out too small objects or those not detected as faces
            filtered_faces = []
            for (x, y, w, h) in faces:
                # Adding a minimum size filter (you can adjust the min size here)
                if w > 50 and h > 50:  # Ignoring objects too small to be faces
                    filtered_faces.append((x, y, w, h))
            
            # Now, the filtered_faces will be used for drawing the rectangles
            for (x, y, w, h) in filtered_faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 150, 255), 2)

            # Add alert overlay
            if alert:
                overlay = frame.copy()
                cv2.rectangle(overlay, (0, 0), (frame.shape[1], 40), (0, 0, 0), -1)
                alpha = 0.6
                frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
                cv2.putText(frame, alert, (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Encode frame to send to browser
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
