import os

alunos = []
professores = []
disciplinas = []
turmas = []
matriculas = []

class Aluno: # Classe de Alunos
    def __init__(self,nome_aluno,idade_aluno,cpf_aluno): 
        self.nome = nome_aluno
        self.idade = idade_aluno
        self.cpf = cpf_aluno
        
class Professor: #Classe de Professores
    def __init__(self,codigo_professor,nome_professor,cpf_professor): 
        self.codigo = codigo_professor
        self.nome = nome_professor
        self.cpf = cpf_professor
        
class Disciplina: #Classe de Disciplinas
    def __init__(self,codigo_disciplina ,nome_disciplina): 
        self.codigo = codigo_disciplina
        self.nome = nome_disciplina
        
class Equipe: #Classe de Turmas
    def __init__(self,codigo_turma,codigo_instrutor, codigo_materia): 
        self.codigo = codigo_turma
        self.cod = codigo_instrutor
        self.mat = codigo_materia
        
class Codigo: #Classe de Matriculas
    def __init__(self,cod_turma,cod_estudante): 
        self.codigo = cod_turma
        self.cod = cod_estudante
        
           
    
def linha(tam = 42): #cabeçalho 
    return '-' * tam
   

def limpar(): # Função para limpar o console
    os.system("cls")


def menu_principal(): # funcão do menu principal
    print("""
        (1) Gerenciar estudantes.
        (2) Gerenciar professores.
        (3) Gerenciar disciplinas.
        (4) Gerenciar turmas.
        (5) Gerenciar matriculas.
        (9) Sair.
                """)


def sub_menu(): # função do submenu 
    print("""
        (1) Incluir.          
        (2) Listar.
        (3) Atualizar.
        (4) Excluir.
        (9) Voltar ao menu principal.
            """)


def estudantes(opcao): #função para inserir , listar , editar e excluir (aluno)
    
    limpar()
    if opcao == 1: # Inserir Alunos
        
        nome_aluno = input('Digite o nome do aluno: ')
        idade_aluno = input('Digite a idade do aluno: ')
        cpf_aluno = input('Digite o CPF do aluno: ')
               
        aluno = Aluno(nome_aluno, idade_aluno, cpf_aluno)
        alunos.append(aluno)
        
        print('Aluno criado com sucesso! ')            

    elif opcao == 2:  # Listar Alunos
        if not alunos:  # Verifica se a lista está vazia
            print("Não tem alunos no banco de dados!")
        else:
            print("----- LISTAGEM -----")
        for aluno in alunos:  # Itera por todos os alunos
            print(f"Nome: {aluno.nome}")
            print(f"Idade: {aluno.idade}")
            print(f"CPF: {aluno.cpf}")
            print("-" * 20)  # Separador para melhor visualização

            
    if opcao == 3: # Editar Alunos
        cpf_aluno = input('Qual o CPF do aluno que deseja editar: ')
        achou = 1
        for aluno in alunos:
            if cpf_aluno == aluno.cpf:
                
                aluno.nome = input('Digite o nome do aluno: ')
                aluno.idade = input('Digite a idade do aluno: ')
                aluno.cpf = input('Digite o CPF do aluno: ')                
                
                achou = 0
                print('Aluno editado com sucesso! ')   
                break
        
        if achou == 1:
            print('Aluno não encontrado!')
            
      
    elif opcao == 4: # Deletar aluno
        cpf_aluno = input('Qual o CPF do aluno que deseja excluir: ')
        achou = 1
        for aluno in alunos:
            if cpf_aluno == aluno.cpf:
                
                achou = 0
                print(f'Aluno {aluno.nome} removido com sucesso! ')   
                alunos.remove(aluno) 
                break
                
        if achou == 1:
            print('Aluno não encontrado!')   
    

