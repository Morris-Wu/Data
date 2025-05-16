import random

def generate_comment(df, data_type='batting', team=None, year_start=None, year_end=None):
    """
    生成 AI 評語摘要，根據資料類型與條件給出簡短分析與建議。

    :param df: DataFrame，已過濾好的球員資料
    :param data_type: 'batting' 或 'pitching'，預設為 'batting'
    :param team: 球隊名稱字串（可選）
    :param year_start: 起始年份（可選）
    :param year_end: 結束年份（可選）
    :return: 字串形式的報表摘要與評語
    """

    player_count = len(df)
    years = df['年份'].unique()
    teams = df['Team Name'].unique()

    summary = f"這份報表包含 {player_count} 位球員的資料，涵蓋 {len(years)} 年"
    if team:
        summary += f"，針對「{team}」球隊"
    else:
        summary += f"，共 {len(teams)} 支球隊"
    summary += "。\n\n"

    if player_count == 0:
        return summary + "查無符合條件的資料，請嘗試不同的年份或球隊。"

    if data_type == 'batting':
        avg_hit = round(df['H'].mean(), 2)
        avg_hr = round(df['HR'].mean(), 2)
        summary += f"平均每位球員擊出 {avg_hit} 支安打，{avg_hr} 支全壘打。"
        if avg_hr > 10:
            summary += " 火力相當不錯！"
        elif avg_hr < 2:
            summary += " 全壘打火力略顯不足。"
    else:  # pitching
        avg_so = round(df['SO'].mean(), 2)
        avg_bb = round(df['BB'].mean(), 2)
        summary += f"平均三振數為 {avg_so}，保送數為 {avg_bb}。"
        if avg_so > avg_bb * 2:
            summary += " 控球與壓制力表現不錯。"
        else:
            summary += " 投手控球仍有加強空間。"

    tips = [
        "可試著比較不同年代的球隊差異。",
        "想看打者與投手表現轉變，建議選擇跨年範圍的資料。",
        "資料來源為 CPBL 歷年成績統計，僅供參考。"
    ]
    summary += "\n\n" + random.choice(tips)

    return summary
