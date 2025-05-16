import re

# HW4
def parse_instruction(instruction):
    """
    解析使用者輸入的指令，抽取報表產生相關參數：
    - action: 動作，固定為 'generate_report'
    - year_start: 起始年份（若有）
    - year_end: 結束年份（若有）
    - team: 指定球隊名稱（若有）
    - data_type: 資料類型，打者或投手

    :param instruction: 字串，使用者輸入指令
    :return: dict，解析後的參數
    """
    instruction = instruction.strip()
    result = {
        'action': 'generate_report',
        'year_start': None,
        'year_end': None,
        'team': None,
        'data_type': 'batting'  # 預設為打者資料
    }

    # 解析年限範圍，例如：2010~2020 或 2005-2015 # HW4
    year_range = re.search(r'(\d{4})[~\-](\d{4})', instruction)
    if year_range:
        result['year_start'] = int(year_range.group(1))
        result['year_end'] = int(year_range.group(2))

    # 判斷資料類型，若包含「投手」關鍵字則設為 pitching  # HW4
    if '投手' in instruction:
        result['data_type'] = 'pitching'

    # 解析指定球隊名稱，支援六支中職球隊關鍵字 # HW4
    team_match = re.search(r'(統一|味全|樂天|中信|富邦|兄弟)', instruction)
    if team_match:
        result['team'] = team_match.group(1)

    return result
