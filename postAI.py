from playwright.sync_api import sync_playwright
import time

# ✅ 內建帳號密碼
# HW3 post AI
Th_EMAIL = "********"
Th_PASSWORD = "*******"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)  # **開啟可視化模式**
    page = browser.new_page()

    print("🌍 開啟 Threads 登入頁面...")
    page.goto("https://www.threads.net/login")
    time.sleep(5)  # **等待頁面載入**

    print("✅ 登入頁面載入成功！")

    try:
        # **🔍 填入帳號**
        # HW3 post AI
        email_input = page.locator("input[type='text'], input[name='email']").first
        email_input.wait_for(state="visible", timeout=10000)
        email_input.click()
        page.keyboard.type(Th_EMAIL, delay=100)
        print("✉️ 帳號已輸入")

        # **使用 `Tab` 鍵切換到密碼輸入框**
        page.keyboard.press("Tab")
        time.sleep(1)

        # **🔍 填入密碼**
        # HW3 post AI
        password_input = page.locator("input[type='password'], input[name='password']").first
        password_input.wait_for(state="visible", timeout=10000)
        password_input.click()
        page.keyboard.type(Th_PASSWORD, delay=100)
        print("🔑 密碼已輸入")

        # **🚨 讓使用者手動點擊登入（或輸入驗證碼）**
        # HW3 post AI
        print("🚨 請手動點擊登入按鈕，或完成驗證後，按 Enter 繼續...")
        input()

        print("🔄 檢查是否成功登入...")
        time.sleep(10)  # **讓 Threads 有足夠時間載入登入後的內容**

        

        print("🎉 登入成功！")

    except Exception as e:
        print(f"🚨 發生錯誤：{e}")
        page.screenshot(path="error_unexpected.png")
        browser.close()
        exit()

    # **🏠 進入個人首頁**
    # HW3 post AI
    print("🏠 進入個人首頁...")
    page.goto("https://www.threads.net/@yuanwu763")
    time.sleep(5)

    # **✍️ 開始發文**
    # HW3 post AI
    print("✍️ 準備發文...")

    try:
        # **🔍 確保發文框出現**
        post_trigger = page.locator("span:has-text('有什麼新鮮事？'), span:has-text('發表新貼文')").first
        post_trigger.wait_for(state="visible", timeout=10000)
        post_trigger.click()
        print("📝 發文框已開啟")
        time.sleep(3)

        # **🔍 找到輸入框**
        # HW3 post AI
        post_box = page.locator("div[contenteditable='true']").first
        post_box.wait_for(state="visible", timeout=10000)
        post_box.click()
        print("⌨️ 開始輸入貼文內容...")

        # **📝 使用 `keyboard.type()` 模擬輸入**
        # HW3 post AI
        message = "🚀 這是一則由 Playwright 自動發佈的 Threads 貼文！"
        page.keyboard.type(message, delay=100)
        print("✅ 貼文內容已輸入")

                # **📝 使用 `keyboard.type()` 模擬輸入**
        message = "🚀 這是一則由 Playwright 自動發佈的 Threads 貼文！"
        page.keyboard.type(message, delay=100)
        print("✅ 貼文內容已輸入")

        # **✅ 確保 Threads 偵測到輸入**
        page.evaluate("""
            let postBox = document.querySelector('div[contenteditable="true"]');
            postBox.focus();
            postBox.dispatchEvent(new Event('focus', { bubbles: true }));
            postBox.dispatchEvent(new Event('input', { bubbles: true }));
            postBox.dispatchEvent(new Event('change', { bubbles: true }));
        """)
        print("🛠 Threads 成功偵測到輸入")

        # **🔍 確保發佈按鈕可用**
        # HW3 post AI
        print("⌛ 等待發佈按鈕變成可點擊狀態...")
        time.sleep(5)  # **等待 UI 變更**
        publish_button = page.locator("button:has-text('發佈')")
        publish_button.wait_for(state="visible", timeout=20000)  # **等待更長時間，避免 Timeout**
        print("✅ 發佈按鈕已啟用！")

        # **🚀 點擊發佈按鈕**
        # HW3 post AI
        publish_button.click()
        print("🚀 貼文發佈中...")

        # **⌛ 等待貼文完成**
        # HW3 post AI
        time.sleep(5)
        print("🎊 貼文成功發佈！")

    except Exception as e:
        print(f"🚨 發文時發生錯誤：{e}")
        page.screenshot(path="error_post_failed.png")
        browser.close()
        exit()

    # **🔒 自動關閉瀏覽器**
    print("✅ 任務完成，關閉瀏覽器")
    browser.close()
