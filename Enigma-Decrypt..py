import random  # 用于生成示例接线，当你使用真实数据时可以移除

# --- 0. 配置常量 ---
NUM_ROTORS = 20

# --- 1. 定义基础组件 (必须与加密程序完全一致) ---

# !!! 用户替换区 START: ALPHABET 定义 !!!
# 请将下面的 ALPHABET 字符串替换为你的包含5000个唯一常用汉字的字符串。
# 必须与加密时使用的 ALPHABET 完全相同。
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 这是一个占位符/示例，请务必替换！
if ALPHABET == "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and NUM_ROTORS == 20:
    print("警告: 你正在使用一个非常短的示例ALPHABET (26个字母) 和20个转盘。")
    print("       这仅用于演示代码结构，实际应用中请替换为你的5000字字符集。")
    print("       否则，解密将无法正确工作（除非加密也用了这个短字符集）。\n")
# !!! 用户替换区 END: ALPHABET 定义 !!!

N = len(ALPHABET)
if N == 0:
    print("错误：ALPHABET 为空！请提供一个有效的字符集。")
    exit()

# !!! 用户替换区 START: 转盘接线 (rotor_wirings) 定义 !!!
# rotor_wirings 是一个包含 NUM_ROTORS 个字符串的列表。
# 每个字符串都必须是你上面定义的 ALPHABET 的一个精确的随机置换。
# 必须与加密时使用的 rotor_wirings 完全相同。
rotor_wirings = []
print("--- 正在生成/使用示例转盘接线 (解密) ---")
temp_alphabet_list_dec = list(ALPHABET)  # 使用不同变量名以防意外
for i in range(NUM_ROTORS):
    # 为了与加密时的示例数据一致，如果加密时用了随机种子，这里也要用相同的种子
    # 为简单起见，我们假设每次运行代码，加密和解密的示例数据都是独立生成的，但结构相同
    random.seed(i)  # 加一个种子使得每次运行这个示例部分时，生成的接线是固定的（但仍是示例）
    random.shuffle(temp_alphabet_list_dec)
    rotor_wirings.append("".join(temp_alphabet_list_dec))
    if i < 2:
        print(f"  解密用示例转盘 {i + 1} 接线 (前10字符): '{rotor_wirings[i][:min(10, N)]}...'")
print("警告: 以上是示例转盘接线，请务必替换为你的真实数据！")
print("--- 示例转盘接线生成完毕 ---")
# !!! 用户替换区 END: 转盘接线 (rotor_wirings) 定义 !!!

if len(rotor_wirings) != NUM_ROTORS:
    print(f"错误：rotor_wirings 列表的长度 ({len(rotor_wirings)}) 与 NUM_ROTORS ({NUM_ROTORS}) 不匹配！")
    exit()
for i, wiring in enumerate(rotor_wirings):
    if len(wiring) != N or set(wiring) != set(ALPHABET):
        print(f"错误：转盘 {i + 1} 的接线 '{wiring[:10]}...' 不是 ALPHABET 的有效置换。")
        exit()

# !!! 用户替换区 START: 转盘槽口字符 (rotor_notch_chars) 定义 !!!
# rotor_notch_chars 是一个包含 NUM_ROTORS 个字符的列表。
# 必须与加密时使用的 rotor_notch_chars 完全相同。
rotor_notch_chars = []
print("\n--- 正在生成/使用示例转盘槽口 (解密) ---")
for i in range(NUM_ROTORS):
    if i < NUM_ROTORS - 1:
        notch_char_index = (N - 1 - (i % N))
        rotor_notch_chars.append(ALPHABET[notch_char_index])
    else:
        rotor_notch_chars.append(None)
if NUM_ROTORS > 0:
    print(f"  解密用示例槽口字符 (前几个): {rotor_notch_chars[:min(5, NUM_ROTORS)]}...")
print("警告: 以上是示例转盘槽口，请务必替换为你的真实数据！")
print("--- 示例转盘槽口生成完毕 ---")
# !!! 用户替换区 END: 转盘槽口字符 (rotor_notch_chars) 定义 !!!

if len(rotor_notch_chars) != NUM_ROTORS:
    print(f"错误：rotor_notch_chars 列表的长度 ({len(rotor_notch_chars)}) 与 NUM_ROTORS ({NUM_ROTORS}) 不匹配！")
    exit()

rotor_notch_indices = []
for i, char in enumerate(rotor_notch_chars):
    if char is not None:
        idx = ALPHABET.find(char)
        if idx == -1:
            print(f"严重错误：预设的槽口字符 '{char}' (用于转盘 {i + 1}) 不在ALPHABET中！程序将退出。")
            exit()
        rotor_notch_indices.append(idx)
    else:
        rotor_notch_indices.append(None)

rotor_positions = [0] * NUM_ROTORS

print(f"\n字符集 ALPHABET 长度 N={N}")
print(f"转盘数量: {NUM_ROTORS}")
print("-" * 30)


# --- 辅助函数：根据偏移量应用转盘“移位”效果 (与加密程序一致) ---
def get_shifted_turntable(wiring_str, position_offset):
    if not wiring_str: return ""
    length = len(wiring_str)
    if length == 0: return ""
    actual_offset = position_offset % length
    return wiring_str[actual_offset:] + wiring_str[:actual_offset]


# --- 2. 获取用户输入 ---
print('请输入密文内容：')
cipher_text_input = input()
# if ALPHABET == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     cipher_text_input = cipher_text_input.upper() # 假设密文也是大写

