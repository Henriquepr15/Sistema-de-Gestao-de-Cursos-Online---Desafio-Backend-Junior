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

Configuração atual no arquivo `settings.py`:
- ENGINE: 'mssql'
- NAME: Nome do banco de dados.
- USER: Usuário do SQL Server.
- PASSWORD: Senha do SQL Server.
- HOST: Host do servidor SQL.
- OPTIONS: Configurações adicionais, como driver ODBC.
Problemas encontrados:
1. Conexão com o servidor SQL Server ainda não foi estabelecida devido a erros de configuração do servidor.
2. Instalação do SQL Server Developer Edition apresentou falhas e está sendo corrigida.
