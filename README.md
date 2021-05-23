# Banco-API-DJANGO-Rest-Framework

Operações presentes nesse exemplo:

Cadastrar ativos
Os ativos devem conter no mínimo as informações abaixo:
Nome - uma denominação para este ativo
Modalidade - renda fixa, renda variável ou cripto

Fazer aplicações e resgates em um ativo
Aplicação é quando o usuário aporta dinheiro em um ativo
Resgate é quando o usuário retira dinheiro de um ativo
Aplicações e resgates são transacionais e imutáveis. Uma vez realizada não há como alterar.
As aplicações e resgates devem conter no mínimo as informações abaixo:
Ativo - O ativo ao qual a aplicação/resgate se refere
Data de solicitação - a data em que a aplicação/resgate foi solicitada
Quantidade - número de ativos que foram aplicados/resgatados
Preço unitário - preço unitário do ativo na aplicação/resgate

Usuários podem fazer aplicações/resgate em ativos cadastrados por qualquer usuário

Exemplo:
O usuário A cadastra um ativo chamado BITCOIN e faz uma aplicação de mil reais
O usuário B pode aplicar no ativo BITCOIN também, pois ele já foi cadastrado pelo usuário A

Saldo da sua carteira de investimentos
O saldo da carteira é o somatório de saldos investidos em cada um dos ativos

Prerequisites required include:
- Python
- Pip 
- Virtualenv 
- Django 