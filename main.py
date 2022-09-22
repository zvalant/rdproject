import pandas as pd
from fpdf import FPDF
projects = pd.read_csv("C:\\Users\\Zac\\Desktop\\files\\R&D Items Due.csv", keep_default_na=False)
pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option("display.max_rows", 3000)
pd.set_option("display.max_columns", 3000)
active_demand = {}
print(projects)
for i in range(len(projects)):
    idx = 0
    idx_pn = 0
    pns = []
    qtys = []
    if projects["Due Date"][i] != "":
        while i+idx_pn < len(projects) and (projects["Due Date"] [i+idx_pn] == projects["Due Date"][i] or projects["Due Date"][i+idx_pn] == ""):
            pns.append(projects["Part Number"][i+idx_pn])
            qtys.append(projects["QTY"][i+idx_pn])
            idx_pn+=1
        while projects["Machine"][i-idx] == "":
            idx +=1
        if projects["Machine"][i-idx] + " " + projects["Due Date"][i] not in active_demand:
            active_demand[projects["Machine"][i-idx] + " " + projects["Due Date"][i]] = [pns,qtys]
        else:
            for j in range(len(pns)):
                active_demand[projects["Machine"][i-idx] + " " + projects["Due Date"][i]][0].append(pns[j])
                active_demand[projects["Machine"][i - idx] + " " + projects["Due Date"][i]][1].append(qtys[j])
print(active_demand)
#generate pdfs for active projects
for i in active_demand:
    pdf = FPDF(orientation="P", unit="pt", format="Letter")
    pdf.add_page()
    pdf.set_font(family="Times", style="B",size=24)
    pdf.multi_cell(w=0, h=50, txt=str(i))
    for j in range(len(active_demand[i][0])):
        pdf.set_font(family="Times", style="B",size=18)
        pdf.multi_cell(w=0,h=50, txt="        " + str(active_demand[i][0][j]) + " (" + str(active_demand[i][1][j]) + "X)")
    filename = i.replace("/", "-")
    pdf.output(f"C:\\Users\\Zac\\Desktop\\files\\rdproject\\{filename}.pdf")
# generate email including pdf for project