def instrutor(opcao):

    limpar()
    if opcao == 1: # Inserir Professores
        
        codigo_professor = input('Digite o código do professor: ')
        nome_professor = input('Digite o nome do professor: ')         
        cpf_professor = input('Digite o CPF do professor: ')
               
        professor = Professor(codigo_professor, nome_professor, cpf_professor)

        professores.append(professor)
        
        print('Professor criado com sucesso! ')            

    elif opcao == 2:  # Listar Professores
        if not professores:  # Verifica se a lista está vazia
            print("Não tem professores no banco de dados!")
        else:
            print("----- LISTAGEM -----")
        for professor in professores:
            print(f"Código: {professor.codigo}")
            print(f"Nome: {professor.nome}")
            print(f"CPF: {professor.cpf}")            
              
            
    if opcao == 3: # Editar Professores
        cpf_professor = input('Qual o CPF do Professor que deseja editar: ')
        achou = 1
        for professor in professores:
            if codigo_professor == professor.codigo:
                
                professor.codigo = input('Digite o código do Professor: ')
                professor.nome = input('Digite o nome do Professor: ')
                professor.cpf = input('Digite o CPF do Professor: ')                
                
                achou = 0
                print('Professor editado com sucesso! ')   
                break
        
        if achou == 1:
            print('Professor não encontrado!')
            
      
    elif opcao == 4: # Deletar Professor
        cpf_professor = input('Qual o código do professor que deseja excluir: ')
        achou = 1
        for professor in professores:
            if codigo_professor == professor.codigo:
                
                achou = 0
                print(f'Professor {professor.nome} removido com sucesso! ')   
                professores.remove(professor) 
                break
                
        if achou == 1:
            print('Professor não encontrado!')

    elif opcao == 9: # Retorna ao menu principal 
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()
        
        
def materias(opcao): #função para inserir , listar , editar e excluir (disciplinas)
    
    limpar()
    if opcao == 1: # Inserir Matérias
        
        codigo_disciplina = input('Digite o codigo da disciplina: ')
        nome_disciplina = input('Digite o nome da disciplina: ')
               
        disciplina = Disciplina(codigo_disciplina, nome_disciplina)
        disciplinas.append(disciplina)
        
        print('Disciplina criada com sucesso! ')            

    elif opcao == 2:  # Listar Discplinas
        if not disciplinas:  # Verifica se a lista está vazia
            print("Não tem disciplinas no banco de dados!")
        else:
            print("----- LISTAGEM -----")
        for disciplina in disciplinas:  # Itera por todos as disciplinas
            print(f"Código: {disciplina.codigo}")
            print(f"Nome Discipina: {disciplina.nome}")
            
            
    if opcao == 3: # Editar Disciplina
        codigo_disciplina = input('Qual o código da disciplina que deseja editar: ')
        achou = 1
        for disciplina in disciplinas:
            if codigo_disciplina == disciplina.codigo:
                
                disciplina.codigo = input('Digite o codigo da disciplina: ')
                disciplina.nome = input('Digite o nome da disciplina: ')               
                
                achou = 0
                print('Disciplina editada com sucesso! ')   
                break
        
        if achou == 1:
            print('Disciplina não encontrado!')
            
      
    elif opcao == 4: # Deletar aluno
        codigo_disciplina = input('Qual a disciplina que deseja excluir: ')
        achou = 1
        for disciplina in disciplinas:
            if codigo_disciplina == disciplina.codigo:
                
                achou = 0
                print(f'Disciplina {disciplina.nome} removida com sucesso! ')   
                disciplinas.remove(disciplina) 
                break
                
        if achou == 1:
            print('Disciplina não encontrada!')        
        
    elif opcao == 9: # Retorna ao menu principal 
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()   
                

def equipes(opcao):  # Função para inserir, listar, editar e excluir turmas
    limpar()
    if opcao == 1:  # Inserir Turma
        codigo_turma = input('Digite o código da Turma: ')
        codigo_instrutor = input('Digite o código do Professor: ')
        codigo_materia = input('Digite o código da Disciplina: ')
        turma = Equipe(codigo_turma, codigo_instrutor, codigo_materia)
        turmas.append(turma)
        print('Turma criada com sucesso!')

    elif opcao == 2:  # Listar Turmas
        if not turmas:
            print("Não tem turmas no banco de dados!")
        else:
            print("----- LISTAGEM DE TURMAS -----")
            for turma in turmas:
                # Buscar professor associado
                instrutor_nome = "Professor não encontrado"
                for professor in professores:
                    if professor.codigo == turma.cod:
                        instrutor_nome = professor.nome
                        break

                # Buscar disciplina associada
                disciplina_nome = "Disciplina não encontrada"
                for disciplina in disciplinas:
                    if disciplina.codigo == turma.mat:
                        disciplina_nome = disciplina.nome
                        break

                print(f"Código da Turma: {turma.codigo}")
                print(f"Professor: {instrutor_nome}")
                print(f"Disciplina: {disciplina_nome}")
                print("-" * 20)

    elif opcao == 3:  # Editar Turma
        codigo_turma = input('Digite o código da Turma que deseja editar: ')
        for turma in turmas:
            if turma.codigo == codigo_turma:
                turma.cod = input(f"Novo código do Professor ({turma.cod}): ") or turma.cod
                turma.mat = input(f"Novo código da Disciplina ({turma.mat}): ") or turma.mat
                print('Turma editada com sucesso!')
                break
        else:
            print('Turma não encontrada!')

    elif opcao == 4:  # Deletar Turma
        codigo_turma = input('Digite o código da Turma que deseja excluir: ')
        for turma in turmas:
            if turma.codigo == codigo_turma:
                turmas.remove(turma)
                print(f'Turma {codigo_turma} removida com sucesso!')
                break
        else:
            print('Turma não encontrada!')        
        
    elif opcao == 9: # Retorna ao menu principal 
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal() 


