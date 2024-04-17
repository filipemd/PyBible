import pybible

print("Teste da Gênesis capítulo 1 na Bíblia Novo Tradução na Linguagem de Hoje:")
print(pybible.bible("ntlh", "gn", 1))
print("*"*50)

print("Teste da Gênesis capítulo 1 versículo 1 na Bíblia Novo Tradução na Linguagem de Hoje:")
print(pybible.bible("ntlh", "gn", 1, 1))
print("*"*50)

print("Teste na Bíblia New International Version:")
print(pybible.bible("niv", "gn", 1, 1))
print("*"*50)

print("Teste do número de capítulos de Gênesis: ")
print(pybible.chapter_amount("nvi", "gn"))
print("*"*50)

print("Teste do número de capítulos de Salmos: ")
print(pybible.chapter_amount("nvi", "sl"))
print("*"*50)