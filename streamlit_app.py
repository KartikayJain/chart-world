import streamlit as st

pages = {
    "Home and Dataframe": [
        st.Page("home.py", title="Home"),
        st.Page("dataframe.py", title="Dashboard"),
    ],
    "Charts": [
        st.Page("pie.py", title="Pie Chart"),
        st.Page("sunburst.py", title="Sunburst Chart"),
        st.Page("scatter.py", title="Scatter Chart"),
        st.Page("line.py", title="Line Chart"),
        st.Page("bar.py", title="Bar Chart"),
        st.Page("stacked_bar.py", title="Stacked Bar Chart"),
        st.Page("area_chart.py", title="Area Chart"),
        st.Page("treemap.py", title="Treemap Chart"),
        st.Page("histogram.py", title="Histogram"),
        st.Page("boxplot.py", title="Box Plot"),
    ],
}

pg = st.navigation(pages)
pg.run()
