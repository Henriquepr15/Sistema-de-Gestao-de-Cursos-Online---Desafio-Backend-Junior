# Sistema-de-Gestao-de-Cursos-Online---Desafio-Backend-Junior

Sistema de Gestão de Cursos Online - Documentação Técnica
Objetivos
Este projeto foi desenvolvido como parte de um desafio técnico para a posição de Desenvolvedor Backend Junior. O objetivo é criar uma API RESTful utilizando Django e SQL Server para o gerenciamento de cursos online. A aplicação inclui funcionalidades como cadastro de cursos, professores, alunos, matrículas e agendamento de aulas.
Estrutura do Projeto
O projeto está estruturado da seguinte forma:
- `online_courses/`: Diretório principal do projeto contendo as configurações globais do Django.
- `courses/`: Aplicação principal com os modelos, visualizações e serializers.
- `templates/`: Contém os arquivos HTML para renderização da interface do usuário.
- `db.sqlite3`: Banco de dados SQLite utilizado temporariamente para testes.
- `manage.py`: Arquivo de gerenciamento do Django.
Descrição dos Arquivos
- **models.py**: Define os modelos do banco de dados, incluindo Professor, Course, Student, Enrollment e Lesson.
- **serializers.py**: Contém os serializers para a integração dos modelos com a API RESTful.
- **views.py**: Implementa as visualizações que gerenciam a lógica de negócio e os endpoints da API.
- **urls.py**: Define as rotas do projeto e da aplicação, incluindo a configuração do Swagger.
- **homepage.html**: Página inicial exibindo os cursos, professores, alunos e aulas cadastradas.
Implementação via SQL Server
A implementação com SQL Server ainda está em andamento. O banco de dados foi configurado no arquivo `settings.py` com o uso do driver `django-mssql-backend` e a instalação do ODBC Driver 17 para SQL Server.

  Pagina inicial

  ![image](https://github.com/user-attachments/assets/1c3d2fda-1374-4392-be0d-c012ece45674)

Configuração atual no arquivo `settings.py`:
- ENGINE: 'mssql'
- NAME: Nome do banco de dados.
- USER: Usuário do SQL Server.
- PASSWORD: Senha do SQL Server.
- HOST: Host do servidor SQL.
- OPTIONS: Configurações adicionais, como driver ODBC.
- 
Problemas encontrados:
1. Conexão com o servidor SQL Server ainda não foi estabelecida devido a erros de configuração do servidor.


Banco de dados
Este projeto utiliza o SQLite, o banco de dados padrão do Django, ideal para desenvolvimento por sua simplicidade e integração direta. O SQLite armazena os dados localmente em um único arquivo (db.sqlite3), facilitando o gerenciamento e a portabilidade do projeto. É uma solução eficiente para ambientes de teste e APIs pequenas, mas não recomendada para produção em larga escala.




Criação de ADM

![image](https://github.com/user-attachments/assets/067d9a99-263b-4447-848d-18d94bb66cca)

URLs da API e Como Usá-las
Professores (Professors)
URL: http://127.0.0.1:8000/api/professors/
Descrição: Use esta URL para listar, criar, atualizar ou deletar professores.

Cursos (Courses)
URL: http://127.0.0.1:8000/api/courses/
Descrição: Use esta URL para listar, criar, atualizar ou deletar cursos.

Estudantes (Students)
URL: http://127.0.0.1:8000/api/students/
Descrição: Use esta URL para listar, criar, atualizar ou deletar estudantes.

Matrículas (Enrollments)
URL: http://127.0.0.1:8000/api/enrollments/
Descrição: Use esta URL para listar, criar, atualizar ou deletar matrículas.

Aulas (Lessons)
URL: http://127.0.0.1:8000/api/lessons/
Descrição: Use esta URL para listar, criar, atualizar ou deletar aulas.

imagens do uso da API

![image](https://github.com/user-attachments/assets/6bbc3875-392e-432f-bae2-e1aa8af7127a)
![image](https://github.com/user-attachments/assets/8515c774-5370-4c3f-8006-fc7feac41afb)
![image](https://github.com/user-attachments/assets/affb3d3b-7006-4b21-a1cd-a42317c94d75)
