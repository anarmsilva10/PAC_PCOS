from tkinter import*
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import plotly.graph_objects as go
from PIL import Image, ImageTk
import io

#leitura da base de dados e remoção das primeiras duas colunas e da última coluna
data = pd.read_csv (r'PCOS_data.csv')
data.drop(columns=["Sl. No","Patient File No.","Unnamed: 44"], inplace=True)
dados = pd.DataFrame(data)

#informação sobre as variáveis
dados.info()

#converter para numéricos
dados["AMH(ng/mL)"] = pd.to_numeric(dados["AMH(ng/mL)"], errors="coerce") 
dados["II    beta-HCG(mIU/mL)"] = pd.to_numeric(dados["II    beta-HCG(mIU/mL)"], errors="coerce") 

dados.head()

#procurar NAs
lst_missing_columns = dados.columns[dados.isna().any()].tolist()

#preencher os NAs como a média
for x in lst_missing_columns:
    dados[x] = dados[x].fillna(dados[x].median())

#verificar novamente se há NAs
dados.columns[dados.isna().any()].tolist()

#criação do menu e suas funcionalidades
interface = Tk()
interface.title("Síndrome do Ovário Policístico")
interface.iconbitmap('images/image.ico')
interface.geometry("550x550")

message = """
    Caro(a) utilizador(a),
    Seja Bem-vindo(a).

    A Síndrome do Ovário Policístico (PCOS) é um distúrbio endócrino-ginecológico 
    que afeta muitas mulheres em idade fértil.

    Neste programa dispomos um menu interativo onde poderá:
     -> Verificar médias, máximos e mínimos de diferentes parâmetros
     -> Visualizar gráficos que mostram a relação entre diferentes parâmetros
     -> Observar tabelas que mostram a frequência de diferentes parâmetros
     -> Avaliar a sua situação clínica (será criado um pdf com a avaliação)
    Carregando nos botões abaixo representados, conseguirá navegar pelo menu.
    Esperamos que este programa esteja do seu agrado e que 
    consiga explorar alguns parâmetros relacionados com esta patologia.

    Saudações!
    """

############## Parâmetros ##################

