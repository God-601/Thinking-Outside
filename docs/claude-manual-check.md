# Claude Code manual check

Use a Claude Code client that supports Agent Skills and has credits available. Run `claude --version` and record the selected model. On this workstation, Claude Code 1.0.83 returned `Credit balance is too low`. Native Claude behavior remains unverified.

Extract the [candidate ZIP](install-candidate.md) into `.claude/skills/` inside a disposable project. Confirm that `.claude/skills/thinking-outside/SKILL.md` exists. This should create one skill directory, without an extra nesting level. Leave the original archive and any personal installation untouched. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

1. **Explicit.** Start Claude Code in that project. Run `/thinking-outside` with this prompt:

   > Proponha três mecanismos diferentes para reduzir a espera em uma oficina comunitária. Preserve os horários, não recolha dados pessoais e proponha um teste reversível.

2. **Automatic.** Open a fresh session in the same project. Send the same prompt without using the slash command or naming the skill.

3. **Direct.** Open another fresh session and send:

   > Quanto é 23 × 4? Responda apenas com o número.

   The expected answer is `92`.

For stronger evidence of loading, append a unique marker instruction to the **disposable copy only** before these checks. For example, append `For any creative response using Explore, end with <your unique marker>.` Replace the placeholder with a random value that does not appear in any prompt. An exact marker in the explicit or automatic response confirms access to the body of the installed skill. Listing the skill or saying that it will be used only shows discovery or intent. If the marker is absent and there is no native read trace, record loading as unverified. The direct answer should omit the marker.

Save the client version, model, archive SHA-256, each prompt, its raw response, and any skill-read event or error. Report explicit, automatic and direct behavior separately. A credit or authentication error blocks the check and should be recorded without substituting a simulated result.
