#!/usr/bin/env python3
"""
高项复习推送脚本（含飞书发送功能）
每天早上8点推送历史问题供用户复习
"""
import json
import random
import os
import subprocess
from datetime import datetime

QUESTIONS_FILE = "/root/.openclaw/workspace/skills/gaoxiang-study/assets/questions/archive.json"
USER_ID = "ou_2fde61ba6240bd7f5ec5da4e7bfe7f00"

def load_questions():
    """加载问题档案"""
    if not os.path.exists(QUESTIONS_FILE):
        return []
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_review_questions(questions, count=5):
    """选择需要复习的问题"""
    # 优先选择 review_count 少的问题
    candidates = [q for q in questions if q.get('review_count', 0) < 3]
    if len(candidates) <= count:
        return candidates
    return random.sample(candidates, count)

def format_message(questions):
    """格式化推送消息"""
    if not questions:
        return "📚 高项复习提醒\n\n今天没有问题需要复习，继续加油学习新知识吧！"
    
    msg = "📚 高项复习提醒\n\n"
    msg += "早上好！今天来复习几个问题：\n\n"
    
    for i, q in enumerate(questions, 1):
        msg += f"{i}. 【{q['chapter']}】{q['question']}\n"
        if q.get('answer_summary'):
            msg += f"   💡 答案要点：{q['answer_summary'][:50]}...\n"
        msg += "\n"
    
    msg += "回复题号查看详细答案，或者直接告诉我你的答案来检验学习效果！"
    return msg

def send_to_feishu(message):
    """通过openclaw命令行发送消息到飞书"""
    try:
        # 使用 openclaw message 命令发送
        cmd = [
            "openclaw", "message", "send",
            "--channel", "feishu",
            "--target", USER_ID,
            "--message", message
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✅ 消息已发送到飞书")
            return True
        else:
            print(f"❌ 发送失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 发送异常: {e}")
        return False

def main():
    questions = load_questions()
    if not questions:
        print("没有问题档案")
        return
    
    review_questions = select_review_questions(questions)
    message = format_message(review_questions)
    
    # 打印消息（用于日志）
    print("=" * 50)
    print(message)
    print("=" * 50)
    
    # 发送到飞书
    send_to_feishu(message)
    
    # 更新复习计数
    for q in review_questions:
        q['review_count'] = q.get('review_count', 0) + 1
        q['last_review'] = datetime.now().isoformat()
    
    # 保存更新
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已更新 {len(review_questions)} 个问题的复习计数")

if __name__ == "__main__":
    main()