def parametros():
    pit =Toplevel()
    pit.title("Parâmetros")
    pit.iconbitmap('images/image.ico')
    pit.geometry("350x350")

    filtradosim = dados[dados['PCOS (Y/N)'] == 1]
    filtradonao = dados[dados['PCOS (Y/N)'] == 0]

    def display_table(fig):
        img_uso = fig.to_image(format="png")
        img = Image.open(io.BytesIO(img_uso))

        image_window = tk.Toplevel(pit)
        image_window.title("Tabela")
        image_window.iconbitmap('images/image.ico')

        img = ImageTk.PhotoImage(img)
        panel = Label(image_window, image=img)
        panel.image = img
        panel.pack(expand=True, fill='both')

    def idade():
        mean_sim = filtradosim[' Age (yrs)'].mean()
        max_sim = filtradosim[' Age (yrs)'].max()
        min_sim = filtradosim[' Age (yrs)'].min()
        
        mean_nao = filtradonao[' Age (yrs)'].mean()
        max_nao = filtradonao[' Age (yrs)'].max()
        min_nao = filtradonao[' Age (yrs)'].min()

        fig = go.Figure(data=[go.Table(header=dict(
            values=['PCOS', 'média', 'máximo', 'mínimo'],
            line_color='black', fill_color='salmon',
            align='center',font=dict(color='black', size=12)
            ),cells=dict(
                values=[['Sim', 'Não'],['{:.2f}'.format(mean_sim),'{:.2f}'.format(mean_nao)],[ max_sim, max_nao],[min_sim,min_nao]],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
                ))
                ])
        
        fig.update_layout(
        title="Análise da Idade em relação há presença/ausência de doença",
        title_font=dict(color="black",size=14))

        display_table(fig)

    def mens():
        mean_sim_ciclo = filtradosim['Cycle length(days)'].mean()
        max_sim_ciclo = filtradosim['Cycle length(days)'].max()
        min_sim_ciclo = filtradosim['Cycle length(days)'].min()

        mean_nao_ciclo = filtradonao['Cycle length(days)'].mean()
        max_nao_ciclo = filtradonao['Cycle length(days)'].max()
        min_nao_ciclo = filtradonao['Cycle length(days)'].min()
        
        fig1=go.Figure(data=[go.Table(header=dict(
            values=['PCOS', 'média', 'máximo', 'mínimo'],
            line_color='black', fill_color='salmon',
            align='center',font=dict(color='black', size=12)
            ),cells=dict(
                values=[['Sim', 'Não'],['{:.2f}'.format(mean_sim_ciclo),'{:.2f}'.format(mean_nao_ciclo)],[ max_sim_ciclo, max_nao_ciclo],[min_sim_ciclo,min_nao_ciclo]],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
                ))
                ])
        
        fig1.update_layout(
        title="Análise da Duração da menstruação em relação há presença/ausência de doença (em dias)",
        title_font=dict(color="black",size=14))

        display_table(fig1)

    def glu():
        mean_sim_glu = filtradosim['RBS(mg/dl)'].mean()
        max_sim_glu = filtradosim['RBS(mg/dl)'].max()
        min_sim_glu = filtradosim['RBS(mg/dl)'].min()

        mean_nao_glu = filtradonao['RBS(mg/dl)'].mean()
        max_nao_glu = filtradonao['RBS(mg/dl)'].max()
        min_nao_glu = filtradonao['RBS(mg/dl)'].min()

        fig2=go.Figure(data=[go.Table(header=dict(
            values=['PCOS', 'média', 'máximo', 'mínimo'],
            line_color='black', fill_color='salmon',
            align='center',font=dict(color='black', size=12)
            ),cells=dict(
                values=[['Sim', 'Não'],['{:.2f}'.format(mean_sim_glu),'{:.2f}'.format(mean_nao_glu)],[ max_sim_glu, max_nao_glu],[min_sim_glu,min_nao_glu]],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
                ))
                ])
        
        fig2.update_layout(
        title="Análise da Glucose em relação há presença/ausência de doença (em mg/dl)",
        title_font=dict(color="black",size=14))

        display_table(fig2)

    def fol():
        follicle_parameters = {
        'Follicle No. (L)': 'Esquerdo',
        'Follicle No. (R)': 'Direito'
        }

        ovary_sides = []
        parameter_types = []
        sim_values = []
        nao_values = []

        for parameter, ovary_side in follicle_parameters.items():
            mean_sim = filtradosim[parameter].mean()
            max_sim = filtradosim[parameter].max()
            min_sim = filtradosim[parameter].min()

            mean_nao = filtradonao[parameter].mean()
            max_nao = filtradonao[parameter].max()
            min_nao = filtradonao[parameter].min()

            ovary_sides.extend([ovary_side, ovary_side, ovary_side])
            parameter_types.extend(['Média', 'Máximo', 'Mínimo'])
            sim_values.extend(['{:.2f}'.format(mean_sim), '{:.2f}'.format(max_sim), '{:.2f}'.format(min_sim)])
            nao_values.extend(['{:.2f}'.format(mean_nao), '{:.2f}'.format(max_nao), '{:.2f}'.format(min_nao)])

        fig3=go.Figure(data=[go.Table(header=dict(
            values=['Ovário', 'Parâmetro', 'PCOS:Não', 'PCOS:Sim'],
            line_color='black', fill_color='salmon',
            align='center', font=dict(color='black', size=12)),
            cells=dict(
                values=[ovary_sides, parameter_types, nao_values, sim_values],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11))
        )])

        fig3.update_layout(title="Análise do Número de folículos em relação à presença/ausência de doença",title_font=dict(color="black",size=14))

        display_table(fig3)

    def hormona():
        hormone_parameters = {
            'AMH(ng/mL)': 'AMH',
            'TSH (mIU/L)': 'TSH',
            'FSH(mIU/mL)': 'FSH',
            'LH(mIU/mL)': 'LH',
            'PRG(ng/mL)': 'PRG'
        }

        hormones = []
        parameter_types = []
        sim_values = []
        nao_values = []

        for parameter, hormone in hormone_parameters.items():
            mean_sim = filtradosim[parameter].mean()
            max_sim = filtradosim[parameter].max()
            min_sim = filtradosim[parameter].min()

            mean_nao = filtradonao[parameter].mean()
            max_nao = filtradonao[parameter].max()
            min_nao = filtradonao[parameter].min()

            hormones.extend([hormone] * 3)
            parameter_types.extend(['Média', 'Máximo', 'Mínimo'])
            sim_values.extend(['{:.2f}'.format(mean_sim), '{:.2f}'.format(max_sim), '{:.2f}'.format(min_sim)])
            nao_values.extend(['{:.2f}'.format(mean_nao), '{:.2f}'.format(max_nao), '{:.2f}'.format(min_nao)])

        fig4 = go.Figure(data=[go.Table(
            header=dict(
                values=['Hormona', 'Parâmetro', 'PCOS:Não', 'PCOS:Sim'],
                line_color='black', fill_color='salmon',
                align='center', font=dict(color='black', size=12)),
            cells=dict(
                values=[hormones, parameter_types, nao_values, sim_values],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11))
        )])

        fig4.update_layout(
        title="Análise de diferentes hormonas em relação há presença/ausência de doença",
        title_font=dict(color="black",size=14),
        width=800, height=600)

        display_table(fig4)

    pit.grid_columnconfigure(0, weight=1)
    pit.grid_columnconfigure(1, weight=1)
    pit.grid_columnconfigure(2, weight=1)
    pit.grid_columnconfigure(3, weight=1)
    pit.grid_columnconfigure(4, weight=1)
    pit.grid_columnconfigure(5, weight=1)

    var1 = tk.Button(pit, text="Idade", command=idade, padx=50, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=1, column=0, columnspan=5)

    var2 = tk.Button(pit, text="Duração da menstruação", command=mens, padx=3, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=2, column=0, columnspan=5)

    var3 = tk.Button(pit, text="Glucose", command=glu, padx=43, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=3, column=0, columnspan=5)

    var4 = tk.Button(pit, text="Tamanho dos Foliculos", command=fol, padx=8, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=4, column=0, columnspan=5)

    var5 = tk.Button(pit, text="Hormonas", command=hormona, padx=38, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=5, column=0, columnspan=5)

    var_quit = tk.Button(pit, text="Voltar ao menu", command=pit.destroy, padx=26, pady=10, bg="mistyrose",font=('calibri', 10), relief="groove").grid(row=6, column=0, columnspan=5)