print(f"\n请输入加密时使用的 {NUM_ROTORS} 个转盘的初始位置 (每个都是ALPHABET中的单个字符):")
initial_rotor_positions_chars_key = []
for i in range(NUM_ROTORS):
    while True:
        char_pos_str_key = input(f"  加密时转盘 {i + 1} 的初始位置字符: ").strip()
        if len(char_pos_str_key) == 1 and char_pos_str_key in ALPHABET:
            initial_rotor_positions_chars_key.append(char_pos_str_key)
            break
        else:
            print(f"    输入无效，请输入ALPHABET中的单个字符。")

try:
    for i in range(NUM_ROTORS):
        rotor_positions[i] = ALPHABET.find(initial_rotor_positions_chars_key[i])
except Exception as e:
    print(f"错误：转换初始位置时发生意外。{e} 程序将退出。")
    exit()

print("-" * 30)
current_pos_display_key_str = ", ".join(
    [f"R{i + 1}={ALPHABET[rotor_positions[i]]}({rotor_positions[i]})" for i in range(min(NUM_ROTORS, 5))])
if NUM_ROTORS > 5: current_pos_display_key_str += " ..."
print(f"解密使用的初始转盘位置: {current_pos_display_key_str}")
print("-" * 30)
print("开始解密过程...")

# --- 3. 解密过程 ---
decrypted_text = ""

for char_idx_main_loop_dec, encrypted_char in enumerate(cipher_text_input):
    print(f"\n解密字符 #{char_idx_main_loop_dec + 1}: '{encrypted_char}'")

    # --- 3a. 精确重现加密时该字符对应的转盘步进 (与加密程序完全一致) ---
    pos_display_before_step_dec_str = ", ".join([f"{ALPHABET[pos]}" for pos in rotor_positions[:min(NUM_ROTORS, 5)]])
    if NUM_ROTORS > 5: pos_display_before_step_dec_str += "..."
    print(f"  本轮开始时 (加密时步进前) 转盘位置: {pos_display_before_step_dec_str}")

    step_triggers_dec = [False] * NUM_ROTORS
    if NUM_ROTORS > 0:
        step_triggers_dec[0] = True

    for i in range(NUM_ROTORS - 1):
        if step_triggers_dec[i] and \
                rotor_notch_indices[i] is not None and \
                (rotor_positions[i] == rotor_notch_indices[i]):
            step_triggers_dec[i + 1] = True

    for i in range(NUM_ROTORS):
        if step_triggers_dec[i]:
            rotor_positions[i] = (rotor_positions[i] + 1) % N

    pos_display_after_step_dec_str = ", ".join([f"{ALPHABET[pos]}" for pos in rotor_positions[:min(NUM_ROTORS, 5)]])
    if NUM_ROTORS > 5: pos_display_after_step_dec_str += "..."
    print(f"  加密此字符时步进后的转盘位置: {pos_display_after_step_dec_str}")

    # --- 3b. 计算加密此字符时，各转盘的有效“移位后”状态 (与加密程序一致) ---
    current_shifted_rotors_for_decryption = []
    for i in range(NUM_ROTORS):
        shifted_rotor_dec_str = get_shifted_turntable(rotor_wirings[i], rotor_positions[i])
        current_shifted_rotors_for_decryption.append(shifted_rotor_dec_str)
        # if char_idx_main_loop_dec < 1 and i < 2:
        #     print(f"    解密用有效转盘 {i+1} (部分): {shifted_rotor_dec_str[:min(10,N)]}...")

    # --- 3c. 字符通过转盘栈进行反向解密 ---
    # 信号路径: Ciphertext -> R(NUM_ROTORS)_inv -> ... -> R2_inv -> R1_inv -> Plaintext_char

    char_to_reverse_transform = encrypted_char
    # print(f"    开始反向传递的字符: '{char_to_reverse_transform}' (来自密文)")

    for i in range(NUM_ROTORS - 1, -1, -1):  # 从最后一个转盘 (索引NUM_ROTORS-1) 反向到第一个 (索引0)
        current_rotor_shifted_state = current_shifted_rotors_for_decryption[i]

        # 我们需要找到哪个输入索引 (idx_at_alphabet_before_this_rotor) 经过这个转盘的当前状态映射后
        # 会得到 char_to_reverse_transform。
        # 即：current_rotor_shifted_state[idx_at_alphabet_before_this_rotor] == char_to_reverse_transform
        # 所以：idx_at_alphabet_before_this_rotor = current_rotor_shifted_state.find(char_to_reverse_transform)

        idx_found_in_shifted_rotor = current_rotor_shifted_state.find(char_to_reverse_transform)

        if idx_found_in_shifted_rotor == -1:
            print(
                f"严重错误：在解密时，字符 '{char_to_reverse_transform}' 未在转盘 {i + 1} 的当前状态 ('{current_rotor_shifted_state[:min(10, N)]}...') 中找到。")
            print("       这通常意味着密文损坏、密钥错误，或者转盘接线不是ALPHABET的置换。")
            char_to_reverse_transform = "ERROR_FIND"
            break

        # 这个 idx_found_in_shifted_rotor 是 ALPHABET 中的一个索引，它代表了进入这个转盘之前的信号
        # （或者是上一级转盘的输出字符在 ALPHABET 中的索引）
        char_to_reverse_transform = ALPHABET[idx_found_in_shifted_rotor]
        # print(f"    反向通过转盘 {i+1} 后，得到字符 (或上一级输出): '{char_to_reverse_transform}' (基于索引 {idx_found_in_shifted_rotor})")

    current_decrypted_char = char_to_reverse_transform  # 经过所有反向映射后，得到原始明文字符

    if "ERROR" not in current_decrypted_char:
        print(f"    密文字符 '{encrypted_char}' 经过反向解密为: '{current_decrypted_char}'")

    decrypted_text += current_decrypted_char

print("-" * 30)
print(f"原始密文: '{cipher_text_input}'")
print(f"解密后明文: '{decrypted_text}'")
print("-" * 30)