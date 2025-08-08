import streamlit as st

# Page setup
st.set_page_config(page_title="Chart World", page_icon="📊", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>📊 Welcome to Chart World</h1>
    <p style='text-align: center; font-size:18px; color: grey;'>
    Explore interactive visualizations and analyze your product sales data in style 🚀
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

st.write("### 📌 App Overview")
st.markdown("""
This dashboard contains multiple interactive charts to help you explore and understand your product sales data.
Click on **Preview Chart** buttons below to jump directly to the chart view.
""")

# List of charts with descriptions
chart_pages = [
    ("Dashboard", "📑 View the complete sales data table.", "dataframe.py"),
    ("Pie Chart", "🥧 Shows product sales as percentage shares.", "pie.py"),
    ("Sunburst Chart", "🌞 Category & product breakdown in a hierarchical layout.", "sunburst.py"),
    ("Scatter Plot", "🎯 Price vs Quantity relationship with sales as color intensity.", "scatter.py"),
    ("Line Chart", "📈 Trend of sales across products.", "line.py"),
    ("Bar Chart", "📊 Compare sales across products.", "bar.py"),
    ("Stacked Bar Chart", "📊 Category-wise sales stacked by product.", "stacked_bar.py"),
    ("Area Chart", "📉 Cumulative sales trend by product.", "area_chart.py"),
    ("Treemap Chart", "📦 Visualize category-product sales in a tree structure.", "treemap.py"),
    ("Histogram", "📊 Distribution of sales values.", "histogram.py"),
    ("Box Plot", "🔍 Price variation and outliers by category.", "boxplot.py")
]

# Chart summary cards
for title, desc, file in chart_pages:
    with st.container():
        st.markdown(f"#### {title}")
        st.write(desc)
        if st.button(f"▶ Preview {title}", key=title):
            st.switch_page(file)
        st.markdown("---")

# Footer
st.markdown("<p style='text-align: center; color: grey;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
