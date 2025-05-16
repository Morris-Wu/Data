from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from data_loader import load_all_data, filter_data
from report_generator import generate_pdf_report
from instruction_parser import parse_instruction
from aigent_commenter import generate_comment
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    # 從前端取得指令
    instruction = request.json.get('instruction', '')
    params = parse_instruction(instruction)

    # 驗證指令是否合法
    if params['action'] != 'generate_report':
        return jsonify({'error': 'Invalid instruction'}), 400

    # 載入資料並篩選
    df = load_all_data('data', data_type=params['data_type'])
    df_filtered = filter_data(df,
                              team=params['team'],
                              year_start=params['year_start'],
                              year_end=params['year_end'])

    # 產生 PDF 報表
    filepath = generate_pdf_report(df_filtered, title=instruction, data_type=params['data_type'])
    filename = os.path.basename(filepath)

    # 產生 AI 評語
    comment = generate_comment(df_filtered, instruction)

    # 回傳 PDF 路徑（靜態）與 AI 評語
    return jsonify({
        'pdf_path': f'reports/{filename}',
        'comment': comment
    })

# 提供報表檔案下載
@app.route('/reports/<path:filename>')
def download_file(filename):
    return send_from_directory('reports', filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=port)
