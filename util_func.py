import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import warnings



def unlimit_columns_and_rows(max_columns:int =None, max_rows:int=None) -> None:
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.max_rows', max_rows) 
    return None


# Parameter 없을 시 시스템에 설치된 폰트 경로 출력 후 현재 폰트 확인
# Parameter 사용 시 폰트 경로 지정 후 현재 폰트 확인
# font_setter("C:/Windows/Fonts/malgun.ttf")  # Windows 예시
def font_setter(font_path:str=None) -> None:
    if font_path is None:
        for font in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
            if "Gothic" in font or "gulim" in font.lower():
                print(font)

    else:
        fontprop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = fontprop.get_name()
        plt.rcParams['axes.unicode_minus'] = False

    print("현재 설정된 font.family:", plt.rcParams['font.family'])
    print("폰트 파일 경로:", font_path)
    return None


def ignore_warnings() -> None:
    warnings.filterwarnings('ignore')
    return None