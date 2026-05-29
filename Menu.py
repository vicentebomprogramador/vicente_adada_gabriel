def menu():


    while True:


        print("=== ESCOLHA O ATOR ===")
        print("1 - aluno")
        print("2 - professor")
        print("3 - diretor")

        
        ator = input("quem é você? ").strip()


        if ator == "1":
            print("\n=== MENU DO ALUNO ===")
            print("1 - cadastrar aluno")
            print("2 - calcular media")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_aluno()

            elif opcao == "2":
                calcular_media()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        elif ator == "2":
            print("\n=== MENU DO PROFESSOR ===")
            print("1 - registrar notas")
            print("2 - atualizar aluno")
            print("3 - calcular media")
            print("4 - situação do aluno")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                registrar_notas()

            elif opcao == "2":
                atualizar_aluno()

            elif opcao == "3":
                calcular_media()

            elif opcao == "4":
                situação_aluno()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        elif ator == "3":
            print("\n=== MENU DO DIRETOR ===")
            print("1 - listar alunos")
            print("2 - apagar aluno")
            print("0 - sair")

            opcao = input("escolha uma opção: ").strip()

            if opcao == "1":
                listar_alunos()

            elif opcao == "2":
                apagar_aluno()

            elif opcao == "0":
                print("saindo...")
                break

            else:
                print("opção inválida.")

        else:
            print("ator inválido.")
        continue
        
menu()