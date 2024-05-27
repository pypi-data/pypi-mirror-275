#!/usr/bin/env bash
set -e

tmp=$(mktemp -d ivylantern.XXXXX)

if [ -z "${tmp+x}" ] || [ -z "$tmp" ]; then
    echo "error: $tmp is not set or is an empty string."
    exit 1
fi

if ! command -v txtar-c >/dev/null; then
    echo go install github.com/rogpeppe/go-internal/cmd/txtar-c@latest
	exit 1
fi

declare -a files=(
	# Makefile # loc: 3
	# README.md # loc: 5
	# ivylantern.code-workspace # loc: 8
	# make_txtar.sh # loc: 50
	# pyproject.toml # loc: 34
	# requirements-dev.lock # loc: 83
	# requirements.lock # loc: 11
	src/ivylantern/__init__.py # loc: 37
	# src/ivylantern/__main__.py # loc: 5
	src/ivylantern/main.py # loc: 21
	
)
for file in "${files[@]}"; do
    echo $file
done | tee $tmp/filelist.txt

tar -cf $tmp/ivylantern.tar -T $tmp/filelist.txt
mkdir -p $tmp/ivylantern
tar xf $tmp/ivylantern.tar -C $tmp/ivylantern
rg --hidden --files $tmp/ivylantern

mkdir -p $tmp/gpt_instructions_XXYYBB

cat >$tmp/gpt_instructions_XXYYBB/1.txt <<EOF

EOF

{
    cat $tmp/gpt_instructions_XXYYBB/1.txt
    echo txtar archive is below
    txtar-c -quote -a $tmp/ivylantern
} | pbcopy

rm -rf $tmp
