def listar_alunos():

    conexao = criar_conexao()

    if conexao:

        cursor = conexao.cursor()

        sql = "SELECT * FROM alunos"

        cursor.execute(sql)

        dados = cursor.fetchall()

        if len(dados) == 0:
            print("nenhum aluno cadastrado")

        else:

            print("\n=== lista de alunos ===")

            for aluno in dados:

                print("matricula:", aluno[0])
                print("nome:", aluno[1])
                print("turma:", aluno[2])
                print()

        cursor.close()
        conexao.close()


