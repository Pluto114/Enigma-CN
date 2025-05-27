import random  # 用于生成示例接线，当你使用真实数据时可以移除

# --- 0. 配置常量 ---
NUM_ROTORS = 20

# --- 1. 定义基础组件 ---

# !!! 用户替换区 START: ALPHABET 定义 !!!
# 请将下面的 ALPHABET 字符串替换为你的包含5000个唯一常用汉字的字符串。
# 示例: ALPHABET = "一乙二十丁厂七卜人入八九儿了力乃刀又三于干亏士工土才寸下大丈与万上小口山巾千乞川..."
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 这是一个占位符/示例，请务必替换！
if ALPHABET == "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and NUM_ROTORS == 20:
    print("警告: 你正在使用一个非常短的示例ALPHABET (26个字母) 和20个转盘。")
    print("       这仅用于演示代码结构，实际应用中请替换为你的5000字字符集。")
    print("       否则，加密强度会非常低，且槽口等设置可能不合理。\n")
# !!! 用户替换区 END: ALPHABET 定义 !!!

N = len(ALPHABET)
if N == 0:
    print("错误：ALPHABET 为空！请提供一个有效的字符集。")
    exit()

# !!! 用户替换区 START: 转盘接线 (rotor_wirings) 定义 !!!
# rotor_wirings 是一个包含 NUM_ROTORS 个字符串的列表。
# 每个字符串都必须是你上面定义的 ALPHABET 的一个精确的随机置换。
# (即，包含ALPHABET中的所有字符，每个字符只出现一次，但顺序被打乱)
# 你需要自己准备这 NUM_ROTORS 个置换。
# 下面是生成【示例数据】的逻辑，请用你的真实数据替换整个 rotor_wirings 列表。
rotor_wirings = []
print("--- 正在生成/使用示例转盘接线 ---")
temp_alphabet_list = list(ALPHABET)
for i in range(NUM_ROTORS):
    random.shuffle(temp_alphabet_list)  # 打乱字符顺序
    rotor_wirings.append("".join(temp_alphabet_list))
    if i < 2:  # 只打印前2个示例转盘的部分内容，避免输出过长
        print(f"  示例转盘 {i + 1} 接线 (前10字符): '{rotor_wirings[i][:min(10, N)]}...'")
print("警告: 以上是示例转盘接线，请务必替换为你的真实数据！")
print("--- 示例转盘接线生成完毕 ---")
# 示例替换格式:
# rotor_wirings = [
#     "你的第一个5000字随机置换字符串...",  # 转盘1 (R1)
#     "你的第二个5000字随机置换字符串...",  # 转盘2 (R2)
#     # ... (共 NUM_ROTORS 个)
#     "你的第二十个5000字随机置换字符串..." # 转盘20 (R20)
# ]
# !!! 用户替换区 END: 转盘接线 (rotor_wirings) 定义 !!!

if len(rotor_wirings) != NUM_ROTORS:
    print(f"错误：rotor_wirings 列表的长度 ({len(rotor_wirings)}) 与 NUM_ROTORS ({NUM_ROTORS}) 不匹配！")
    exit()
for i, wiring in enumerate(rotor_wirings):
    if len(wiring) != N or set(wiring) != set(ALPHABET):
        print(f"错误：转盘 {i + 1} 的接线 '{wiring[:10]}...' 不是 ALPHABET 的有效置换。")
        print(f"       所需长度: {N}, 实际长度: {len(wiring)}")
        print(f"       是否包含所有ALPHABET字符且无重复: {set(wiring) == set(ALPHABET)}")
        exit()

# !!! 用户替换区 START: 转盘槽口字符 (rotor_notch_chars) 定义 !!!
# rotor_notch_chars 是一个包含 NUM_ROTORS 个字符的列表。
# 通常，前 NUM_ROTORS - 1 个转盘有槽口，最后一个转盘的槽口不触发其他转盘 (设为 None)。
# 槽口字符必须存在于你上面定义的 ALPHABET 中。
rotor_notch_chars = []
print("\n--- 正在生成/使用示例转盘槽口 ---")
for i in range(NUM_ROTORS):
    if i < NUM_ROTORS - 1:  # 前 NUM_ROTORS-1 个转盘可以有实际槽口
        # 示例：让槽口为ALPHABET中的特定字符，实际应用中应精心选择
        # 为了示例的唯一性，这里简单地选择ALPHABET中靠后的字符
        # 注意：如果N较小而NUM_ROTORS较大，这里的示例槽口可能会重复，对于真实应用需要仔细设计
        notch_char_index = (N - 1 - (i % N))  # 简单的示例选择逻辑
        rotor_notch_chars.append(ALPHABET[notch_char_index])
    else:
        rotor_notch_chars.append(None)  # 最后一个转盘的槽口通常不驱动其他转盘
