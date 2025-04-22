# Projeto Prático de Monitoramento 🛠️

Este repositório contém um projeto prático com foco na aplicação de conceitos de **Site Reliability Engineering (SRE)**, utilizando ferramentas modernas de monitoramento como **Prometheus** e **Grafana**.

## 📌 Descrição

O objetivo principal deste projeto é fornecer uma base sólida para compreender e implementar um sistema de monitoramento eficaz, acompanhando métricas de aplicações em tempo real e promovendo maior confiabilidade e observabilidade nos sistemas.

## 🎯 Objetivos

- Configurar e integrar Prometheus e Grafana.
- Coletar métricas de aplicações Python.
- Visualizar dados em tempo real com dashboards customizados.
- Criar alertas com base em eventos e condições específicas.

## ⚙️ Tecnologias Utilizadas

- [Docker](https://www.docker.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Python](https://www.python.org/) (exemplo de aplicação monitorada)

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

## 🚀 Como executar

Clone o projeto:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

Suba os serviços com Docker:

```bash
docker-compose up -d
```

Acesse o Grafana em: [http://localhost:3000](http://localhost:3000)

## 📈 Dashboards e Monitoramento

O dashboard principal inclui:

- Quantidade de requisições por status HTTP
- Tempo de resposta por endpoint
- Total de erros registrados
- Alertas configuráveis

## 🛡️ Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

