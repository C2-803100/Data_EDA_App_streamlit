# import streamlit
import streamlit as st
import os

# EDA Pkgs
import pandas as pd

# visualization pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
    """ Common ML dataset Explorer """
    st.title(" Common ML Data-set Explorer")
    st.subheader(" simple Data Science Explorer with Streamlit")
    html_temp = """
    <div style = "background-color:tomato;"><p style = 'color:white;font-size:50px'>Streamlit is Awesome</p></div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('select a file',filenames)
        return os.path.join(folder_path,selected_filename)

    filename = file_selector()
    st.info("your selected {}".format(filename))

    # Read Dataset
    df = pd.read_csv(filename)

    # Show data
    if st.checkbox("show dataset"):
        number = st.number_input("number of rows to views", 5, 10)
        st.dataframe(df.head(number))

    # show columns
    if st.button('Column Names'):
        st.write(df.columns)

    # show Shape
    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show Dimension By ",("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim == 'Columns':
            st.text('Number of Columns')
            st.write(df.shape[1])
        else:
            st.write(df.shape)

    # Select Columns
    if st.checkbox("Select Columns to Show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("select",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    # show values
    if st.button("value counts"):
        st.text("value counts by target/class")
        st.write(df.iloc[:,-1].value_counts())

    # show Datatypes
    if st.button("data type"):
        st.text("data type")
        st.write(df.dtypes)

    # show summary
    if st.checkbox("summary"):
        st.write(df.describe().T)

    # show plot and viz

    st.subheader("data visualization")
    # correlation
    # seaborn plot
    if st.checkbox("Correlation plot[seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()


    # pie chat
    if st.checkbox("pie plot"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate plot"):
            st.success("Generating a pie plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct='%1.1f%'))
            st.pyplot()

    # count plot
    if st.checkbox("Plot of value counts"):
        st.text("value counts by target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("primary column to GroupBy",all_columns_names)
        selected_columns_names = st.multiselect('select columns',all_columns_names)
        if st.button('plot'):
            st.text('Generate plot')
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot
    # customizable plot

    st.subheader("customizable plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select type of plot",['area','bar','line','hist','box',"kde"])
    selected_columns_names = st.multiselect('select columns to plot',all_columns_names)

    if st.button("Generate plot"):
        st.success("Generate Customizable plot of {} for {}".format(type_of_plot,selected_columns_names))

    #plot by streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

# Custome plot
        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()


if __name__ == '__main__':
    main()

