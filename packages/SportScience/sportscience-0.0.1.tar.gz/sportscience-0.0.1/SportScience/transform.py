#fucntions to be exported
__all__ = ['long_format', 'wide_format', 'min_std_format', 'plot_progression']
#preprocesing files to feed them in to the other functions

def hd_cmj(file_path, file_name):
    """
    Reads a Hawkin Dynamics CMJ file, transforms it from wide to long format, 
    and returns the transformed DataFrame.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.

    Returns:
        pandas.DataFrame: The transformed DataFrame in long format.
    """
    import pandas as pd
    import numpy as np

    # Reading and transforming csv_file
    df = pd.read_csv(file_path + file_name, parse_dates=['Date'])

    # Converting 'Time' column to string type
    df = df.astype({'Time': 'string'})

    # Replacing specific values in the 'Tags' column
    df['Tags'] = df['Tags'].replace({np.nan: 'Two legged', 'fast': 'Two legged', 'high': 'Two legged'})

    # Dropping specific columns
    drop_columns = ['TestId', 'Segment', 'Position', 'Excluded']
    df.drop(drop_columns, axis=1, inplace=True)

    # Adding equipment and renaming columns
    df['Equipment'] = 'Hawkin Dynamics Force Plates'
    df.rename(columns={'Type': 'Test'}, inplace=True)

    # Transforming wide to long format
    id_vars = np.append(df.columns[0:5], df.columns[-1])
    df = pd.melt(df, id_vars=id_vars, var_name='metric', value_name='value')

    return df

def forcedecks(file_path, file_name, test):
    """
    Reads a Vald Force Decks file, transforms it from wide to long format, 
    and returns the transformed DataFrame.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.
        test (str): The type of test performed (either 'imtp' or 'cmj').

    Returns:
        pandas.DataFrame: The transformed DataFrame in long format.
    """
    import pandas as pd
    import numpy as np
    
    # Reading and transforming the raw CSV file
    try:
        df = pd.read_csv(file_path + file_name, parse_dates=['Date'])
    except:
        df = pd.read_csv(file_path + file_name)
    if 'Athlete' in df.columns:
        df.rename(columns={'Device': 'Equipment', 'Test Type': 'Test', 'Athlete': 'Name', 'Test Date': 'Date'}, inplace=True)
        df.Date = pd.to_datetime(df.Date).dt.date
        drop = ['Unnamed: 0', 'Athlete Id', 'Date of Birth', 'Gender', 'Athlete Notes', 'Test Notes', 'Test Parameters',  'Trial']
        #Dropping columns
        df = df.drop(drop, axis=1)

    else:
        # Dropping columns
        df.rename(columns={'Device': 'Equipment', 'Test Type': 'Test'}, inplace=True)
        df = df.drop(['ExternalId', 'Time', 'Reps'], axis=1)
    
    # Adding equipment and tag information
    df['Equipment'] = "Force Decks"
    if test == 'imtp':
        # Creating a tag column for consistency with other files
        df['Tags'] = ''
        df['Test'] = 'IMTP'

    elif test == 'cmj':
        df['Tags'] = 'CMJ'
    
    # Applying the convert_assymmetries function to all columns
    for column in df.columns:
        try:   
            df[column] = df[column].apply(convert_assymmetries)
        except:
            pass
    
    # Defining the id_vars for the long format
    id_vars = ['Date', 'Name', 'Equipment', 'Test', 'Tags']
    
    # Transforming wide to long format
    df = pd.melt(df, id_vars=id_vars, var_name='metric', value_name='value')
    
    return df

def nordbord(file_path, file_name):
    """
    Reads a Nordbord testing file, transforms it from wide to long format,
    and returns the transformed DataFrame.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.

    Returns:
        pandas.DataFrame: The transformed DataFrame in long format.
    """
    import pandas as pd
    import numpy as np

    # Reading and transforming the raw CSV file
    df = pd.read_csv(file_path + file_name)

    # Ensure 'Date UTC' is a datetime object without timezone information
    df['Date UTC'] = pd.to_datetime(df['Date UTC'], utc=True)

    # Parse 'Time UTC' and combine with 'Date UTC' to create a new 'Date and Time' column
    df['Time UTC'] = pd.to_datetime(df['Time UTC'], format='%I:%M %p', utc=True).dt.time

    # Step 3: Combine 'Date UTC' and 'Time UTC' into a new 'Date and Time' column
    df['Date and Time'] = pd.to_datetime(df['Date UTC'].astype(str) + ' ' + df['Time UTC'].astype(str))
    df['Date and Time'] = df['Date and Time'].dt.tz_convert('America/Los_Angeles')

    # Convert 'Date and Time' to UTC timezone, then convert to Pacific Time
    df['Date UTC'] = df['Date and Time'].dt.date
    df['Time UTC'] = df['Date and Time'].dt.time

    # Renaming columns
    df.rename(columns={'Date UTC': 'Date', 'Device': 'Equipment'}, inplace=True)

    # Dropping columns
    df = df.drop(['ExternalId', 'Time UTC', 'L Reps', 'R Reps', 'Notes', 'Date and Time'], axis=1)

    # Creating a tag column for consistency with other files
    df['Tags'] = 'hamstring'

    # Defining the id_vars for the long format
    id_vars = np.append(df.columns[0:4], df.columns[-1])

    # Getting long format
    df = pd.melt(df, id_vars=id_vars, var_name='metric', value_name='value')

    return df




