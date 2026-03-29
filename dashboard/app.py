import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# =========================
# 🎨 PREMIUM CSS
# =========================
st.markdown("""
<style>
body {
    background-color: #0b0f1a;
    color: #e5e7eb;
}

.block-container {
    padding-top: 1.5rem;
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: 600;
    margin-bottom: 20px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 40px;
}

.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1f2937;
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #7c3aed;
}

.section {
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 📥 LOAD DATA
# =========================
df = pd.read_csv("../data/cleaned_data.csv")
rfm = pd.read_csv("../data/rfm_data.csv")

# =========================
# 🎯 HEADER
# =========================
st.markdown('<div class="title">E-commerce Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Business Intelligence • Customer Segmentation • Revenue Insights</div>', unsafe_allow_html=True)

# =========================
# 🎛 FILTERS (UPDATED)
# =========================
st.sidebar.title("Filters")

# Add "All" option
year_options = ["All"] + sorted(df['order_year'].unique().tolist())
state_options = ["All"] + sorted(df['customer_state'].unique().tolist())

year = st.sidebar.selectbox("Year", year_options)
state = st.sidebar.selectbox("State", state_options)

# Apply filters dynamically
filtered_df = df.copy()

if year != "All":
    filtered_df = filtered_df[filtered_df['order_year'] == year]

if state != "All":
    filtered_df = filtered_df[filtered_df['customer_state'] == state]

# =========================
# 🔢 KPI ROW
# =========================
col1, col2, col3 = st.columns(3)

col1.markdown(f'<div class="card">Revenue<br><span class="metric">{filtered_df["total_price"].sum():,.0f}</span></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="card">Orders<br><span class="metric">{filtered_df["order_id"].nunique()}</span></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="card">Customers<br><span class="metric">{filtered_df["customer_unique_id"].nunique()}</span></div>', unsafe_allow_html=True)

# =========================
# 📊 SECTION 1
# =========================
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    monthly = filtered_df.groupby('order_month')['total_price'].sum().reset_index()
    fig = px.line(monthly, x='order_month', y='total_price')
    fig.update_traces(mode='lines+markers')
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Revenue trend over months")
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    cities = filtered_df.groupby('customer_city')['total_price'].sum().reset_index().sort_values(by='total_price', ascending=False).head(10)
    fig = px.bar(cities, x='customer_city', y='total_price')
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Top revenue-generating cities")
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    products = filtered_df['product_category_name'].value_counts().reset_index().head(10)
    products.columns = ['category', 'count']
    fig = px.bar(products, x='category', y='count')
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Most popular product categories")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 📊 SECTION 2
# =========================
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
col7, col8 = st.columns(2)

with col7:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    cluster_counts = rfm['cluster'].value_counts().reset_index()
    cluster_counts.columns = ['cluster', 'count']

    cluster_labels = {
        0: "Low Value",
        1: "Regular",
        2: "Frequent Buyers",
        3: "High Value"
    }

    cluster_counts['segment'] = cluster_counts['cluster'].map(cluster_labels)

    fig = px.pie(cluster_counts, values='count', names='segment')
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Customer segmentation distribution")

    st.info("High value customers contribute significantly more revenue despite lower volume.")

    st.markdown('</div>', unsafe_allow_html=True)

with col8:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    sample_size = min(1000, len(filtered_df))
    sample_df = filtered_df.sample(sample_size)

    fig = px.scatter(sample_df, x="price", y="total_price")
    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)
    st.caption("Relationship between price and total revenue")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 📥 DOWNLOAD SECTION
# =========================
st.markdown('<div class="section"></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Export Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download Filtered Dataset", csv, "data.csv")

st.markdown('</div>', unsafe_allow_html=True)