import os
import json
import random
import time
from typing import List, Dict, Optional


class XieChengAccountPool:
    def __init__(self, cookie_path: str = "accounts.json"):
        self.cookie_path = cookie_path
        self.accounts: List[Dict] = []
        self.index = 0
        self.load_accounts()

    def load_accounts(self):
        """从 accounts.json 加载所有账号"""
        if not os.path.exists(self.cookie_path):
            raise FileNotFoundError(f"账号池文件不存在: {self.cookie_path}")

        if os.path.isdir(self.cookie_path):
            raise ValueError(f"账号池路径错误，预期是文件却是目录: {self.cookie_path}")

        with open(self.cookie_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"账号池 JSON 格式错误: {e}")

        for account in data:
            if (
                    isinstance(account, dict)
                    and "uid" in account
                    and "cookies" in account
                    and "cticket" in account["cookies"]
            ):
                self.accounts.append(account)

        if not self.accounts:
            raise RuntimeError("账号池为空或无有效账号，请先扫码登录")

    def get_cookie(self) -> Dict:
        """轮询获取一个账号的 cookie"""
        if not self.accounts:
            raise RuntimeError("账号池为空")
        account = self.accounts[self.index]
        self.index = (self.index + 1) % len(self.accounts)
        return account["cookies"]

    def get_account_by_uid(self, uid: str) -> Optional[Dict]:
        """根据 UID 获取账号"""
        for account in self.accounts:
            if account.get("uid") == uid:
                return account["cookies"]
        return None

    def mark_invalid(self, uid: str):
        """标记账号无效（只在内存中生效）"""
        self.accounts = [acc for acc in self.accounts if acc.get("uid") != uid]

    def save_account(self, uid: str, cookies: Dict):
        """将新账号追加到账号池并写入 JSON 文件"""
        if "cticket" not in cookies:
            raise ValueError("缺少 cticket，无法保存该账号")

        new_account = {
            "uid": uid,
            "cookies": cookies,
            "last_login": int(time.time())
        }

        # 加载已有数据
        data = []
        if os.path.exists(self.cookie_path):
            with open(self.cookie_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

        # 去重并添加新账号
        data = [acc for acc in data if acc.get("uid") != uid]
        data.append(new_account)

        # 保存
        with open(self.cookie_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"[√] 账号 {uid} 已写入账号池")