if NUM_ROTORS > 0:
    print(f"  示例槽口字符 (前几个): {rotor_notch_chars[:min(5, NUM_ROTORS)]}...")
print("警告: 以上是示例转盘槽口，请务必替换为你的真实数据！")
print("--- 示例转盘槽口生成完毕 ---")
# 示例替换格式:
# rotor_notch_chars = [
#     '你为R1选的槽口汉字',
#     '你为R2选的槽口汉字',
#     # ...
#     '你为R(NUM_ROTORS-1)选的槽口汉字',
#     None  # R(NUM_ROTORS)的槽口不触发别的
# ]
# !!! 用户替换区 END: 转盘槽口字符 (rotor_notch_chars) 定义 !!!

if len(rotor_notch_chars) != NUM_ROTORS:
    print(f"错误：rotor_notch_chars 列表的长度 ({len(rotor_notch_chars)}) 与 NUM_ROTORS ({NUM_ROTORS}) 不匹配！")
    exit()

# 将槽口字符转换为索引
rotor_notch_indices = []
for i, char in enumerate(rotor_notch_chars):
    if char is not None:  # 最后一个可能是None
        idx = ALPHABET.find(char)
        if idx == -1:
            print(f"严重错误：预设的槽口字符 '{char}' (用于转盘 {i + 1}) 不在ALPHABET中！程序将退出。")
            exit()
        rotor_notch_indices.append(idx)
    else:
        rotor_notch_indices.append(None)

# 转盘的当前位置 (用整数索引 0 到 N-1 表示)
rotor_positions = [0] * NUM_ROTORS  # 初始化所有转盘位置为0 (对应ALPHABET的第一个字符)

print(f"\n字符集 ALPHABET 长度 N={N}")
print(f"转盘数量: {NUM_ROTORS}")
# (为避免过多输出，已注释掉完整打印接线和槽口列表的部分)
print("-" * 30)


# --- 辅助函数：根据偏移量应用转盘“移位”效果 ---
def get_shifted_turntable(wiring_str, position_offset):
    if not wiring_str:
        return ""
    length = len(wiring_str)
    if length == 0: return ""  # 以防万一
    # position_offset 是指转盘的'零位'对准了定子的哪个字符的偏移
    # 这等效于 wiring_str 本身左移 position_offset 位
    actual_offset = position_offset % length
    return wiring_str[actual_offset:] + wiring_str[:actual_offset]


# --- 2. 获取用户输入 ---
print(f'请输入明文内容（只能包含字符集 "{ALPHABET[:min(10, N)]}..." 中的字符）：')
plain_text_input = input()
# 如果你的ALPHABET是大小写敏感的汉字，则不需要转换大小写
# if ALPHABET == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     plain_text_input = plain_text_input.upper()


# 校验输入明文
valid_input = True
for char_idx, char_in_input in enumerate(plain_text_input):
    if char_in_input not in ALPHABET:
        print(f"错误：输入字符 '{char_in_input}' (在位置 {char_idx + 1}) 不在支持的字符集 ALPHABET 中。")
        valid_input = False
        # break # 可以选择找到一个就退出，或全部检查完
if not valid_input:
    print("程序将退出。")
    exit()

print(f"\n请输入 {NUM_ROTORS} 个转盘的初始位置 (每个都是ALPHABET中的单个字符):")
initial_rotor_positions_chars_input = []
for i in range(NUM_ROTORS):
    while True:
        char_pos_str_input = input(f"  转盘 {i + 1} 的初始位置字符: ").strip()
        if len(char_pos_str_input) == 1 and char_pos_str_input in ALPHABET:
            initial_rotor_positions_chars_input.append(char_pos_str_input)
            break
        else:
            print(f"    输入无效，请输入ALPHABET中的单个字符。")

try:
    for i in range(NUM_ROTORS):
        rotor_positions[i] = ALPHABET.find(initial_rotor_positions_chars_input[i])
except Exception as e:
    print(f"错误：转换初始位置时发生意外。{e} 程序将退出。")
    exit()