def convert_assymmetries(value):
    """
    Convert asymmetry values from a string to a float.

    Args:
        value (str): The value to convert. The string should be in the format
                     'NUMBER L' or 'NUMBER R'.

    Returns:
        float: The converted value. Negative values indicate asymmetry on the
               left side, positive values indicate asymmetry on the right side.
    """
    # Split the string into number and letter
    number, letter = value.strip().split(' ')

    # Convert the number to a float
    number = float(number)

    # Check if the letter is 'L', indicating asymmetry on the left side
    if letter == 'L':
        return -number
    # If the letter is 'R', indicating asymmetry on the right side
    return number



def long_format(file_name,
                equipment,
                test,
                brand = '',
                file_path = '',
                included_up_to_trials=3, 
                dropnull=False, 
                save=False, 
                get_best_std=True, 
                ):
    """
    Reads a Hawkin Dynamics CMJ file, transforms it from wide to long format, 
    aggregates the best trials for each testing session, computes mean and std, 
    calculates CV%, and saves the result to a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.
        included_up_to_trials (int, optional): The number of best trials to include for each testing session. Defaults to 3.
        dropnull (bool, optional): Whether to drop rows with null values. Defaults to True.
        save (bool, optional): Whether to save the result to a CSV file. Defaults to False.
        get_best_std (bool, optional): Whether to get the minimal std for each metric and include it in the result. Defaults to True.

    Returns:
        pandas.DataFrame: The transformed DataFrame in long format.
    """
    
    #conditional format for selecting the right function depending on brand and test performed
    
    if (equipment == 'force plates') & (brand == 'hawkindynamics') & (test == 'jumps'):
        df = hd_cmj(file_path, file_name)

    elif (equipment == 'force decks') & (brand == 'vald'):
        df = forcedecks(file_path, file_name, test)
    
    
    elif (equipment == 'nordbord'):
        df = nordbord(file_path, file_name)
        
    else:
        ValueError('Please provide a valid equipment, brand and/or test combination')

    #aggregating best trials for each testing session and computing the mean and std
    df = df.groupby(['Date', 'Name', 'Equipment', 'Test', 'Tags', 'metric'])['value'].nlargest(included_up_to_trials).reset_index().drop('level_6', axis=1)
    df = df.groupby(['Date', 'Name', 'Equipment', 'Test', 'Tags', 'metric']).agg({'value': ['mean', 'std']}).reset_index()
    #removing multiindex columns
    df.columns = df.columns.map(', '.join).str.strip(', ')
    df.rename(columns={'value, mean': 'mean', 'value, std': 'std'}, inplace=True)

    #calculating the CV%
    df['CV%'] = df['std'] / df['mean'] * 100

    if dropnull:
        df = df.dropna()

    if get_best_std:
        #getting a df with the minimal std for each metric and getting the matching date and cv%
        minimal_std = df.groupby(['Name','Equipment', 'Test', 'Tags', 'metric'])['std'].min().reset_index().dropna()
        minimal_std = minimal_std.merge(df, on=['Name','Equipment', 'Test', 'Tags', 'metric', 'std'], how='left')
        minimal_std = minimal_std.drop('mean', axis=1)
        minimal_std.set_index(['Date', 'Name', 'Equipment', 'Test', 'Tags'], inplace=True)
        minimal_std = minimal_std.reset_index()

        df.drop(['std', 'CV%'], axis=1, inplace=True)
        df.rename(columns={'Date': 'test_date'}, inplace=True)
        minimal_std.rename(columns={'Date': 'variation_est_date'}, inplace=True)
        df = df.merge(minimal_std, on=['Name', 'Equipment', 'Test', 'Tags', 'metric'], how='left')

    #saving files
    if save:
        df.to_csv(f'{file_name.split(".")[0]}_long_format_summary_output.csv', index=False)

    return df


def wide_format(file_name, #GETTING WIDE FORMAT
           equipment,
           test,
            brand = '',
            file_path = '',
           dropnull = True,
           save = False):
    """
    Transforms a CSV file in long format to wide format and aggregates the values.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.
        dropnull (bool, optional): Whether to drop rows with null values. Defaults to True.
        save (bool, optional): Whether to save the result to a CSV file. Defaults to False.

    Returns:
        pandas.DataFrame: The transformed DataFrame in wide format.

    """
    df = long_format(file_path=file_path, file_name = file_name, equipment=equipment, brand=brand, test=test, dropnull = dropnull, save = save, get_best_std=False)
    df = df.set_index(['Date', 'Name', 'Equipment', 'Test', 'Tags'])
    
    # Pivot the DataFrame to wide format and aggregate the values
    df_wide = df.pivot_table(index=df.index.names, columns='metric', values='mean', aggfunc='mean')
    df_wide.reset_index(inplace=True)   
    #saving files

    if save:
        df_wide.to_csv(f'{file_name.split(".")[0]}_wide_format_summary_output.csv', index=False)
        
    return df_wide    
    
    
