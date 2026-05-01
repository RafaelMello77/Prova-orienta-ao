def exibir_herois(lista):
    print("\n--- HEROIS ---")
    for h in lista:
        print(h.resumo())


def exibir_missao(m):
    print(f"Missao: {m.resumo()}")


def erro(msg):
    print("[ERRO]", msg)