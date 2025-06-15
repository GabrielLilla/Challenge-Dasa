# Registro de Estoque - CLI  
*Challenge Dasa 2025 • FIAP*

**Grupo**: *Gabriel Terra Lilla dos Santos RM:554575, Caio Felipe de Lima Bezerra — RM 556197, Rickelmyn de Souza Ruescas — RM 556055, Fabrini Soares — RM 557813, Vitor Couto Victorino — RM 554965*  

## Pré-requisitos
* **Python 3.8+** (sem dependências externas)  
* Terminal com suporte a **cores ANSI**  
  *Windows 10/11, macOS, Linux modernos já atendem.*

## Download
```bash
curl -O https://github.com/GabrielLilla/Challenge-Dasa/blob/main/estoque.py
```
> Ou simplesmente salve o arquivo como **`registro_estoque_cli.py`**.


## Como executar
```bash
python registro_estoque_cli.py          # Linux / macOS
py -3 registro_estoque_cli.py           # Windows
```


## Fluxo de uso
1. **Menu principal**
   ```
   1) Registrar entrada/retirada
   2) Ver recibo de últimas operações
   ENTER para sair
   ```
2. **Registrar operação**
   * Escolher **local**: `ESTOQUE`, `ALMOXARIFADO` ou `SALA`.  
   * Informar **data** no formato **DD/MM/AAAA** (ENTER = hoje).  
   * Selecionar **produto** (*VOLTAR* para retornar).  
   * Escolher **E** *(entrada)* ou **R** *(retirada)*.  
   * Digitar **quantidade** (> 0).  
     *Se tentar retirar mais que o saldo, o programa avisa e repete.*  
   * Saldo é atualizado; alerta ⚠ aparece se ≤ nível mínimo.
3. **Recibo**  
   Opção *2* mostra as **10 operações mais recentes**:  
   ```
   14/05/2025 | ESTOQUE     | Seringa | ENTRADA  30 un | Saldo: 430
   ```


## Níveis mínimos
```python
minimo = {"Seringa": 20, "Agulha": 20, "Algodao": 10}
```
Saldo ≤ mínimo gera aviso:
```
⚠  Alerta: Algodao baixo (10 ≤ mín 10)
```

## Personalizar estoque inicial
```python
estoque = {
    "ESTOQUE":      {"Seringa": 400, "Agulha": 450},
    "ALMOXARIFADO": {"Seringa": 120},
    "SALA":         {"Seringa":  15},
}
```

### Limitações
* Dados **em memória** – perdem-se ao fechar o script.  
* Sem validação de caracteres especiais.  
* Terminais muito antigos podem não exibir cores.


