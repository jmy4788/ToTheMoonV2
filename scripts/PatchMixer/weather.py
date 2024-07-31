import os
import subprocess
import sys

# 현재 실행 중인 Python이 가상 환경의 Python인지 확인

# 디렉토리 생성
if not os.path.exists("./logs"):
    os.makedirs("./logs")

if not os.path.exists("./logs/LongForecasting"):
    os.makedirs("./logs/LongForecasting")

seq_len = 336
model_name = "PatchMixer"

root_path_name = "./dataset/weather"
data_path_name = "weather.csv"
model_id_name = "weather"
data_name = "custom"

random_seed = 2021
pred_lens = [96]
# 일단 pred_lens 96만 Study해보자
# pred_lens = [96, 192, 336, 720]

for pred_len in pred_lens:
    log_file = f"logs/LongForecasting/{model_name}_{model_id_name}_sl{seq_len}_pl{pred_len}_random_seed{random_seed}.log"
    command = [
        "python", "-u", "run_longExp.py", 
        "--random_seed", str(random_seed),
        "--is_training", "0",
        "--root_path", root_path_name,
        "--data_path", data_path_name,
        "--model_id", model_id_name,
        "--model", model_name,
        "--data", data_name,
        "--features", "M",
        "--seq_len", str(seq_len),
        "--pred_len", str(pred_len),
        "--enc_in", "21",
        "--e_layers", "1",
        "--d_model", "256",
        "--dropout", "0.2",
        "--head_dropout", "0",
        "--patch_len", "16",
        "--stride", "8",
        "--des", "Exp",
        # Train_epochs 초기값은 200이었음
        "--train_epochs", "10",
        "--patience", "10",
        "--loss_flag", "2",
        "--itr", "1",
        "--batch_size", "1024",
        "--learning_rate", "0.001",
        # do predict 자체가 flag이기 때문에 Value가 필요 없음
        "--do_predict"
    ]
    
    with open(log_file, "w") as log:
        subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)

print("All tasks completed.")