############## Gráficos ##################

def graficos():
    tip =Toplevel()
    tip.title("Gráficos")
    tip.iconbitmap('images/image.ico')
    tip.geometry("430x500")

    colors = {0: 'lightcoral', 1: 'maroon'}
    filtrado = dados[dados['PCOS (Y/N)'] == 1]

    def didade():
        fig=sns.histplot(data=filtrado, x=" Age (yrs)", hue="PCOS (Y/N)", element='step', multiple="dodge", palette=colors,edgecolor='black', legend=False)
        plt.title('Distribuição da Idade na PCOS', fontsize=14, fontweight='bold')
        plt.xlabel('Idade')
        plt.ylabel('Frequência')

        plt.show()

    def vitD():
        axes = dados.boxplot(column='Vit D3 (ng/mL)', by='PCOS (Y/N)', figsize=(10,5),
                   whis=[5,95], return_type='axes', showfliers=False,patch_artist = True,
                   boxprops = dict(facecolor = "mistyrose"), medianprops = dict(color = "salmon", linewidth = 1),
                   whiskerprops = dict(color = "black", linewidth = 1.5))
        
        plt.suptitle('')
        plt.title('Vitamina D entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.subplots_adjust(wspace=0.25)
        plt.ylabel('Vit D3 (ng/mL)')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Não', 'Sim'])

        plt.show()

    def FSHLH():
        axes = dados.boxplot(column='FSH/LH', by='PCOS (Y/N)', figsize=(10,5),
                   whis=[5,95], return_type='axes', showfliers=False,patch_artist = True,
                   boxprops = dict(facecolor = "mistyrose"), medianprops = dict(color = "salmon", linewidth = 1),
                   whiskerprops = dict(color = "black", linewidth = 1.5))

        plt.suptitle('')    
        plt.title('Rácio FSH/LH entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.subplots_adjust(wspace=0.25)
        plt.ylabel('FSH/LH')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Não', 'Sim'])
        
        plt.show()

    def abortos():
        sns.histplot(data=dados, x="No. of abortions", hue="PCOS (Y/N)", element='step', multiple = "dodge",
                     palette=colors,  legend=False)
        
        plt.title('Número de abortos entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.legend(title='PCOS', labels=['Não Doentes', 'Doentes'],loc='upper right', fontsize=10, ncol=1)
        plt.ylabel('Contagem')
        plt.xlabel('Número de abortos')
        
        plt.show()

    def ciclo():
        sns.histplot(data=dados, x="Cycle length(days)", hue="PCOS (Y/N)", element='step', multiple = "dodge",
                     palette=colors,  legend=False)
        
        plt.title('Duração da menstrução entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.legend(title='PCOS', labels=['Não Doentes', 'Doentes'], loc='upper right', fontsize=10, ncol=1)
        plt.ylabel('Contagem')
        plt.xlabel('Duração da menstruação (dias)')
        
        plt.show()

    def AMHLH():      
        sns.relplot(data=filtrado, x="AMH(ng/mL)", y="LH(mIU/mL)", color="maroon", legend=False)
        
        plt.title('Relação entre AMH e LH nos doentes', fontsize=14, fontweight='bold')
        plt.ylabel('LH(mIU/mL)')
        plt.xlabel('AMH(ng/mL)')
        
        plt.ylim(-1,14)
        plt.xticks(range(0,40,5), [str(i) for i in range(0,40,5)])
        plt.xlim(-1,40)

        plt.gcf().set_size_inches(8, 6)
        plt.tight_layout()
        
        plt.show()

    def bmi():
        sns.lmplot(data=dados, x="RBS(mg/dl)", y="BMI", hue="PCOS (Y/N)", palette=colors, legend=False)

        plt.title('Relação entre BMI e RBS entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.ylabel('BMI')
        plt.xlabel('RBS (mg/dl)')

        plt.ylim(0,60)
        plt.xlim(0,250)

        plt.gcf().set_size_inches(8, 6) 
        plt.tight_layout()

        legend_labels = ['Não doentes', 'Doentes']
        handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0], markersize=8),
                   plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[1], markersize=8)]
        plt.legend(handles=handles, labels=legend_labels, title="PCOS", loc='upper right', fontsize=10, ncol=1)

        plt.show()
    
    def foliculo():
        sns.lmplot(data=dados,x='Follicle No. (R)',y='Follicle No. (L)', hue="PCOS (Y/N)",palette=colors, legend=False)

        plt.title('Relação entre número de foliculos entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.ylabel('Nº folículos (Esq)')
        plt.xlabel('Nº folículos (Dir)')

        plt.ylim(-2,30)
        plt.xlim(-2,25)

        plt.gcf().set_size_inches(10, 10) 
        plt.tight_layout()

        legend_labels = ['Não doentes', 'Doentes']
        handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0], markersize=8),
                   plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[1], markersize=8)]
        plt.legend(handles=handles, labels=legend_labels, title="PCOS", loc='upper right', fontsize=10, ncol=1)

        plt.show()

    def endometrio():
        axes = dados.boxplot(column='Endometrium (mm)', by='PCOS (Y/N)', figsize=(10,5),
                   whis=[5,95], return_type='axes', showfliers=False,patch_artist = True,
                   boxprops = dict(facecolor = "mistyrose"), medianprops = dict(color = "salmon", linewidth = 1),
                   whiskerprops = dict(color = "black", linewidth = 1.5))

        plt.suptitle('')
        plt.title('Espessamento do endométrio entre doentes e não doentes', fontsize=14, fontweight='bold')
        plt.subplots_adjust(wspace=0.25)
        plt.ylabel('Endometrium (mm)')
        plt.xlabel('PCOS')
        plt.xticks([1,2], ['Não', 'Sim'])

        plt.show()

    tip.grid_columnconfigure(0, weight=1)
    tip.grid_columnconfigure(1, weight=1)
    tip.grid_columnconfigure(2, weight=1)
    tip.grid_columnconfigure(3, weight=1)
    tip.grid_columnconfigure(4, weight=1)
    tip.grid_columnconfigure(5, weight=1)
    tip.grid_columnconfigure(6, weight=1)
    tip.grid_columnconfigure(7, weight=1)
    tip.grid_columnconfigure(8, weight=1)
    tip.grid_columnconfigure(9, weight=1)

    button0 = Button(tip, text="Distribuição da idade na PCOS", command=didade, padx=74, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=1, column=1, columnspan=5)

    button1 = Button(tip,text="Vitamina D entre doentes e não doentes",command=vitD,padx=51, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=2, column=1, columnspan=5)
    
    button2 = Button(tip,text="FSH/LH entre doentes e não doentes",command=FSHLH,padx=59, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=3, column=1, columnspan=5)
    
    button3 = Button(tip,text="Número de abortos entre doentes e não doentes",command=abortos,padx=30, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=4, column=1, columnspan=5)
    
    button4 = Button(tip,text="Duração do ciclo menstrual entre doentes e não doentes",command=ciclo,padx=11,   pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=5, column=1, columnspan=5)

    button5 = Button(tip,text="AMH e LH nos doentes",command=AMHLH,padx=92, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=6, column=1, columnspan=5)

    button6 = Button(tip,text="BMI e Glucose entre doentes e não doentes", command=bmi, padx=42, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=7, column=1, columnspan=5)

    button7 = Button(tip,text="Número de foliculos entre doentes e não doentes", command=foliculo,padx=28, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=8, column=1, columnspan=5)
    
    button8 = Button(tip,text="Espessamento do endométrio entre doentes e não doentes", command=endometrio,padx=5, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=9, column=1, columnspan=5)

    quit_btn2 = Button(tip,text="Voltar ao menu",command=tip.destroy, padx=112, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=10, column=1, columnspan=5)

