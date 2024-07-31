import numpy as np
import matplotlib.pyplot as plt

def load_predictions(file_path):
    return np.load(file_path)

def plot_predictions(predictions, num_samples=5):
    # 데이터 길이를 확인하여 num_samples 값을 조정합니다.
    num_samples = min(num_samples, predictions.shape[0])
    
    # 샘플 예측 결과를 몇 개 시각화합니다.
    plt.figure(figsize=(15, 10))
    for i in range(num_samples):
        plt.plot(predictions[i], label=f'Sample {i+1}')
    plt.title('Predictions')
    plt.xlabel('Time Steps')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # 저장된 .npy 파일 경로 설정
    setting = "loss_flag2_lr0.001_dm256_weather_PatchMixer_custom_ftM_sl336_pl96_p16s8_random2021_0"
    file_path = f"./results/{setting}/real_prediction.npy"
    
    # 예측 결과 로드
    predictions = load_predictions(file_path)
    
    # 예측 결과의 형태 출력
    print(f"Predictions shape: {predictions.shape}")
    
    # 예측 결과 시각화
    plot_predictions(predictions, num_samples=5)
