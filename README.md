# 比較各股走勢(Trend-of-Multiple-Stocks)
Clone 程式並進入資料夾
```
git clone https://github.com/wade951233/Trend-of-Multiple-Stocks.git
cd Trend-of-Multiple-Stocks
```

1. 創建環境
```
python3 -m venv Multiple-Stocks-env
```
2. 激活環境
```
[windows]
Set-ExecutionPolicy Unrestricted -Scope Process
.\Multiple-Stocks-env\Scripts\activate

[macos]
source Multiple-Stocks-env/bin/activate
```
3. 安裝套件
```
pip install -r requirements.txt
```
4. 打包成執行檔
```
pyinstaller --onefile --noconsole stocksApp.py
```

## 執行畫面
輸入：006208.TW,00631L.TW
![image](https://github.com/wade951233/Trend-of-Multiple-Stocks/assets/54468254/0a3dc047-d466-4dd9-ada0-e9790ed068d9)

![image](https://github.com/wade951233/Trend-of-Multiple-Stocks/assets/54468254/6f05f915-beaf-4827-9977-04236f130f44)
