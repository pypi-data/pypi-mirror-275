#!/usr/bin/env bash
set -e

tmp=$(mktemp -d ourchester.XXXXX)

if [ -z "${tmp+x}" ] || [ -z "$tmp" ]; then
    echo "error: $tmp is not set or is an empty string."
    exit 1
fi

if ! command -v txtar-c >/dev/null; then
    echo go install github.com/rogpeppe/go-internal/cmd/txtar-c@latest
	exit 1
fi

declare -a files=(
	# .gitignore # loc: 1
	# Makefile # loc: 3
	# README.md # loc: 9
	# make_txtar.sh # loc: 55
	# pyproject.toml # loc: 36
	# requirements-dev.lock # loc: 30
	# requirements.lock # loc: 19
	src/ourchester/__init__.py # loc: 45
	src/ourchester/cli.py # loc: 43
	src/ourchester/indexer.py # loc: 79
	src/ourchester/log.py # loc: 9
	# src/ourchester/ourchester.code-workspace # loc: 8
	src/ourchester/searcher.py # loc: 13
	
)
for file in "${files[@]}"; do
    echo $file
done | tee $tmp/filelist.txt

tar -cf $tmp/ourchester.tar -T $tmp/filelist.txt
mkdir -p $tmp/ourchester
tar xf $tmp/ourchester.tar -C $tmp/ourchester
rg --hidden --files $tmp/ourchester

mkdir -p $tmp/gpt_instructions_XXYYBB

cat >$tmp/gpt_instructions_XXYYBB/1.txt <<EOF

EOF

{
    cat $tmp/gpt_instructions_XXYYBB/1.txt
    echo txtar archive is below
    txtar-c -quote -a $tmp/ourchester
} | pbcopy

rm -rf $tmp
