## 计算相关系数矩阵， 分析股票特征的相关性
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_corre_matrix(ticker):
    # 读取数据
    stock_file = f'{ticker}_data.csv'
    data = pd.read_csv(stock_file, parse_dates=['Date'])
    data['MA_5'] = data['Adj Close'].rolling(window=5).mean()
    data['MA_10'] = data['Adj Close'].rolling(window=10).mean()
    data['MA_20'] = data['Adj Close'].rolling(window=20).mean()
    data['RSI'] = 100 - (100 / (1 + data['Adj Close'].pct_change().rolling(window=14).mean() / data['Adj Close'].pct_change().rolling(window=14).std()))
    data['Bollinger_Upper'] = data['Adj Close'].rolling(window=20).mean() + 2 * data['Adj Close'].rolling(window=20).std()
    data['Bollinger_Lower'] = data['Adj Close'].rolling(window=20).mean() - 2 * data['Adj Close'].rolling(window=20).std()

        
    # 移除非数值列
    data_numeric = data.drop(columns=['Date', 'Ticker'])
        
    # 计算相关性矩阵（使用Pearson相关系数）
    correlation_matrix = data_numeric.corr(method='pearson')
        
    # 可视化相关性矩阵
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Pearson Correlation Matrix for {ticker}')
    plt.show()