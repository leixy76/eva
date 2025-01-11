import os
import pandas as pd

def add_header_to_csv(folder_path):
    # 遍历指定文件夹
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # 确保处理的是CSV文件
            file_path = os.path.join(folder_path, filename)
            # 读取CSV文件，假设没有header
            df = pd.read_csv(file_path, header=None)

            # 随机抽取10%
            sample_df = df.sample(frac=0.1)

            # 保存到新的CSV文件
            sample_df.to_csv('val/' + filename.replace('_test.csv', '_val.csv'), index=False)
            print('<file>mmlu-exam/val/' + filename.replace('_test.csv', '_val.csv') + '</file>')
            

# 调用函数，传入你的文件夹路径
folder_path = 'test'
add_header_to_csv(folder_path)
