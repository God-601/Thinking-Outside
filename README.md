# Thinking Outside

**A universal creative-thinking skill for AI agents.**  
Skill universal de pensamento criativo aplicado: ideias menos óbvias, solução de problemas, reformulação útil de perguntas e respeito às restrições reais.

**Status:** pré-1.0, candidato em validação — sem promessa de melhoria comprovada até testes comparativos.  
**Custo de infraestrutura:** R$ 0 para a própria skill; o uso do agente segue os limites e custos do provedor escolhido.

## Por que existe?

Agentes podem sugerir dez versões da mesma ideia, insistir em soluções já rejeitadas ou tentar inovar quando basta resolver algo diretamente. Thinking Outside orienta o agente a:

- entender o objetivo e as restrições antes de propor alternativas;
- explorar mecanismos **diferentes**, não só nomes diferentes;
- questionar a formulação do problema **quando isso ajudar** — sem mudar o escopo por conta própria;
- escolher técnicas criativas conforme a tarefa, sem ritual de brainstorming;
- filtrar repetição, inviabilidade e promessas de originalidade sem evidências;
- complementar skills especializadas de código, Blender, Roblox, música ou design.

Não cria um novo modelo de IA, não garante ideias inéditas e não depende de APIs pagas.

## Exemplo

**Pedido:** “Me dê oito sistemas diferentes para um jogo Roblox competitivo. Não quero inventário, níveis nem missões diárias.”

**Comportamento desejado:** oito propostas com mecanismos distintos e regras concretas, justificando como mudam decisões dos jogadores; sem reciclar os sistemas rejeitados. Se não houver oito ideias boas, esclarecer a limitação em vez de inventar sugestões ruins.

**Pedido:** “Mude apenas a cor deste botão, sem alterar layout nem lógica.”

**Comportamento desejado:** cumprir objetivamente; não propor redesign.

## Instalação e uso

**Entrada da skill:** [thinking-outside/SKILL.md](thinking-outside/SKILL.md).

Este repositório segue a estrutura de [Agent Skills](https://agentskills.io/). Instale o diretório da skill no local de skills indicado pela documentação **do seu agente**, copiando a pasta **thinking-outside/** inteira, com SKILL.md e references/ juntos; a raiz do repositório não é a pasta da skill. A descoberta/ativação automática **depende de cada cliente** e precisa ser testada.

Para testar manualmente: “Use a skill Thinking Outside para explorar soluções não genéricas para [seu problema], respeitando [restrições].”

**Compatibilidade pretendida:** Codex, Claude Code, OpenCode e Cursor. A compatibilidade de formato não prova resultados idênticos; ainda faltam testes reais por cliente. Veja [compatibilidade](docs/compatibility.md).

## Documentação

- [Especificação](docs/specification.md)
- [Métodos criativos e critérios de seleção](docs/creative-methods.md)
- [Arquitetura leve](docs/architecture.md)
- [Compatibilidade e limitações](docs/compatibility.md)
- [Roadmap](docs/roadmap.md)
- [15 testes de aceitação](thinking-outside/evals/ACCEPTANCE_CASES.md)
- [Protocolo comparativo](thinking-outside/evals/BENCHMARK_PROTOCOL.md)
- [Estado de validação](VALIDATION.md)
- [Histórico](CHANGELOG.md)

Veja também o [protocolo](docs/benchmark.md), os [resultados medidos](docs/benchmark-results.md) e os [critérios para publicar a 1.0](docs/release-readiness.md).

Para revisar a 1.0, veja a [lista de verificações e os testes manuais](docs/review-1.0.md).

## Teste estrutural local

~~~bash
python tests/validate_repo.py
python -m unittest discover -s tests -p "test_*.py" -v
# Validação de referência, após instalar skills-ref:
agentskills validate ./thinking-outside
~~~

Isso valida arquivos e cenários, **não** avalia a criatividade de um modelo. Os testes comportamentais A/B são separados.

## Licença

MIT — veja [LICENSE](LICENSE).
