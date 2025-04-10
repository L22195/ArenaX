# ArenaX - Smart Stadium Attendance System

ArenaX is a smart attendance management system designed for stadiums, helping organizers monitor and predict seat occupancy using data analytics, Python, QR codes, and barcodes. The project enhances operational efficiency and the fan experience through technology.

## Project Objectives
- Predict the number of empty seats using attendance data
- Provide real-time tracking through QR/Barcode scanning
- Improve planning for events and staff allocation
- Generate useful reports and visualizations

##  Features
- Upload and analyze stadium attendance datasets
- Generate QR/Barcodes for individual ticket holders
- Real-time scanning and tracking system (via camera or handheld scanner)
- Seat occupancy prediction using machine learning
- Export reports and visual summaries

## Technologies Used
- **Python**: Core programming
- **Pandas, NumPy**: Data manipulation
- **Matplotlib, Seaborn**: Data visualization
- **Scikit-learn**: Machine learning (seat prediction)
- **OpenCV / ZBar / pyzbar**: QR and Barcode reading
- **Flask (optional)**: For web app deployment

## Folder Structure
```
ArenaX_Project/
├── data/                  # CSV attendance files
├── qr_barcodes/          # Generated QR & barcodes
├── model/                # Machine learning models
├── notebooks/            # Jupyter notebooks for analysis
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

##  How to Run
```bash
# 1. Clone the repo
$ git clone https://github.com/L22195/ArenaX.git
$ cd ArenaX

# 2. (Optional) Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Run the main app or notebook
$ python app.py
```

##  Sample Features
- `generate_qr_code(user_id)` – creates a unique QR code
- `scan_qr_code(image_path)` – reads data from QR/Barcode image
- `predict_empty_seats(date, match_id)` – returns prediction based on past patterns

##  Future Improvements
- Integration with online ticketing platforms
- Mobile app version for scanning
- Admin dashboard
- Multilingual support

## License
This project is licensed under the MIT License.

---
Made with ❤️ by ArenaX Team

