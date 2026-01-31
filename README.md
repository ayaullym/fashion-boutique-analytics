# Fashion Boutique Performance Analysis: Sales, Inventory & Returns

## Project Overview
This project analyzes sales performance, inventory health, discount behavior, and customer returns for a fashion boutique. The goal is to identify revenue risks, operational inefficiencies, and opportunities for inventory and pricing optimization using cleaned transactional data and interactive dashboards.

## Problem Statement
Fashion retailers often struggle to balance revenue growth, inventory availability, discount strategy, and customer experience. This project aims to uncover key drivers of sales performance, identify inventory risks, and understand return behavior to support data-driven business decisions.


## Tools & Technologies
- **Python** (pandas, numpy, scikit-learn) — data cleaning, feature engineering, ML-based imputation  
- **Tableau** — interactive dashboards, KPI tracking, exploratory analysis  
- **Data Analysis** — KPI definition, segmentation, business insight generation  



## Data Preparation & Advanced Imputation Strategy
Several data quality challenges were addressed to ensure reliable analysis:

- **Return reasons** were missing for non-returned purchases by design. These records were explicitly labeled as **“Not Returned”** to preserve business logic.
- **Customer ratings (~16.6% missing)** were imputed using a **supervised machine-learning approach** rather than mean imputation.
- A **Random Forest regression pipeline** was trained on existing ratings using product attributes, pricing, inventory levels, and return behavior as predictors.
- Predicted ratings were clipped to the valid range (1–5) and rounded for reporting consistency.
- Categorical gaps (e.g., missing size values) were handled using an explicit **“Unknown”** category.

This approach preserved relationships between variables and reduced bias introduced by simplistic imputation methods, resulting in a fully cleaned dataset suitable for analysis and visualization.


## Key Metrics
- **Total Revenue:** $186K  
- **Total Purchases:** 2,176  
- **Average Markdown:** 12.14%  
- **Average Discount:** $11.70  
- **Low Stock Items:** 244  
- **Return Rate:** 14.7%  
- **Average Customer Rating:** ~3.0  



## Key Insights

### Sales & Seasonality
Revenue remains relatively stable across seasons, with **Summer performing best** and **Winter slightly lower**, indicating mild seasonality rather than extreme demand swings.

### Inventory Health
A high number of low-stock items suggests potential **missed sales opportunities**, particularly in high-revenue categories where demand remains strong.

### Discount Strategy
Certain categories consistently require higher markdowns, signaling **pricing or demand-fit challenges** that may benefit from revised assortment or pricing strategies.

### Returns & Customer Experience
Returns are driven primarily by **size issues and quality concerns**, highlighting opportunities to improve product descriptions, sizing guidance, and quality control processes.



## Business Recommendations
- Prioritize restocking for **high-demand, low-stock categories** to reduce lost sales.
- Review pricing strategies for categories with **consistently high markdowns**.
- Improve sizing guidance and quality controls to **reduce return rates**.
- Use return-reason analysis to identify **brand-level operational issues** and supplier risks.



## Dashboards
Interactive dashboards were built in Tableau to explore sales, inventory, discounting, and return behavior across seasons, categories, and brands.

🔗 **Tableau Public Story:**  
https://public.tableau.com/views/Fashion-boutique-charts/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


## Assumptions & Limitations
- The dataset represents historical transactions from a single fashion boutique and may not generalize to all retail environments.
- Imputed customer ratings are predictive estimates and should be interpreted as approximations rather than direct customer feedback.
- Inventory levels are treated as static snapshots rather than real-time stock movements.

## Project Structure

- `data/` – raw transactional dataset  
- `notebooks/` – exploratory analysis and ML-based imputation  
- `outputs/` – cleaned datasets used for visualization  
- `src/` – reusable helper scripts for data loading and preprocessing  