print("-" * 30)
current_pos_display_str = ", ".join(
    [f"R{i + 1}={ALPHABET[rotor_positions[i]]}({rotor_positions[i]})" for i in range(min(NUM_ROTORS, 5))])
if NUM_ROTORS > 5: current_pos_display_str += " ..."
print(f"初始转盘位置: {current_pos_display_str}")
print("-" * 30)
print("开始加密过程...")

# --- 3. 加密过程 ---
encrypted_text = ""

for char_idx_main_loop, current_input_char in enumerate(plain_text_input):
    print(f"\n加密字符 #{char_idx_main_loop + 1}: '{current_input_char}'")

    pos_display_before_step_str = ", ".join([f"{ALPHABET[pos]}" for pos in rotor_positions[:min(NUM_ROTORS, 5)]])
    if NUM_ROTORS > 5: pos_display_before_step_str += "..."
    print(f"  步进前转盘位置: {pos_display_before_step_str}")

    # --- 3a. 执行转盘步进机制 (在加密当前字符之前) ---
    step_triggers = [False] * NUM_ROTORS

    if NUM_ROTORS > 0:
        step_triggers[0] = True  # R1 (索引0, 最右/快轮) 总是尝试步进

    for i in range(NUM_ROTORS - 1):
        if step_triggers[i] and \
                rotor_notch_indices[i] is not None and \
                (rotor_positions[i] == rotor_notch_indices[i]):
            step_triggers[i + 1] = True

    for i in range(NUM_ROTORS):
        if step_triggers[i]:
            rotor_positions[i] = (rotor_positions[i] + 1) % N

    pos_display_after_step_str = ", ".join([f"{ALPHABET[pos]}" for pos in rotor_positions[:min(NUM_ROTORS, 5)]])
    if NUM_ROTORS > 5: pos_display_after_step_str += "..."
    print(f"  步进后转盘位置: {pos_display_after_step_str}")

    # --- 3b. 计算当前各转盘的有效“移位后”状态 ---
    current_shifted_rotors = []
    for i in range(NUM_ROTORS):
        shifted_rotor_str = get_shifted_turntable(rotor_wirings[i], rotor_positions[i])
        current_shifted_rotors.append(shifted_rotor_str)
        # if char_idx_main_loop < 1 and i < 2 :
        #     print(f"    当前有效转盘 {i+1} (部分): {shifted_rotor_str[:min(10,N)]}...")

    # --- 3c. 字符通过转盘栈进行加密 (链式替换) ---
    idx_in_alphabet_for_chain = ALPHABET.find(current_input_char)
    # print(f"    '{current_input_char}' 在 ALPHABET 中原始索引: {idx_in_alphabet_for_chain}")

    char_to_pass_to_next_rotor = ""

    for i in range(NUM_ROTORS):
        if not (0 <= idx_in_alphabet_for_chain < N):
            print(
                f"严重逻辑错误：在处理转盘 {i + 1} 时，来自上一级的索引 {idx_in_alphabet_for_chain} 无效。字符 '{current_input_char}' 加密失败。")
            char_to_pass_to_next_rotor = "ERROR_IDX"
            break

        output_char_from_this_rotor = current_shifted_rotors[i][idx_in_alphabet_for_chain]
        # print(f"    索引 {idx_in_alphabet_for_chain} 经过转盘 {i+1} 映射为: '{output_char_from_this_rotor}'")

        if i < NUM_ROTORS - 1:  # 如果不是最后一个转盘
            idx_in_alphabet_for_chain = ALPHABET.find(output_char_from_this_rotor)
            if idx_in_alphabet_for_chain == -1:
                print(
                    f"严重错误：转盘 {i + 1} 的输出 '{output_char_from_this_rotor}' 不在 ALPHABET 中。这通常意味着转盘接线错误（不是ALPHABET的置换）。字符 '{current_input_char}' 加密失败。")
                char_to_pass_to_next_rotor = "ERROR_WIRING"
                break
        else:  # 是最后一个转盘
            char_to_pass_to_next_rotor = output_char_from_this_rotor

    if "ERROR" not in char_to_pass_to_next_rotor:  # 如果没有发生错误
        print(f"    字符 '{current_input_char}' 经过 {NUM_ROTORS} 个转盘后最终加密为: '{char_to_pass_to_next_rotor}'")

    encrypted_text += char_to_pass_to_next_rotor

print("-" * 30)
print(f"原始明文: '{plain_text_input}'")
print(f"加密后密文: '{encrypted_text}'")
print("-" * 30)