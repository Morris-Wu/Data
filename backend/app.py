from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from data_loader import load_all_data, filter_data
from report_generator import generate_pdf_report
from instruction_parser import parse_instruction
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    # 獲取前端傳遞的指令  #HW5
    instruction = request.json.get('instruction', '')
    params = parse_instruction(instruction)

    # 若指令無效，返回錯誤訊息  #HW5
    if params['action'] != 'generate_report':
        return jsonify({'error': 'Invalid instruction'}), 400

    # 根據指令載入並篩選資料  #HW5
    df = load_all_data('data', data_type=params['data_type'])
    df_filtered = filter_data(df, team=params['team'], year_start=params['year_start'], year_end=params['year_end'])
 
    # 生成報表並返回檔案  #HW5
    filepath = generate_pdf_report(df_filtered, title=instruction, data_type=params['data_type'])
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
