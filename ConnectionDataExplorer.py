# Import 3rd Party Libraries
import pandas as pd
import matplotlib.pyplot as plt

def main():

    '''Pandas Manipulation Example'''

    # Set display limits and large width for better readability
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)

    # Load the CSV file into a DataFrame
    df = pd.read_csv("IP-CONNECT.csv")
    print("\nColumns in Dataframe:\n", df.columns)

    # Display the first 10 rows of the DataFrame
    print("\nSample Dataframe:")
    print(df.head(10))

    # Filter out ipV6 Rows
    df = df[df.ipV6 == 0]
    print("\n",df.head(10))
    
    # List of columns to pair with 'CONNECTION'
    columns_to_pair = ['TOTAL', 'TCP', 'UDP', 'ARP', 'ICMP', 'IGMP', 'CAST', 'INTERNAL', 'DOMESTIC', 'FOREIGN', 'HOSTILE']

    # Loop over the columns and create paired DataFrames
    for col in columns_to_pair:
        # Create a new DataFrame with 'CONNECTION' and the current column
        df_pair = pd.DataFrame([df.CONNECTION, df[col]]).transpose()
        print(f"\nPaired DataFrame (CONNECTION vs {col}):")
        print(df_pair.head(10))

        '''
        Setup for plotting the results
        '''
        
        colNdx = df_pair.columns
        # Plot the paired DataFrame as a horizontal bar chart
        plt.figure(figsize=(10, 6))
        plt.barh(df_pair[colNdx[0]], df_pair[colNdx[1]], color='blue')
        plt.xlabel(f'{col} OBSERVATIONS')
        plt.ylabel('CONNECTION')
        plt.title(f'CONNECTION vs {col}')
        plt.show()

# Main Program Starts Here
#===================================

if __name__ == '__main__':
    main()