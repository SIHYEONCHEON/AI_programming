import random


# 8-Queen 문제에서 충돌을 계산하는 함수
def fitness(board):
    n = len(board)
    clashes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                clashes += 1
    return 28 - clashes  # 최대 28개의 비충돌 쌍


# 새로운 개체(보드) 생성
def generate_board():
    return [random.randint(0, 7) for _ in range(8)]


# 선택 연산 (룰렛 휠 선택)
def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i in range(len(population)):
        current += fitnesses[i]
        if current > pick:
            return population[i]


# 교차 연산 (한 지점 교차)
def crossover(parent1, parent2):
    point = random.randint(0, 7)
    return parent1[:point] + parent2[point:]


# 돌연변이 연산
def mutate(board):
    if random.random() < 0.2:  # 20% 확률로 돌연변이 발생
        index = random.randint(0, 7)
        board[index] = random.randint(0, 7)
    return board


# 체스판을 텍스트로 출력 (숫자 포함)
def draw_board(board):
    board_size = len(board)
    print("  " + " ".join(str(i) for i in range(board_size)))  # 열 번호 출력
    for row in range(board_size):
        line = "".join("♛ " if board[col] == row else "■ " for col in range(board_size))
        print(f"{row} {line}")  # 행 번호 출력
    print("\n")


# 유전자 알고리즘 실행 함수
def genetic_algorithm():
    population_size = 100
    generations = 1000
    population = [generate_board() for _ in range(population_size)]

    for gen in range(generations):
        fitnesses = [fitness(board) for board in population]
        if max(fitnesses) == 28:
            best_board = population[fitnesses.index(28)]
            return best_board

        new_population = []
        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return None  # 해결책을 찾지 못함


# 실행 및 결과 출력
solution = genetic_algorithm()
if solution:
    print("해결된 8-Queen 보드:")
    draw_board(solution)
    print("퀸 위치 (열 기준):", solution)
else:
    print("해결책을 찾지 못했습니다.")