import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def maesyorikun(in_csv_pass,out_csv_pass):
  def visualize_dataframe(df):
      # Display basic statistics of the dataframe
      print("Basic statistics of the dataframe:")
      print(df.describe())

      # Draw histograms for numeric columns
      numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
      for column in numeric_columns:
          plt.figure(figsize=(8, 6))
          sns.histplot(df[column], bins=20, kde=True)
          plt.title(f'Distribution of {column}')
          plt.xlabel(column)
          plt.ylabel('Frequency')
          plt.show()

      # Draw count plots for categorical columns
      categorical_columns = df.select_dtypes(include=['object']).columns
      for column in categorical_columns:
          plt.figure(figsize=(8, 6))
          sns.countplot(data=df, x=column)
          plt.title(f'Count of {column}')
          plt.xlabel(column)
          plt.ylabel('Count')
          plt.xticks(rotation=45)
          plt.show()

        # Compute correlation matrix for numeric columns
      numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
      correlation_matrix = df[numeric_columns].corr()

      # Visualize correlation matrix as heatmap
      plt.figure(figsize=(10, 8))
      sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
      plt.title('Correlation between numeric columns')
      plt.show()


  def detect_outliers(df, columns, threshold=3):
      outliers = pd.DataFrame()
      for column in columns:
          z_scores = (df[column] - df[column].mean()) / df[column].std()
          column_outliers = df[abs(z_scores) > threshold]
          outliers = pd.concat([outliers, column_outliers])
      return outliers


  def analyze_csv(in_csv_path,out_csv_pass):
      # Specify the input file
      df = pd.read_csv(in_csv_path)

      # Display the number of columns
      num_columns = len(df.columns)
      print(f"Number of columns: {num_columns}")

      # Display the data types of each column
      print("Data types of each column:")
      for column in df.columns:
          print(f"{column}: {df[column].dtype}")

              # Prompt for data type modification
      for column in df.columns:
          print(f"\nModify the data type of {column}?")
          action = input("(Modify/Keep as is): ").strip().lower()
          if action == 'modify':
              print(f"Available data types: {['float64', 'int64', 'object']}")
              new_dtype = input(f"Select the new data type for {column}: ").strip().lower()
              # Convert data type
              try:
                  df[column] = df[column].astype(new_dtype)
                  print(f"The data type of {column} has been converted to {new_dtype}.")
              except ValueError as e:
                  print(f"Error: {e}")
                  print(f"Unable to convert the data type of {column}.")


        # Check for missing values
      print("\nChecking for missing values:")
      missing_values = df.isnull().sum()
      for column in df.columns:
          print(f"{column}: {missing_values[column]} missing values")

      # Display rows with missing values
      print("\nRows with missing values:")
      rows_with_missing = df[df.isnull().any(axis=1)]
      if rows_with_missing.empty:
          print("No rows with missing values.")
      else:
          print(rows_with_missing)

          # Select the processing method for numeric columns with missing values
      for column in df.columns:
          if df[column].dtype == 'float64' or df[column].dtype == 'int64':
              if missing_values[column] > 0:
                  print(f"\nColumn '{column}' has {missing_values[column]} missing values.")
                  action = input(f"What would you like to do with this column? (Fill with mean/Fill with mode/Manually input/Delete/Keep as is): ").strip().lower()
                  if action == 'fill with mean':
                      mean_value = df[column].mean()
                      df[column].fillna(mean_value, inplace=True)
                  elif action == 'fill with mode':
                      mode_value = df[column].mode()[0]
                      df[column].fillna(mode_value, inplace=True)
                  elif action == 'manually input':
                      for index, row in rows_with_missing.iterrows():
                          if pd.isnull(row[column]):
                              fill_value = input(f"Enter the value to fill the missing value in column {column} of row {index}: ")
                              df.at[index, column] = fill_value
                  elif action == 'delete':
                      df = df.dropna(subset=[column])
                  elif action == 'keep as is':
                      pass  # Do nothing

      for column in df.columns:
          if df[column].dtype == 'object':
              print(f"\nColumn '{column}' has {missing_values[column]} missing values.")
              action = input(f"What would you like to do with this column? (Manually input/Delete/Keep as is): ").strip().lower()
              if action == 'manually input':
                  for index, row in rows_with_missing.iterrows():
                      if pd.isnull(row[column]):
                          fill_value = input(f"Enter the value to fill the missing value in column {column} of row {index}: ")
                          df.at[index, column] = fill_value
              elif action == 'delete':
                  df = df.dropna(subset=[column])
              elif action == 'keep as is':
                  pass  # Do nothing



      numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

      # Detect outliers
      outliers = detect_outliers(df, columns=numeric_columns, threshold=2.5)

      if outliers.empty:
          print("No outliers found.")
      else:
          print("Outliers found:")
          print(outliers)

          for index, row in outliers.iterrows():
              print(f"\nModify the outlier in row {index}?")
              action = input("(Modify/Keep as is/Delete): ").strip().lower()
              if action == 'modify':
                  for column in numeric_columns:
                      if abs((row[column] - df[column].mean()) / df[column].std()) > 2.5:
                          print(f"Select how to modify the outlier in column {column} of row {index}:")
                          method = input("(Modify with mean/Modify with mode/Manually input): ").strip().lower()
                          if method == 'modify with mean':
                              new_value = df[column].mean()
                          elif method == 'modify with mode':
                              new_value = df[column].mode()[0]
                          elif method == 'manually input':
                              new_value = float(input(f"Enter the value to replace the outlier in column {column} of row {index}: "))
                          df.at[index, column] = new_value
              elif action == 'delete':
                  df = df.drop(index)
              elif action == 'keep as is':
                pass  # Do nothing

      visualize_dataframe(df)


      # Save the preprocessed data
      df.to_csv(out_csv_pass, index=False)
      print(f"Preprocessed data saved to {out_csv_pass}.")


  analyze_csv(in_csv_pass,out_csv_pass)
