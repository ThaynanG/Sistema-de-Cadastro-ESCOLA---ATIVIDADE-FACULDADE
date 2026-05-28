from conexao import conectar_banco


def listar_alunos():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM alunos ORDER BY nome")

        alunos = cursor.fetchall()

        print("\n====================================================")
        print("                 LISTA DE ALUNOS")
        print("====================================================")

        print(f"{'ID':<5}{'NOME':<20}{'DATA NASC':<15}{'CPF':<15}")

        print("----------------------------------------------------")

        for aluno in alunos:

            print(f"{aluno[0]:<5}{aluno[1]:<20}{aluno[2]:<15}{aluno[3]:<15}")

        print("====================================================")

        cursor.close()
        conn.close()