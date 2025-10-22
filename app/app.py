from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    seen_counts = defaultdict(int)
    result: List[str] = []
    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1
    return result

# 可选：添加测试入口（本地验证用）
if __name__ == "__main__":
    test_cols = ["id", "id", "name", "id", "name"]
    print(dedupe_header(test_cols))  # 预期输出：["id", "id.1", "name", "id.2", "name.1"]