def min_std_format(file_name,
           equipment,
           test,
            brand = '',
            file_path = '',
           dropnull = True,
           save = False): 
    """
    Gets the minimal std for each metric and computes the best date for each subject, equipment, test, tag, and metric. It also computes the CV% for that date.

    Args:
        file_path (str): The path to the CSV file.
        file_name (str): The name of the CSV file.
        dropnull (bool, optional): Whether to drop rows with null values. Defaults to True.
        save (bool, optional): Whether to save the result to a CSV file. Defaults to False.

    Returns:
        pandas.DataFrame: The DataFrame with the minimal std for each metric and the corresponding date and CV%.
    """
    
    # Get the long-format data with the best trials for each testing session
    df = long_format(file_path=file_path, file_name = file_name, equipment=equipment, brand=brand, test=test, dropnull = dropnull, save = save, get_best_std=False)
    
    # Get a DataFrame with the minimal std for each metric
    minimal_std = df.groupby(['Name','Equipment', 'Test', 'Tags', 'metric'])['std'].min().reset_index().dropna()
    
    # Merge the minimal std DataFrame with the original data to get the matching date and CV%
    minimal_std = minimal_std.merge(df, on=['Name','Equipment', 'Test', 'Tags', 'metric', 'std'], how='left')
    minimal_std = minimal_std.drop('mean', axis=1)
    minimal_std.set_index(['Date', 'Name', 'Equipment', 'Test', 'Tags'], inplace=True)
    minimal_std = minimal_std.reset_index()
    
    # Saving files
    if save:
        minimal_std.to_csv(f'{file_name.split(".")[0]}_minimal_std.csv', index=False)
        
    return minimal_std







def plot_progression(data, subject, metric, tag):
    import matplotlib.pyplot as plt
    import seaborn as sns
    """
    Plots the progression of a subject's mean and std over time for a given metric and tag.

    Args:
        data (pandas.DataFrame): The long-format data.
        subject (str): The subject's name.
        metric (str): The metric to plot.
        tag (str): The tag to plot.

    Returns:
        None
    """
    """
    Filters the data to only include the given subject, tag, and metric, and plots the progression of
    the mean and std over time.
    """
    filtered_data = data.loc[(data['Name'] == subject) & (data['Tags'] == tag) & (data['metric'] == metric)]

    """
    Creates a figure and axis for the plot, with a size of 10x6 inches and a dpi of 100.
    """
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

    """
    Plots the mean values over time using a black line.
    """
    try:
        ax.plot(filtered_data['test_date'], filtered_data['mean'], color='#e60010', alpha=0.5)
    except:
        filtered_data = filtered_data.rename(columns={'Date': 'test_date'})
        ax.plot(filtered_data['test_date'], filtered_data['mean'], color='#e60010', alpha=0.5)
    """
    Plots the std values over time using error bars. The error bars are colored red and have a
    capsize of 5.
    """
    ax.errorbar(filtered_data['test_date'], filtered_data['mean'], yerr=filtered_data['std'], fmt='o', capsize=5, color='#e60010', alpha=0.5)

    """
    Plots horizontal lines matching the error bars, with a transparency of 0.05. This is used to
    visualize the range of values.
    """
    for index, row in filtered_data.iterrows():
        """
        Calculates the lower and upper bounds of the error bar.
        """
        lower_bound = row['mean'] - row['std']
        upper_bound = row['mean'] + row['std']

        """
        Plots the horizontal lines.
        """
        ax.fill_between([row['test_date'], filtered_data['test_date'].max()], lower_bound, upper_bound, color='#e60010', alpha=0.05)

        """
        Adds a text annotation to the plot, showing the mean value at the time of testing.
        """
        ax.text(row['test_date'], round(row['mean'], 3), round(row['mean'], 3), ha='center', va='bottom')

    """
    Sets the title of the plot to include the subject, tag, and test.
    """
    ax.set_title(f'{subject} {tag} {filtered_data.Test.unique()[0]}')

    """
    Sets the x and y labels of the plot.
    """
    ax.set_xlabel('Date')
    ax.set_ylabel(f'Mean {metric}')

    """
    Rotates the x-axis tick labels by 45 degrees.
    """
    ax.tick_params(axis='x', rotation=45)

    """
    Adjusts the layout of the plot to fit all the elements.
    """
    plt.tight_layout()

    """
    Shows the plot.
    """
    plt.show()



