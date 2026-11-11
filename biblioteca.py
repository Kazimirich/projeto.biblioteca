def validar(tipo, prompt, minimo=None, maximo=None):
    while True:
        entrada = input(prompt)
        if tipo == "int":
            try:
                valor = int(entrada)
            except ValueError:
                print("Erro: digite um número inteiro.")
                continue
            if minimo != None and valor < minimo:
                print("Erro: o valor deve ser no mínimo", minimo)
                continue
            if maximo != None and valor > maximo:
                print("Erro: o valor deve ser no máximo", maximo)
                continue
            return valor
        elif tipo == "str":
            valor = entrada.strip()
            if minimo != None and len(valor) < minimo:
                print("Erro: o texto deve ter no mínimo", minimo, "caracteres.")
                continue
            if maximo != None and len(valor) > maximo:
                print("Erro: o texto deve ter no máximo", maximo, "caracteres.")
                continue
            return valor


class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.emprestado = False

    def mostrar(self):
        if self.emprestado:
            estado = "Emprestado"
        else:
            estado = "Disponível"
        print("Código:", self.codigo, "| Título:", self.titulo, "| Autor:", self.autor, "|", estado)


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def mostrar(self):
        print("Matrícula:", self.matricula, "| Nome:", self.nome, "| Livros emprestados:", len(self.livros_emprestados))


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.alunos = []
        self.limite = 5
        self.proximo_codigo = 1
        self.proxima_matricula = 1

    def buscar_livro(self, codigo):
        for livro in self.catalogo:
            if livro.codigo == codigo:
                return livro
        return None

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def registar_livro(self):
        titulo = validar("str", "Título: ", 1, 100)
        autor = validar("str", "Autor: ", 1, 100)
        livro = Livro(titulo, autor, self.proximo_codigo)
        self.proximo_codigo = self.proximo_codigo + 1
        self.catalogo.append(livro)
        print("Livro registado com sucesso. Código:", livro.codigo)

    def registar_aluno(self):
        nome = validar("str", "Nome: ", 1, 100)
        aluno = Aluno(nome, self.proxima_matricula)
        self.proxima_matricula = self.proxima_matricula + 1
        self.alunos.append(aluno)
        print("Aluno registado com sucesso. Matrícula:", aluno.matricula)

    def consultar_disponiveis(self):
        encontrou = False
        print("--- Livros disponíveis ---")
        for livro in self.catalogo:
            if livro.emprestado == False:
                livro.mostrar()
                encontrou = True
        if encontrou == False:
            print("Não há livros disponíveis.")

    def emprestar(self):
        matricula = validar("int", "Matrícula do aluno: ", 1)
        aluno = self.buscar_aluno(matricula)
        if aluno == None:
            print("Aluno não encontrado.")
            return
        if len(aluno.livros_emprestados) >= self.limite:
            print("O aluno já atingiu o limite de", self.limite, "livros.")
            return
        codigo = validar("int", "Código do livro: ", 1)
        livro = self.buscar_livro(codigo)
        if livro == None:
            print("Livro não encontrado.")
            return
        if livro.emprestado:
            print("Este livro já está emprestado.")
            return
        livro.emprestado = True
        aluno.livros_emprestados.append(livro)
        print("Empréstimo realizado:", livro.titulo, "para", aluno.nome)

    def devolver(self):
        matricula = validar("int", "Matrícula do aluno: ", 1)
        aluno = self.buscar_aluno(matricula)
        if aluno == None:
            print("Aluno não encontrado.")
            return
        codigo = validar("int", "Código do livro: ", 1)
        for livro in aluno.livros_emprestados:
            if livro.codigo == codigo:
                livro.emprestado = False
                aluno.livros_emprestados.remove(livro)
                print("Livro devolvido:", livro.titulo)
                return
        print("Este aluno não tem esse livro emprestado.")

    def mostrar_livros_aluno(self):
        matricula = validar("int", "Matrícula do aluno: ", 1)
        aluno = self.buscar_aluno(matricula)
        if aluno == None:
            print("Aluno não encontrado.")
            return
        print("--- Livros emprestados por", aluno.nome, "---")
        if len(aluno.livros_emprestados) == 0:
            print("Nenhum livro emprestado.")
            return
        for livro in aluno.livros_emprestados:
            livro.mostrar()

    def relatorio(self):
        emprestados = 0
        for livro in self.catalogo:
            if livro.emprestado:
                emprestados = emprestados + 1
        disponiveis = len(self.catalogo) - emprestados
        print("===== RELATÓRIO =====")
        print("Total de livros:", len(self.catalogo))
        print("Livros emprestados:", emprestados)
        print("Livros disponíveis:", disponiveis)
        print("Total de alunos:", len(self.alunos))
        for aluno in self.alunos:
            aluno.mostrar()


biblioteca = Biblioteca()

while True:
    print()
    print("===== BIBLIOTECA =====")
    print("1 - Registar livro")
    print("2 - Registar aluno")
    print("3 - Consultar livros disponíveis")
    print("4 - Fazer empréstimo")
    print("5 - Devolver livro")
    print("6 - Mostrar livros de um aluno")
    print("0 - Sair e gerar relatório")
    opcao = validar("int", "Escolha uma opção: ", 0, 6)
    if opcao == 1:
        biblioteca.registar_livro()
    elif opcao == 2:
        biblioteca.registar_aluno()
    elif opcao == 3:
        biblioteca.consultar_disponiveis()
    elif opcao == 4:
        biblioteca.emprestar()
    elif opcao == 5:
        biblioteca.devolver()
    elif opcao == 6:
        biblioteca.mostrar_livros_aluno()
    elif opcao == 0:
        biblioteca.relatorio()
        print("Programa encerrado.")
        break
