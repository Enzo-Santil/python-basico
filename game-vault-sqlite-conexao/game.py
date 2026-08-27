import os
import sqlite3

# Nome do banco de dados
CAMINHO_BANCO = "jogos.db"


def exibir_cabecalho(texto):
    os.system("cls")

    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def inicializar_banco():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            zerado BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def listar_jogos():
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")
    jogos = cursor.fetchall()

    conn.close()

    # Se BD vazio mostra a mensagem abaixo
    if not jogos:
        print("Nenhum jogo cadastrado ainda!\n")
        return

    # Formam o cabeçalho visual
    print(f"{'Título'.ljust(25)} | {'Plataforma'.ljust(12)} | Status")
    print("-" * 55)

    # Laço para exibir todos os jogos cadastrados
    for titulo, plataforma, zerado in jogos:
        status = "Zerado" if zerado else "Jogando"
        print(f"{titulo.ljust(25)} | {plataforma.ljust(12)} | {status}")

    print()


def adicionar_jogo(titulo, plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # SQL - Para inserir novos jogos
    cursor.execute(
        "INSERT INTO jogos (titulo, plataforma, zerado) VALUES (?, ?, ?)",
        (titulo, plataforma, False)
    )

    conn.commit()
    conn.close()


def marcar_como_zerado(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # SQL - Para atualizar Status de: jogando para zerado
    cursor.execute(
        "UPDATE jogos SET zerado = ? WHERE titulo = ?",
        (True, titulo)
    )

    # Guarda quantas linhas foram afetadas na atualização
    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou


def excluir_jogo(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # SQL - Para excluir um jogo
    cursor.execute(
        "DELETE FROM jogos WHERE titulo = ?",
        (titulo,)
    )

    # Guarda quantas linhas foram afetadas na exclusão
    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return encontrou


def exibir_menu():
    exibir_cabecalho("🤪🤪 GameVault")
    print("1. Adicionar jogo")
    print("2. Listar jogo")
    print("3. Marcar jogo como zerado")
    print("4. Sair")
    print("5. Excluir Jogo\n")


def pausar():
    input("Pressione Enter para voltar ao menu...")


def main():
    inicializar_banco()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_cabecalho("Adicionar jogo")

            titulo = input("Título do jogo: ")
            plataforma = input("Plataforma: ")

            adicionar_jogo(titulo, plataforma)

            print(f"\n'{titulo}' adicionado com sucesso!")
            pausar()

        elif opcao == "2":
            exibir_cabecalho("Seus jogos")

            listar_jogos()
            pausar()

        elif opcao == "3":
            exibir_cabecalho("Marcar como zerado")

            titulo = input("Título do jogo que zerou: ")

            if marcar_como_zerado(titulo):
                print(f"\n'{titulo}' marcado como zerado!")
            else:
                print(f"\n'{titulo}' não encontrado!")
                print("Confira se digitou corretamente.")

            pausar()

        elif opcao == "4":
            print("Até a próxima! 👋")
            break

        elif opcao == "5":
            exibir_cabecalho("Excluir jogo")

            titulo = input("Título do jogo que deseja excluir: ")

            if excluir_jogo(titulo):
                print(f"\n'{titulo}' excluído com sucesso!")
            else:
                print(f"\n'{titulo}' não encontrado!")

            pausar()

        else:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida! Escolha um número de 1 a 5.")
            pausar()


# Fechamento da função main
if __name__ == "__main__":
    main()
    