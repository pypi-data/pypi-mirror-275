# SPDX-FileCopyrightText: 2018-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections import OrderedDict

from ruamel.yaml import YAML
from ruamel.yaml.comments import Comment, CommentedMap, CommentedSeq

yaml = YAML(typ="rt")

yaml.preserve_quotes = True
yaml.sequence_dash_offset = 2
yaml.map_indent = 2
yaml.sequence_indent = 4


def main() -> None:
    with open(".pre-commit-config.yaml") as f:
        data = yaml.load(f)

    repos: CommentedSeq = data["repos"]
    for j in range(len(repos)):
        repo: CommentedMap = repos[j]
        new_repo = repo.copy_attributes(CommentedMap())

        for v in ("repo", "rev"):
            if v in repo:
                old = repo.pop(v)
                # print(type(old))
                new_repo[v] = old

        for k, v in repo.items():
            new_repo[k] = v

        hooks = new_repo["hooks"]
        for i in range(len(hooks)):
            hook = hooks[i]
            new_hook = hook.copy_attributes(CommentedMap())
            for k in ("id", "exclude"):
                if k in hook:
                    new_hook[k] = hook.pop(k)

            for k, v in hook.items():
                new_hook[k] = v

            hooks[i] = new_hook

        repos[j] = new_repo

    with open(".pre-commit-config.yaml", "w") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()
