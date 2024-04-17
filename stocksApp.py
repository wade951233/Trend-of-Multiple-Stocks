import webbrowser
from threading import Timer
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import plotly.graph_objs as go

app = Dash(__name__)
# 定義技術指標計算函數
def calculate_moving_average(data, window):
    return data.rolling(window=window).mean()

# 應用的佈局，包括搜尋框、技術指標選擇器和圖表元件
app.layout = html.Div([
    dcc.Input(id='search-box', type='text', placeholder='Enter stock tickers separated by comma...', style={'width': '400px'}),
    dcc.Dropdown(
        id='indicator-selector',
        options=[
            {'label': 'Month Moving Average (30 days)', 'value': 'MMA30'},
            {'label': 'Quarter Moving Average (90 days)', 'value': 'QMA90'},
            {'label': 'Year Moving Average (250 days)', 'value': 'YMA250'},
            {'label': 'Five Year Moving Average (1250 days)', 'value': 'FIVEYMA1250'},
            {'label': 'Ten Year Moving Average (2500 days)', 'value': 'TENYMA2500'}
        ],
        value=['YMA250'],  # Default value
        multi=True,  # Allow multiple selections
        style={'width': '400px'}
    ),
    dcc.Graph(id='stock-chart'),
])

@app.callback(
    Output('stock-chart', 'figure'),
    [Input('search-box', 'value'),
     Input('indicator-selector', 'value')]
)
def update_graph(search_value, selected_indicators):
    """
    根據搜尋框和技術指標選擇器的輸入更新圖表。
    
    :param search_value: 從搜尋框輸入的股票代碼，用逗號分隔
    :param selected_indicators: 選擇的技術指標列表
    :return: 更新的圖表對象
    """
    tickers = search_value.split(',') if search_value else []  # 解析股票代碼
    fig = go.Figure()  # 創建新的圖表
    for ticker in tickers:
        ticker = ticker.strip()  # 清除多餘空格
        if ticker:  # 如果股票代碼非空
            stock = yf.Ticker(ticker)  # 獲取股票對象
            hist_data = stock.history(period='max')  # 取得最大時間範圍的歷史數據
            close = hist_data['Close']
            fig.add_trace(go.Scatter(x=hist_data.index, y=close, mode='lines', name=ticker))

            # 加入選擇的技術指標
            if 'MMA30' in selected_indicators:
                mma30 = calculate_moving_average(close, 30)
                fig.add_trace(go.Scatter(x=hist_data.index, y=mma30, mode='lines', name=f'{ticker} 30d MA'))

            if 'QMA90' in selected_indicators:
                qma90 = calculate_moving_average(close, 90)
                fig.add_trace(go.Scatter(x=hist_data.index, y=qma90, mode='lines', name=f'{ticker} 90d MA'))

            if 'YMA250' in selected_indicators:
                yma250 = calculate_moving_average(close, 250)
                fig.add_trace(go.Scatter(x=hist_data.index, y=yma250, mode='lines', name=f'{ticker} 250d MA'))

            if 'FIVEYMA1250' in selected_indicators:
                fiveyma1250 = calculate_moving_average(close, 1250)
                fig.add_trace(go.Scatter(x=hist_data.index, y=fiveyma1250, mode='lines', name=f'{ticker} 1250d MA'))

            if 'TENYMA2500' in selected_indicators:
                tenyma2500 = calculate_moving_average(close, 2500)
                fig.add_trace(go.Scatter(x=hist_data.index, y=tenyma2500, mode='lines', name=f'{ticker} 2500d MA'))

    fig.update_layout(title='Stock Data Comparison', xaxis_title='Date', yaxis_title='Close Price')
    return fig

def open_browser():
      webbrowser.open_new("http://127.0.0.1:8050/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=False, use_reloader=False)
