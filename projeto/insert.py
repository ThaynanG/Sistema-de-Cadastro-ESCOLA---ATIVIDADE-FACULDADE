from conexao import conectar_banco


def cadastrar_aluno():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        print("\n--- Cadastro de Aluno ---")

        nome = input("Nome: ")
        data = input("Data de nascimento: ")
        cpf = input("CPF: ")

        sql = """
        INSERT INTO alunos (nome, data_nascimento, cpf)
        VALUES (%s, %s, %s)
        """

        try:

            cursor.execute(sql, (nome, data, cpf))
            conn.commit()

            print("\nAluno cadastrado com sucesso!")

        except Exception as e:

            print(f"Erro: {e}")

        finally:

            cursor.close()
            conn.close()