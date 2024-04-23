import os
def list_files_in_directory(path):
    # 경로가 존재하는지 확인
    if not os.path.exists(path):
        print("경로가 존재하지 않습니다.")
        return

    # 디렉토리인지 확인
    if not os.path.isdir(path):
        print("유효한 디렉토리가 아닙니다.")
        return

    # 디렉토리 내 파일 목록 확인
    files = os.listdir(path)

    # 파일 출력
    print("경로 '{}' 에 있는 파일 목록:".format(path))
    for file in files:
        print(file)


# 경로 지정
directory_path = '../static/img/data/'

# 함수 호출
list_files_in_directory(directory_path)