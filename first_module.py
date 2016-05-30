import requests
import pandas
from bokeh.plotting import figure


def quandl(symbol, start_date='2000-01-01'):
    # Get data and transform it into a python object (dict)
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=XQKAhbrdid5hNyDptPBx&start_date=%s'
    response = requests.get(url % (symbol, start_date))
    json = response.json()
    
    # Create variables to refer to the data we are interested in
    dataset = json['dataset']
    data = dataset['data']
    columns = dataset['column_names']
    
    # Create dataframe out of the data
    df = pandas.DataFrame(data, columns=columns)
    
    # Transform the Date column from str into an actual date type
    df['Date'] = pandas.to_datetime(df['Date'])
    
    # Use the Date column as index
    df = df.set_index('Date')
    return df


def plot(history, title='Market history', adj_closing=True, closing=False,
         adj_opening=False, opening=False):
    # Create the figure canvas 
    f = figure(title=title,
          x_axis_label='Date',
          x_axis_type='datetime',
          y_axis_label='Price')
    
    # Plot the line in the figure
    if adj_closing == True:
        f.line(x = history.index, y = history['Adj. Close'],
               color='green', legend='Adj. Close')
    if closing == True:
        f.line(x = history.index, y = history['Close'],
               color='blue', legend='Close')
    if adj_opening == True:
        f.line(x = history.index, y = history['Adj. Open'],
               color='red', legend='Adj. Open')
    if opening == True:
        f.line(x = history.index, y = history['Open'],
               color='yellow', legend='Open')

    return f
    
