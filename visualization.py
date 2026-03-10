import plotly.express as px

def warehouse_delay_chart(df):

    avg_delay = df.groupby("warehouse")["shipping_delay"].mean().reset_index()

    fig = px.bar(
        avg_delay,
        x="warehouse",
        y="shipping_delay",
        title="Average Shipping Delay per Warehouse"
    )

    return fig


def product_speed_chart(df):

    speed = df.groupby("product")["processing_time"].mean().reset_index()

    fig = px.bar(
        speed,
        x="product",
        y="processing_time",
        title="Product Shipping Speed"
    )

    return fig