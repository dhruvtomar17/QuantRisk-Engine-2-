# QuantRisk Engine 2.0 🚀
### High-Frequency Volatility Forecasting with LightGBM

This repository contains a quantitative pipeline designed to predict realized volatility across 112 equities. By leveraging market microstructure features, this model achieved a **41.97% improvement** over the naive baseline.

## 📊 Key Highlights
- **Mathematical Edge:** Utilized **Weighted Average Price (WAP)** and **Log Returns** to filter noise from the Limit Order Book (LOB).
- **Architecture:** Gradient Boosted Decision Trees (LightGBM) optimized for RMSE.
- **Result:** Significant reduction in prediction error compared to traditional historical volatility models.

## 🛠️ Feature Engineering
- **WAP Calculation:** $$WAP = \frac{BidPrice_1 \cdot AskSize_1 + AskPrice_1 \cdot BidSize_1}{BidSize_1 + AskSize_1}$$
- **Realized Volatility:** Computed as the square root of the sum of squared log returns over 10-minute windows.
