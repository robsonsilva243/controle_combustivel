⛽ Controle de Combustível - Machado Pré-Moldados

Repositório desenvolvido para o teste prático de Desenvolvedor Full Stack Python Junior. O foco deste projeto foi a implementação de um fluxo de gestão de abastecimento e controle de estoque de tanques utilizando o framework Odoo 19 Community.

🛠 Tecnologias e Versões

Framework: Odoo 19.0 Community

Linguagem: Python 3.12 (Downgrade realizado para garantir estabilidade)

Banco de Dados: PostgreSQL

Sistema Operacional: macOS (Ambiente de desenvolvimento)

🚀 Funcionalidades Implementadas

Gestão de Tanques: Cadastro de tanques com controle de capacidade (padrão 6.000L) e monitoramento de estoque atual.

Registro de Abastecimentos: Vínculo com veículos/placas, horímetro/odômetro e data/hora.

Cálculos Automáticos: O sistema calcula o valor total do abastecimento (Litros x Valor Unitário) em tempo real.

Regra de Negócio (Estoque): Implementação de gatilho no ORM para desconto automático do combustível no estoque do tanque no momento da criação do registro.

Segurança e Permissões: Estrutura de grupos para Motoristas (registro), Analistas (relatórios) e Administradores (acesso total).

📝 Retorno Técnico e Decisões de Projeto

1. Estrutura do Módulo
O módulo controle_combustivel segue o padrão MVC (Model-View-Controller) rigoroso do Odoo:

Models: tanque.py e abastecimento.py definem a camada de dados e lógica de negócio.

Views: Foram desenvolvidas utilizando o novo padrão <list> oficial do Odoo 19, garantindo a compatibilidade com as futuras atualizações do framework.

Segurança: Configuração via ir.model.access.csv e security.xml para gestão de privilégios.

2. Dificuldades Superadas
Ambiente Python: Identifiquei uma incompatibilidade de opcodes (LOAD_SMALL_INT) na versão 3.14 do Python (atualmente em desenvolvimento), o que causava erros críticos no safe_eval do Odoo. Realizei o downgrade estratégico para a versão 3.12, restabelecendo a estabilidade do sistema.

Frontend SASS: Necessidade de configuração manual de compiladores no macOS para renderização correta do visual da versão Community.

3. Proposta de Integração NF-e/NFS-e
Conforme solicitado no Passo 3 do edital, a estratégia sugerida para a Machado Pré-Moldados é:

Base: Adoção dos módulos de localização brasileira da OCA (l10n-brazil).

Workflow: Integração do recebimento de XMLs de compra de combustível para alimentação automática do estoque do tanque, eliminando a digitação manual de entradas.

Transmissão: Utilização de APIs de mensageria via Python para comunicação simplificada com os webservices da SEFAZ.

Candidato: Robson
Data de Conclusão: 17 de Fevereiro de 2026
