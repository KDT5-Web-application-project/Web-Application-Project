from flask import Blueprint, request, render_template

bp = Blueprint('main', 
               __name__, 
               url_prefix='/')


# -----------------------------------------------------------------------
# 라우팅 함수들
# -----------------------------------------------------------------------

@bp.route('/', methods=['GET', 'POST'])
def index():
    # braille_image = None
    # if request.method == 'POST':
    #     if 'image' in request.files:
    #         # 요청에서 이미지 가져오기
    #         image_file = request.files['image']
    #         image = Image.open(image_file.stream)

    #         # 캡션 생성
    #         caption = generate_caption(image)

    #         # 이미지를 바이너리 데이터로 변환
    #         image_binary = image_to_binary(image)

    #         # 이미지와 캡션을 데이터베이스에 저장
    #         # new_image = Image(image=image_binary, caption=caption)
    #         # db.session.add(new_image)
    #         # db.session.commit()

    #         # 캡션을 음성으로 변환
    #         # engine.say(caption)
    #         # engine.runAndWait()

    #         return render_template('index.html', caption=caption)
    #     elif 'text' in request.form:
    #         # text = request.form['text']
    #         # braille_image = text_to_braille_image(text)

    # return render_template('index.html', braille_image=braille_image)
    return render_template(template_name_or_list="index.html")





## 제출된 사진을 확인하고 모델 돌려서 결과 얻기
@bp.route('/sign_model', methods = ['POST', 'GET'])
def check_sign():
    import os, datetime
    import torch
    import torchvision.transforms as transforms
    import torchvision.models as models
    from PIL import Image


    if request.method == 'POST':
        # -----------------------------------------
        # 업로드된 이미지를 로컬에 저장
        # -----------------------------------------
        
        OKT = 'Team5_web'   # 영신님 노트북에서는 이경로로 실행되어야 함
        # OKT = 'teamWeb'


        # 이미지 파일 경로
        dir = f'./{OKT}/static/img/'
        suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file = request.files['file2']
        save_dir = os.path.join(dir, suffix + file.filename)

        # 이미지 저장
        file.save(save_dir)

        # 불러올 이미지 경로
        open_dir = '../static/img/' + suffix + file.filename
        img_tag = f"<img src = '{open_dir}'>" 

        # -----------------------------------------
        # 모델 준비
        # -----------------------------------------

        # 저장된 모델 돌릴 클래스
        class MyResNet(torch.nn.Module):
            def __init__(self):
                super(MyResNet, self).__init__()
                self.resnet = models.resnet18()
            def forward(self, x):
                return self.resnet(x)

        # 모델 인스턴스 생성 : 방법1 
        # model = MyResNet()

        # 모델 인스턴스 생성 : 방법2
        model = models.resnet18(weights = "ResNet18_Weights.DEFAULT")
        # 전결합층 변경
        model.fc = torch.nn.Linear(in_features = 512, out_features = 43)

        # 저장된 모델의 가중치 로딩
        model_file = f'./{OKT}/static/model/sign_3.pth'            # 웹 기준
        model.load_state_dict(torch.load(model_file))  

        open_img_dir = f'./{OKT}/static/img/{suffix + file.filename}'
        img = Image.open(open_img_dir)

        # 모델이 학습된 형태의 이미지로 변화 (전처리 같게끔)
        preprocessing = transforms.Compose([
            transforms.Resize((30, 30)),
            transforms.ToTensor(),
            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
        ])

        p_img = preprocessing(img)

        # -----------------------------------------
        # 모델 시연
        # -----------------------------------------
        model.eval()

        with torch.no_grad():
            p_img = p_img.unsqueeze(dim = 0)
            output = model(p_img)
            result = torch.argmax(output, dim=1).item()

        file_name = f'./{OKT}/static/img/labels.csv'
        import pandas as pd
        file = pd.read_csv(file_name)
        sign = file.iloc[result][1]

        # -----------------------------------------
        # browser에 show
        # -----------------------------------------
        # return (f"img : {img_tag}")
        # return (f"img : {img_tag} <br> result : {result}")
        return (f"img : {img_tag} <br> result : {result} <br> sign : {sign}")