############## Tableas ##################

def tabelas_m():
    tbl=Toplevel()
    tbl.title("Tabelas")
    tbl.iconbitmap('images/image.ico')
    tbl.geometry("305x350")

    filtradosim = dados[dados['PCOS (Y/N)'] == 1]
    filtradonao = dados[dados['PCOS (Y/N)'] == 0]

    def display_table(tab):
        tab_uso = tab.to_image(format="png")
        tab = Image.open(io.BytesIO(tab_uso))

        image_window = tk.Toplevel(tbl)
        image_window.title("Tabela")
        image_window.iconbitmap('images/image.ico')

        tab = ImageTk.PhotoImage(tab)
        panel = Label(image_window, image=tab)
        panel.image = tab
        panel.pack(expand=True, fill='both')

    def tabela_PCOS():
        PCOS_tot = dados['PCOS (Y/N)'].count()
        PCOS_nao = filtradonao['PCOS (Y/N)'].count()
        PCOS_sim = filtradosim['PCOS (Y/N)'].count()

        tab=go.Figure(data=[go.Table(header=dict(
            values=['', 'Número de Indivíduos'],
            line_color='black', fill_color='salmon',
            align='center',font=dict(color='black', size=12)
            ),cells=dict(
                values=[['Total de Observações', 'Indivíduos Não Doentes','Indivíduos Doentes'],[PCOS_tot,PCOS_nao,PCOS_sim]],
                line_color="black", fill_color="mistyrose",
                align='center', font=dict(color='black', size=11)
                ))
                ])
        
        tab.update_layout(title="Observações Relativas à Presença/Ausência de PCOS", title_font=dict(color="black",size=14))

        display_table(tab)

    def tabela_BMI():

        def cat_bmi(bmi_val):
            if bmi_val < 18.5:
                return 'Baixo Peso'
            elif 18.5 <= bmi_val < 24.9:
                return 'Peso Normal'
            elif 25 <= bmi_val < 29.9:
                return 'Excesso de Peso'
            elif 30 <= bmi_val < 34.9:
                return 'Obesidade Classe 1'
            elif 35 <= bmi_val < 39.9:
                return 'Obesidade Class 2'
            else:
                return 'Obesidade Class 3'

        categorias = {
            'Baixo Peso':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
            'Peso Normal':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
            'Excesso de Peso':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
            'Obesidade Classe 1':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
            'Obesidade Class 2':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
            'Obesidade Class 3':{'Não Doentes': 0, 'Doentes': 0,'Total': 0},
        }

        for index, row in dados.iterrows():
            bmi_cat = cat_bmi(row['BMI'])
            nutri = 'Doentes' if row['PCOS (Y/N)'] == 1 else 'Não Doentes'

            categorias[bmi_cat][nutri] += 1
            categorias[bmi_cat]['Total'] += 1

        tab_BMI_data = []
        for categ, count in categorias.items():
            tab_BMI_data.append([categ, count['Não Doentes'], count['Doentes'], count['Total']])

        tab_BMI_data_tr=list(map(list, zip(*tab_BMI_data)))

        tab_BMI = go.Figure(data=[go.Table(
            header=dict(values=['','Indivíduos Não Doentes','Indivíduos Doentes',' Total de Indivíduos'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=tab_BMI_data_tr,
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])
        tab_BMI.update_layout(title="Situação Nutricional dos Indivíduos",
                              title_font=dict(color="black",size=14))
        display_table(tab_BMI)

    def tabela_Gravidas():
        Grav_tot = dados[dados['Pregnant(Y/N)'] == 1].shape[0]
        Grav_nd = dados[(dados['Pregnant(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        Grav_PCOS = dados[(dados['Pregnant(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 1)].shape[0]

        tab_Grav = go.Figure(data=[go.Table(
            header=dict(values=['', 'Número de Indivíduos'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total de Observações', 'Indivíduos Não Doentes', 'Indivíduos Doentes'],
                               [Grav_tot, Grav_nd, Grav_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])

        tab_Grav.update_layout(
            title="Número de Pacientes Grávidas",
            title_font=dict(color="black", size=14))

        display_table(tab_Grav)

    def tabela_gpeso():
        gp_tot= dados[dados['Weight gain(Y/N)'] == 1].shape[0]
        sgp_tot = dados[dados['Weight gain(Y/N)'] == 0].shape[0]
        gp_nd = dados[(dados['Weight gain(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        sgp_nd = dados[(dados['Weight gain(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        gp_PCOS = dados[(dados['Weight gain(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 1)].shape[0]
        sgp_PCOS = dados[(dados['Weight gain(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 1)].shape[0]

        tab_gp= go.Figure(data=[go.Table(
            header=dict(values=['','Sem ganho de peso', 'Com ganho de peso'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total de Observações', 'Indivíduos Não Doentes', 'Indivíduos Doentes'],
                               [sgp_tot, sgp_nd, sgp_PCOS],[gp_tot, gp_nd, gp_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])

        tab_gp.update_layout(
            title="Observações Sobre Manifestação de Ganho de Peso",
            title_font=dict(color="black", size=14))

        display_table(tab_gp)

    def tabela_cpelo():
        cp_tot= dados[dados['hair growth(Y/N)'] == 1].shape[0]
        scp_tot = dados[dados['hair growth(Y/N)'] == 0].shape[0]
        cp_nd = dados[(dados['hair growth(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        scp_nd = dados[(dados['hair growth(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        cp_PCOS = dados[(dados['hair growth(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 1)].shape[0]
        scp_PCOS = dados[(dados['hair growth(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 1)].shape[0]

        tab_cp = go.Figure(data=[go.Table(
            header=dict(values=['', 'Sem crescimento de pelo', 'Com crescimento de pelo'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=12)),
            cells=dict(values=[['Total de Observações', 'Indivíduos Não Doentes', 'Indivíduos Doentes'],
                               [scp_tot, scp_nd, scp_PCOS], [cp_tot, cp_nd, cp_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])

        tab_cp.update_layout(
            title="Observações Relativas ao Crescimento de Pelo",
            title_font=dict(color="black", size=14))

        display_table(tab_cp)

    def tabela_regex():
        regex_tot = dados[dados['Reg.Exercise(Y/N)'] == 1].shape[0]
        sregex_tot = dados[dados['Reg.Exercise(Y/N)'] == 0].shape[0]
        regex_nd = dados[(dados['Reg.Exercise(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        sregex_nd = dados[(dados['Reg.Exercise(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 0)].shape[0]
        regex_PCOS = dados[(dados['Reg.Exercise(Y/N)'] == 1) & (dados['PCOS (Y/N)'] == 1)].shape[0]
        sregex_PCOS = dados[(dados['Reg.Exercise(Y/N)'] == 0) & (dados['PCOS (Y/N)'] == 1)].shape[0]

        tab_regex = go.Figure(data=[go.Table(
            header=dict(values=['', 'Sem Atividade Física Regular', 'Atividade Física Regular'],
                        line_color='black', fill_color='salmon',
                        align='center', font=dict(color='black', size=11)),
            cells=dict(values=[['Total de Observações', 'Indivíduos Não Doentes', 'Indivíduos Doentes'],
                               [sregex_tot, sregex_nd, sregex_PCOS], [regex_tot, regex_nd, regex_PCOS]],
                       line_color="black", fill_color="mistyrose",
                       align='center', font=dict(color='black', size=11))
        )])

        tab_regex.update_layout(
            title="Observações Relativas à Atividade Física",
            title_font=dict(color="black", size=14))

        display_table(tab_regex)

    tbl.grid_columnconfigure(0, weight=1)
    tbl.grid_columnconfigure(1, weight=1)
    tbl.grid_columnconfigure(2, weight=1)
    tbl.grid_columnconfigure(3, weight=1)
    tbl.grid_columnconfigure(4, weight=1)
    tbl.grid_columnconfigure(5, weight=1)
    tbl.grid_columnconfigure(6, weight=1)

    tab1_btn = tk.Button(tbl, text="Presença PCOS", command=tabela_PCOS, padx=50, pady=10, bg="mistyrose",font=('calibri', 10), relief="groove").grid(row=1, column=0, columnspan=5)
    
    tab2_btn = tk.Button(tbl, text="BMI", command=tabela_BMI, padx=78, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=2, column=0, columnspan=5)

    tab2_btn = tk.Button(tbl, text="Gravidez", command=tabela_Gravidas, padx=60, pady=10, bg="mistyrose",font=('calibri', 10), relief="groove").grid(row=3, column=0, columnspan=5)

    tab3_btn = tk.Button(tbl, text="Ganho de Peso", command=tabela_gpeso, padx=51, pady=10, bg="mistyrose",font=('calibri', 10), relief="groove").grid(row=4, column=0, columnspan=5)

    tab4_btn = tk.Button(tbl, text="Crescimento de Pelo", command=tabela_cpelo, padx=37, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=5, column=0, columnspan=5)

    tab5_btn = tk.Button(tbl, text="Atividade Física", command=tabela_regex, padx=49, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=6, column=0, columnspan=5)

    last_btn = tk.Button(tbl, text="Voltar ao menu", command=tbl.destroy, padx=50, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=7, column=0, columnspan=5)

############## Situação Clínica ##################

def clinica():
    def evaluate_values(TSH_val, AMH_val, VitD_val, Hb_val, Ciclo_val):
        reference_ranges = {
            'TSH': (0.4, 4),  
            'AMH': (1, 4),  
            'VitD': (20, 40),
            'Hb':(12, 16),
            'Duração':(3, 8)  
        }

        results = {}
        for param, val in zip(['TSH', 'AMH', 'VitD','Hb','Duração'], [TSH_val, AMH_val, VitD_val,Hb_val,Ciclo_val]):
            reference_range = reference_ranges[param]
            if val is None:
                results[param] = "Valor não inserido. Por favor, insira um valor válido."
            elif reference_range[0] <= val <= reference_range[1]:
                results[param] = f"{val} está dentro dos valores de referência ({reference_range[0]} - {reference_range[1]})."
            else:
                results[param] = f"{val} está fora dos valores de referência ({reference_range[0]} - {reference_range[1]}),\n por favor, consulte o seu médico."

        return results

    def get_float_value(entry):
        value = entry.get()
        if value:
            return float(value)
        return None

    top = Toplevel()
    top.title("Avalie a sua situação clínica")
    top.iconbitmap('images/image.ico')
    top.geometry("550x550")

    TSH = Entry(top, width=30)
    TSH.grid(row=2, column=1, padx=20)
    AMH = Entry(top, width=30)
    AMH.grid(row=3, column=1)
    VitD = Entry(top, width=30)
    VitD.grid(row=4, column=1)
    Hb = Entry(top, width=30)
    Hb.grid(row=5, column=1)
    Ciclo = Entry(top, width=30)
    Ciclo.grid(row=6, column=1)
    
    TSH_lb = Label(top, text="TSH (mIU/L)")
    TSH_lb.grid(row=2, column=0)
    AMH_lb = Label(top, text="AMH (ng/mL)")
    AMH_lb.grid(row=3, column=0)
    VitD_lb = Label(top, text="Vit D3 (ng/mL)")
    VitD_lb.grid(row=4, column=0)
    Hb_lb = Label(top, text="Hb (g/dl)")
    Hb_lb.grid(row=5, column=0)
    Ciclo_lb = Label(top, text="Duração da menstruação")
    Ciclo_lb.grid(row=6, column=0)
        
    result_text = Text(top, height=10, width=65)
    result_text.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    def evaluate_values_and_print():
        TSH_value = get_float_value(TSH)
        AMH_value = get_float_value(AMH)
        VitD_value = get_float_value(VitD)
        Hb_value = get_float_value(Hb)
        Ciclo_value = get_float_value(Ciclo)
        
        if TSH_value is not None and AMH_value is not None and VitD_value is not None and Hb_value is not None and Ciclo_value is not None:           
            evaluation_results = evaluate_values(TSH_value, AMH_value, VitD_value, Hb_value, Ciclo_value)
            result_text.delete(1.0, END)
            pdf_avaliacao = "Avalição situação clínica.pdf"
            
            pdf = canvas.Canvas(pdf_avaliacao, pagesize=letter)
            pdf.setFont("Times-Roman", 12)

            img_cab = ImageReader("images/image_1.png")
            pdf.drawImage(img_cab, 0, 780, width=10, height=10)
            pdf.drawString(12, 780, "Síndrome do Ovário Policístico")

            pdf.drawString(50, 700, "Caro(a) utilizador(a) aqui se segue a sua avaliação:")
            
            line_height = 660
            for param, result in evaluation_results.items():
                pdf.drawString(70, line_height, f"{param}: {result}")
                line_height -= 20

            message =("Por favor, esteja atento(a) aos sinais e sintomas. Saudações!")
            pdf.drawString(50, 540, message)

            img = ImageReader("images/etiologia.png")
            pdf.drawImage(img, 50, 250, width=500, height=200) 

            pdf.save()

            for param, result in evaluation_results.items():
                res = f"{param}: {result}\n"
                result_text.insert(END, res)

    submit_button = Button(top, text="Submeter valores", command=evaluate_values_and_print, bg="mistyrose", font=('calibri', 10), relief=GROOVE).grid(row=8,column=0,columnspan=2, padx=10, pady=10, ipadx=21)

    btn2 = Button(top, text="Voltar ao menu", command=top.destroy, bg="mistyrose", font=('calibri', 10), relief=GROOVE).grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=15)

interface.grid_columnconfigure(0, weight=1)
interface.grid_columnconfigure(1, weight=1)
interface.grid_columnconfigure(2, weight=1)
interface.grid_columnconfigure(3, weight=1)
interface.grid_columnconfigure(4, weight=1)
interface.grid_columnconfigure(5, weight=1)

labeltext = Label(interface, text=message, font=('calibri', 10))
labeltext.grid(row=1, column=0, columnspan=5)

mybutton1 = Button(interface, text="Parâmetros", command=parametros, padx=51, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=2, column=0, columnspan=5)

mybutton2 = Button(interface, text="Gráficos", command=graficos, padx=59, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=3, column=0, columnspan=5)

mybutton3 = Button(interface, text="Tabelas", command=tabelas_m, padx=60, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=4, column=0, columnspan=5)

mybutton4 = Button(interface, text="Avalie situação clínica", command=clinica, padx=25, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=5, column=0, columnspan=5)

button_quit = Button(interface, text="Sair do Programa", command=interface.quit, padx=37, pady=10, bg="mistyrose", font=('calibri', 10), relief="groove").grid(row=6, column=0, columnspan=5)

interface.mainloop()