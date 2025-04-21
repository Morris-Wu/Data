import re

def parse_instruction(instruction):
    result = {
        'action': 'unknown',
        'data_type': None,
        'year_start': None,
        'year_end': None,
        'team': None
    }

    if "報表" in instruction:
        result['action'] = 'generate_report'

        # 判斷是打者還是投手
        if "打者" in instruction:
            result['data_type'] = 'batting'
        elif "投手" in instruction:
            result['data_type'] = 'pitching'

        # 擷取年份
        year_match = re.search(r'(\d{4})[~\-](\d{4})', instruction)
        if year_match:
            result['year_start'] = int(year_match.group(1))
            result['year_end'] = int(year_match.group(2))

        # 擷取球隊名稱
        teams = ['中信兄弟', '富邦悍將', '樂天桃猿', '統一獅', '味全龍']
        for team in teams:
            if team in instruction:
                result['team'] = team
                break

    return result



