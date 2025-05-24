Desafio de Avaliação Técnica Axur: Análise de Imagem com IA
Este repositório contém um script Python desenvolvido para um desafio de avaliação técnica da Axur. O projeto foca na visão computacional e na integração de APIs, demonstrando a capacidade de extrair informações visuais de uma página web, processá-las com um modelo de inteligência artificial e submeter os resultados.

🚀 Funcionalidades
O script automatiza o seguinte fluxo de trabalho:

Scraping de Imagem: Acessa uma URL específica para extrair uma imagem codificada em Base64.
Processamento com IA: Envia a imagem para uma API de inferência de IA (microsoft-florence-2-large) para gerar uma legenda detalhada do seu conteúdo.
Submissão de Resposta: Envia a descrição gerada pela IA para a plataforma de avaliação da Axur, completando o desafio.
🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem de programação principal.
requests: Para fazer requisições HTTP e interagir com APIs.
BeautifulSoup4: Para parsing HTML e extração de dados (a imagem).
base64: Para codificação e decodificação de dados da imagem.
json: Para manipulação de dados JSON.
⚙️ Como Executar
Siga os passos abaixo para configurar e executar o script:

Pré-requisitos
Python 3.x instalado.
Acesso a um TOKEN de autorização fornecido pela Axur para a API.
Instalação
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/nome-do-seu-repositorio.git
cd nome-do-seu-repositorio
Crie e ative um ambiente virtual (opcional, mas recomendado):

Bash

python -m venv venv
# No Windows
.\venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
(Crie um arquivo requirements.txt com as dependências: requests, beautifulsoup4)

Configuração do Token
Abra o arquivo main.py (ou como você o nomeou).

Substitua o placeholder P9snEZdwPD9aK6Bfp0WRuHNFao7pW1VI pelo seu TOKEN real fornecido pela Axur:

Python

TOKEN = "SEU_TOKEN_AQUI"
⚠️ Atenção: Nunca exponha seu token de forma pública em um repositório! Considere usar variáveis de ambiente ou um arquivo .env para armazenar o token em projetos reais. Para este desafio, a substituição direta é aceitável, mas em um ambiente de produção, a segurança deve ser priorizada.

Execução
Após a configuração, execute o script:

Bash

python main.py
O script imprimirá o progresso e o resultado no console. Em caso de sucesso, você receberá uma mensagem de confirmação da submissão.

🧠 Lógica do Script
get_image_bytes():

Faz uma requisição GET para a SCRAPE_URL.
Usa BeautifulSoup para encontrar a tag <img> e extrair seu atributo src.
Decodifica a string Base64 da src em bytes brutos da imagem.
send_image_to_model(image_bytes):

Codifica os bytes da imagem de volta para Base64.
Monta um payload JSON para a API de inferência, especificando o modelo (microsoft-florence-2-large) e a instrução (<DETAILED_CAPTION>).
Faz uma requisição POST para a INFERENCIA_URL com o payload e o cabeçalho de autorização.
submit_response(response_json):

Recebe a resposta JSON do modelo de IA.
Faz uma requisição POST para a SUBMISSAO_URL com a resposta para submeter o resultado do desafio.
🛑 Tratamento de Erros
O script inclui blocos try-except para capturar exceções comuns, como falhas na requisição HTTP, imagem não encontrada ou erros na API, fornecendo mensagens de erro informativas para auxiliar na depuração.

Contribuição
Embora este seja um desafio técnico, sinta-se à vontade para abrir issues ou sugestões se encontrar alguma melhoria.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
