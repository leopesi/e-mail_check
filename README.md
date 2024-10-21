# Sending confirmation Emails with Flask, Redis Queue, and Amazon SES

Nesse trabalho foi criado um código em python para testar um fluxo que envolve um processo comum de verificação de e-mail em uma aplicação cliente/servidor, usado normalmente durante o registro de novos usuários. A confirmação de e-mail é essencial para garantir que os usuários forneçam endereços válidos e acessíveis.
A integração começa ao adicionar o Redis Queue ao aplicativo Flask para gerenciar tarefas assíncronas, como o envio de e-mails de verificação. Essas tarefas são executadas em segundo plano por meio de um processo de trabalho separado, permitindo que a aplicação continue a responder rapidamente às solicitações dos usuários. O Docker é utilizado para conterizar o Flask e o Redis, simplificando o gerenciamento de dependências e a implantação da aplicação.
Para tokens de confirmação de e-mail, utiliza-se o módulo itsdangerous, que codifica e decodifica informações de forma segura, gerando links de verificação únicos para cada usuário. Quando o usuário clica no link enviado por e-mail (usando o Amazon SES para gerenciar os envios transacionais), o servidor processa a solicitação e atualiza o status do registro no banco de dados via um endpoint GET.
Além disso, a interação com a API da AWS é feita por meio do Boto3, o que permite acessar serviços como o SES para envio de e-mails. Isso forma um ciclo completo e eficiente para a confirmação de e-mail.

## Want to use this project?

1. Fork/Clone

1. [Sign up](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sign-up-for-aws.html) for AWS (if necessary), [verify](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) an email for [SES](https://aws.amazon.com/ses/), and update the following environment variables for the `worker` service in _docker-compose.yml_:

   ```yaml
   - SES_REGION=us-east-2
   - SES_EMAIL_SOURCE=your_email
   - AWS_ACCESS_KEY_ID=your_access_key_id
   - AWS_SECRET_ACCESS_KEY=your_secret_access_key
   ```

1. Spin up the containers and update the database:

   ```sh
   $ docker compose up -d --build
   $ docker compose run users python manage.py create_db
   ```

1. Open your browser to http://localhost:5003 to view the app.
