import os, platform, sys
from datetime import datetime

def clear(): os.system("cls" if platform.system() == "Windows" else "clear")

CORES = {"azul":"\033[94m","verde":"\033[92m","amarelo":"\033[93m","vermelho":"\033[91m","reset":"\033[0m"}
def cor(txt, c): return CORES.get(c,"")+txt+CORES["reset"]

estoque = {
    "ESTOQUE":      {"Seringa": 400, "Agulha": 450, "Algodao": 300},
    "ALMOXARIFADO": {"Seringa": 120, "Agulha":  80, "Algodao":  25},
    "SALA":         {"Seringa":  15, "Agulha":  10, "Algodao":   5},
}
minimo = {"Seringa": 20, "Agulha": 20, "Algodao": 10}
historico = []        

def alerta(produto,saldo):
    if saldo<=minimo.get(produto,0):
        print(cor(f"⚠  Alerta: {produto} baixo ({saldo} ≤ mín {minimo[produto]})","vermelho"))

while True:
    clear()
    print(cor("=== CONTROLE DE INSUMOS ===","azul"))
    print("1) Registrar entrada/retirada")
    print("2) Ver recibo de últimas operações")
    print("ENTER para sair")
    escolha=input(cor("\nSelecione uma opção: ","verde")).strip()

    if escolha=="2":
        clear(); print(cor("=== RECIBO (10 últimas) ===\n","azul"))
        if not historico: print("Nenhuma operação registrada.")
        else:
            for op in historico[-10:][::-1]:
                linha=(f"{op['data']} | {op['local']:<12} | "
                       f"{op['produto']:<10} | {op['operacao']} {op['qtd']:>4} un | "
                       f"Saldo: {op['saldo']}")
                print(linha)
        input(cor("\nENTER p/ menu...","verde")); continue

    if escolha=="": print("Encerrado."); sys.exit()
    if escolha!="1": continue

    while True:
        clear(); print("Locais:"); [print("  •",n) for n in estoque]
        loc=input(cor("\nLocal (ENTER sai): ","verde")).strip().upper()
        if not loc: sys.exit()
        if loc in estoque: break
        print(cor("Local inválido.","vermelho"))

    while True:
        dstr=input(cor("Data (DD/MM/AAAA) [hoje]: ","verde")).strip()
        if not dstr:
            data=datetime.today().strftime("%d/%m/%Y"); break
        try:
            datetime.strptime(dstr,"%d/%m/%Y")
            data=dstr; break
        except ValueError:
            print(cor("Formato inválido. Use DD/MM/AAAA.","vermelho"))

    clear()
    while True:
        print(cor(f"=== {loc} em {data} ===","azul"))
        for p,q in estoque[loc].items():
            col="amarelo" if q<=minimo.get(p,0) else "reset"
            print(f"  {p:<12} saldo {cor(str(q),col)}")
        p_in=input(cor("\nProduto (ou VOLTAR): ","verde")).strip().title()
        if p_in.lower()=="voltar": p_in=None; break
        if p_in in estoque[loc]: prod=p_in; break
        print(cor("Produto não disponível.","vermelho"))
    if p_in is None: continue

    while True:
        op=input(cor("Entrada (E) ou Retirada (R)? ","verde")).strip().upper()
        if op in("E","R"): break
        print(cor("Digite E ou R.","vermelho"))

    while True:
        try:
            qt=int(input(cor("Quantidade (>0): ","verde")))
            if qt<=0: raise ValueError
            if op=="R" and qt>estoque[loc][prod]:
                print(cor(f"Só há {estoque[loc][prod]} unidades.","vermelho")); continue
            break
        except ValueError:
            print(cor("Número inteiro positivo.","vermelho"))

    estoque[loc][prod]+=qt if op=="E" else -qt
    saldo=estoque[loc][prod]

    historico.append({"data":data,"local":loc,"produto":prod,
                      "operacao":"ENTRADA" if op=="E" else "RETIRADA",
                      "qtd":qt,"saldo":saldo})

    clear()
    print(cor("=== OPERAÇÃO REGISTRADA ===\n","azul"))
    print(f"Data      : {data}")
    print(f"Local     : {loc}")
    print(f"Produto   : {prod}")
    print(f"Operação  : {'Entrada' if op=='E' else 'Retirada'}")
    print(f"Quantidade: {qt}")
    print(f"Saldo atual: {saldo}\n")
    alerta(prod, saldo)
    input(cor("ENTER p/ menu...","verde"))
