from data_loader import load_all_data, filter_data
from report_generator import generate_pdf_report
from instruction_parser import parse_instruction

def main():
    instruction = input("請輸入你的需求（例如：請幫我產生 2010~2015 打者的打擊報表）：\n")
    params = parse_instruction(instruction)
    print(f"解析結果：{params}")

    if params['action'] != 'generate_report':
        print("❌ 無法辨識指令，請重新輸入！")
        return

    data_type = params.get('data_type')
    df = load_all_data('data', data_type=data_type)

    filtered_df = filter_data(
        df,
        team=params.get('team'),
        year_start=params.get('year_start'),
        year_end=params.get('year_end')
    )

    generate_pdf_report(filtered_df, title=instruction, data_type=data_type)

if __name__ == "__main__":
    main()


