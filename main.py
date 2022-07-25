# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot
import datetime

def main():
    # Streamlit が対応している任意のオブジェクトを可視化する (ここでは文字列)
    st.title('Streamlit Title')
    st.write('2022-07-25 Ryo Takashima')

    df = pd.read_csv("C:/Users/1487006/python/Streamlit_TEST/csv_data.csv")# , encoding = "shift-jis")
    df = df.sort_values(['ファンド名','取得日時'])
    
    fand = df["ファンド名"].unique()
    
    col = df.columns # 列名を取得する

    fig = pyplot.figure() # フィギュアの作成
    ax = fig.add_subplot(1, 1, 1) # フィギュアにグラフを追加

    for i in range(len(fand)): # ファンドの種類すべてで繰り返す
        print(fand[i]) # ファンド名の確認
        data = df[(df['ファンド名'] == fand[i])]
        np_data = data.reset_index().values
        ax.plot(np_data[:,11],np_data[:,8] , label=fand[i])
        
    ax.legend(bbox_to_anchor=(0, 0.2), loc='upper left', borderaxespad=0, fontsize=6, prop = {"family" : "Meiryo"})
    ax.set_title("評価額推移", fontname = 'Meiryo')
    #ax.set_xticklabels(np_data[:,11], rotation= 90)
    # ax.set_xticks(rotation=90)
    ax.set_ylabel("評価額[円]", fontname ='Meiryo')
    ax.set_xlabel("取得日時", fontname ='Meiryo')
    #ax.set_ylim(['5,000','25,000'])
    ax.grid(True) # (5)目盛線表示
    
    st.pyplot(fig)
    
    
if __name__ == '__main__':
    main()
