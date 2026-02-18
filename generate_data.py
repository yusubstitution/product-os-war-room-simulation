"""
Generate synthetic data for EventFlow Analytics Dashboard
This creates realistic-looking data with intentional patterns for the simulation.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# ============================================================================
# 1. REGISTRATION FUNNEL DATA (F04 - Mobile Registration Signal)
# ============================================================================

def generate_registration_funnel():
    """
    Generate registration funnel data showing mobile abandonment issue.
    SIGNAL: 62% mobile traffic, 51% mobile abandonment vs 28% desktop
    """
    data = []

    # Generate daily data for last 90 days
    for day in range(90):
        date = datetime.now() - timedelta(days=90-day)
        date_str = date.strftime('%Y-%m-%d')

        # Desktop data - lower traffic, better conversion
        desktop_started = np.random.randint(800, 1200)
        desktop_completed = int(desktop_started * np.random.uniform(0.70, 0.75))  # 72-75% completion

        data.append({
            'date': date_str,
            'device': 'Desktop',
            'registrations_started': desktop_started,
            'registrations_completed': desktop_completed,
            'abandonment_rate': round((1 - desktop_completed/desktop_started) * 100, 1)
        })

        # Mobile data - higher traffic, worse conversion
        mobile_started = np.random.randint(1400, 2000)  # 62% of total traffic
        mobile_completed = int(mobile_started * np.random.uniform(0.47, 0.52))  # 48-52% completion

        data.append({
            'date': date_str,
            'device': 'Mobile',
            'registrations_started': mobile_started,
            'registrations_completed': mobile_completed,
            'abandonment_rate': round((1 - mobile_completed/mobile_started) * 100, 1)
        })

    df = pd.DataFrame(data)
    df.to_csv('data/registration_funnel.csv', index=False)
    print("✓ Generated registration_funnel.csv")
    return df

# ============================================================================
# 2. SUPPORT TICKET DATA (F05 - Event Cloning Signal)
# ============================================================================

def generate_support_tickets():
    """
    Generate support ticket data showing high volume for event cloning requests.
    SIGNAL: 247 tickets in Q4 about event cloning/templates
    """

    # Define ticket categories and their volumes
    categories = [
        # Hidden Gem signals
        ('Event Cloning/Templates', 247, 'high'),  # F05 - THE SIGNAL
        ('Mobile Registration Issues', 89, 'high'),  # F04 - Supporting signal
        ('Analytics/Reporting Requests', 134, 'medium'),  # F06 - Supporting signal

        # Trap signals (low volume, but will be loud in Sales packet)
        ('Custom Mobile App Requests', 3, 'low'),  # F01 - Trap
        ('Networking Features', 12, 'low'),  # F02 - Trap
        ('AI Content Generation', 5, 'low'),  # F03 - Trap

        # Defensible features
        ('Email Personalization', 45, 'medium'),  # F08
        ('Multi-Currency Support', 28, 'medium'),  # F09
        ('Speaker Portal Issues', 34, 'medium'),  # F10
        ('Capacity/Waitlist Automation', 19, 'low'),  # F11
        ('API Rate Limits', 15, 'low'),  # F07

        # Bad ideas (very low)
        ('VR/AR Features', 0, 'none'),  # F12
        ('Payment Processing Issues', 4, 'low'),  # F13 (but about Stripe, not wanting custom)
        ('Gamification Requests', 6, 'low'),  # F14

        # General noise
        ('Login/Authentication', 156, 'high'),
        ('Event Page Loading', 98, 'medium'),
        ('Email Delivery', 112, 'medium'),
        ('Integration Issues', 67, 'medium'),
        ('Billing Questions', 43, 'low'),
    ]

    data = []
    for category, q4_volume, priority in categories:
        # Generate monthly breakdown for full year (Q1-Q4)
        for month in range(1, 13):
            # Q4 (Oct-Dec) = months 10-12
            if month >= 10:
                # This is Q4 - use the specified volume
                monthly_volume = q4_volume // 3 + np.random.randint(-5, 5)
            else:
                # Q1-Q3 - slightly lower volume
                monthly_volume = int((q4_volume // 3) * 0.85) + np.random.randint(-3, 3)

            monthly_volume = max(0, monthly_volume)  # No negative tickets

            data.append({
                'month': f'2025-{month:02d}',
                'category': category,
                'ticket_count': monthly_volume,
                'priority': priority
            })

    df = pd.DataFrame(data)
    df.to_csv('data/support_tickets.csv', index=False)
    print("✓ Generated support_tickets.csv")
    return df

# ============================================================================
# 3. FEATURE USAGE & RETENTION DATA (F06 - Analytics Correlation Signal)
# ============================================================================

def generate_feature_usage_retention():
    """
    Generate feature usage data correlated with retention.
    SIGNAL: Customers who use analytics ≥5 times/quarter have 95% retention vs 73%
    """

    data = []

    # Generate 500 customers with usage patterns
    for customer_id in range(1, 501):
        # Determine customer segment
        if customer_id <= 200:
            segment = 'Enterprise'
            base_retention = 0.90
        elif customer_id <= 400:
            segment = 'Mid-Market'
            base_retention = 0.80
        else:
            segment = 'SMB'
            base_retention = 0.65

        # Analytics usage (the golden feature - F06)
        analytics_views_per_quarter = np.random.choice(
            [0, 1, 3, 7, 15, 25],
            p=[0.35, 0.15, 0.19, 0.15, 0.10, 0.06]  # 69% use <5 times (opportunity!)
        )

        # High analytics usage = much better retention
        if analytics_views_per_quarter >= 5:
            retention_boost = 0.15  # 95% retention
        else:
            retention_boost = -0.07  # 73% retention

        # Email personalization usage (F08 - moderate signal)
        uses_email_personalization = np.random.choice([0, 1], p=[0.65, 0.35])
        email_boost = 0.03 if uses_email_personalization else -0.02

        # API usage (F07 - weak signal, only enterprise)
        if segment == 'Enterprise':
            api_calls_per_month = np.random.randint(100, 5000)
            hits_rate_limit = 1 if api_calls_per_month > 3500 else 0
            api_boost = -0.05 if hits_rate_limit else 0
        else:
            api_calls_per_month = 0
            hits_rate_limit = 0
            api_boost = 0

        # Events per month (usage indicator)
        if segment == 'Enterprise':
            events_per_month = np.random.randint(8, 20)
        elif segment == 'Mid-Market':
            events_per_month = np.random.randint(3, 12)
        else:
            events_per_month = np.random.randint(1, 8)

        # Calculate final retention (with noise)
        retention_probability = base_retention + retention_boost + email_boost + api_boost
        retention_probability = np.clip(retention_probability + np.random.normal(0, 0.03), 0, 1)
        renewed = 1 if np.random.random() < retention_probability else 0

        data.append({
            'customer_id': f'CUST-{customer_id:04d}',
            'segment': segment,
            'events_per_month': events_per_month,
            'analytics_views_per_quarter': analytics_views_per_quarter,
            'uses_email_personalization': uses_email_personalization,
            'api_calls_per_month': api_calls_per_month,
            'hits_api_rate_limit': hits_rate_limit,
            'renewed': renewed,
            'retention_probability': round(retention_probability, 3)
        })

    df = pd.DataFrame(data)
    df.to_csv('data/feature_usage_retention.csv', index=False)
    print("✓ Generated feature_usage_retention.csv")
    return df

# ============================================================================
# 4. CUSTOMER SEGMENT DATA
# ============================================================================

def generate_customer_segments():
    """
    Generate customer segment breakdown data.
    """

    data = [
        {
            'segment': 'Enterprise',
            'customer_count': 200,
            'avg_acv': 250000,
            'total_arr': 50000000,
            'avg_events_per_year': 80,
            'primary_product': 'EventFlow Pro',
            'retention_rate': 0.95
        },
        {
            'segment': 'Mid-Market',
            'customer_count': 800,
            'avg_acv': 35000,
            'total_arr': 28000000,
            'avg_events_per_year': 35,
            'primary_product': 'EventFlow Pro (60%), EventFlow Live (40%)',
            'retention_rate': 0.80
        },
        {
            'segment': 'SMB',
            'customer_count': 3500,
            'avg_acv': 5000,
            'total_arr': 17500000,
            'avg_events_per_year': 12,
            'primary_product': 'EventFlow Live',
            'retention_rate': 0.70
        }
    ]

    df = pd.DataFrame(data)
    df.to_csv('data/customer_segments.csv', index=False)
    print("✓ Generated customer_segments.csv")
    return df

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("Generating synthetic data for EventFlow simulation...")
    print()

    generate_registration_funnel()
    generate_support_tickets()
    generate_feature_usage_retention()
    generate_customer_segments()

    print()
    print("✓ All data files generated successfully!")
    print()
    print("Generated files:")
    print("  - data/registration_funnel.csv")
    print("  - data/support_tickets.csv")
    print("  - data/feature_usage_retention.csv")
    print("  - data/customer_segments.csv")
