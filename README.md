Controle de Combustível - Machado Pré-Moldados
Módulo desenvolvido para o teste prático de Desenvolvedor Full Stack Python Junior.

🛠 Tecnologias e Versões
Framework: Odoo 19.0 Community

Linguagem: Python 3.12

Banco de Dados: PostgreSQL

🚀 Funcionalidades
Cadastro de Tanques com controle de estoque.

Registro de abastecimentos vinculado a veículos/placas.

Cálculo automático de valores (Litros x Valor Unitário).

Regra de negócio: Desconto automático de estoque no momento do abastecimento.

Hierarquia de acesso: Grupos específicos para Motoristas e Administradores.

Texto Explicativo e Retorno Técnico
1. Estrutura do Módulo
O módulo controle_combustivel foi estruturado seguindo as melhores práticas do Odoo:

Models: tanque.py (estoque) e abastecimento.py (lógica de consumo).

Views: Desenvolvidas com o novo padrão <list> do Odoo 19, garantindo modernidade e compatibilidade.

Segurança: Implementação de grupos de acesso para Motorista, Analista e Administrador via XML e CSV.

2. Dificuldades e Evolução
Ambiente Local: O primeiro contato com o Odoo 19 exigiu ajustes finos de infraestrutura.

Python 3.14: Identifiquei uma incompatibilidade de opcodes na versão 3.14 do Python e realizei o downgrade para a versão 3.12, garantindo estabilidade ao framework.

SASS/CSS: Configuração manual dos compiladores de estilo no macOS para garantir o carregamento correto da interface Community.

3. Melhorias Possíveis
Criação de um painel de indicadores (Dashboards) para consumo médio por placa.

Automatização de reabastecimento do tanque quando o estoque atingir um nível crítico.

4. Proposta de Integração NF-e/NFS-e
Para a Machado Pré-Moldados, a melhor estratégia de integração fiscal no Odoo Community é:

Localização: Utilização dos módulos da OCA (L10n-Brazil) e do ecossistema BrERP.

Automatização: Implementação de leitura de XML de entrada para que, ao receber uma nota de compra de combustível, o estoque do tanque seja incrementado automaticamente no módulo de controle.

Transmissão: Uso de APIs de mensageria (como NFe.io ou Focus NFe) integradas via Python para garantir a emissão de notas de serviço e produto sem depender de softwares externos.