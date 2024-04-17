# PyBible

PyBible é uma Biblioteca para acessar a Bíblia no Python. Ela funciona fazendo Web Scraping do site [bibliaonline.com.br](https://bibliaonline.com.br). Por isso, é necessário o acesso à Internet para utilizar a Biblioteca.

A Biblioteca só tem duas funções:

- `bible(version, book, chapter, verse=0)`: Com ela, é possível acessar um capítulo todo da Bíblia ou apenas um versículo. Se o parâmetro `verse` for maior que zero, a função pega apenas um versículo. Caso contrário, pega o capítulo todo.

- `chapter_amount(version, book)`: Com ela, é possível acessar a quantidade de capítulos de um livro.