from flask import Flask, request, render_template
from scraper import fetch_case_details
from database import create_connection, create_table, log_query
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        year = request.form['year']

        data = fetch_case_details(case_type, case_number, year)
        if data:
            conn = create_connection()
            if conn:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query_details = (case_type, case_number, year, timestamp, str(data))
                log_query(conn, query_details)
                conn.close()
            return render_template('result.html', data=data, case_number=case_number)
        else:
            return render_template('result.html', error="Unable to fetch case details. Please try again.", case_number=case_number)

    return render_template('index.html')

# ✅ Call database setup here instead
if __name__ == '__main__':
    conn = create_connection()
    if conn:
        create_table(conn)
        conn.close()
    app.run(debug=True)
