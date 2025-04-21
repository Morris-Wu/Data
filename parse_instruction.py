import re

def parse_instruction(instruction):
    """
    解析指令並回傳字典，包含 action、資料類型、年份範圍、球隊等資訊
    """
    instruction = instruction.strip().lower()

    # 顯示原始輸入
    print(f"指令原始輸入：{instruction}")  # 顯示原始指令

    result = {
        'action': 'unknown',
        'data_type': 'batting',  # 預設為打者資料
        'year_start': None,
        'year_end': None,
        'team': None
    }

    # 如果是產生報表的指令
    if "產生報表" in instruction or "生成報表" in instruction:
        result['action'] = 'generate_report'

        # 強化年份範圍匹配：支持2010~2015 或 2010-2015
        year_match = re.search(r'(\d{4})\s*[-~]\s*(\d{4})', instruction)  # 改進正則表達式，匹配 - 或 ~
        if year_match:
            result['year_start'] = int(year_match.group(1))
            result['year_end'] = int(year_match.group(2))
            print(f"找到年份範圍：{result['year_start']} 到 {result['year_end']}")  # 顯示匹配到的年份範圍
        else:
            print("未找到年份範圍。")  # 沒有匹配到年份範圍時，輸出提示

        # 查找資料類型（打者或投手）
        if "打者" in instruction:
            result['data_type'] = 'batting'
        elif "投手" in instruction:
            result['data_type'] = 'pitching'

        # 查找球隊名稱（如果有）
        team_match = re.search(r'(中信兄弟|富邦悍將|樂天桃猿|統一獅|味全龍)', instruction)
        if team_match:
            result['team'] = team_match.group(1)

    # 如果是退出指令
    elif "離開" in instruction or "退出" in instruction:
        result['action'] = 'exit'

    # 顯示解析結果，方便調試
    print(f"解析結果：{result}")  # 顯示最終解析結果

    return result

