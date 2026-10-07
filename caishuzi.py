import random

def guess_number():
    print("=" * 40)
    print("        欢迎来到猜数字游戏！")
    print("=" * 40)

    low, high = 1, 100
    answer = random.randint(low, high)   # 随机生成答案
    count = 0                            # 记录猜测次数

    print(f"请猜一个 {low}~{high} 之间的整数")

    while True:
        user_input = input("请输入你猜的数字：").strip()

        # 校验输入是否为整数
        if not user_input.lstrip("-").isdigit():
            print("输入无效，请输入一个整数。\n")
            continue

        guess = int(user_input)

        # 校验是否在范围内（不算作一次有效猜测）
        if guess < low or guess > high:
            print(f"提示：请输入 {low} 到 {high} 之间的数字。\n")
            continue

        count += 1  # 有效猜测才计数

        if guess < answer:
            print("太小了，再大一点！\n")
        elif guess > answer:
            print("太大了，再小一点！\n")
        else:
            print(f"\n恭喜你，猜对了！答案就是 {answer}。")
            print(f"你一共猜了 {count} 次。")
            break


if __name__ == "__main__":
    guess_number()