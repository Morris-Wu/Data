def parse_instruction(instruction):
    import re
    instruction = instruction.strip()
    result = {
        'action': 'generate_report',
        'year_start': None,
        'year_end': None,
        'team': None,
        'data_type': 'batting'
    }

    year_range = re.search(r'(\d{4})[~\-](\d{4})', instruction)
    if year_range:
        result['year_start'] = int(year_range.group(1))
        result['year_end'] = int(year_range.group(2))

    if '投手' in instruction:
        result['data_type'] = 'pitching'

    team_match = re.search(r'(統一|味全|樂天|中信|富邦|兄弟)', instruction)
    if team_match:
        result['team'] = team_match.group(1)

    return result

