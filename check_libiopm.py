import subprocess

def uninstall_packages(packages):
    for package in packages:
        print(f"Uninstalling {package}...")
        subprocess.call(['pip', 'uninstall', '-y', package])

# requirements.txt 파일을 읽어와서 패키지 목록을 생성
with open('requirements.txt', 'r') as f:
    packages = f.read().splitlines()

# 패키지 제거 함수 호출
uninstall_packages(packages)
