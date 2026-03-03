from django.shortcuts import render

# Create your views here.
import pandas as pd
from .dashboard import pivot_table,visualize_treemap,visualize_map
from .dashboard import frequency_table,group_table,crosstab,crosstab_multi,visualize_sunburst
def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    df = pd.DataFrame(queryset)
    return render(request, "vehicles/index.html", {
    "frequency_table": frequency_table(df),
    "group_tables":group_table(df),
    "cross_tables":crosstab(df),
    "cross_tables_multi":crosstab_multi(df),
    "pivot_tables":pivot_table(df),
    "sunburst":visualize_sunburst(df,height=800),
    "treemap":visualize_treemap(df,height=800),
    "map":visualize_map(df,height=800)
    })
