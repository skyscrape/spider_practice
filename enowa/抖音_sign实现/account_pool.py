# account_pool.py
import pandas as pd
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class AccountInfoModel(BaseModel):
    """账号数据模型"""
    id: str = Field(..., title="账号ID")
    account_name: str = Field(..., title="账号名称")
    cookies: str = Field(..., title="登录cookie")



class AccountPool:
    """账号池管理类"""

    def __init__(self, platform_name: str = "dy"):
        self._platform_name = platform_name
        self._accounts: Dict[str, AccountInfoModel] = {}
        self._current_index = 0

    def add_account(self, account: AccountInfoModel):
        """将账号加入池子"""
        self._accounts[account.id] = account

    def all_accounts(self) -> List[AccountInfoModel]:
        """返回池中所有账号"""
        return list(self._accounts.values())

    def load_accounts_from_xlsx(self, file_path: str):
        """从 Excel 文件中导入账号"""
        df = pd.read_excel(file_path, sheet_name=self._platform_name, engine="openpyxl")
        for _, row in df.iterrows():
            account = AccountInfoModel(
                id=str(row.get("id")),
                account_name=row.get("account_name", ""),
                cookies=row.get("cookies", ""),
            )
            self.add_account(account)


if __name__ == "__main__":
    # 使用示例
    pool = AccountPool("dy")
    pool.load_accounts_from_xlsx("accounts_cookies.xlsx")  # Excel 表格中要有 id / account_name / cookies 三列
    print(pool.all_accounts())