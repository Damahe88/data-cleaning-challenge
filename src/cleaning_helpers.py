def clean_postcodes(df, column_name='postcode'):
    """Eliminates decimal notation of postcodes

    Returns the dataframe with postcode as string without decimal point and filled with leading zero to a total of five digits.

    Parameters:
    df :            pandas DataFrame
    column_name:    str
                    name of the postcode column. Default='postcode'
    
    Returns:
    pandas DataFrame
    
    Notes:
    Currently only a decimal point for splitting is implemented
    """

    postcodes_as_strings = df[column_name].astype('str')
    postcodes_without_decimal = [postcode.split('.')[0].zfill(5)  if '.' in postcode else postcode.zfill(5) for postcode in postcodes_as_strings]
    df[column_name] = postcodes_without_decimal
    
    return df


def match_postcodes_to_bundesland(df, bundesland='bundesland', postcode='postcode'):
    """Matches missing values in bundesland based on bundesland/postcode pair that already appear in the data

    Returns the dataframe with values filled in bundesland where applicable

    Parameters:
    df:             pandas Dataframe
    bundesland:     str
                    column name that contains bundeslaender
    postcodes:      str
                    column name that contains postcodes
    
    Returns:
    pandas DataFrame
    """

    bundesland_without_nan = df[(df[bundesland].notna())]
    postcode_bundesland_dict = dict(set(zip(bundesland_without_nan[postcode],bundesland_without_nan[bundesland])))

    copy_of_dataframe = df.copy()
    copy_of_dataframe[bundesland] = copy_of_dataframe.bundesland.fillna(copy_of_dataframe.postcode.map(postcode_bundesland_dict))

    return copy_of_dataframe