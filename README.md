# Court-Data Fetcher & Mini-Dashboard

A web application built with Python and Flask that allows users to fetch case details from the Delhi High Court website. This application provides a simple interface to look up cases by type, number, and year, and view their current status.

## 📂 Table of Contents

- [License](#license)
- [Court Chosen](#court-chosen)
- [File Structure](#file-structure)
- [Setup Steps](#setup-steps)
- [CAPTCHA Handling Strategy](#captcha-handling-strategy)
- [Environment Variables](#environment-variables)
- [Demo Video](#demo-video)
- [Contributing](#contributing)

## 📜 License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## ⚖️ Court Chosen

The application interacts with the **Delhi High Court** website: `https://delhihighcourt.nic.in/`.


## File Structure

The project is organized into the following file structure to keep the backend logic, web templates, and static files separate and maintainable.

```
court-data-fetcher/
│                   
├── static/
│   └── style.css             # CSS for styling the web pages
│
├── templates/
│   ├── index.html            # Main form page
│   └── result.html           # Display results or error
│
├── app.py                    # Flask backend application
├── database.py               # SQLite database logic
├── scraper.py                # Selenium-based scraper for Delhi High Court
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation (this file)
```


## Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/court-data-fetcher.git
   cd court-data-fetcher
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download ChromeDriver:**
   - Download the appropriate ChromeDriver for your version of Google Chrome from the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) page.
   - Ensure you check your Chrome version by going to `Help` > `About Google Chrome` in your browser.
   - Place the `chromedriver` executable in the project directory.
   - Alternatively, you can add the `chromedriver` executable to your system's PATH for easier access.

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```

## 🛡️ CAPTCHA Handling Strategy

The application employs a straightforward approach to handle CAPTCHA challenges:

- It reads the CAPTCHA text directly from the webpage and automatically fills it into the input field.
- Future improvements could include integrating with a CAPTCHA-solving service or exploring alternative methods to enhance user experience.

✅ No image processing or OCR required.

## Sample Case Inputs

You can test with the following real Delhi High Court cases:

| Case Type  | Case Number | Year  |
|------------|-------------|-------|
| W.P.(C)    | 12230       | 2022  |
| CRL.M.C.   | 1784        | 2021  |
| FAO        | 86          | 2019  |
| CS(OS)     | 1729        | 2013  |
| W.P.(CRL)  | 1309        | 2020  |

## Environment Variables

No external environment variables are required at this stage. If future CAPTCHA APIs or deployment steps are added, they may be documented here.

## Demo Video

📽️ Screen capture video (≤ 5 minutes) showcasing:

- Entering valid case details
- Fetching metadata and PDF link
- Error handling demo
- Database logging view (SQLite)

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

✅ For any feedback or deployment help, feel free to reach out!