def codigos(opcao):  # Função para inserir, listar, editar e excluir matrículas
    limpar()
    if opcao == 1:  # Inserir Matrículas
        codigo_turma = input('Digite o código da Turma: ')
        codigo_estudante = input('Digite o código do Estudante: ')
        matricula = Codigo(codigo_turma, codigo_estudante)
        matriculas.append(matricula)
        print('Matrícula criada com sucesso!')

    elif opcao == 2:  # Listar Matrículas
        if not matriculas:
            print("Não tem matrículas no banco de dados!")
        else:
            print("----- LISTAGEM DE MATRÍCULAS -----")
            for matricula in matriculas:
                # Buscar turma associada
                turma_nome = "Turma não encontrada"
                for turma in turmas:
                    if turma.codigo == matricula.codigo:
                        turma_nome = turma.codigo
                        break

                # Buscar estudante associado
                estudante_nome = "Estudante não encontrado"
                for aluno in alunos:
                    if aluno.cpf == matricula.cod:
                        estudante_nome = aluno.nome
                        break

                print(f"Código da Turma: {turma_nome}")
                print(f"Estudante: {estudante_nome}")
                print("-" * 20)

    elif opcao == 3:  # Editar Matrícula
        codigo_turma = input('Digite o código da Turma da matrícula que deseja editar: ')
        for matricula in matriculas:
            if matricula.codigo == codigo_turma:
                matricula.cod = input(f"Novo código do Estudante ({matricula.cod}): ") or matricula.cod
                print('Matrícula editada com sucesso!')
                break
        else:
            print('Matrícula não encontrada!')

    elif opcao == 4:  # Deletar Matrícula
        codigo_turma = input('Digite o código da Turma da matrícula que deseja excluir: ')
        for matricula in matriculas:
            if matricula.codigo == codigo_turma:
                matriculas.remove(matricula)
                print(f'Matrícula removida com sucesso!')
                break
        else:
            print('Matrícula não encontrada!')

    elif opcao == 9:  # Retorna ao menu principal
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()



while True: # Mostra o menu principal
    print(linha())    
    print('MENU PRINCIPAL'.center(42))
    print(linha())
    menu_principal()
    break
    
while True:    
    userInput = int(input('Escolha uma opção: '))
        
    if userInput == 1: # Gerenciar Alunos
        
        print(linha())
        print('GERENCIAR ESTUDANTES'.center(42))
        print(linha())
        sub_menu()
                
        opcao = int(input('Escolha uma opção: '))
        
        estudantes(opcao)
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()
      
    elif userInput == 2: # Gerenciar Professores
         
        print(linha())
        print('GERENCIAR PROFESSORES'.center(42))
        print(linha())
        sub_menu() 

        opcao = int(input('Escolha uma opção: '))
        
        instrutor(opcao)
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()     
      
      
    elif userInput == 3: # Gerenciar Disciplinas
         
        print(linha())
        print('GERENCIAR DISCIPLINAS'.center(42))
        print(linha())
        sub_menu() 

        opcao = int(input('Escolha uma opção: '))
        
        materias(opcao)
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()  
    
    elif userInput == 4: # Gerenciar Turmas
         
        print(linha())
        print('GERENCIAR TURMAS'.center(42))
        print(linha())
        sub_menu() 

        opcao = int(input('Escolha uma opção: '))
        
        equipes(opcao)
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()  
      
    elif userInput == 5: # Gerenciar Matrículas
         
        print(linha())
        print('GERENCIAR MATRÍCULAS'.center(42))
        print(linha())
        sub_menu() 

        opcao = int(input('Escolha uma opção: '))
        
        codigos(opcao)
        print(linha())
        print('MENU PRINCIPAL'.center(42))
        print(linha())
        menu_principal()   
   
        
        
          












