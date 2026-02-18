"""
EventFlow Analytics Dashboard - TPM Packet
Product OS War Room Simulation

This dashboard contains the "signal" buried across different tabs.
Teams must explore to find the hidden gems.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page config
st.set_page_config(
    page_title="EventFlow Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .big-metric {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 1rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    registration = pd.read_csv('data/registration_funnel.csv')
    tickets = pd.read_csv('data/support_tickets.csv')
    retention = pd.read_csv('data/feature_usage_retention.csv')
    segments = pd.read_csv('data/customer_segments.csv')
    return registration, tickets, retention, segments

registration_df, tickets_df, retention_df, segments_df = load_data()

# Header
st.title("📊 EventFlow Analytics Dashboard")
st.markdown("**Q4 2025 - Q1 2026 Product Analytics Report**")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Overview",
    "🔄 Registration Funnel",
    "🎫 Support Tickets",
    "💡 Feature Usage & Retention",
    "👥 Customer Segments"
])

# ============================================================================
# TAB 1: OVERVIEW (Vanity metrics - not much signal here)
# ============================================================================

with tab1:
    st.header("Overview - Key Metrics")
    st.markdown("High-level business metrics for EventFlow")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total ARR", "$80.0M", "+12% YoY")
    with col2:
        st.metric("Total Customers", "4,500", "+8% YoY")
    with col3:
        st.metric("Events Created (Q4)", "28,450", "+15% QoQ")
    with col4:
        st.metric("Overall NRR", "108%", "+3% YoY")

    st.markdown("---")

    # ARR by segment
    st.subheader("ARR Distribution by Segment")
    fig_arr = px.pie(
        segments_df,
        values='total_arr',
        names='segment',
        title="",
        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
    )
    st.plotly_chart(fig_arr, use_container_width=True, key="overview_arr_pie")

    # Monthly events trend (vanity metric)
    st.subheader("Monthly Events Created (Last 6 Months)")
    months = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
    events = [6200, 6500, 7100, 7300, 7450, 7600]

    fig_events = go.Figure()
    fig_events.add_trace(go.Scatter(
        x=months, y=events,
        mode='lines+markers',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10)
    ))
    fig_events.update_layout(
        xaxis_title="Month",
        yaxis_title="Events Created",
        showlegend=False
    )
    st.plotly_chart(fig_events, use_container_width=True, key="overview_events_trend")

    st.info("💡 Explore other tabs for detailed analytics on specific areas.")

# ============================================================================
# TAB 2: REGISTRATION FUNNEL (F04 - MOBILE SIGNAL IS HERE)
# ============================================================================

with tab2:
    st.header("Registration Funnel Analysis")
    st.markdown("Analyzing registration completion rates by device type")

    # Calculate aggregated metrics
    desktop_data = registration_df[registration_df['device'] == 'Desktop']
    mobile_data = registration_df[registration_df['device'] == 'Mobile']

    desktop_completion = (desktop_data['registrations_completed'].sum() /
                          desktop_data['registrations_started'].sum() * 100)
    mobile_completion = (mobile_data['registrations_completed'].sum() /
                         mobile_data['registrations_started'].sum() * 100)

    total_started = registration_df['registrations_started'].sum()
    mobile_traffic_pct = (mobile_data['registrations_started'].sum() / total_started * 100)

    # Key metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mobile Traffic %", f"{mobile_traffic_pct:.1f}%")
        st.caption("Percentage of registrations starting on mobile")
    with col2:
        st.metric("Desktop Completion Rate", f"{desktop_completion:.1f}%")
        st.caption("Desktop registration completion")
    with col3:
        st.metric("Mobile Completion Rate", f"{mobile_completion:.1f}%",
                  delta=f"{mobile_completion - desktop_completion:.1f}% vs Desktop",
                  delta_color="inverse")
        st.caption("Mobile registration completion")

    st.markdown("---")

    # THE SIGNAL: Mobile abandonment chart
    st.subheader("Registration Abandonment by Device")

    abandonment_comparison = pd.DataFrame({
        'Device': ['Desktop', 'Mobile'],
        'Abandonment Rate %': [100 - desktop_completion, 100 - mobile_completion],
        'Completion Rate %': [desktop_completion, mobile_completion]
    })

    fig_abandonment = go.Figure()
    fig_abandonment.add_trace(go.Bar(
        name='Abandonment Rate',
        x=abandonment_comparison['Device'],
        y=abandonment_comparison['Abandonment Rate %'],
        marker_color=['#2ca02c', '#d62728'],
        text=abandonment_comparison['Abandonment Rate %'].round(1),
        textposition='auto',
    ))

    fig_abandonment.update_layout(
        yaxis_title="Abandonment Rate (%)",
        showlegend=False,
        height=400
    )

    st.plotly_chart(fig_abandonment, use_container_width=True, key="registration_abandonment")

    # Call out the opportunity
    st.warning(f"""
    **Key Finding:** Mobile devices account for {mobile_traffic_pct:.0f}% of registration traffic
    but have a {100-mobile_completion:.1f}% abandonment rate compared to {100-desktop_completion:.1f}% on desktop.

    **Impact:** If mobile abandonment matched desktop rates, we would gain approximately
    **18,000+ additional registrations per month** across our customer base.
    """)

    # Trend over time
    st.subheader("Daily Registration Trends (Last 90 Days)")

    # Aggregate by date and device
    daily_by_device = registration_df.groupby(['date', 'device']).agg({
        'registrations_started': 'sum',
        'registrations_completed': 'sum'
    }).reset_index()

    fig_trend = px.line(
        daily_by_device,
        x='date',
        y='registrations_completed',
        color='device',
        title="",
        labels={'registrations_completed': 'Completions', 'date': 'Date'},
        color_discrete_map={'Desktop': '#2ca02c', 'Mobile': '#ff7f0e'}
    )

    st.plotly_chart(fig_trend, use_container_width=True, key="registration_trend")

    # Data table
    with st.expander("📊 View Detailed Data Table"):
        st.dataframe(
            abandonment_comparison.style.format({
                'Abandonment Rate %': '{:.1f}%',
                'Completion Rate %': '{:.1f}%'
            }),
            use_container_width=True
        )

# ============================================================================
# TAB 3: SUPPORT TICKETS (F05 - EVENT CLONING SIGNAL IS HERE)
# ============================================================================

with tab3:
    st.header("Support Ticket Analysis")
    st.markdown("Customer support ticket volume by feature category (2025)")

    # Filter Q4 data
    tickets_q4 = tickets_df[tickets_df['month'].isin(['2025-10', '2025-11', '2025-12'])]

    # Aggregate by category for Q4
    category_totals_q4 = tickets_q4.groupby('category')['ticket_count'].sum().reset_index()
    category_totals_q4 = category_totals_q4.sort_values('ticket_count', ascending=False)

    # Top 10 categories
    top_categories = category_totals_q4.head(10)

    st.subheader("Top 10 Support Ticket Categories (Q4 2025)")

    fig_tickets = go.Figure()
    fig_tickets.add_trace(go.Bar(
        x=top_categories['ticket_count'],
        y=top_categories['category'],
        orientation='h',
        marker_color='#1f77b4',
        text=top_categories['ticket_count'],
        textposition='auto',
    ))

    fig_tickets.update_layout(
        xaxis_title="Number of Tickets (Q4 2025)",
        yaxis_title="",
        height=500,
        yaxis={'categoryorder': 'total ascending'}
    )

    st.plotly_chart(fig_tickets, use_container_width=True, key="support_tickets_bar")

    # THE SIGNAL: Call out event cloning
    event_cloning_tickets = category_totals_q4[
        category_totals_q4['category'] == 'Event Cloning/Templates'
    ]['ticket_count'].values[0]

    st.warning(f"""
    **Key Finding:** Event Cloning/Templates requests generated **{event_cloning_tickets} support tickets in Q4 2025** -
    the 2nd highest category after general login/auth issues.

    **Context:** Customers are repeatedly asking for ability to duplicate events or save templates
    rather than rebuilding similar events from scratch each time.
    """)

    st.markdown("---")

    # Monthly trend for top categories
    st.subheader("Monthly Ticket Volume Trends")

    # Filter to show top 5 categories over time
    top_5_categories = category_totals_q4.head(5)['category'].tolist()
    tickets_top5 = tickets_df[tickets_df['category'].isin(top_5_categories)]

    fig_monthly = px.line(
        tickets_top5,
        x='month',
        y='ticket_count',
        color='category',
        title="",
        labels={'ticket_count': 'Tickets', 'month': 'Month'}
    )

    st.plotly_chart(fig_monthly, use_container_width=True, key="support_tickets_monthly")

    # Full data table
    with st.expander("📊 View Full Category Breakdown (Q4 2025)"):
        display_df = category_totals_q4.copy()
        display_df.columns = ['Category', 'Q4 2025 Tickets']
        st.dataframe(display_df, use_container_width=True, hide_index=True)

# ============================================================================
# TAB 4: FEATURE USAGE & RETENTION (F06 - THE GOLDEN CORRELATION)
# ============================================================================

with tab4:
    st.header("Feature Usage & Retention Analysis")
    st.markdown("Analyzing relationship between feature adoption and customer retention")

    # Calculate retention by analytics usage
    retention_df['analytics_user_type'] = retention_df['analytics_views_per_quarter'].apply(
        lambda x: 'High Usage (≥5 views)' if x >= 5 else 'Low Usage (<5 views)'
    )

    retention_by_analytics = retention_df.groupby('analytics_user_type').agg({
        'renewed': 'mean',
        'customer_id': 'count'
    }).reset_index()
    retention_by_analytics.columns = ['Analytics Usage', 'Retention Rate', 'Customer Count']
    retention_by_analytics['Retention Rate'] = retention_by_analytics['Retention Rate'] * 100

    # Key metrics
    col1, col2, col3 = st.columns(3)

    high_usage_retention = retention_by_analytics[
        retention_by_analytics['Analytics Usage'] == 'High Usage (≥5 views)'
    ]['Retention Rate'].values[0]

    low_usage_retention = retention_by_analytics[
        retention_by_analytics['Analytics Usage'] == 'Low Usage (<5 views)'
    ]['Retention Rate'].values[0]

    analytics_adoption = (retention_df['analytics_views_per_quarter'] >= 5).sum() / len(retention_df) * 100

    with col1:
        st.metric("High Analytics Users", f"{high_usage_retention:.1f}%")
        st.caption("Retention rate (≥5 analytics views/quarter)")
    with col2:
        st.metric("Low Analytics Users", f"{low_usage_retention:.1f}%",
                  delta=f"{low_usage_retention - high_usage_retention:.1f}% vs High",
                  delta_color="inverse")
        st.caption("Retention rate (<5 analytics views/quarter)")
    with col3:
        st.metric("Analytics Adoption Rate", f"{analytics_adoption:.1f}%")
        st.caption("% of customers with high analytics usage")

    st.markdown("---")

    # THE GOLDEN SIGNAL: Retention correlation chart
    st.subheader("Retention Rate by Analytics Usage Level")

    fig_retention = go.Figure()
    fig_retention.add_trace(go.Bar(
        x=retention_by_analytics['Analytics Usage'],
        y=retention_by_analytics['Retention Rate'],
        marker_color=['#d62728', '#2ca02c'],
        text=retention_by_analytics['Retention Rate'].round(1),
        texttemplate='%{text}%',
        textposition='auto',
    ))

    fig_retention.update_layout(
        yaxis_title="Retention Rate (%)",
        xaxis_title="",
        showlegend=False,
        height=400
    )

    st.plotly_chart(fig_retention, use_container_width=True, key="retention_by_analytics")

    # THE KILLER INSIGHT
    st.error(f"""
    **CRITICAL FINDING:** Customers who actively use analytics (≥5 views per quarter) have
    **{high_usage_retention:.0f}% retention** compared to **{low_usage_retention:.0f}% retention**
    for low-usage customers - a **{high_usage_retention - low_usage_retention:.0f} percentage point gap**.

    **Opportunity:** Only {analytics_adoption:.0f}% of customers are currently high analytics users.
    If we can improve analytics capabilities and drive adoption among the remaining {100-analytics_adoption:.0f}%,
    we could significantly improve overall retention.
    """)

    st.markdown("---")

    # Correlation by segment
    st.subheader("Retention Analysis by Customer Segment")

    retention_by_segment = retention_df.groupby(['segment', 'analytics_user_type']).agg({
        'renewed': 'mean',
        'customer_id': 'count'
    }).reset_index()
    retention_by_segment.columns = ['Segment', 'Analytics Usage', 'Retention Rate', 'Count']
    retention_by_segment['Retention Rate'] = retention_by_segment['Retention Rate'] * 100

    fig_segment = px.bar(
        retention_by_segment,
        x='Segment',
        y='Retention Rate',
        color='Analytics Usage',
        barmode='group',
        title="",
        color_discrete_map={
            'Low Usage (<5 views)': '#d62728',
            'High Usage (≥5 views)': '#2ca02c'
        }
    )

    st.plotly_chart(fig_segment, use_container_width=True, key="retention_by_segment")

    # Other features (weaker signals)
    st.subheader("Other Feature Usage Patterns")

    col1, col2 = st.columns(2)

    with col1:
        email_retention = retention_df.groupby('uses_email_personalization')['renewed'].mean() * 100
        st.metric("Email Personalization Impact",
                  f"+{email_retention[1] - email_retention[0]:.1f}%")
        st.caption("Retention lift from using email personalization")

    with col2:
        api_users = retention_df[retention_df['hits_api_rate_limit'] == 1]
        if len(api_users) > 0:
            api_impact = (api_users['renewed'].mean() - retention_df['renewed'].mean()) * 100
            st.metric("API Rate Limit Impact", f"{api_impact:.1f}%")
            st.caption(f"Impact on retention for {len(api_users)} customers hitting rate limits")

    # Data table
    with st.expander("📊 View Detailed Retention Data"):
        st.dataframe(retention_by_analytics, use_container_width=True, hide_index=True)

# ============================================================================
# TAB 5: CUSTOMER SEGMENTS (Supporting data)
# ============================================================================

with tab5:
    st.header("Customer Segment Breakdown")
    st.markdown("Overview of EventFlow customer base by segment")

    # Display segment table
    st.subheader("Segment Summary")

    display_segments = segments_df.copy()
    display_segments['avg_acv'] = display_segments['avg_acv'].apply(lambda x: f"${x:,.0f}")
    display_segments['total_arr'] = display_segments['total_arr'].apply(lambda x: f"${x:,.0f}")
    display_segments['retention_rate'] = display_segments['retention_rate'].apply(lambda x: f"{x:.0%}")

    display_segments.columns = [
        'Segment', 'Customers', 'Avg ACV', 'Total ARR',
        'Avg Events/Year', 'Primary Product', 'Retention'
    ]

    st.dataframe(display_segments, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Customer count by segment
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Customer Distribution")
        fig_customers = px.pie(
            segments_df,
            values='customer_count',
            names='segment',
            title="",
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
        )
        st.plotly_chart(fig_customers, use_container_width=True, key="segments_customer_pie")

    with col2:
        st.subheader("ARR Distribution")
        fig_arr_segment = px.pie(
            segments_df,
            values='total_arr',
            names='segment',
            title="",
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
        )
        st.plotly_chart(fig_arr_segment, use_container_width=True, key="segments_arr_pie")

    # Events per segment
    st.subheader("Average Events Per Year by Segment")

    fig_events_segment = go.Figure()
    fig_events_segment.add_trace(go.Bar(
        x=segments_df['segment'],
        y=segments_df['avg_events_per_year'],
        marker_color='#1f77b4',
        text=segments_df['avg_events_per_year'],
        textposition='auto',
    ))

    fig_events_segment.update_layout(
        xaxis_title="Segment",
        yaxis_title="Avg Events/Year",
        showlegend=False
    )

    st.plotly_chart(fig_events_segment, use_container_width=True, key="segments_events_bar")

# Footer
st.markdown("---")
st.markdown("**EventFlow Analytics Dashboard** | Q1 2026 Product Planning Exercise")
st.markdown("*For simulation purposes only - data is synthetic*")
