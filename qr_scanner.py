
import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            print("Scanned QR/Barcode Data:", obj.data.decode('utf-8'))
            cap.release()
            return
        cv2.imshow("QR/Barcode Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
